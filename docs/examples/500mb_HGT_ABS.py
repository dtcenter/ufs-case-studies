"""
Plotting 500mb Geopotential Height and Absolute Vorticity
==========================================

This example plots the 500mb geopotential height and absolute vorticity.

"""

from __future__ import print_function
import Ngl, Nio
import pandas as pd
import numpy as np
import xarray as xr
import netCDF4 as nc
from netCDF4 import Dataset
import matplotlib.pyplot as plt

# Read in NETCDF data
fv3=nc.MFDataset('GFSv16beta/GFSPRS.GrbF156.nc')
gridlat=fv3["latitude"][:]
gridlon=fv3["longitude"][:]
hgt=fv3["HGT_500mb"][0,:,:]*0.1
ugrd=fv3["UGRD_500mb"][0,:,:]
vgrd=fv3["VGRD_500mb"][0,:,:]
absv=fv3["ABSV_500mb"][0,:,:]*1e5
lat=gridlat
lon=gridlon
maxlat=lat.max()
minlat=lat.min()
maxlon=lon.max()
minlon=lon.min()

# Define work station and output figure name
wks_type = "png"
wks = Ngl.open_wks(wks_type,"GFSv16beta_500mb_Hgt_Abs")

# Define map resources
mpres = Ngl.Resources()
mpres.nglMaximize = False
mpres.nglFrame     = False
mpres.mpFillOn               = True
mpres.mpGridAndLimbOn = True
mpres.mpOceanFillColor       = "Transparent"
mpres.mpLandFillColor        = "Gray90"#"Gray90"
mpres.mpInlandWaterFillColor = "Transparent"
mpres.mpLimitMode        = "LatLon"
mpres.mpDataBaseVersion     = "MediumRes"
mpres.mpOutlineBoundarySets = "USStates"
mpres.mpUSStateLineThicknessF=2 
mpres.mpGeophysicalLineThicknessF= 2
mpres.mpCountyLineThicknessF=2
mpres.mpNationalLineThicknessF=2
mpres.mpGeophysicalLineColor="gray60"
mpres.mpNationalLineColor="gray60"
mpres.mpUSStateLineColor="gray60"
mpres.mpGridLineDashPattern=11
mpres.mpGridLineColor="grey60"

# Define plot resources
cnres                 = Ngl.Resources()
cnres.cnLevelSelectionMode="ExplicitLevels"# Contour resources

# Define color map attributes
cnres.cnFillColors=["Transparent","(/1.,.9607843,.8/)","(/1,0.9019608,0.4392157/)","(/1,.8,.2/)","(/1.,0.6862745,0.2/)","(/1.,0.6,0.2/)","(/1.,0.43529412,0.2, /)","(/1.,0.33333334,0./)","(/0.9019608,0.15686275,0.11764706/)","(/0.78431374,0.11764706,0.07843138/)"]
cnres.cnLevels    = [9,12,15,18,21,24,27,30]

# Define plot resources
cnres.cnFillOn        = True
cnres.cnLinesOn       = False
cnres.cnLineLabelsOn  = False
cnres.nglFrame    = False
cnres.tiXAxisString = "Lon"
cnres.tiYAxisString = "Lat"
cnres.lbOrientation   = "horizontal"
cnres.sfXArray        = lon[:]
cnres.sfYArray        = lat[:]

# Define resources for ABSV
cnres0=cnres
cnres0.lbLabelFontHeightF = 0.012
cnres0.pmLabelBarHeightF =0.1
cnres0.pmLabelBarWidthF=0.6
mpres.tiMainString = "MRW_GFSv16beta: 500mb Heights(dam) /Abs Vorticity (10^-5/s)/ Winds (m/s)  ~C~  Initialized: 12Z 25 Oct 2019 | Valid: 00Z 1 Nov 2019"
mpres.tiMainFontHeightF=0.012
mpres.tiMainPosition = "Center"

# Define resources for HGT
cnres1= Ngl.Resources()
cnres1.nglDraw=False
cnres1.nglFrame    = False
cnres1.cnFillOn    = False
cnres1.cnLinesOn = True
cnres1.sfXArray        = lon[:]
cnres1.sfYArray        = lat[:]
cnres1.cnLineThicknessF = 3.0
cnres1.cnLevelSelectionMode = "ManualLevels"
cnres1.cnMinLevelValF = 504#-45
cnres1.cnMaxLevelValF = 624
cnres1.cnLevelSpacingF=6
cnres1.cnInfoLabelOn   = False
cnres1.cnLineLabelBackgroundColor= "white"#"Transparent" 
cnres1.cnLineLabelDensityF=1.5
cnres1.cnLineLabelFontHeightF=0.008

# Define resources for wind field
resources= cnres
resources.nglDraw     = False
resources.nglFrame    = False
resources.vcMinFracLengthF = 1
resources.vcRefMagnitudeF  =10
resources.vcRefLengthF     = 0.025
resources.vcMinDistanceF = 0.025
resources.vcMonoLineArrowColor  = True   # Draw vectors in color.
resources.vfXArray=lon[:]
resources.vfYArray=lat[:]
resources.vcGlyphStyle = "WindBarb"

# Make plots for ABSV, wind field, and HGT
map=Ngl.map(wks,mpres)
pabsv=Ngl.contour(wks,absv[:,:],cnres0)
pwb=Ngl.vector(wks,ugrd,vgrd,resources)
phgt=Ngl.contour(wks,hgt[:,:],cnres1)

#Ovelay plots
Ngl.overlay(map,pabsv)
Ngl.overlay(map,phgt)
Ngl.overlay(map,pwb)
Ngl.draw(map)
Ngl.frame(wks)
Ngl.end()

# %%
# .. figure:: ../images/500mb_2019110100_GFSv16beta_150s.png
#  :width: 600
#  :align: center
