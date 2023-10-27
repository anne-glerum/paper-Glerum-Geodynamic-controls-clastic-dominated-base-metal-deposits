/*
  Copyright (C) 2011 - 2016 by the authors of the ASPECT code.

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


#ifndef _aspect_boundary_velocity_compensating_bottom_flow_h
#define _aspect_boundary_velocity_compensating_bottom_flow_h

#include <aspect/boundary_velocity/interface.h>
#include <aspect/simulator_access.h>

//#include <deal.II/base/std_cxx11/array.h>


namespace aspect
{
  namespace BoundaryVelocity
  {
    using namespace dealii;

    /**
     * A class that implements prescribed velocity boundary conditions
     * determined from angular rotation vectors specified for each boundary
     * with prescribed velocity boundary conditions.
     *
     * @ingroup BoundaryVelocities
     */
    template <int dim>
    class CompensatingBottomFlow : public Interface<dim>, public SimulatorAccess<dim>
    {
      public:
        /**
         * Empty Constructor.
         */
        CompensatingBottomFlow ();

        /**
         * Return the boundary velocity as a function of position and boundary
         * indicator. For the current class, this function returns the value
         * of the cross product of the angular velocity vector and the point vector.
         */
        Tensor<1,dim>
        boundary_velocity (const types::boundary_id boundary_indicator,
                           const Point<dim> &position) const;

        // avoid -Woverloaded-virtual warning until the deprecated function
        // is removed from the interface:
        using Interface<dim>::boundary_velocity;

        /**
         * Initialization function. This function is called once at the
         * beginning of the program. Checks preconditions.
         */
        virtual
        void
        initialize ();

        virtual
        void
        update ();

        /**
         * Compute the integral of the net flux due to the prescribed velocity
         * on the lateral domain boundaries.
         */
        double
        compute_net_outflow () const;

        /**
         * Declare the parameters this class takes through input files.
         */
        static
        void
        declare_parameters (ParameterHandler &prm);

        /**
         * Read the parameters this class declares from the parameter file.
         */
        void
        parse_parameters (ParameterHandler &prm);

      private:
        /**
         * The outer and inner radius of the model domain.
         */
        double outer_radius;
        double inner_radius;

        double bottom_boundary_area = 0;

        double net_outflow = 0;




        /**
         * The ids of the lateral boundaries for which the net in/outflow is computed
         * and compensated through the bottom boundary flow.
         */
        std::set<types::boundary_id> vertical_boundary_indicators;
        types::boundary_id bottom_boundary_indicator = numbers::invalid_boundary_id;

        /**
         * The boundary velocity objects on the lateral boundaries that need to be compensated.
         */
        //std::map<types::boundary_id, std::vector<std::unique_ptr<BoundaryVelocity::Interface<dim>>>>
        //lateral_boundary_velocity_objects;
    };
  }
}


#endif
