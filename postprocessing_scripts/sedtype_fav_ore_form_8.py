# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
from os.path import exists

file_name_base = '/scratch/usr/bbpanneg/runs/FastScapeASPECT/'

# res_x default = 4000
res_x = 4000
# res_y default = 500
res_y = 500
# cam_parllel_scale default = 25000
cam_parallel_scale = 25000
# cam_y default = 280000
cam_y = 280000

model_names = [
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',

#'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',

#'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',

#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf4e-05_SL-200_vel10',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf4e-05_SL-200_vel10',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf4e-05_SL-200_vel10',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf4e-05_SL-200_vel10',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf4e-05_SL-200_vel10',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf4e-05_SL-200_vel10',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf4e-05_SL-200_vel10',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf4e-05_SL-200_vel10',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf4e-05_SL-200_vel10',

#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0002_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0002_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0002_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0002_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0002_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0002_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0002_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0002_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0002_Ksilt210_Ksand70_Kf1e-05_SL-200',
#
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0004_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0004_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0004_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0004_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0004_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0004_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0004_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0004_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0004_Ksilt210_Ksand70_Kf1e-05_SL-200',
#
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',

#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-06_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-06_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-06_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-06_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-06_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-06_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-06_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-06_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-06_SL-200',
#
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
#
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt300_Ksand100_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt300_Ksand100_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt300_Ksand100_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt300_Ksand100_Kf1e-05_SL-200',
#
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt120_Ksand40_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt120_Ksand40_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt120_Ksand40_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt120_Ksand40_Kf1e-05_SL-200',
              ]
# Loop over all models
for m in model_names: 

  ASPECT_time_steps = ['00001','00005','00010','00015','00020','00025','00030','00035','00040','00045','00050']

  for t in range(0,len(ASPECT_time_steps)):
  
    print("Model name: ", m)
    print ("Time step number: ", ASPECT_time_steps[t])
  
    ASPECT_filename=file_name_base+m+'/solution/solution-'+ASPECT_time_steps[t]+'.pvtu'

    file_exists = exists(ASPECT_filename)
    if not file_exists:
      print ("File does not exist, continuing")
      continue
  
    # load state
    LoadState('/scratch/usr/bbpanneg/postprocessing/CERI/9_no1350isotherm.pvsm', LoadStateDataFileOptions='Choose File Names',
        DataDirectory='/scratch/usr/bbpanneg/postprocessing/CERI/',
        solutionpvtuFileName=[ASPECT_filename])
    
    renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
    renderView1.ViewSize = [2560, 1920]
  
    # Hide Stratigraphy legend
    strat = FindSource('ProgrammableFilter_SedType_z0')
    stratDisplay = Show(strat, renderView1)
    stratDisplay.SetScalarBarVisibility(renderView1, False)

    # current camera placement for renderView1
    position = 350000. #centered zoom2
    renderView1.CameraPosition = [position, cam_y, 550000]
    renderView1.CameraFocalPoint = [position, cam_y, -43924.18361557276]
    renderView1.CameraViewUp = [0.0, 1., 0.]
    renderView1.CameraParallelScale = cam_parallel_scale
    
    renderView1.ViewSize = [res_x, res_y] 
    LoadPalette(paletteName='WhiteBackground')

    # save screenshot
    output_filename=file_name_base+m+'/'+m+'_'+ASPECT_time_steps[t]+'_heatfluxcontours_sedtypes_Tcontours_source_host_sedage2_8_zoom2_'+ str(cam_y)+'_'+str(cam_parallel_scale)+'.png'
    SaveScreenshot(output_filename, renderView1, ImageResolution=[res_x, res_y],
        TransparentBackground=0)
  
    # Delete sources and their children
    for x in GetSources().values():
      Delete(x[0])
    Delete(StratigraphyLUT)
