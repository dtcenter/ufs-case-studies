.. BarryCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



2019 Halloween Storm
=====================================

The 2019 Halloween storm stroke the eastern U.S. cities with wind gusts, thunderstorms, and flash flooding. 

..............................
Model Configuration and Datasets
..............................
.. tabs::
  .. group-tab:: MRW.v1.0

    The UFS Medium-Range Weather (MRW) Application (App) is used to prepare initial conditions, compile and run the UFS model, and post process the raw model outputs. Two model configuration compsets (``GFSv15p2`` and ``GFSv16beta``) are tested using the :emphasis:`C768` (~13km) spatial resolution with 64 vertical levels (default).

    The case runs are initialized at 12z Oct 25, 2019 with 120 hours forecasting. The corresponding namelist options that need to be changed are listed below. The app uses ``./xmlchange`` to change the runtime settings. The settings that need to be modified to set up the start date, start time, and run time are listed below.

    .. code-block:: bash
 
      ./xmlchange RUN_STARTDATE=20191025,START_TOD=43200,STOP_OPTION=nhours,STOP_N=120

    .. warning:: The model run time step is reduced from the default 225s to 150s in this case due to the model instability in GFSv16beta. To set the time step, add ``dt_atmos=150`` to ``user_nl_ufsatm``

    Initial condition (IC) files are created from GFS operational dataset in NEMSIO format. The `GFS reanalysis dataset <https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs>`_ are used as 'truth' to compare with simulation results.

    .. container:: sphx-glr-footer
       :class: sphx-glr-footer-example


      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2019102512.gfs.nemsio.tar.gz <https://domain.invalid/>`
  
  .. group-tab:: GFS.v16.0.10

    The GFS model EMC global workflow points to the most up-to-date GFS model development code. The GFS.v16.0.10 is tested in C768 (~13km) resolution and in 128 vertical levels. It uses to two scripts, ``./setup_expt_fcstonly.py`` and ``setup_workflow_fcstonly.py`` to set up the mode simulation date and case directories.

    The case runs are initialized at 12z Oct 25, 2019 with 120 hours forecasting. The settings that need to be modified to set up the start date and directories are listed below. 

    .. code-block:: bash
 
      ./setup_expt_fcstonly.py --pslot 2019Halloween --configdir /PATH/TO/YOUR/GLOBAL/WORKFLOW/parm/config --idate 2019071100 --edate 2019071100 --res 768 --comrot /PATH/TO/YOUR/EXP/DIR/comrot --expdir /PATH/TO/YOUR/EXP/OUTPUT/expdir 

    The account and simulation duration time can be set up in ``/expdir/2019Halloween/config.base`` file. 

    .. code-block:: bash

      ./setup_workflow_fcstonly.py --expdir /PATH/TO/YOUR/OUTPUT/expdir/Barry 

    Next step is to go to ``/expdir/2019Halloween`` to submit the run by

    .. code-block:: bash
   
      crontab Barry.crontab  
        
..............
Case Results
..............

======================================================
500 mb Geopotential Height and Absolute Vorticity Map
======================================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/500mb_2019110100_150s.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam), absolute vorticity (10 :sup:`-5`/s), and winds (m/s)

    * MRW_GFSv15p2 generates a progressive synoptic pattern compared with reanalysis data. 
    * MRW_GFSv16beta alleviates the progressiveness of synoptic pattern.
  .. group-tab:: GFS.v16.0.10

    .. figure:: images/Halloween_GFS.v16.0.10_500mb_2019110100.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam), absolute vorticity (10 :sup:`-5`/s), and winds (m/s)

    * GFS.v16.0.10 generates a progressive synoptic pattern compared with reanalysis data. 

====================================
Surface Gust and 2-m Temperature
====================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/Halloween_f156_GUST_surface.png
      :width: 1200
      :align: center

      Surface gust (m/s) valid at 00z 1 Nov 2019

    * MRW_GFSv15p2 captures the magnitudes of surface gust in GFS_ANL. 
    * MRW_GFSv16beta does not reach the peak of surface gust in GFS_ANL. 
    .. figure:: images/Haloween_f156_TMP_2maboveground.png
      :width: 1200
      :align: center

      2-m temperature (K) valid at 00z 1 Nov 2019 

    * Colder 2-m T in MRW_GFSv15p2 along the U.S. east coast compared with GFS_ANL
    * Colder 2-m T at New England and warmer 2-m T at the Southeast in MRW_GFSv16beta  
  .. group-tab:: GFS.v16.0.10

    .. figure:: images/Halloween_GFS16.0.10_f156_GUST_surface.png
      :width: 1200
      :align: center

      Surface gust (m/s) valid at 00z 1 Nov 2019

    * GFS.v16.0.10 does not capture the surface gust at the Great Lakes Region, accompanied by a faster-moving and narrower trough compared with GFS_ANL. 
      
    .. figure:: images/Halloween_GFS16.0.10_f156_TMP_2maboveground.png
      :width: 1200
      :align: center

      2-m temperature (K) valid at 00z 1 Nov 2019 

    * Colder 2-m T in GFS.v16.0.10 along the U.S. east coast compared with GFS_ANL


====================================
Composite Reflectivity
====================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/Halloween_f156_REFC_entireatmosphere.png
      :width: 1200
      :align: center

      Composite reflectivity (dB)
  .. group-tab:: GFS.v16.0.10

    .. figure:: images/Halloween_GFS16.0.10_f156_REFC_entireatmosphere.png
      :width: 1200
      :align: center

      Composite reflectivity (dB)  
