.. BarryCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. _2019 Halloween Storm:
2019 Halloween Storm
=====================================

The 2019 Halloween storm struck the eastern U.S. cities with wind gusts, thunderstorms, and flash flooding. 

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

        :download:`Download initial condition files: 2019102512.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2019102512.gfs.nemsio.tar.gz>`
  
  .. group-tab:: GFS.v16.0.10

    The GFS model EMC global workflow points to the most up-to-date GFS model development code. The GFS.v16.0.10 is tested in C768 (~13km) resolution and in 128 vertical levels. It uses two scripts, ``setup_expt_fcstonly.py`` and ``setup_workflow_fcstonly.py`` to set up the mode simulation date and case directories.

    The case runs are initialized at 12z Oct 25, 2019 with 120 hours forecasting. The settings that need to be modified to set up the start date and directories are listed below. 

    .. code-block:: bash
 
      ./setup_expt_fcstonly.py --pslot 2019Halloween --configdir /PATH/TO/YOUR/GLOBAL/WORKFLOW/parm/config --idate 2019102512 --edate 2019102512 --res 768 --comrot /PATH/TO/YOUR/EXP/DIR/comrot --expdir /PATH/TO/YOUR/EXP/OUTPUT/expdir 

    The account and simulation duration time can be set up in ``/expdir/2019Halloween/config.base`` file. 

    .. code-block:: bash

      ./setup_workflow_fcstonly.py --expdir /PATH/TO/YOUR/OUTPUT/expdir/2019Halloween

    Next step is to go to ``/expdir/2019Halloween`` to submit the run by

    .. code-block:: bash
   
      crontab 2019Halloween.crontab  
        
  .. group-tab:: SRW.v1.0

    The UFS Short-Range Weather (SRW) Application (App) is used to prepare initial conditions, compile and run the UFS model, and postprocess the raw model outputs. Two model configuration compsets (``GFSv15p2`` and ``RRFSv1alpha``) are tested using the :emphasis:`C768` (~13km) spatial resolution with 64 vertical levels (default).

    The case was initialized at 12z Oct 28, 2019 and forecast out to 90 hours. The app uses ``config.sh`` to define the runtime settings. The settings that need to be modified to set up the first cycle, last cycle, forecast length and cycle hour are listed below.

    .. code-block:: bash
 
      FCST_LEN_HRS="90"
      LBC_SPEC_INTVL_HRS="3"
      DATE_FIRST_CYCL="20191028"
      DATE_LAST_CYCL="20191028"
      CYCL_HRS=( "12" )

    Initial condition (IC) and boundary condition (BC) files are created from GFS operational dataset in NEMSIO format. The `RAP reanalysis dataset (RAP_ANL) <https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/rapid-refresh-rap>`_ are used as 'truth' to compare with simulation results.

    .. container:: sphx-glr-footer
       :class: sphx-glr-footer-example


      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2019102812.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2019102812.gfs.nemsio.tar.gz>`
	:download:`Download the script for getting boundary conditions: get_hsup_bc_ic.sh <./get_hsup_bc_ic.sh>`
  
..............
Case Results
..............
======================================================
Synoptic Dynamics
======================================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2019Halloween/MSLP_MRW_v1.0_2019HalloweenStorm_trim.png
      :width: 1200
      :align: center

      Mean sea-level pressure (MSLP, hPa)

    * MRW_GFSv15p2 simulates the sea level pressure structure more reasonably than MRW_GFSv16beta.

    .. figure:: images/2019Halloween/500mb_MRW_v1.0_2019HalloweenStorm_trim.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam) and absolute vorticity (10 :sup:`-5`/s)

    * MRW_GFSv15p2 generates a progressive synoptic pattern compared with reanalysis data.
    * MRW_GFSv16beta alleviates the progressiveness of synoptic pattern.     
  .. group-tab:: GFS.v16.0.10

    .. figure:: images/2019Halloween/MSLP_GFS.v16.0.10_2019HalloweenStorm_trim.png
      :width: 1200
      :align: center

      Mean sea-level pressure (MSLP, hPa)

    * The strength of sea level pressure gradient is weaker in GFS.v16.0.10 over the Northeastern U.S.
    * Higher sea level pressure controls the U.S. east coast in GFS.v16.0.10.

    .. figure:: images/2019Halloween/500mb_GFS.v16.0.10_2019HalloweenStorm_trim.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam) and absolute vorticity (10 :sup:`-5`/s)

    * GFS.v16.0.10 generates a progressive synoptic pattern compared with reanalysis data.
    * The positive tilted trough in GFS.v16.0.10, versus the negative tilted trough in GFS_ANL, indicates a less severe storm over the eastern U.S.
  .. group-tab:: SRW.v1.0

    .. figure:: images/2019Halloween/MSLP_SRW_v1.0_2019HalloweenStorm_trim.png
      :width: 1200
      :align: center

      Mean sea-level pressure (MSLP, hPa)

    * SRW_GFSv15p2 simulates the sea level pressure structure better than SRW_RRFSv1alpha. The MSLP from SRW_RRFSv1alpha is very noisy over Rocky mountain area.

    .. figure:: images/2019Halloween/500mb_SRW_v1.0_2019HalloweenStorm_trim.png
      :width: 1200
      :align: center

      500 hPa geopotential heights (dam) and absolute vorticity (10 :sup:`-5`/s)

    * The trough position is well represented in SRW_GFSv15p2 and SRW_RRFSv1alpha
    * The results over Rocky mountain are noisy for both SRW_GFSv15p2 and SRW_RRFSv1alpha.

====================================
Surface Temperature and Wind Speed
====================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2019Halloween/2mT_MRW_v1.0_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      2-m temperature (F) valid at 00z 1 Nov 2019 

    * Colder 2-m T in MRW_GFSv15p2 along the U.S. east coast compared with RAP_ANL.
    * Colder 2-m T at New England and warmer 2-m T at the Southeast in MRW_GFSv16beta.

    .. figure:: images/2019Halloween/GUST_MRW_v1.0_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      Surface gust (m/s) valid at 00z 1 Nov 2019

    * Negative biases of surface gust over the eastern U.S. for both MRW_GFSv15p2 and MRW_GFSv16beta compared with RAP_ANL.
  .. group-tab:: GFS.v16.0.10

    .. figure:: images/2019Halloween/2mT_GFS.v16.0.10_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      2-m temperature (F) valid at 00z 1 Nov 2019 

    * Colder 2-m T in GFS.v16.0.10 along the U.S. east coast compared with RAP_ANL.

    .. figure:: images/2019Halloween/GUST_GFS.v16.0.10_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      Surface gust (m/s) valid at 00z 1 Nov 2019

    * GFS.v16.0.10 does not capture the surface gust at the Great Lakes Region, accompanied by a faster-moving and narrower trough compared with analysis data.
  .. group-tab:: SRW.v1.0

    .. figure:: images/2019Halloween/2mT_SRW_v1.0_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      2-m temperature (F) valid at 00z 1 Nov 2019 

    * Colder 2-m T in SRW_RRFSv1apha  along the U.S. northeast coast compared with RAP_ANL.
    * Warmer 2-m T in SRW_RRFSv1alpha at central and eastern U.S.
    * Colder 2-m T at New England and warmer 2-m T at the Northwest in SRW_GFSv15p2.

    .. figure:: images/2019Halloween/GUST_SRW_v1.0_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      Surface gust (m/s) valid at 00z 1 Nov 2019

    * Negative biases of surface gust over the eastern U.S. for both SRW_GFSv15p2 and SRW_RRFSv1alpha compared with RAP_ANL.

====================================
Moisture/Precipitation
====================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2019Halloween/2mRH_MRW_v1.0_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      2-m relative Humidity (RH,%) valid at 00z 1 Nov 2019

    * Dryline across the central U.S. is not simulated well in the two physics compsets.

    .. figure:: images/2019Halloween/Refc_MRW_v1.0_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      Composite reflectivity (dB) valid at 00z 1 Nov 2019 

    * The precipitation location lags behind the MRW_GFSv16beta compared with RAP_ANL, while the precipitation location moves further northeastwards in MRW_GFSv15p2 compared with RAP_ANL. 
  .. group-tab:: GFS.v16.0.10

    .. figure:: images/2019Halloween/2mRH_GFS.v16.0.10_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      2-m relative Humidity (RH,%) valid at 00z 1 Nov 2019 

    * The dryline across the middle U.S. blurs out in GFS.v16.0.10.
    * Dry bias over the Eastern U.S. and wet bias over the Western U.S.  

    .. figure:: images/2019Halloween/Refc_GFS.v16.0.10_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      Composite reflectivity (dB) valid at 00z 1 Nov 2019  

    * Lower composite reflectivity values suggest less intensive precipitation over the Northeastern U.S. 
      
  .. group-tab:: SRW.v1.0

    .. figure:: images/2019Halloween/2mRH_SRW_v1.0_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      2-m relative Humidity (RH,%) valid at 00z 1 Nov 2019

    * Dryline across the central U.S. is not simulated well in the two physics compsets.

    .. figure:: images/2019Halloween/Refc_SRW_v1.0_2019HalloweenStorm_RAP_trim.png
      :width: 1200
      :align: center

      Composite reflectivity (dB) valid at 00z 1 Nov 2019 

    * The rainband orientation in SRW_RRFSv1alpha and SRW_GFSv15p2 is slightly different than that in RAP_ANL. The results from SRW_GFSv15p2 is sligtly stronger and better than that from SRW_RRFSv1alpha. 

......................
Summary and Discussion
......................

MRW_GFSv15p2 generates a progressive synoptic pattern during the 2019 Halloween Storm, while MRW_GFSv16beta generates a regressive synoptic pattern compared with GFS analysis data. GFS.v16.0.10 alleviates the progressiveness of MRW_GFSv15p2 but still generates a cold bias along the U.S. east coast. Major changes in GFS.v16 from GFS.v15 can be referred to `Yang (2020) <https://ufscommunity.org/wp-content/uploads/2020/10/UFS_Webnair_GFSv16_20201022_FanglinYang.pdf>`_.
The sea level structure in SRW_GFSv15p2 is more reasonably simulated than that in SRW_RRFSv1alpha. The MSLP and 500mb Height from SRW_RRFSv1alpha are very noisy. The SRW App forecasts have shorter duration because of limitations in the availability of lateral boundary conditions for longer lead times.

**References**

Yang F. (2020). Development and evaluation of NCEP's Global Forecast System Version 16. *Unified Forecast System Community Webinar*, Oct 22, 2020. [`Link <https://ufscommunity.org/wp-content/uploads/2020/10/UFS_Webnair_GFSv16_20201022_FanglinYang.pdf>`_]
