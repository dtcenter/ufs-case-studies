.. BarryCase documentation master file, created by
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

.. _2018 Hurricane Michael:
2018 Hurricane Michael
=====================================

................................
Model Configuration and Datasets
................................
.. tabs::
  .. group-tab:: MRW.v1.0

    The case runs are initialized at 00z Oct 07, 2018 with 120 hours forecasting. The app uses ``./xmlchange`` to change the runtime settings. The settings that need to be modified to set up the start date, start time, and run time are listed below.

    .. code-block:: bash
 
      ./xmlchange RUN_STARTDATE=2018-10-07,START_TOD=0,STOP_OPTION=nhours,STOP_N=120

    Initial condition (IC) files are created from GFS operational dataset in NEMSIO format. The `Stand-alone Geophysical Fluid Dynamics Laboratory (GFDL) Vortex Tracker <https://dtcenter.org/community-code/gfdl-vortex-tracker>`_ is a tool to estimate hurricane tracks and intensities. The `Best Track dataset <https://www.nhc.noaa.gov/data/#hurdat>`_ provides the ‘truth’ data for hurricane evolution.

    .. container:: sphx-glr-footer
        :class: sphx-glr-footer-example



      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2018100700.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2018100700.gfs.nemsio.tar.gz>`
  .. group-tab:: GFS.v16.0.10

    The GFS model EMC global workflow points to the most up-to-date GFS model development code. The GFS.v16.0.10 is tested in C768 (~13km) resolution and in 128 vertical levels. It uses two scripts, ``setup_expt_fcstonly.py`` and ``setup_workflow_fcstonly.py`` to set up the mode simulation date and case directories.

    The case runs are initialized at 00z Oct 07, 2018 with 120 hours forecasting. The settings that need to be modified to set up the start date and directories are listed below. 

    .. code-block:: bash
 
      ./setup_expt_fcstonly.py --pslot Michael --configdir /PATH/TO/YOUR/GLOBAL/WORKFLOW/parm/config --idate 2018100700 --edate 2018100700 --res 768 --comrot /PATH/TO/YOUR/EXP/DIR/comrot --expdir /PATH/TO/YOUR/EXP/OUTPUT/expdir 

    The account and simulation duration time can be set up in ``/expdir/Michael/config.base`` file. 

    .. code-block:: bash

      ./setup_workflow_fcstonly.py --expdir /PATH/TO/YOUR/OUTPUT/expdir/Michael

    Next step is to go to ``/expdir/Michael`` to submit the run by

    .. code-block:: bash
   
      crontab Michael.crontab     
..............
Case Results
..............

==============================
Hurricane Track and Intensity
==============================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2018Michael/tracker_Michael_ufsv1.png
      :width: 400
      :align: center

      Hurricane tracks from MRW_GFSv16beta (red line), MRW_GFSv15p2 (blue line), and Best Track (black line). The dots are color coded with the vortex maximum 10-m wind speed (WS, kt). 

    * MRW_GFSv16beta and MRW_GFSv15p2 generate left-of-track bias. 
    * MRW_GFSv16beta and MRW_GFSv15p2 do not capture the hurricane intensities (represented by max WS), especially before the landfall.


    .. figure:: images/2018Michael/tracker_timeseries_Michael_ufsv1.png
      :width: 1200
      :align: center

      Time series of the vortex maximum surface wind speed (WS, left panel) and minimum mean sea level pressure (MSLP, right panel)
  
  .. group-tab:: GFS.v16.0.10

     .. figure:: images/2018Michael/tracker_Michael_GFS.v16.0.10.png
      :width: 400
      :align: center

      Hurricane tracks from GFS.v16.0.10 (red line) and Best Track (black line). The dots are color coded with the vortex maximum 10-m wind speed (WS, kt). 

    * GFS.v16.0.10 generates left-of-track bias. 

    .. figure:: images/2018Michael/tracker_ws_mslp_Michael_GFS.v16.0.10.png
      :width: 1200
      :align: center
      
      Time series of the vortex maximum surface wind speed (WS, left panel) and minimum mean sea level pressure (MSLP, right panel) 


