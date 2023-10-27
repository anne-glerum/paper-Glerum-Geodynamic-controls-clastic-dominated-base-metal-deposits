/*
  Copyright (C) 2011 - 2019 by the authors of the ASPECT code.

  This file is part of ASPECT.

  ASPECT is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2, or (at your option)
  any later version.

  ASPECT is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with ASPECT; see the file LICENSE.  If not see
  <http://www.gnu.org/licenses/>.
*/


#include <aspect/postprocess/visualization/vertical_heat_flux.h>
#include <aspect/gravity_model/interface.h>


namespace aspect
{
  namespace Postprocess
  {
    namespace VisualizationPostprocessors
    {
      template <int dim>
      VerticalHeatFlux<dim>::
      VerticalHeatFlux ()
        :
        DataPostprocessor<dim> ()
      {}



      template <int dim>
      std::vector<std::string>
      VerticalHeatFlux<dim>::
          get_names() const
      {
        std::vector<std::string> property_names(2, "vertical_conductive_heat_flux");
        property_names[1] = "vertical_advective_heat_flux";
        return property_names;
      }



      template <int dim>
      std::vector<DataComponentInterpretation::DataComponentInterpretation>
      VerticalHeatFlux<dim>::
      get_data_component_interpretation () const
      {
        return std::vector<DataComponentInterpretation::DataComponentInterpretation> (get_names().size(),
                                                                                      DataComponentInterpretation::component_is_scalar);
      }



      template <int dim>
      UpdateFlags
      VerticalHeatFlux<dim>::
      get_needed_update_flags () const
      {
        return update_gradients | update_values  | update_quadrature_points;
      }



      template <int dim>
      void
      VerticalHeatFlux<dim>::
      evaluate_vector_field(const DataPostprocessorInputs::Vector<dim> &input_data,
                            std::vector<Vector<double>> &computed_quantities) const
      {
        const unsigned int n_quadrature_points = input_data.solution_values.size();
        Assert (computed_quantities.size() == n_quadrature_points,    ExcInternalError());
        // conductive value and advective value
        Assert (computed_quantities[0].size() == 2,                   ExcInternalError());
        Assert (input_data.solution_values[0].size() == this->introspection().n_components,           ExcInternalError());

        //Create vector for the temperature gradients.  All the other things
        //we need are in MaterialModelInputs/Outputs
        std::vector<Tensor<1,dim>> temperature_gradient(n_quadrature_points);
        for (unsigned int q=0; q<n_quadrature_points; ++q)
          for (unsigned int d = 0; d < dim; ++d)
            temperature_gradient[q][d] = input_data.solution_gradients[q][this->introspection().component_indices.temperature][d];


        MaterialModel::MaterialModelInputs<dim> in(input_data,
                                                   this->introspection(),
                                                   false);
        MaterialModel::MaterialModelOutputs<dim> out(n_quadrature_points,
                                                     this->n_compositional_fields());
        this->get_material_model().evaluate(in, out);

        for (unsigned int q=0; q<n_quadrature_points; ++q)
          {
            const Tensor<1,dim> gravity = this->get_gravity_model().gravity_vector(in.position[q]);
            const Tensor<1,dim> vertical = -gravity/( gravity.norm() != 0.0 ?
                                                      gravity.norm() : 1.0 );
            const double advective_flux = (in.velocity[q] * vertical) * in.temperature[q] *
                                          out.densities[q]*out.specific_heat[q];
            const double conductive_flux = -(temperature_gradient[q]*vertical) *
                                           out.thermal_conductivities[q];
            computed_quantities[q](0) = conductive_flux;
            computed_quantities[q](1) = advective_flux;
          }
      }
    }
  }
}


// explicit instantiations
namespace aspect
{
  namespace Postprocess
  {
    namespace VisualizationPostprocessors
    {
      ASPECT_REGISTER_VISUALIZATION_POSTPROCESSOR(VerticalHeatFlux,
                                                  "vertical heat flux",
                                                  "A visualization output object that generates output "
                                                  "for the heat flux in the vertical direction. The first "
                                                  "value represents the vertical conductive heat flux, "
                                                  "the second the vertical advective heat flux, "
                                                  "with the sign convention of positive flux upwards.")
    }
  }
}
