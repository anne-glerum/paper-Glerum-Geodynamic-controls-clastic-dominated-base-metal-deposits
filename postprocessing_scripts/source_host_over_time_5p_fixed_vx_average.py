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
# make lables editable in svg in Inkscape
plt.rcParams["text.usetex"] = False
plt.rcParams["svg.fonttype"] = "none"
from os.path import exists
import io
import re

# Path to models
base = "../"

# Model names
models = [
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel20',
         ]

output_name = '5p_fixed_rain0.0001_Km210_Km70_Kf1e-5_velvar_'

labels = [
          'NA-av. $v_{x}$ = 5 mm/yr',
          'NA-av. $v_{x}$ = 10 mm/yr',
          'NA-av. $v_{x}$ = 20 mm/yr',
          'NA-av. $v_{x}$ = 5 mm/yr',
          'NA-av. $v_{x}$ = 10 mm/yr',
          'NA-av. $v_{x}$ = 20 mm/yr',
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
color_source = 'blue'
color_host = color7
colors = [
          color_source,
          color_source,
          color_source,
          color_host,
          color_host,
          color_host,
         ]
cmap = plt.cm.get_cmap(cm.batlow)

linestyles = [
              'dotted', 
              'dashed',
              'solid', 
              'dotted', 
              'dashed',
              'solid', 
             ]
markers = [
           '','','','','','',
          ]
dmark = 200

# File name
tail = r"/statistics"

# Create file paths
paths = [base+m+tail for m in models]

counter = 0
mean_t = np.arange(0, 250, 0.250)
average_source_area_1 = [0.0 for t in mean_t]
average_source_area_2 = [0.0 for t in mean_t]
average_source_area_3 = [0.0 for t in mean_t]
average_host_area_1 = [0.0 for t in mean_t]
average_host_area_2 = [0.0 for t in mean_t]
average_host_area_3 = [0.0 for t in mean_t]
max_source = -2e9
average_max_source = 0

cm = 2.54  # centimeters in inches
fig = plt.figure(figsize=(10.5/cm,6.6/cm),dpi=300)
ax = fig.add_subplot(111, label = 'source')
ax2 = fig.add_subplot(111, label = 'host', frame_on='False', sharex=ax)

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
    # of timesteps. And add to respective average based on vel.

    if 'vel5' in p:
      interpolated_source_area = np.interp(mean_t, t*0.005/1000.0, source_area)
      interpolated_host_area = np.interp(mean_t, t*0.005/1000.0, host_area)
      average_source_area_1 += interpolated_source_area
      average_host_area_1 += interpolated_host_area
    elif 'vel20' in p:
      interpolated_source_area = np.interp(mean_t, t*0.02/1000.0, source_area)
      interpolated_host_area = np.interp(mean_t, t*0.02/1000.0, host_area)
      average_source_area_3 += interpolated_source_area
      average_host_area_3 += interpolated_host_area
    else:
      interpolated_source_area = np.interp(mean_t, t*0.01/1000.0, source_area)
      interpolated_host_area = np.interp(mean_t, t*0.01/1000.0, host_area)
      average_source_area_2 += interpolated_source_area
      average_host_area_2 += interpolated_host_area

    max_source = max(source_area.max(),max_source)
    average_max_source += source_area.max()

    counter += 1

print ("Max source area:", max_source, "m2")
print ("Average max source area:", average_max_source/9, "m2")

# Plot the average source area over time (divide by nine to get the average) in km2
ax.plot(mean_t,average_source_area_1/9e6,color=colors[0],linestyle=linestyles[0],label=None,marker=markers[0],markevery=dmark,fillstyle='none')
ax.plot(mean_t,average_source_area_2/9e6,color=colors[1],linestyle=linestyles[1],label=None,marker=markers[1],markevery=dmark,fillstyle='none')
ax.plot(mean_t,average_source_area_3/9e6,color=colors[2],linestyle=linestyles[2],label=None,marker=markers[2],markevery=dmark,fillstyle='none')

# Plot the average host area over time (divide by nine to get the average) in km2
ax2.plot(mean_t,average_host_area_1/9e6,color=colors[3],linestyle=linestyles[3],label=labels[3],marker=markers[3],markevery=dmark,fillstyle='none')
ax2.plot(mean_t,average_host_area_2/9e6,color=colors[4],linestyle=linestyles[4],label=labels[4],marker=markers[4],markevery=dmark,fillstyle='none')
ax2.plot(mean_t,average_host_area_3/9e6,color=colors[5],linestyle=linestyles[5],label=labels[5],marker=markers[5],markevery=dmark,fillstyle='none')

# Labelling of plot
ax.set_xlabel("Total extension [km]",weight="bold")
ax.set_ylabel(r"Source area [$\mathbf{km^2}$]",weight="bold", color=color_source)
# Grid
ax.grid(axis='x',color='0.95')
ax.grid(axis='y',color='0.95')

# Ranges of the axes
ax.set_xlim(-2.5,252.5) # km
ax.set_ylim(-1.2,121.2) # km2
# Ticks
ax.ticklabel_format(axis='y',useOffset=False)
ax.set_xticks(np.arange(0,300,50))
ax.set_yticks([0,30,60,90,120])

# Second subplot
# Transparent background
ax2.patch.set_facecolor('None')
ax2.set_ylabel("Host area [km$\mathbf{^2}$]", weight="bold", color=color_host)
ax2.legend(loc='upper left',ncol=1, columnspacing = 1.5)
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right')
ax2.set_ylim(-3.6,363.6)
ax2.set_yticks([0,90,180,270,360])

# No tight layout so that all graphs have the same shape
# and can be synthesized into one figure
#plt.tight_layout()
#fig.tight_layout()

# Name the png according to the plotted field
field='average_source_host_area_'
plt.savefig(output_name + '_CERI_' + str(field) + '.png',dpi=300,bbox_inches='tight')
print ("Output in: ", output_name + '_CERI_' + str(field) + '.png')

# Output svg
plt.savefig(output_name + '_CERI_' + str(field) + '.svg',dpi=300,bbox_inches='tight',format='svg')
print ("Output in: ", output_name + '_CERI_' + str(field) + '.svg')

# Also output an svg with y tick labels of the same, largest size
field='average_source_host_area_nolabel'
ax.set_yticklabels(["200","200","200","200","200"])
ax2.set_yticklabels(["1000","1000","1000","1000","1000"])
plt.savefig(output_name + '_CERI_' + str(field) + '.svg',dpi=300,bbox_inches='tight',format='svg')
print ("Output in: ", output_name + '_CERI_' + str(field) + '.svg')
