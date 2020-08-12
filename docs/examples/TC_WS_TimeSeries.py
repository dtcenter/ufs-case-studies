"""
Plotting Time Series of Vortex Center Max. WS
==========================================

This example plots time series of the maximum wind speed at the vortex center estimated from tc-tracker, as well as BestTrack data.
"""

from matplotlib import pyplot as plt
import numpy as np
import matplotlib


# Read GFSv15p2 vortext tracker results
csv_file = "GFSv15p2/fort.69"
tc = np.recfromcsv(csv_file, unpack=True, names=['stormid', 'count', 'initdate', 'constant', 'atcf', 'leadtime', 'lat','lon','ws','mslp','placehoder', 'thresh', 'neq', 'blank1', 'blank2', 'blank3','blank4','blank5','blank6','blank7'], dtype=None)

# Read GFSv16beta vortext tracker results
csv_file2 = "GFSv16beta/fort.69"
tc2 = np.recfromcsv(csv_file2, unpack=True, names=['stormid', 'count', 'initdate', 'constant', 'atcf', 'leadtime', 'lat','lon','ws','mslp','placehoder', 'thresh', 'neq', 'blank1', 'blank2', 'blank3','blank4','blank5','blank6','blank7'], dtype=None)

# Read BestTrack data
bal_file ="/home/Xia.Sun/PySripts/TC_tracker/bal022019_post.dat"
bal = np.recfromcsv(bal_file,unpack=True,delimiter=",",usecols=[0,2,6,7,8,9,10,11],names=['stormid','time','lat','lon','ws','mslp','intens','thresh'],dtype=None)

# Read in wind speed from BestTrack Data
balws=[]
for k in range(len(bal.lat)):
    if bal.thresh[k] == 34 or bal.thresh[k] == 0:
        balwsd=float(bal.ws[k])
        balws.append(balwsd)

# Read in wind speed from GFSv15p2
encoding='utf-8'
tcws=[]
for j in range(len(tc.ws)):
    tcstormid=str(tc.stormid[j],encoding)
    if tcstormid=='AL' and tc.count[j]== 2 and tc.thresh[j]==34 and tc.leadtime[j]<=9000:
        tcwsd=float(tc.ws[j])
        tcws.append(tcwsd) 

# Read in wind speed from GFSv16beta
tc2ws=[]
for j in range(len(tc2.ws)-1):
    tc2stormid=str(tc2.stormid[j],encoding)
    if tc2stormid=='AL' and tc2.count[j]==2 and tc2.thresh[j]==34 and tc2.leadtime[j]<=9000:
        tc2wsd=float(tc2.ws[j])
        tc2ws.append(tc2wsd)

# Make x axis
t=np.arange(0,16,1)

# Make the plot
plt.figure(figsize=(8,6)) 
plt.plot(t,tcws,'.-r',label="GFSv15p2")
plt.plot(t,tc2ws,'.-b',label="GFSv16beta")
plt.plot(t,balws,'.-k',label="BestTrack")
plt.legend(loc="upper left")
my_xticks=['11/00z','','11/12z','','12/00z','','12/12z','','13/00z','','13/12z','','14/00z','','14/12z','']
plt.xlabel('Date/Time (UTC)')
plt.ylabel('Maximum surface wind (kt)')
frequency=2
plt.xticks(t,my_xticks)
plt.show()
plt.savefig('tracker_ws_Barry_ufsv1.png')

# %%
# .. figure:: images/thumb/sphx_glr_tracker_ws_Barry_thumb.png
#  :width: 600
#  :align: center
