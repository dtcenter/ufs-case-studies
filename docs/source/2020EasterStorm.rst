.. BarryCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

   
.. _2020 Easter Sunday Storm:
2020 Easter Sunday Storm
=====================================

The 2020 Easter Sunday storm is a widespread tornado outbreak that affected the Southeastern U.S on Apr 12-13.  

..............................
Model Configuration and Datasets
..............................
.. tabs::
  .. group-tab:: MRW.v1.0

    The UFS Medium-Range Weather (MRW) Application (App) is used to prepare initial conditions, compile and run the UFS model, and post process the raw model outputs. Two model configuration compsets (``GFSv15p2`` and ``GFSv16beta``) are tested using the :emphasis:`C768` (~13km) spatial resolution with 64 vertical levels (default).

    The case runs are initialized at 12z Apr 07, 2020 with 120 hours forecasting. The corresponding namelist options that need to be changed are listed below. The app uses ``./xmlchange`` to change the runtime settings. The settings that need to be modified to set up the start date, start time, and run time are listed below.

    .. code-block:: bash
 
      ./xmlchange RUN_STARTDATE=20200407,START_TOD=43200,STOP_OPTION=nhours,STOP_N=120

    Initial condition (IC) files are created from GFS operational dataset in NEMSIO format. The `GFS reanalysis dataset <https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs>`_ are used as 'truth' to compare with simulation results.

    .. container:: sphx-glr-footer
       :class: sphx-glr-footer-example


      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2020040712.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2020040712.gfs.nemsio.tar.gz>`
  
  .. group-tab:: GFS.v16.0.10

    The GFS model EMC global workflow points to the most up-to-date GFS model development code. The GFS.v16.0.10 is tested in C768 (~13km) resolution and in 128 vertical levels. It uses two scripts, ``setup_expt_fcstonly.py`` and ``setup_workflow_fcstonly.py`` to set up the mode simulation date and case directories.

    The case runs are initialized at 12z Apr 07, 2020 with 120 hours forecasting. The settings that need to be modified to set up the start date and directories are listed below. 

    .. code-block:: bash
 
      ./setup_expt_fcstonly.py --pslot 2020Easter --configdir /PATH/TO/YOUR/GLOBAL/WORKFLOW/parm/config --idate 2020040712 --edate 2020040712 --res 768 --comrot /PATH/TO/YOUR/EXP/DIR/comrot --expdir /PATH/TO/YOUR/EXP/OUTPUT/expdir 

    The account and simulation duration time can be set up in ``/expdir/2020Easter/config.base`` file. 

    .. code-block:: bash

      ./setup_workflow_fcstonly.py --expdir /PATH/TO/YOUR/OUTPUT/expdir/2020Easter

    Next step is to go to ``/expdir/2020Easter`` to submit the run by

    .. code-block:: bash
   
      crontab 2020Easter.crontab  
        
..............
Case Results
..............
======================================================
Synoptic Dynamics
======================================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2020Easter/MSLP_MRW_v1.0_2020EasterStorm_trim.png
      :width: 1200
      :align: center

      Mean sea level pressure (hPa)

    * MRW_GFSv16beta more correctly forecasts the surface low compared with MRW_GFSv15p2.

    .. figure:: images/2020Easter/500mb_MRW_v1.0_2020EasterStorm_trim.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam), absolute vorticity (10 :sup:`-5`/s), and winds (m/s)

    * Stronger positive tilted trough in MRW_GFSv15p2, suggesting a weakening weather system compared with GFS_ANL.
  .. group-tab:: GFS.v16.0.10

    .. figure:: images/2020Easter/MSLP_GFS.v16.0.10_2020EasterStorm_trim.png
      :width: 1200
      :align: center

      Mean sea level pressure (hPa)

    * GFS.v16.0.10 generates a surface low eastward of GFS_ANL. 

    .. figure:: images/2020Easter/500mb_GFS.v16.0.10_2020EasterStorm_trim.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam), absolute vorticity (10 :sup:`-5`/s), and winds (m/s)

    * GFS.v16.0.10 generates a progressive synoptic pattern compared GFS_ANL. 

====================================
Surface Temperature and Wind Speed
====================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2020Easter/2mT_MRW_v1.0_2020EasterStorm_trim.png
      :width: 1200
      :align: center

      2-m temperature (F)

    * Colder 2-m T in both MRW_GFSv15p2 and MRW_GFSv16beta over central and eastern U.S.

    .. figure:: images/2020Easter/GUST_MRW_v1.0_2020EasterStorm_trim.png
      :width: 1200
      :align: center

      Surface gust (m/s)

    * MRW_GFSv16beta more correctly captures the magnitudes of surface gust at the Gulf of Mexico compared with MRW_GFSv15p2.
  .. group-tab:: GFS.v16.0.10

    .. figure:: images/2020Easter/2mT_GFS.v16.0.10_2020EasterStorm_trim.png
      :width: 1200
      :align: center

      2-m temperature (F)

    * Colder 2-m T in GFS.v16.0.10 over Texas and Oklahoma compared with GFS_ANL
    .. figure:: images/2020Easter/GUST_GFS.v16.0.10_2020EasterStorm_trim.png
      :width: 1200
      :align: center

      Surface gust (m/s)

    * GFS.v16.0.10 generates higher magnitudes of surface gust over the Southeastern U.S. which is related to the progressive synoptic pattern compared with GFS_ANL. 

