.. 2020ColdBiasCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. _2020 January Cold Bias:
2020 January Cold Bias
=====================================

Arctic blast brought cold air to Iowa, Minnesota, and Wisconsin on Jan 20, 2020.

..............................
Model Configuration and Datasets
..............................
.. tabs::
  .. group-tab:: MRW.v1.0

    The case runs are initialized at 12z Jan 17, 2020 with 120 hours forecasting. The corresponding namelist options that need to be changed are listed below. The app uses ``./xmlchange`` to change the runtime settings. The settings that need to be modified to set up the start date, start time, and run time are listed below.

    .. code-block:: bash
 
      ./xmlchange RUN_STARTDATE=2020-01-17,START_TOD=43200,STOP_OPTION=nhours,STOP_N=120


    Initial condition (IC) files are created from GFS operational dataset in NEMSIO format. The `GFS reanalysis dataset <https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs>`_ are used as 'truth' to compare with simulation results.

    .. container:: sphx-glr-footer
        :class: sphx-glr-footer-example



      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2020011712.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2020011712.gfs.nemsio.tar.gz>`
  .. group-tab:: GFS.v16.0.10

    The GFS model EMC global workflow points to the most up-to-date GFS model development code. The GFS.v16.0.10 is tested in C768 (~13km) resolution and in 128 vertical levels. It uses two scripts, ``setup_expt_fcstonly.py`` and ``setup_workflow_fcstonly.py`` to set up the mode simulation date and case directories.

    The case runs are initialized at 12z Jan 17, 2020 with 120 hours forecasting. The settings that need to be modified to set up the start date and directories are listed below. 

    .. code-block:: bash
 
      ./setup_expt_fcstonly.py --pslot 2020ColdBias --configdir /PATH/TO/YOUR/GLOBAL/WORKFLOW/parm/config --idate 2020011712 --edate 2020011712 --res 768 --comrot /PATH/TO/YOUR/EXP/DIR/comrot --expdir /PATH/TO/YOUR/EXP/OUTPUT/expdir 

    The account and simulation duration time can be set up in ``/expdir/2020ColdBias/config.base`` file. 

    .. code-block:: bash

      ./setup_workflow_fcstonly.py --expdir /PATH/TO/YOUR/OUTPUT/expdir/2020ColdBias

    Next step is to go to ``/expdir/2020ColdBias`` to submit the run by

    .. code-block:: bash
   
      crontab 2020ColdBias.crontab  

..............
Case Results
..............
======================================================
Synoptic Dynamics
======================================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2020JanCold/MSLP_MRW_v1.0_2020JanCold_trim.png
      :width: 1200
      :align: center

      Mean sea level pressure (hPa)

    .. figure:: images/2020JanCold/500mb_MRW_v1.0_2020JanCold_trim.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam), absolute vorticity (10 :sup:`-5`/s), and winds (m/s)

  .. group-tab:: GFS.v16.0.10

    .. figure:: images/2020JanCold/MSLP_GFS.v16.0.10_2020JanCold_trim.png
      :width: 1200
      :align: center

      Mean sea level pressure (hPa)

    .. figure:: images/2020JanCold/500mb_GFS.v16.0.10_2020JanCold_trim.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam), absolute vorticity (10 :sup:`-5`/s), and winds (m/s)

======================================================
Surface Temperature and Wind Speed
======================================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2020JanCold/2mT_MRW_v1.0_2020JanCold_trim.png
      :width: 1200
      :align: center

      2-m temperature (F) 

    .. figure:: images/2020JanCold/GUST_MRW_v1.0_2020JanCold_trim.png
      :width: 1200
      :align: center

      Surface gust (m/s)
  .. group-tab:: GFS.v16.0.10

    .. figure:: images/2020JanCold/2mT_GFS.v16.0.10_2020JanCold_trim.png
      :width: 1200
      :align: center

      2-m temperature (F)

    .. figure:: images/2020JanCold/GUST_GFS.v16.0.10_2020JanCold_trim.png
      :width: 1200
      :align: center

      Surface gust (m/s)