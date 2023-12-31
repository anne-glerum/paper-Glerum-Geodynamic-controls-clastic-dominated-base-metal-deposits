# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import numpy as np
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
#from pathlib import Path
import platform
print(platform.python_version())
import glob
from os.path import exists
from os import mkdir

# Path to models
base = r"../"
model = "5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5"
path = base + model

# the range of the topography color bar
topo_min = -3500
topo_max = 1500
topo_SL = -200
searange = np.linspace(topo_min,topo_SL,128, endpoint=True)
landrange = np.linspace(topo_SL,topo_max,128, endpoint=True)
fullrange = np.append(searange,landrange)

# the topography exaggeration
topo_exag = 5

plot_topo = True
plot_catchment = True
plot_erosionrate = True
plot_drainage = True

# Crameri et al. 2020 Scientific colour maps
cm_data = [[0.10105, 0.15003, 0.35027],      
           [0.10721, 0.15579, 0.35609],      
           [0.11329, 0.16159, 0.36192],      
           [0.11927, 0.16739, 0.36777],      
           [0.12525, 0.17322, 0.37365],      
           [0.13122, 0.17911, 0.37954],      
           [0.13717, 0.18502, 0.38546],      
           [0.1431, 0.19093, 0.39141],      
           [0.14904, 0.19692, 0.39737],      
           [0.15498, 0.20288, 0.40336],      
           [0.16095, 0.20889, 0.40937],      
           [0.16694, 0.21492, 0.4154],      
           [0.17291, 0.22102, 0.42146],      
           [0.17894, 0.22709, 0.42756],      
           [0.18498, 0.23318, 0.43365],      
           [0.19102, 0.23934, 0.43979],      
           [0.19712, 0.24548, 0.44594],      
           [0.20322, 0.25169, 0.45213],      
           [0.20936, 0.25788, 0.45832],      
           [0.21553, 0.26413, 0.46456],      
           [0.22171, 0.27039, 0.4708],      
           [0.22794, 0.27666, 0.47706],      
           [0.23417, 0.28297, 0.48335],      
           [0.24042, 0.28929, 0.48967],      
           [0.24672, 0.29562, 0.496],      
           [0.25305, 0.30198, 0.50237],      
           [0.25939, 0.30838, 0.50876],      
           [0.26575, 0.31478, 0.51515],      
           [0.27212, 0.32122, 0.52157],      
           [0.27855, 0.32766, 0.52802],      
           [0.28496, 0.33415, 0.53448],      
           [0.29144, 0.34064, 0.54097],      
           [0.2979, 0.34716, 0.54747],      
           [0.3044, 0.35367, 0.554],      
           [0.31094, 0.36022, 0.56055],      
           [0.31747, 0.36681, 0.56712],      
           [0.32403, 0.37339, 0.5737],      
           [0.33061, 0.38, 0.58031],      
           [0.33723, 0.38662, 0.58693],      
           [0.34384, 0.39328, 0.59357],      
           [0.3505, 0.39994, 0.60023],      
           [0.35717, 0.40664, 0.60692],      
           [0.36384, 0.41334, 0.61361],      
           [0.37054, 0.42006, 0.62034],      
           [0.37727, 0.42681, 0.62707],      
           [0.38401, 0.43356, 0.63383],      
           [0.39077, 0.44034, 0.6406],      
           [0.39755, 0.44713, 0.64739],      
           [0.40434, 0.45395, 0.6542],      
           [0.41116, 0.46078, 0.66102],      
           [0.41799, 0.46763, 0.66787],      
           [0.42485, 0.4745, 0.67472],      
           [0.43173, 0.48137, 0.6816],      
           [0.4386, 0.48828, 0.6885],      
           [0.4455, 0.49519, 0.69541],      
           [0.45244, 0.50212, 0.70234],      
           [0.45937, 0.50908, 0.70929],      
           [0.46632, 0.51603, 0.71625],      
           [0.47329, 0.52302, 0.72322],      
           [0.48029, 0.53002, 0.73022],      
           [0.4873, 0.53704, 0.73723],      
           [0.49432, 0.54406, 0.74425],      
           [0.50136, 0.55111, 0.7513],      
           [0.50841, 0.55817, 0.75835],      
           [0.51547, 0.56524, 0.76542],      
           [0.52256, 0.57235, 0.7725],      
           [0.52967, 0.57946, 0.7796],      
           [0.53679, 0.58658, 0.78671],      
           [0.54392, 0.59372, 0.79382],      
           [0.55107, 0.60087, 0.80094],      
           [0.55822, 0.60804, 0.80806],      
           [0.5654, 0.61521, 0.81518],      
           [0.5726, 0.62241, 0.8223],      
           [0.57981, 0.62961, 0.8294],      
           [0.58702, 0.63684, 0.83647],      
           [0.59424, 0.64405, 0.84351],      
           [0.60147, 0.65129, 0.85051],      
           [0.60872, 0.65852, 0.85745],      
           [0.61595, 0.66575, 0.86431],      
           [0.62318, 0.67298, 0.87109],      
           [0.6304, 0.68018, 0.87775],      
           [0.6376, 0.68737, 0.88428],      
           [0.64477, 0.69453, 0.89065],      
           [0.65191, 0.70165, 0.89685],      
           [0.659, 0.70873, 0.90284],      
           [0.66603, 0.71575, 0.90861],      
           [0.673, 0.72268, 0.91414],      
           [0.67987, 0.72954, 0.9194],      
           [0.68666, 0.7363, 0.92438],      
           [0.69334, 0.74297, 0.92907],      
           [0.69991, 0.74951, 0.93347],      
           [0.70637, 0.75595, 0.93757],      
           [0.71269, 0.76226, 0.94137],      
           [0.7189, 0.76845, 0.94489],      
           [0.72499, 0.77451, 0.94812],      
           [0.73094, 0.78046, 0.9511],      
           [0.73679, 0.78631, 0.95383],      
           [0.74254, 0.79203, 0.95633],      
           [0.74818, 0.79766, 0.95864],      
           [0.75373, 0.80321, 0.96077],      
           [0.7592, 0.80868, 0.96274],      
           [0.76461, 0.81408, 0.96457],      
           [0.76995, 0.81943, 0.9663],      
           [0.77525, 0.82473, 0.96793],      
           [0.78052, 0.83, 0.96948],      
           [0.78575, 0.83524, 0.97097],      
           [0.79096, 0.84045, 0.97241],      
           [0.79615, 0.84564, 0.97381],      
           [0.80133, 0.85083, 0.97518],      
           [0.80651, 0.85602, 0.97653],      
           [0.81168, 0.86119, 0.97787],      
           [0.81685, 0.86637, 0.97919],      
           [0.82203, 0.87155, 0.9805],      
           [0.8272, 0.87673, 0.98181],      
           [0.83238, 0.88193, 0.98311],      
           [0.83757, 0.88712, 0.98442],      
           [0.84276, 0.89233, 0.98572],      
           [0.84795, 0.89753, 0.98702],      
           [0.85315, 0.90275, 0.98831],      
           [0.85836, 0.90797, 0.98962],      
           [0.86357, 0.9132, 0.99091],      
           [0.86879, 0.91844, 0.99221],      
           [0.874, 0.92368, 0.99351],      
           [0.87922, 0.92893, 0.9948],      
           [0.88444, 0.93418, 0.9961],      
           [0.88967, 0.93945, 0.99739],      
           [0.89489, 0.94472, 0.99869],      
           [0.90011, 0.94999, 0.99997],      
           [0.10024, 0.29901, 0.00015511],      
           [0.11206, 0.30199, 0.00022614],      
           [0.12317, 0.30497, 0.00025664],      
           [0.1339, 0.3079, 0.00024737],      
           [0.14418, 0.31082, 0.00020433],      
           [0.15412, 0.31369, 0.00016131],      
           [0.16383, 0.31653, 0.00012503],      
           [0.17323, 0.31932, 9.6573e-05],      
           [0.18245, 0.32208, 7.7354e-05],      
           [0.19152, 0.3248, 6.932e-05],      
           [0.2004, 0.32749, 7.5132e-05],      
           [0.20919, 0.33016, 9.8417e-05],      
           [0.21784, 0.33279, 0.00014406],      
           [0.2264, 0.3354, 0.00021853],      
           [0.23486, 0.33797, 0.00033026],      
           [0.24321, 0.34055, 0.00049005],      
           [0.25156, 0.34313, 0.00071147],      
           [0.25983, 0.34569, 0.0010113],      
           [0.26806, 0.3483, 0.0014102],      
           [0.27631, 0.35093, 0.0019325],      
           [0.28451, 0.35358, 0.0026075],      
           [0.29274, 0.35632, 0.0034694],      
           [0.30099, 0.3591, 0.0045572],      
           [0.3093, 0.36199, 0.005916],      
           [0.31763, 0.36496, 0.0075965],      
           [0.32602, 0.36806, 0.009658],      
           [0.33451, 0.37128, 0.012367],      
           [0.34305, 0.37466, 0.015348],      
           [0.35167, 0.37818, 0.01893],      
           [0.36038, 0.38186, 0.023166],      
           [0.36919, 0.38571, 0.028136],      
           [0.37806, 0.38973, 0.033895],      
           [0.38702, 0.39393, 0.0408],      
           [0.39605, 0.39829, 0.047888],      
           [0.40512, 0.4028, 0.055327],      
           [0.41425, 0.40747, 0.06302],      
           [0.42339, 0.41228, 0.070789],      
           [0.43257, 0.41721, 0.078726],      
           [0.44174, 0.42223, 0.086949],      
           [0.45088, 0.42738, 0.095228],      
           [0.46, 0.43259, 0.10362],      
           [0.4691, 0.43785, 0.11211],      
           [0.47812, 0.44317, 0.12065],      
           [0.4871, 0.44852, 0.12932],      
           [0.49601, 0.45389, 0.13805],      
           [0.50487, 0.45928, 0.14676],      
           [0.51366, 0.46468, 0.15555],      
           [0.52237, 0.47008, 0.16436],      
           [0.53104, 0.47548, 0.17315],      
           [0.53964, 0.48087, 0.18196],      
           [0.5482, 0.48628, 0.1908],      
           [0.5567, 0.4917, 0.19962],      
           [0.56516, 0.49712, 0.20847],      
           [0.57361, 0.50256, 0.21731],      
           [0.58203, 0.50804, 0.22616],      
           [0.59044, 0.51354, 0.235],      
           [0.59885, 0.51909, 0.24381],      
           [0.60727, 0.52468, 0.25267],      
           [0.61569, 0.53033, 0.26152],      
           [0.62414, 0.53605, 0.27039],      
           [0.63261, 0.54183, 0.27926],      
           [0.64111, 0.54769, 0.28812],      
           [0.64966, 0.55363, 0.29703],      
           [0.65823, 0.55966, 0.30594],      
           [0.66685, 0.56576, 0.31483],      
           [0.67551, 0.57195, 0.32377],      
           [0.6842, 0.57822, 0.33273],      
           [0.69296, 0.58458, 0.34168],      
           [0.70173, 0.591, 0.35066],      
           [0.71056, 0.59751, 0.35964],      
           [0.71941, 0.60408, 0.36865],      
           [0.7283, 0.61071, 0.37767],      
           [0.73722, 0.6174, 0.3867],      
           [0.74616, 0.62415, 0.39577],      
           [0.75513, 0.63095, 0.40484],      
           [0.76411, 0.63778, 0.41394],      
           [0.77309, 0.64467, 0.42306],      
           [0.78209, 0.6516, 0.43223],      
           [0.79107, 0.65857, 0.44141],      
           [0.80005, 0.66558, 0.45063],      
           [0.809, 0.67262, 0.45989],      
           [0.81789, 0.6797, 0.46922],      
           [0.82674, 0.68682, 0.47857],      
           [0.83551, 0.69397, 0.48799],      
           [0.84419, 0.70116, 0.49746],      
           [0.85274, 0.70839, 0.50699],      
           [0.86114, 0.71565, 0.51658],      
           [0.86936, 0.72293, 0.52624],      
           [0.87737, 0.73025, 0.53595],      
           [0.88513, 0.73757, 0.54572],      
           [0.89262, 0.74491, 0.55551],      
           [0.89981, 0.75225, 0.56535],      
           [0.90665, 0.75957, 0.57522],      
           [0.91313, 0.76687, 0.58508],      
           [0.91921, 0.77413, 0.59493],      
           [0.92491, 0.78136, 0.60476],      
           [0.9302, 0.78851, 0.61454],      
           [0.93507, 0.7956, 0.62429],      
           [0.93954, 0.80262, 0.63396],      
           [0.94361, 0.80956, 0.64355],      
           [0.94731, 0.81641, 0.65307],      
           [0.95066, 0.82318, 0.66252],      
           [0.95369, 0.82988, 0.67188],      
           [0.95641, 0.8365, 0.68116],      
           [0.95888, 0.84305, 0.69039],      
           [0.96112, 0.84954, 0.69955],      
           [0.96316, 0.85598, 0.70866],      
           [0.96502, 0.86239, 0.71773],      
           [0.96675, 0.86875, 0.72676],      
           [0.96835, 0.87509, 0.73578],      
           [0.96986, 0.88142, 0.74478],      
           [0.9713, 0.88773, 0.75378],      
           [0.97268, 0.89405, 0.76277],      
           [0.974, 0.90036, 0.77179],      
           [0.97529, 0.90668, 0.78081],      
           [0.97655, 0.91301, 0.78985],      
           [0.97779, 0.91936, 0.79891],      
           [0.97902, 0.92572, 0.80799],      
           [0.98023, 0.93209, 0.8171],      
           [0.98143, 0.93848, 0.82624],      
           [0.98261, 0.94489, 0.8354],      
           [0.98378, 0.95132, 0.84459],      
           [0.98495, 0.95776, 0.8538],      
           [0.98609, 0.96422, 0.86304],      
           [0.98722, 0.97069, 0.87231],      
           [0.98833, 0.97718, 0.88159],      
           [0.98942, 0.98369, 0.8909],      
           [0.99049, 0.9902, 0.90023]]      

# Convert RGB list to np array
cm_array = np.asarray(cm_data)
# Merge with topo values, so that each topo value has
# a RGB value
topo_array = np.c_[fullrange,cm_array].flatten()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# get the material library
materialLibrary1 = GetMaterialLibrary()

# get a list of all topo files
filenames = sorted(glob.glob(path+"/VTK/Topography*"))

# create a new 'Legacy VTK Reader'
topography000 = LegacyVTKReader(FileNames=filenames)

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# show data in view
topography000Display = Show(topography000, renderView1)

# trace defaults for the display properties.
topography000Display.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
topography000Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'topography'
topographyLUT = GetColorTransferFunction('topography')

# get opacity transfer function/opacity map for 'topography'
topographyPWF = GetOpacityTransferFunction('topography')

# Rescale transfer function
topographyLUT.RescaleTransferFunction(topo_min, topo_max)

# Rescale transfer function
topographyPWF.RescaleTransferFunction(topo_min, topo_max)

# Make sure the switch from below to above SL is at the SL
topographyLUT.RGBPoints = topo_array.tolist()

# current camera placement for renderView1
renderView1.CameraPosition = [384380.5030903542, -526868.7089745248, 530565.0653625994]
renderView1.CameraFocalPoint = [350625.0, 25625.0, 0.04999995231662449]
renderView1.CameraViewUp = [0.0, 0.6929298137240902, 0.7210050438466415]
renderView1.CameraParallelScale = 351560.1389158084

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
#topographyLUT.ApplyPreset('oleron', True)

# get color legend/bar for topographyLUT in view renderView1
topographyLUTColorBar = GetScalarBar(topographyLUT, renderView1)

# Properties modified on topographyLUTColorBar
topographyLUTColorBar.AutoOrient = 0
topographyLUTColorBar.Orientation = 'Horizontal'
topographyLUTColorBar.WindowLocation = 'UpperCenter'
topographyLUTColorBar.Title = 'Topography [m]'

# Properties modified on topographyLUTColorBar
topographyLUTColorBar.RangeLabelFormat = '%-#6.3g'

# Properties modified on topographyLUTColorBar
topographyLUTColorBar.RangeLabelFormat = '%-#6.3f'

# Properties modified on topographyLUTColorBar
topographyLUTColorBar.RangeLabelFormat = '%-#6.0f'

# Add label at SL
topographyLUTColorBar.UseCustomLabels = 1
topographyLUTColorBar.CustomLabels = [topo_min, topo_SL, topo_max]

# Exaggerate vertical

# Properties modified on topography0001005vtkDisplay
topography000Display.Scale = [1.0, 1.0, topo_exag]

# Properties modified on topography0001005vtkDisplay.DataAxesGrid
topography000Display.DataAxesGrid.Scale = [1.0, 1.0, topo_exag]

# Properties modified on topography0001005vtkDisplay.PolarAxes
topography000Display.PolarAxes.Scale = [1.0, 1.0, topo_exag]

# current camera placement for renderView1
renderView1.CameraPosition = [384380.5030903542, -526868.7089745248, 530565.0653625994]
renderView1.CameraFocalPoint = [350625.0, 25625.0, 0.04999995231662449]
renderView1.CameraViewUp = [0.0, 0.6929298137240902, 0.7210050438466415]
renderView1.CameraParallelScale = 351560.1389158084

# save animation
if plot_topo: 
  SaveAnimation(model + '/FastScape_topography_'+str(topo_min)+ '_'+str(topo_max)+ '_' + str(topo_exag) + '.png', renderView1, ImageResolution=[1551, 810],
      FrameWindow=[0, 101])
      #FrameWindow=[0, 51])

# current camera placement for renderView1
renderView1.CameraPosition = [384380.5030903542, -526868.7089745248, 530565.0653625994]
renderView1.CameraFocalPoint = [350625.0, 25625.0, 0.04999995231662449]
renderView1.CameraViewUp = [0.0, 0.6929298137240902, 0.7210050438466415]
renderView1.CameraParallelScale = 351560.1389158084

topography000Display.SetScalarBarVisibility(renderView1, False)

# save animation
if plot_topo: 
  SaveAnimation(model + '/FastScape_topography_'+str(topo_min)+ '_'+str(topo_max)+'_' + str(topo_exag) + '_nolabels.png', renderView1, ImageResolution=[1551, 810],
      FrameWindow=[0, 51])

# set scalar coloring
ColorBy(topography000Display, ('POINTS', 'drainage_area'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(topographyLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
topography000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
topography000Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'drainage_area'
drainage_areaLUT = GetColorTransferFunction('drainage_area')

# get opacity transfer function/opacity map for 'drainage_area'
drainage_areaPWF = GetOpacityTransferFunction('drainage_area')

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
topography000Display.RescaleTransferFunctionToDataRange(False, True)

# convert to log space
drainage_areaLUT.MapControlPointsToLogSpace()

# Properties modified on drainage_areaLUT
drainage_areaLUT.UseLogScale = 1

# Properties modified on animationScene1
animationScene1.AnimationTime = 11.0

# Properties modified on timeKeeper1
timeKeeper1.Time = 11.0

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
drainage_areaLUT.ApplyPreset('batlowK', True)

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 701250.0, 0.0, 51250.0, -1849.42199707, 2210.03100586)

# get color legend/bar for drainage_areaLUT in view renderView1
drainage_areaLUTColorBar = GetScalarBar(drainage_areaLUT, renderView1)

# Properties modified on drainage_areaLUTColorBar
drainage_areaLUTColorBar.AutoOrient = 0
drainage_areaLUTColorBar.Orientation = 'Horizontal'
drainage_areaLUTColorBar.WindowLocation = 'UpperCenter'
drainage_areaLUTColorBar.Title = 'Drainage area [m2]'

# Rescale transfer function
drainage_areaLUT.RescaleTransferFunction(400000.0, 40000000000.0)

# Rescale transfer function
drainage_areaPWF.RescaleTransferFunction(400000.0, 40000000000.0)

# Properties modified on drainage_areaLUTColorBar
drainage_areaLUTColorBar.UseCustomLabels = 1
drainage_areaLUTColorBar.CustomLabels = [4000000.0, 40000000.0, 400000000.0, 400000000.0]

# Properties modified on drainage_areaLUTColorBar
drainage_areaLUTColorBar.CustomLabels = [4000000.0, 40000000.0, 400000000.0, 4000000000.0]

# current camera placement for renderView1
renderView1.InteractionMode = 3
renderView1.CameraPosition = [384380.5030903542, -526868.7089745248, 530565.0653625994]
renderView1.CameraFocalPoint = [350625.0, 25625.0, 0.04999995231662449]
renderView1.CameraViewUp = [0.0, 0.6929298137240902, 0.7210050438466415]
renderView1.CameraParallelScale = 351560.1389158084

# hide color bar/color legend
topography000Display.SetScalarBarVisibility(renderView1, True)
# save animation
if plot_drainage: 
  SaveAnimation(model + '/FastScape_drainagearea_' + str(topo_exag) + '.png', renderView1, ImageResolution=[1551, 810],
      FrameWindow=[0, 51])

# hide color bar/color legend
topography000Display.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.InteractionMode = 3
renderView1.CameraPosition = [384380.5030903542, -526868.7089745248, 530565.0653625994]
renderView1.CameraFocalPoint = [350625.0, 25625.0, 0.04999995231662449]
renderView1.CameraViewUp = [0.0, 0.6929298137240902, 0.7210050438466415]
renderView1.CameraParallelScale = 351560.1389158084

# save animation
if plot_drainage: 
  SaveAnimation(model + '/FastScape_drainagearea_' + str(topo_exag) + '_nolabels_.png', renderView1, ImageResolution=[1551, 810],
      FrameWindow=[0, 51])

# set scalar coloring
ColorBy(topography000Display, ('POINTS', 'erosion_rate'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(drainage_areaLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
topography000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
topography000Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'erosion_rate'
erosion_rateLUT = GetColorTransferFunction('erosion_rate')

# get opacity transfer function/opacity map for 'erosion_rate'
erosion_ratePWF = GetOpacityTransferFunction('erosion_rate')

# rescale color and/or opacity maps used to exactly fit the current data range
topography000Display.RescaleTransferFunctionToDataRange(False, True)

# set scalar coloring using an separate color/opacity maps
ColorBy(topography000Display, ('POINTS', 'erosion_rate'), True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(erosion_rateLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
topography000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
topography000Display.SetScalarBarVisibility(renderView1, True)

# get separate color transfer function/color map for 'erosion_rate'
separate_topography000Display_erosion_rateLUT = GetColorTransferFunction('erosion_rate', topography000Display, separate=True)

# get separate opacity transfer function/opacity map for 'erosion_rate'
separate_topography000Display_erosion_ratePWF = GetOpacityTransferFunction('erosion_rate', topography000Display, separate=True)

# set scalar coloring
ColorBy(topography000Display, ('POINTS', 'erosion_rate'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(separate_topography000Display_erosion_rateLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
topography000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
topography000Display.SetScalarBarVisibility(renderView1, True)

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
topography000Display.RescaleTransferFunctionToDataRange(False, True)

# Properties modified on animationScene1
animationScene1.AnimationTime = 20.0

# Properties modified on timeKeeper1
timeKeeper1.Time = 20.0

# Rescale transfer function
erosion_rateLUT.RescaleTransferFunction(0.0, 0.000487613055157)

# Rescale transfer function
erosion_ratePWF.RescaleTransferFunction(0.0, 0.000487613055157)

# Rescale transfer function
erosion_rateLUT.RescaleTransferFunction(0.0, 0.0005)

# Rescale transfer function
erosion_ratePWF.RescaleTransferFunction(0.0, 0.0005)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
erosion_rateLUT.ApplyPreset('lajolla', True)

# get color legend/bar for erosion_rateLUT in view renderView1
erosion_rateLUTColorBar = GetScalarBar(erosion_rateLUT, renderView1)

# Properties modified on erosion_rateLUTColorBar
erosion_rateLUTColorBar.Title = 'Erosion rate [m/yr]'

# Properties modified on erosion_rateLUTColorBar
erosion_rateLUTColorBar.AutoOrient = 0
erosion_rateLUTColorBar.Orientation = 'Horizontal'
erosion_rateLUTColorBar.WindowLocation = 'UpperCenter'

# Properties modified on erosion_rateLUTColorBar
erosion_rateLUTColorBar.AutomaticLabelFormat = 0
erosion_rateLUTColorBar.LabelFormat = '%-#6.e'

# Properties modified on erosion_rateLUTColorBar
erosion_rateLUTColorBar.LabelFormat = '%-#6.1e'

# current camera placement for renderView1
renderView1.CameraPosition = [384380.5030903542, -526868.7089745248, 530565.0653625994]
renderView1.CameraFocalPoint = [350625.0, 25625.0, 0.04999995231662449]
renderView1.CameraViewUp = [0.0, 0.6929298137240902, 0.7210050438466415]
renderView1.CameraParallelScale = 351560.1389158084

# save animation
if plot_erosionrate: 
  SaveAnimation(model + '/FastScape_erosionrate_' + str(topo_exag) + '.png', renderView1, ImageResolution=[1551, 810],
      FrameWindow=[0, 51])

# hide color bar/color legend
topography000Display.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.CameraPosition = [384380.5030903542, -526868.7089745248, 530565.0653625994]
renderView1.CameraFocalPoint = [350625.0, 25625.0, 0.04999995231662449]
renderView1.CameraViewUp = [0.0, 0.6929298137240902, 0.7210050438466415]
renderView1.CameraParallelScale = 351560.1389158084

# save animation
if plot_erosionrate: 
  SaveAnimation(model + '/FastScape_erosionrate_' + str(topo_exag) + '_nolabels_.png', renderView1, ImageResolution=[1551, 810],
      FrameWindow=[0, 51])

# set scalar coloring
ColorBy(topography000Display, ('POINTS', 'catchment'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(erosion_rateLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
topography000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
topography000Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'catchment'
catchmentLUT = GetColorTransferFunction('catchment')

# get opacity transfer function/opacity map for 'catchment'
catchmentPWF = GetOpacityTransferFunction('catchment')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
catchmentLUT.ApplyPreset('acton', True)

# get color legend/bar for catchmentLUT in view renderView1
catchmentLUTColorBar = GetScalarBar(catchmentLUT, renderView1)

# Properties modified on catchmentLUTColorBar
catchmentLUTColorBar.AutoOrient = 0
catchmentLUTColorBar.Orientation = 'Horizontal'
catchmentLUTColorBar.WindowLocation = 'UpperCenter'
catchmentLUTColorBar.Title = 'Catchment area [m2]'

# Rescale transfer function
catchmentLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
catchmentPWF.RescaleTransferFunction(0.0, 1.0)

# Properties modified on catchmentLUTColorBar
catchmentLUTColorBar.RangeLabelFormat = '%-#6.3g'

# Properties modified on catchmentLUTColorBar
catchmentLUTColorBar.RangeLabelFormat = '%-#6.1f'

# current camera placement for renderView1
renderView1.CameraPosition = [384380.5030903542, -526868.7089745248, 530565.0653625994]
renderView1.CameraFocalPoint = [350625.0, 25625.0, 0.04999995231662449]
renderView1.CameraViewUp = [0.0, 0.6929298137240902, 0.7210050438466415]
renderView1.CameraParallelScale = 351560.1389158084

# save animation
if plot_catchment: 
  SaveAnimation(model + '/FastScape_catchment_' + str(topo_exag) + '.png', renderView1, ImageResolution=[1512, 810],
      FrameWindow=[0, 51])

# hide color bar/color legend
topography000Display.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.CameraPosition = [384380.5030903542, -526868.7089745248, 530565.0653625994]
renderView1.CameraFocalPoint = [350625.0, 25625.0, 0.04999995231662449]
renderView1.CameraViewUp = [0.0, 0.6929298137240902, 0.7210050438466415]
renderView1.CameraParallelScale = 351560.1389158084

# save animation
if plot_catchment: 
  SaveAnimation(model + '/FastScape_catchment_' + str(topo_exag) + '_nolabels_.png', renderView1, ImageResolution=[1512, 810],
      FrameWindow=[0, 51])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [384380.5030903542, -526868.7089745248, 530565.0653625994]
renderView1.CameraFocalPoint = [350625.0, 25625.0, 0.04999995231662449]
renderView1.CameraViewUp = [0.0, 0.6929298137240902, 0.7210050438466415]
renderView1.CameraParallelScale = 351560.1389158084
