.. 2019MemHeatCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   
.. _2019 Memorial Day Heat Wave:

2019 Memorial Day Heat Wave
=====================================

A heat wave occurred on the weekend of 2019 Memorial Day across the Southeastern U.S. 

..............................
Model Configuration and Datasets
..............................
.. tabs::
  .. group-tab:: MRW.v1.0

    The case runs are initialized at 00z May 23, 2019 with 120 hours forecasting. The corresponding namelist options that need to be changed are listed below. The app uses ``./xmlchange`` to change the runtime settings. The settings that need to be modified to set up the start date, start time, and run time are listed below.

    .. code-block:: bash
 
      ./xmlchange RUN_STARTDATE=2019-05-23,START_TOD=0,STOP_OPTION=nhours,STOP_N=120


    Initial condition (IC) files are created from GFS operational dataset in NEMSIO format. The `GFS reanalysis dataset <https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs>`_ are used as 'truth' to compare with simulation results.

    .. container:: sphx-glr-footer
        :class: sphx-glr-footer-example



      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2019052300_srw.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2019052300_srw.gfs.nemsio.tar.gz>`
  .. group-tab:: GFS.v16.0.10

    The GFS model EMC global workflow points to the most up-to-date GFS model development code. The GFS.v16.0.10 is tested in C768 (~13km) resolution and in 128 vertical levels. It uses two scripts, ``setup_expt_fcstonly.py`` and ``setup_workflow_fcstonly.py`` to set up the mode simulation date and case directories.

    The case runs are initialized at 00z May 23, 2019 with 120 hours forecasting. The settings that need to be modified to set up the start date and directories are listed below. 

    .. code-block:: bash
 
      ./setup_expt_fcstonly.py --pslot 2019MemHeat --configdir /PATH/TO/YOUR/GLOBAL/WORKFLOW/parm/config --idate 2019052300 --edate 2019052300 --res 768 --comrot /PATH/TO/YOUR/EXP/DIR/comrot --expdir /PATH/TO/YOUR/EXP/OUTPUT/expdir 

    The account and simulation duration time can be set up in ``/expdir/2019MemHeat/config.base`` file. 

    .. code-block:: bash

      ./setup_workflow_fcstonly.py --expdir /PATH/TO/YOUR/OUTPUT/expdir/2019MemHeat

    Next step is to go to ``/expdir/2019MemHeat`` to submit the run by

    .. code-block:: bash
   
      crontab 2019MemHeat.crontab

  .. group-tab:: SRW.v1.0

    The case was initialized at 00z May 23, 2019 and forecast out to 90 hours. The app uses ``config.sh`` to define the runtime settings. The settings that need to be modified to set up the first cycle, last cycle, forecast length and cycle hour are listed below. 

    .. code-block:: bash
 
      FCST_LEN_HRS="90"
      LBC_SPEC_INTVL_HRS="3"
      DATE_FIRST_CYCL="20190523"
      DATE_LAST_CYCL="20190523"
      CYCL_HRS=( "00" )

    Initial condition (IC) and boundary condition (BC) files are created from GFS operational dataset in NEMSIO format. The `RAP reanalysis dataset <https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/rapid-refresh-rap>`_ are used as 'truth' to compare with simulation results. 

    .. container:: sphx-glr-footer
        :class: sphx-glr-footer-example



      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2019052300.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2019052300.gfs.nemsio.tar.gz>`
        :download:`Download boundary condition files: 2019052300_bc.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2019052300_bc.gfs.nemsio.tar.gz>`

..............
Case Results
..............
======================================================
Synoptic Dynamics
======================================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2019MemHeat/MSLP_MRW_v1.0_2019MemHeat_trim.png
      :width: 1200
      :align: center

      Mean sea level pressure (hPa)

    .. figure:: images/2019MemHeat/500mb_MRW_v1.0_2019MemHeat_trim.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam) and absolute vorticity (10 :sup:`-5`/s)

    * The synoptic patterns at surface and 500hPa from the two physics compsets agree well with GFS_ANL.
    
  .. group-tab:: GFS.v16.0.10

    .. figure:: images/2019MemHeat/MSLP_GFS.v16.0.10_2019MemHeat_trim.png
      :width: 1200
      :align: center

      Mean sea level pressure (hPa)

    .. figure:: images/2019MemHeat/500mb_GFS.v16.0.10_2019MemHeat_trim.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam) and absolute vorticity (10 :sup:`-5`/s)

    * The synoptic patterns at surface and 500hPa from GFS.v16.0.10 agree well with GFS_ANL.
  .. group-tab:: SRW.v1.0

    .. figure:: images/2019MemHeat/MSLP_SRW_v1.0_2019MemHeat_trim.png
      :width: 1200
      :align: center

      Mean sea level pressure (hPa)

    .. figure:: images/2019MemHeat/500mb_SRW_v1.0_2019MemHeat_trim.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam) and absolute vorticity (10 :sup:`-5`/s)

    * The synoptic patterns at surface and 500hPa from the two physics compsets agree well with RAP_ANL.
    

======================================================
Surface Temperature
======================================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2019MemHeat/2mT_MRW_v1.0_2019MemHeat_RAP_trim.png
      :width: 1200
      :align: center

      2-m temperature (F) 

    * MRW_GFSv15p2 forecasts the heat wave better than MRW_GFSv16beta across the Southeast.
    * There is cold bias over the contiguous U.S. (CONUS) in MRW_GFSv16beta.

  .. group-tab:: GFS.v16.0.10

    .. figure:: images/2019MemHeat/2mT_GFS.v16.0.10_2019MemHeat_RAP_trim.png
      :width: 1200
      :align: center

      2-m temperature (F)

    * GFS.v16.0.10 successfully captures the high temperatures across the Southeast.
  .. group-tab:: SRW.v1.0

    .. figure:: images/2019MemHeat/2mT_SRW_v1.0_2019MemHeat_RAP_trim.png
      :width: 1200
      :align: center

      2-m temperature (F) 

    * SRW_GFSv15p2 forecasts the heat wave better than SRW_RRFSv1alpha across the Southeast.
    * There is warm bias over the contiguous U.S. (CONUS) in SRW_RRFSv1alpha.

......................
Summary and Discussion
......................

MRW_GFSv16beta generates a cold bias for 2-m temperature over most of CONUS during the 2019 Memorial Day Heat Wave event. However, both MRW.GFSv15p2 and GFS.v16.0.10 simulate the extreme temperature well over the Southeastern U.S. This means that the cold bias of this extreme temperature case in the GFS model is already fixed in the following physics developments (see `Timeline of physics frozen`_ for the different model versions). The heat wave signal in SRW_RRFSv1alpha is too strong.

.. _Timeline of physics frozen: _images/TimeLine_Oct2020.png
