# -*- coding: utf-8 -*-
"""
Created on Mon 14 Feb 2022 by Anne Glerum
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc("pdf", fonttype=42)
rc('axes.formatter', useoffset=False)
rc("xtick", labelsize= 12)
rc("font", size=12)
rc("axes", titlesize=15, labelsize=12)
rc("legend", fontsize=8)
plt.rcParams["font.family"] = "Arial"
from os.path import exists
import io
import re

# Path to models
base = "../"

# Model names
models = [
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
         ]

output_name = '5p_fixed_rain0.0001_Km210_Km70_Kf1e-5_'

# Batlow (Scientific colour maps, Crameri et al. 2020)
color1=[0.0051932, 0.098238, 0.34984]
color2=[0.063071, 0.24709, 0.37505]
color3=[0.10684, 0.34977, 0.38455]
color4=[0.23136, 0.4262, 0.33857]
color5=[0.40297, 0.48047, 0.24473]
color6=[0.60052, 0.5336, 0.17065]
color7=[0.81169, 0.57519, 0.25257]
color8=[0.96494, 0.62693, 0.46486]
color9=[0.99277, 0.70769, 0.71238]
color10=[0.98332, 0.79091, 0.95375]

linestyles = [
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
             ]
markers = [
           '','','','','','','','','','','','','','','','','','','','','','','','',''
          ]
dmark = 200

# Parameters to estimate endowment
density = 2410 # kg/m3, sediment
F = 0.65
C_Zn = 100 # ppm
C_Pb = 23 # ppm
width = 20000 # m

# File name
tail = r"/statistics"

# Create file paths
paths = [base+m+tail for m in models]

counter = 0

cm = 2.54  # centimeters in inches
fig = plt.figure(figsize=(10.5/cm,6.6/cm),dpi=300)

n_timesteps = 7148
average_endowment_Zn = np.zeros(n_timesteps)
average_endowment_Pb = np.zeros(n_timesteps)

for p in paths:
    print(p)
    # Read in the area of the current timestep. 
    # The correct columns are selected with usecols.
    # When no visu output file name is given, the respective line will have a lot of
    # placeholder spaces. We need to remove them before genfromtxt can deal with the
    # statistics file. 
    with open(p) as f:
        clean_lines = (re.sub('\s+',' ',line) for line in f)
        t,source_area,host_area,fault_area = np.genfromtxt(clean_lines, comments='#', usecols=(1,62,63,64), delimiter=' ', unpack=True)

    # In case the simulation did not run to completion,
    # pad with zeroes. 
    if np.size(source_area) < n_timesteps:
      print ('before:',np.size(source_area),source_area)
      padded_source_area = np.pad(source_area, (0,n_timesteps-np.size(source_area)), 'constant', constant_values = (0,0))
      print ('after:',np.size(padded_source_area),padded_source_area)
    elif np.size(source_area) > n_timesteps:
      print ('More timesteps: ', np.size(source_area))
      padded_source_area = source_area[0:n_timesteps]
    else:
      padded_source_area = source_area

    # Add the endowment over time of this run to its sum 
    # endowment in Mt (= 1e6 * 1e3 kg) =
    # area [m2] * width [m] * density [kg/m3] * F [-] * C [ppm] / 1e6 / 1e9
    average_endowment_Zn += padded_source_area*width*density*F*C_Zn/1e6/1e9
    average_endowment_Pb += padded_source_area*width*density*F*C_Pb/1e6/1e9

    counter += 1

# Plot average endowment (assuming last run has the right amount of timesteps in t)
plt.plot(t/1e6,average_endowment_Zn/9,color=color1,linestyle='solid',label='NA-av. Zn',marker='')
plt.plot(t/1e6,average_endowment_Pb/9,color=color1,linestyle='dashed',label='NA-av. Pb',marker='')

# add in time range onset of oceanic spreading
plt.axvspan(20.0, 25.25, color='lightgrey', alpha=0.5, lw=0)

# Labelling of plot axes
plt.xlabel("Time [My]",weight="bold")
plt.ylabel(r"Endowment [$\mathbf{Mt}$]",weight="bold")

# Manually place legend
plt.legend(loc='upper left',ncol=1)

# Grid 
plt.grid(axis='x',color='0.95')
plt.grid(axis='y',color='0.95')

# Ranges of the axes
plt.xlim(-0.25,25.25) # My
plt.ylim(-0.75,75.75) # Mt

ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.ticklabel_format(axis='y',useOffset=False)
ax.yaxis.tick_right()
ax.yaxis.set_label_position('right')

# Axes ticks
plt.xticks(np.arange(0,30,5))
plt.yticks([0,25,50,75])

plt.tight_layout()
fig.tight_layout()

# Name the png according to the plotted field
field='average_endowment_'
plt.savefig(output_name + '_CERI_' + str(field) + '.png',dpi=300,bbox_inches='tight')    
print ("Output in: ", output_name + '_CERI_' + str(field) + '.png')
