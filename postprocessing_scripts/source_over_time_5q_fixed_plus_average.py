# -*- coding: utf-8 -*-
"""
Created on Mon 14 Feb 2022 by Anne Glerum
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('axes.formatter', useoffset=False)
plt.rcParams["font.family"] = "Arial"
rc("xtick", labelsize= 12)
rc("font", size=12)
rc("axes", titlesize=15, labelsize=12)
rc("legend", fontsize=8)
from os.path import exists
import io
import re

# Path to models
base = "../"

# Model names
models = [
'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5q_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
         ]

output_name = '5q_fixed_rain0.0001_Km210_Km70_Kf1e-5_'

labels = [
          'NS-1',
          'NS-2',
          'NS-3',
          'NS-4',
          'NS-5',
          'NS-6',
          'NS-7',
          'NS-8',
          'NS-9',
          'NS-av.',
         ]

# Batlow
# Scientific color maps (Crameri et al. 2020)
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
colors = [
          color1, 
          color2, 
          color3, 
          color4, 
          color5, 
          color6, 
          color7, 
          color8, 
          color9, 
          color10, 
         ]
cmap = plt.cm.get_cmap(cm.batlow)

linestyles = [
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'dashed',
              'dotted', 
              'dashdot',
             ]
markers = [
           '','','','','','','','','','','','','','','','','','','','','','','','',''
          ]
dmark = 200

# File name
tail = r"/statistics"

# Create file paths
paths = [base+m+tail for m in models]

counter = 0
mean_t = np.arange(0, 25e6, 2500)
average_source_area = [0.0 for t in mean_t]
max_source = -2e9
average_max_source = 0

cm = 2.54  # centimeters in inches
fig = plt.figure(figsize=(10.5/cm,6.6/cm),dpi=300)

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

    # Interpolate to a predefined set of timesteps, as not all runs have the same number
    # of timesteps.
    interpolated_source_area = np.interp(mean_t, t, source_area)
    print ("interpolated source ", interpolated_source_area)

    average_source_area += interpolated_source_area

    # Plot the raw area in km2 in 
    # categorical batlow colors.
    plt.plot(t/1e6,source_area/1e6,color=colors[counter],linestyle='solid',label=labels[counter],marker=markers[counter],markevery=dmark,fillstyle='none')

    max_source = max(source_area.max(),max_source)
    average_max_source += source_area.max()

    counter += 1

print ("Max source area:", max_source, "m2")
print ("Average max source area:", average_max_source/9, "m2")

# Plot the average source area over time (divide by nine to get the average) in km2
plt.plot(mean_t/1e6,average_source_area/9e6,color=colors[counter],linestyle='solid',label=labels[counter],marker=markers[counter],markevery=dmark,fillstyle='none',linewidth=3)

# add in time range onset of oceanic spreading
plt.axvspan(12.5, 25.25, color='lightgrey', alpha=0.5, lw=0)

# Labelling of plot
plt.xlabel("Time [My]",weight="bold")
plt.ylabel(r"Source area [$\mathbf{km^2}$]",weight="bold")
# Manually place legend
plt.legend(loc='upper left',ncol=2, columnspacing = 1.5)
# Grid
plt.grid(axis='x',color='0.95')
plt.grid(axis='y',color='0.95')

# Ranges of the axes
plt.xlim(-0.25,25.25) # My
plt.ylim(-0.4,40.4) # km2
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_useOffset(False)
# Ticks
plt.ticklabel_format(axis='y',useOffset=False)
plt.xticks(np.arange(0,30,5))

plt.tight_layout()
fig.tight_layout()

# Name the png according to the plotted field
# Change as needed
field='average_source_area_'
plt.savefig(output_name + '_CERI_' + str(field) + '.png',dpi=300,bbox_inches='tight')    
print ("Output in: ", output_name + '_CERI_' + str(field) + '.png')
