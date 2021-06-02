.. Lorenzo Case documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
.. raw:: html

    <style> .red {color:red} 
    .green{color:green}
    .cyan{color:#00D7D7}
    .purple{color:purple}
    .blue{color:blue}
    .yellow{color:#CDCD00}

    </style>

.. role:: red
.. role:: green
.. role:: cyan
.. role:: purple
.. role:: blue
.. role:: yellow

.. _2019 Hurricane Lorenzo:
2019 Hurricane Lorenzo
=====================================
Hurricane Lorenzo was a category 5 hurricane and the second deadliest hurricane in 2019. The initial peak intensity of 125 kt occurred at around 0000 UTC on 27 September. Meanwhile, the hurricane slowed and turned northwestward in response to a break that developed within the subtropical ridge at the Atlantic Ocean (`Zelinsky 2019 <https://www.nhc.noaa.gov/data/tcr/AL132019_Lorenzo.pdf>`_).

................................
Model Configuration and Datasets
................................
.. tabs::
  .. group-tab:: MRW.v1.0

    The case runs are initialized at 12z Sep 25, 2019 with 120 hours forecasting. The app uses ``./xmlchange`` to change the runtime settings. The settings that need to be modified to set up the start date, start time, and run time are listed below.

    .. code-block:: bash
 
      ./xmlchange RUN_STARTDATE=2019-09-25,START_TOD=43200,STOP_OPTION=nhours,STOP_N=120

    Initial condition (IC) files are created from GFS operational dataset in NEMSIO format. The `Stand-alone Geophysical Fluid Dynamics Laboratory (GFDL) Vortex Tracker <https://dtcenter.org/community-code/gfdl-vortex-tracker>`_ is a tool to estimate hurricane tracks and intensities. The `Best Track dataset <https://www.nhc.noaa.gov/data/#hurdat>`_ provides the ‘truth’ data for hurricane evolution.

    .. container:: sphx-glr-footer
        :class: sphx-glr-footer-example



      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2019092512.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2019092512.gfs.nemsio.tar.gz>`
  .. group-tab:: GFS.v16.0.10

    The GFS model EMC global workflow points to the most up-to-date GFS model development code. The GFS.v16.0.10 is tested in C768 (~13km) resolution and in 128 vertical levels. It uses two scripts, ``setup_expt_fcstonly.py`` and ``setup_workflow_fcstonly.py`` to set up the mode simulation date and case directories.

    The case runs are initialized at 12z Sep 25, 2019 with 120 hours forecasting. The settings that need to be modified to set up the start date and directories are listed below. 

    .. code-block:: bash
 
      ./setup_expt_fcstonly.py --pslot Lorenzo --configdir /PATH/TO/YOUR/GLOBAL/WORKFLOW/parm/config --idate 2019092512 --edate 2019092512 --res 768 --comrot /PATH/TO/YOUR/EXP/DIR/comrot --expdir /PATH/TO/YOUR/EXP/OUTPUT/expdir 

    The account and simulation duration time can be set up in ``/expdir/Lorenzo/config.base`` file. 

    .. code-block:: bash

      ./setup_workflow_fcstonly.py --expdir /PATH/TO/YOUR/OUTPUT/expdir/Lorenzo

    Next step is to go to ``/expdir/Lorenzo`` to submit the run by

    .. code-block:: bash
   
      crontab Lorenzo.crontab     

  .. group-tab:: SRW.v1.0

    The case was initialized at 12z Sep 25, 2019 and forecast out to 90 hours. The app uses ``config.sh`` to define the runtime settings. The settings that need to be modified to set up the first cycle, last cycle, forecast length and cycle hour are listed below.

    .. code-block:: bash

      FCST_LEN_HRS="90"
      LBC_SPEC_INTVL_HRS="3"
      DATE_FIRST_CYCL="20190925"
      DATE_LAST_CYCL="20190925"
      CYCL_HRS=( "12" )

    Initial condition (IC) and boundary condition (BC) files are created from GFS operational dataset in NEMSIO format. 

    .. container:: sphx-glr-footer
        :class: sphx-glr-footer-example



      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2019092512.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2019092512.gfs.nemsio.tar.gz>`
        :download:`Download boundary condition files: 2019092512_bc.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2019092512_bc.gfs.nemsio.tar.gz>`

..............
Case Results
..............

==============================
Hurricane Track and Intensity
==============================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2019Lorenzo/tracker_Lorenzo_MRW.v1.0.png
      :width: 400
      :align: center

      Hurricane tracks from MRW_GFSv16beta (blue line), MRW_GFSv15p2 (red line), and Best Track (black line). The dots are color-coded with the vortex maximum 10-m wind speed (WS, kt). 

    * MRW_GFSv16beta and MRW_GFSv15p2 generate right-of-track bias. Hurricane track from MRW_GFSv16beta is closer to the Best Track compared with MRW_GFSv16beta. 
    * MRW_GFSv16beta and MRW_GFSv15p2 do not capture the hurricane intensities (represented by max WS).


    .. figure:: images/2019Lorenzo/tracker_ws_mslp_Lorenzo_MRW.v1.0.png
      :width: 1200
      :align: center

      Time series of the vortex maximum surface wind speed (WS, left panel) and minimum mean sea level pressure (MSLP, right panel)

    * The maximum surface wind speed at the vortex center in MRW_GFSv15p2 is larger than MRW_GFSv16beta. However, both two physics compsets do not reach the peak intensity identified in Best Track data.
    * The minimum sea level pressures from MRW_GFSv15p2 and MRW_GFSv16beta are both larger than Best Track data.
  
  .. group-tab:: GFS.v16.0.10

     .. figure:: images/2019Lorenzo/tracker_Lorenzo_GFS.v16.0.10.png
      :width: 400
      :align: center

      Hurricane tracks from GFS.v16.0.10 (blue line) and Best Track (black line). The dots are color-coded with the vortex maximum 10-m wind speed (WS, kt). 

    * GFS.v16.0.10 generates right-of-track bias. 

    .. figure:: images/2019Lorenzo/tracker_ws_mslp_Lorenzo_GFS.v16.0.10.png
      :width: 1200
      :align: center
      
      Time series of the vortex maximum surface wind speed (WS, left panel) and minimum mean sea level pressure (MSLP, right panel)

    * The maximum surface wind speed at the vortex center in GFS.v16.0.10 is lower than Best Track data.
    * The minimum sea level pressure from GFS.v16.0.10 is larger than the Best Track data. 

  .. group-tab:: SRW.v1.0

    .. figure:: images/2019Lorenzo/tracker_Lorenzo_SRW.v1.0.png
      :width: 400
      :align: center

      Hurricane tracks from SRW_RRFSv1alpha (blue line), SRW_GFSv15p2 (purple dash line), MRW_GFSv15p2 (red line), and Best Track (black line). The dots are color-coded with the vortex maximum 10-m wind speed (WS, kt). 

    * All generate right-of-track bias. Hurricane track from SRW_RRFSv1alpha is closer to the Best Track compared with SRW_GFSv15p2 and MRW_GFSv15p2. 
    * SRW_RRFSv1alpha, SRW_GFSv15p2 and MRW_GFSv15p2 do not capture the hurricane intensities (represented by max WS).


    .. figure:: images/2019Lorenzo/tracker_ws_mslp_Lorenzo_SRW.v1.0.png
      :width: 1200
      :align: center

      Time series of the vortex maximum surface wind speed (WS, left panel) and minimum mean sea level pressure (MSLP, right panel)

    * The maximum surface wind speed at the vortex center in SRW_GFSv15p2 is larger than MRW_GFSv15p2 and SRW_RRFSv1alpha. However, none of the physics compsets reaches the peak intensity identified in Best Track data.
    * The minimum sea level pressures from SRW_RRFSv1alpha, SRW_GFSv15p2 and MRW_GFSv15p2 are all larger than Best Track data.
  

==============================
N. Atl. Subtropical High
==============================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2019Lorenzo/850mb_HGT_Avg_St_2019Lorenzo_MRW_v1.0_trim.png
      :width: 400
      :align: center

      North Atlantic (N. Atl.) Subtropical high boundary (1540 gpm at 850 hPa) from MRW_GFSv16beta (blue line), MRW_GFSv15p2 (red line), and ECMWF Reanalysis v5 (ERA5) (black line). 

    * The subtropical ridges simulated from MRW_GFSv16beta and MRW_GFSv15p2 are located east of the one in ECMWF Reanalysis v5 (ERA5).

  
  .. group-tab:: GFS.v16.0.10

     .. figure:: images/2019Lorenzo/850mb_HGT_Avg_St_2019Lorenzo_GFS.v16.0.10_trim.png
      :width: 400
      :align: center

      North Atlantic Subtropical high boundary (1540 gpm at 850 hPa) from GFS.v16.0.10 (red line) and ECMWF Reanalysis v5 (ERA5) (black line).  

    * GFS.v16.0.10 generates a subtropical ridge east of the one in ECMWF Reanalysis v5 (ERA5).

......................
Summary and Discussion
......................

The physics compset of GFS.v16beta shows improvements in simulating the tracks of hurricane Lorenzo compared with MRW_GFSv15p2. This is related to its better handling of the subtropical high location over the N. Atl. Ocean. However, the MRW_GFSv16beta does not show improvements in capturing the maximum wind speed and minimum surface pressure at the vortex center. In GFS.v.16.10, the right-of-track bias of hurricane Lorenzo over the N. Atl. Ocean still exists. The misrepresentation of the position and/or strength of the subtropical ridge is a key element to explain Lorenzo's early recurvature.

**References**

Zelinsky D A. (2019). National Hurricane Center Tropical Cyclone Report: Hurricane Lorenzo [J]. https://www.nhc.noaa.gov/data/tcr/AL132019_Lorenzo.pdf. [`Link <https://www.nhc.noaa.gov/data/tcr/AL132019_Lorenzo.pdf>`_]
