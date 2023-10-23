# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
from os.path import exists

timestep_size = 0.5e6 # yr
extension_vel = 0.01 # m/yr

file_name_base = '/scratch/usr/bbpanneg/runs/FastScapeASPECT/'

model_names = [
                '5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
              ]
# Loop over all models
for m in model_names: 

  ASPECT_time_steps = ['00000']

  for t in range(0,len(ASPECT_time_steps)):
  
    print("Model name: ", m)
    print ("Time step number: ", ASPECT_time_steps[t])
  
    ASPECT_filename=file_name_base+m+'/solution/solution-'+ASPECT_time_steps[t]+'.pvtu'

    file_exists = exists(ASPECT_filename)
    if not file_exists:
      print ("File does not exist, continuing")
      continue
  
    # load state
    LoadState('/scratch/usr/bbpanneg/postprocessing/CERI/9_no1350isotherm_setup_nomesh.pvsm', LoadStateDataFileOptions='Choose File Names',
        DataDirectory='/scratch/usr/bbpanneg/postprocessing/CERI/',
        solutionpvtuFileName=[ASPECT_filename])
    
    renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
    renderView1.ViewSize = [2560, 1920]
  
    # Hide Stratigraphy legend
    strat = FindSource('ProgrammableFilter_SedType_z0')
    Hide(strat, renderView1)

    # current camera placement for renderView1
    position = 350000. #centered zoom2
    renderView1.CameraPosition = [position, 280000., 550000]
    renderView1.CameraFocalPoint = [position, 280000., -43924.18361557276]
    renderView1.CameraViewUp = [0.0, 1., 0.]
    renderView1.CameraParallelScale = 25000
    
    LoadPalette(paletteName='WhiteBackground')

    # save screenshot
    output_filename=file_name_base+m+'/'+m+'_'+ASPECT_time_steps[t]+'_heatfluxcontours_sedtypes_Tcontours_source_host_sedage2_8_zoom2_setup_nomesh.png'
    SaveScreenshot(output_filename, renderView1, ImageResolution=[2560, 1920],
        TransparentBackground=0)
  
    StratigraphyLUT = GetColorTransferFunction('Stratigraphy')
    StratigraphyLUTColorBar = GetScalarBar(StratigraphyLUT, renderView1)
    StratigraphyLUTColorBar.AutoOrient = 0
    StratigraphyLUTColorBar.Orientation = 'Horizontal'
    StratigraphyLUTColorBar.WindowLocation = 'UpperRightCorner'

    # Hide sediment age contours as they show up as black swatches
    # when zoomed out, similar to the strain rate.
    contour_SedAge_z0 = FindSource('Contour_SedAge_z0')
    Hide(contour_SedAge_z0, renderView1)

    # whole model domain
    renderView1.CameraParallelScale = 300000
    renderView1.CameraPosition = [350000, 150000, 550000]
    renderView1.CameraFocalPoint = [350000, 150000, -43924.18361557276]

    # save screenshot
    output_filename=file_name_base+m+'/'+m+'_'+ASPECT_time_steps[t]+'_heatfluxcontours_sedtypes_Tcontours_source_host_sedage2_8_wholedomain_setup_nomesh.png'
    SaveScreenshot(output_filename, renderView1, ImageResolution=[2560, 1920],
        TransparentBackground=0)
  
    # Delete sources and their children
    for x in GetSources().values():
      Delete(x[0])
    Delete(StratigraphyLUT)
