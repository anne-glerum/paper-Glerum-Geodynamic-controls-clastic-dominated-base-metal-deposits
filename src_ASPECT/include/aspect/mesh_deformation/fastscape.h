/*
  Copyright (C) 2018 by the authors of the ASPECT code.
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

#ifndef _aspect_mesh_deformation_fast_scape_h
#define _aspect_mesh_deformation_fast_scape_h

#include <aspect/mesh_deformation/interface.h>

namespace aspect
{
  using namespace dealii;

  namespace MeshDeformation
  {
    /**
     * Define FastScape functions as C functions. Must use exact same function/variable name
     * and type as used in FastScape. All function names must be made lowercase, and an
     * underscore added at the end. Types must be defined as pointers, and sent to
     * fastscape as a reference.
     */
#ifdef __cplusplus
    extern"C" {
#endif
    // Functions to initialize FastScape
    void fastscape_init_();
    // Set the nx and ny
    void fastscape_set_nx_ny_(const int *nnx, const int *nny);
    void fastscape_setup_();
    // Set the boundary conditions.
    void fastscape_set_bc_(const int *jbc);

    // Set the x and y extent
    void fastscape_set_xl_yl_(const double *xxl,const double *yyl);
    // Set the timestep
    void fastscape_set_dt_(double *dtt);
    // Initialize heights
    void fastscape_init_h_(double *hp);
    // Initialize silt fraction
    void fastscape_init_f_(double *f);
    // Parameters for hillslope diffusion, SPL, and enriched SPL (deposition).
    void fastscape_set_erosional_parameters_(double *kkf,const double *kkfsed,const double *mm,const double *nnn,
                                             double *kkd,const double *kkdsed,const double *gg1,const double *gg2,const double *pp);
    // Parameters for the marine component.
    void fastscape_set_marine_parameters_(const double *sl, const double *p1, const double *p2, const double *z1,
                                          const double *z2, const double *r, const double *l, const double *kds1, const double *kds2);

    // Set the velocities ux and uy, heights, or uplift.
    void fastscape_set_v_(double *ux, double *uy);
    void fastscape_set_u_(double *up);
    void fastscape_set_h_(double *hp);
    void fastscape_set_basement_(double *b);

    // Functions to run FastScape
    void fastscape_get_step_(int *sstep);
    void fastscape_execute_step_();
    // Set the output file directory and visualization step
    void folder_output_(int *length, int *asetp, const char *c, int *produce_output);
    // Create a visualization file into the ASPECT/VTK folder
    void fastscape_named_vtk_(double *fp, const double *vexp, int *astep, const char *c, int *length);
    // Copy the height array from FastScape back into ASPECT.
    void fastscape_copy_h_(double *hp);
    // Copy the basement array from FastScape back into ASPECT.
    void fastscape_copy_basement_(double *b);
    // Copy the silt fraction array from FastScape back into ASPECT.
    void fastscape_copy_f_(double *f);
    // Initialize stratigrapy, called once and handles visualization from there on.
    void fastscape_strati_(const int *nstepp, const int *nreflectorp, int *nfreqp, const double *vexp);
    //void folder_output_(int *length, int *astep, const char *c);
    // Copy slopes, used in determined ghost node height for mass flux flow in from a boundary.
    void fastscape_copy_slope_(double *slopep);

    // extracts tectonic flux, erosion flux, boundary flux in m3/yr
    void fastscape_get_fluxes_(double *tflux, double *eflux, double *bflux);

    // View additional information from FastScape, not included in the .cc.
    void fastscape_view_();
    void fastscape_debug_();

    // end run
    void fastscape_destroy_();
#ifdef  __cplusplus
  }
#endif

  template<int dim>
  class FastScape : public Interface<dim>, public SimulatorAccess<dim>
  {
    public:
      /**
       * Function to initialize variables for FastScape.
       */
      virtual void initialize () override;

      virtual
      void
      compute_velocity_constraints_on_boundary(const DoFHandler<dim> &mesh_deformation_dof_handler,
                                               AffineConstraints<double> &mesh_velocity_constraints,
                                               const std::set<types::boundary_id> &boundary_id) const override;

      /**
       * Declare parameters for the free surface handling.
       */
      static
      void declare_parameters (ParameterHandler &prm);

      /**
       * Parse parameters for the free surface handling.
       */
      void parse_parameters (ParameterHandler &prm) override;

      /**
       * A function that fills the viscosity derivatives in the
       * MaterialModelOutputs object that is handed over, if they exist.
       * Does nothing otherwise.
       */
      void set_ghost_nodes(double *h, double *vx, double *vy, double *vz, int nx, int ny) const;

      /**
       * Return the ratio between marine sediments from background marine sedimentation
       * and continental sediments for a certain point.
       */
      double get_marine_to_continental_sediment_ratio(Point<dim> point) const;

      /**
       * Return the fraction of silt out of the total sand plus silt continental sediments
       * in the marine domain for a certain point.
       */
      double get_silt_fraction(Point<dim> point) const;

      /**
         * Save the state of this object.
         */
      void save(std::map<std::string, std::string> &status_strings) const override;

      /**
         * Restore the state of the object.
         */
      void load(const std::map<std::string, std::string> &status_strings) override;

      /**
         * Serialize the contents of this class as far as they are not read
         * from input parameter files.
         */
      template <class Archive>
      void serialize(Archive &ar, const unsigned int version);

    private :
      // Number of FastScape steps per ASPECT timestep.
      int nstep;
      // Maximum timestep for FastScape, if time_step/nsteps exceeds this, nsteps is doubled.
      double max_timestep;
      // Whether or not the model is being restarted.
      mutable bool restart;
      // FastScape resets to step 0 on restart, this keeps the step number from the previous run.
      mutable int restart_step;
      // Model endtime to check if we should destroy FastScape.
      double end_time;

      // Cell size in FastScape, dx should always equal dy.
      double dx;
      double dy;
      // Length of X in FastScape (model X + 2*dx for ghost nodes).
      double x_extent;
      // Length of Y in FastScape (model Y + 2*dy for ghost nodes).
      double y_extent;
      // Size of y if FastScape is coupled with a 2D ASPECT model.
      double y_extent_2d;
      // Number of x points in FastScape array.
      int nx;
      // Number of y points in FastScape array.
      int ny;
      // Size of the FastScape array (nx*ny).
      int array_size;

      // Vertical exaggeration in FastScape visualization.
      double vexp;
      // How many levels FastScape should be refined above the maximum ASPECT surface resolution
      unsigned int additional_refinement;
      // Maximum expected refinement level at ASPECT's surface.
      int surface_resolution;
      // Expected difference in refinement level of the highest and lowest surface resolution.
      int resolution_difference;
      // Whether or not to send back the center slice or averaged surface in 2D.
      bool slice;
      // Seed number for initializing random topography noise in FastScape.
      int fs_seed;
      // Variable to hold ASPECT model dimensions.
      std::array<std::pair<double,double>,dim> grid_extent;
      // Table for interpolation of FastScape surface velocities back to ASPECT.
      std::array< unsigned int, dim > table_intervals;
      // Used to check whether fastscape is called at the surface.
      std::map<types::boundary_id, std::vector<std::string> > mesh_deformation_boundary_indicators_map;
      // Whether or not to use the ghost nodes.
      bool use_ghost;
      // Magintude in meters of the initial noise appleid to FastScape.
      int noise_h;
      // Sediment rain in m/yr, added to surface every ASPECT timestep.
      std::vector<double> sr_values;
      std::vector<double> sr_times;



      /**
       * Boundary conditions
       */
      // Boundary conditions for all sides, either 1 (fixed) or 0 (open).
      unsigned int bottom;
      unsigned int top;
      unsigned int right;
      unsigned int left;
      // Integer that holds the full boundary conditions (e.g. 1111).
      int bc;

      // Prescribed flux per unit length into the model through a boundary, in m^2/yr.
      double bottom_flux;
      double top_flux;
      double right_flux;
      double left_flux;

      /**
       * Erosional parameters
       */
      // Drainage area exponent (m in SPL)
      double m;
      // Slope exponent (n in SPL)
      double n;
      // Slope exponent for multi-direction flow. where 0 is uniform, and 10 is steepest descent. (-1 is varied)
      double p;
      // Bedrock deposition coefficient. Higher values mean more material is deposited.
      double g;
      // Sediment deposition coefficient.
      double gsed;
      // Bedrock river incision rate for SPL.
      double kff;
      // Sediment river incision rate.
      double kfsed;
      // Bedrock transport coefficient (diffusivity).
      double kdd;
      // Sediment transport coefficient.
      double kdsed;

      // Orographic parameters
      int mmax;
      int wb;
      int wd;
      double reduc_mmax;
      double reduc_wb;
      bool stackoro;

      // Parameters to set an extra erosional base level
      // on the ghost nodes that differs from sea level.
      bool use_extra_base_level;
      double h_extra_base_level;

      /**
       * Marine parameters
       */
      // Sea level. Initial topography of FastScape is set at model height and not changed to zero.
      double sl;
      // Surface porosity for sand.
      double p1;
      // Surface porosity for shale.
      double p2;
      // Sands e-folding depth for exponential porosity law.
      double z1;
      // Shales e-folding depth for exponential porosity law.
      double z2;
      // Sand-shale ratio
      double r;
      // Averaging depth/thickness for sand-shale equation (m).
      double l;
      // Sand marine transport coefficient (diffusivity).
      double kds1;
      // Shale marine transport coefficient (diffusivity).
      double kds2;
      // Whether or not to use the marine component of FastScape.
      bool use_marine;

      /**
       * Stratigraphy parameters.
       */
      bool use_strat;
      int nstepp;
      int nreflectorp;

      // Whether to use fastscape's advection and uplift. Turn off for free surface.
      bool use_v;
      // Precision value for node movement.
      double precision;

      /**
       * Maximum number of steps between the generation of graphical output.
       * This parameter
       * is read from the input file and consequently is not part of the
       * state that needs to be saved and restored.
       */
      unsigned int output_interval_steps;

      /**
       * Interval between the generation of graphical output. This parameter
       * is read from the input file and consequently is not part of the
       * state that needs to be saved and restored.
       */
      double output_interval;

      /**
       * A time (in seconds) at which the last graphical output was supposed
       * to be produced. Used to check for the next necessary output time.
       */
      mutable double last_output_time;
      mutable double last_output_timestep;

      /**
       * The ratio between marine and continental sediments.
       * We have to temporarily store it in this vector to be
       * able to restart the ratio table from a file.
       * TODO Make boost serialization available for Functions::InterpolatedUniformGridData.
       */
      mutable std::vector<double> ratio_marine_continental;

      // Function to hold and query the ratio of marine to continental sediments
      mutable Functions::InterpolatedUniformGridData<dim> *ratio_marine_continental_function;

      /**
       * The fraction of silt out of total sediments.
       * We have to temporarily store it in this vector to be
       * able to restart the ratio table from a file.
       * TODO Make boost serialization available for Functions::InterpolatedUniformGridData.
       */
      mutable std::vector<double> silt_fraction;

      // Function to hold and query the fraction of silt.
      mutable Functions::InterpolatedUniformGridData<dim> *silt_fraction_function;
  };
}
}


#endif
