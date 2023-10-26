This repository belongs to the paper

*Geodynamic controls on clastic-dominated base metal deposits*

by

Glerum, A.
Brune, S.,
Magnall, J. M.,
Weis, P. and
Gleeson, S. A.

currently under review.

# Documentation
The numerical simulations presented in this paper were run with the geodynamics code ASPECT ([https://aspect.geodynamics.org/](https://aspect.geodynamics.org/)) coupled to the surface processes code FastScape ([https://fastscape.org/fastscapelib-fortran/](https://fastscape.org/fastscapelib-fortran/)).


## ASPECT version
The ASPECT input files provided in this repository correspond to commit e5d8d53b65705abf1f328eb918c9e2ac41d26d53 of the ASPECT branch 

[https://github.com/anne-glerum/aspect/tree/FastScapeASPECT](https://github.com/anne-glerum/aspect/tree/FastScapeASPECT)

This branch is built on commit 84d40e745328f62df1a09e15a9f1bb4fdc86141a of the ASPECT 2.4.0-pre development branch,
which can be found at [https://github.com/geodynamics/aspect](https://github.com/geodynamics/aspect). 
A copy of e5d8d53 can be found in the folder /src_ASPECT.

## Additional ASPECT plugins
For the initial model conditions, we used the ASPECT plugins in the folder /plugins. 
The file CMakeLists.txt can be used to install these plugins as shared libraries
against your ASPECT installation.

## FastScape version

The FastScape source code provided in this repository corresponds to commit 592595752e11904e2350159ab0fd50fa37a843b6 
of the FastScape branch [https://github.com/anne-glerum/fastscapelib-fortran/tree/fastscape-with-stratigraphy-for-aspect](https://github.com/anne-glerum/fastscapelib-fortran/tree/fastscape-with-stratigraphy-for-aspect) 
and can be found in the folder /src_FastScape. This branch is built on commit 18f25888b16bf4cf23b00e79840bebed8b72d303 of 
[https://github.com/fastscape-lem/fastscapelib-fortran](https://github.com/fastscape-lem/fastscapelib-fortran).


## ASPECT input files
The ASPECT input files can be found in the respective folders of each simulation presentated in the manuscript under the 
file name original.prm.

Naming conventions:
5p - narrow asymmetric rift simulations
5q - narrow symmetric rift simulations
5o - wide rift simulations

## ASPECT output files
The folder belonging to each simulation also includes ASPECT output files log.txt and statistics. The statistics files have been used to plot source and host rock area and potential endowment over time.

## FastScape installation details
The FastScape version in this repository can by installed by:
1. Cloning this repository
2. Creating a build directory and entering it 
3. cmake -DBUILD_FASTSCAPELIB_SHARED=ON /path/to/fastscape/dir/
4. make

## ASPECT Installation details
ASPECT was built using the underlying library deal.II 10.0.0-pre (master, d944f3d291)
on the German HLRN cluster Lise. deal.II used:
* 32 bit indices and vectorization level 3 (512 bits)
* Trilinos 12.18.1
* p4est 2.2.0

The ASPECT version in this repository can be installed by (assuming deal.II is installed):
1. Creating a build directory and entering it
2. cmake -DEAL_II_DIR=/path/to/dealii/dir/ -DFASTSCAPE_DIR=/path/to/fastscape/build/dir/ path/to/aspect/dir/
3. make

## Postprocessing
Images of model results were created with ParaView 5.7.0 python scripts and statefiles in the folder /postprocessing_scripts (sedtype_fav_ore_form_8.py files and pvsm state files).
Plots of source and host rock area and endowment over time were created with python 3.9.17 scripts that can also be found in the /postprocessing_scripts folder.
