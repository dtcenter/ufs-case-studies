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

.. _2019 Hurricane Barry:
2019 Hurricane Barry
=====================================

Hurricane Barry made landfall in Louisiana on July 11, 2019. The peak wind speed and minimum pressure reached 72 mph and 992 hPa, respectively during the storm. 

................................
Model Configuration and Datasets
................................
.. tabs::
  .. group-tab:: MRW.v1.0

    The UFS Medium-Range Weather (MRW) Application (App) is used to prepare initial conditions, compile and run the UFS model, and postprocess the raw model outputs. Two model configuration suites (``GFSv15p2`` and ``GFSv16beta``) are tested using the :emphasis:`C768` (~13km) spatial resolution with 64 vertical levels (default).

    The case runs are initialized at 00z Jul 11, 2019 with a forecast length of 120 hours. The app uses ``./xmlchange`` to change the runtime settings. The settings that need to be modified to set up the start date, start time, and run time are listed below.

    .. code-block:: bash
 
      ./xmlchange RUN_STARTDATE=2019-07-01,START_TOD=0,STOP_OPTION=nhours,STOP_N=120

    Initial condition (IC) files are created from GFS operational dataset in NEMSIO format. The `Stand-alone Geophysical Fluid Dynamics Laboratory (GFDL) Vortex Tracker <https://dtcenter.org/community-code/gfdl-vortex-tracker>`_ is a tool to estimate hurricane tracks and intensities. The `Best Track dataset <https://www.nhc.noaa.gov/data/#hurdat>`_ provides the ‘truth’ data for hurricane evolution.

    .. container:: sphx-glr-footer
       :class: sphx-glr-footer-example


      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2019071100.gfs.nemsio.tar.gz  <https://ufs-case-studies.s3.amazonaws.com/2019071100.gfs.nemsio.tar.gz>`

  .. group-tab:: GFS.v16.0.10

    The GFS model EMC global workflow points to the most up-to-date GFS model development code. The GFS.v16.0.10 is tested in C768 (~13km) resolution and in 128 vertical levels. It uses two scripts, ``setup_expt.py`` and ``setup_workflow_fcstonly.py`` to set up the mode simulation date and case directories.

    The case runs are initialized at 00z Jul 11, 2019 with 120 hours forecasting. The settings that need to be modified to set up the start date and directories are listed below. 

    .. code-block:: bash
 
      ./setup_expt.py forecast-only --pslot Barry --configdir /PATH/TO/YOUR/GLOBAL/WORKFLOW/parm/config --idate 2019071100 --edate 2019071100 --res 768 --comrot /PATH/TO/YOUR/EXP/DIR/comrot --expdir /PATH/TO/YOUR/EXP/OUTPUT/expdir 

    The account and simulation duration time can be set up in ``/expdir/Barry/config.base`` file. 

    .. code-block:: bash

      ./setup_workflow_fcstonly.py --expdir /PATH/TO/YOUR/OUTPUT/expdir/Barry

    Next step is to go to ``/expdir/Barry`` to submit the run by

    .. code-block:: bash
   
      crontab Barry.crontab  

  .. group-tab:: SRW.v1.0

    The UFS Short-Range Weather (SRW) Application (App) is used to prepare initial conditions, compile and run the UFS model, and postprocess the raw model outputs. Two model configuration suites (``GFSv15p2`` and ``RRFSv1alpha``) are tested using the :emphasis:`C768` (~13km) spatial resolution with 64 vertical levels (default).

    The case was initialized at 00z Jul 12, 2019 and forecast out to 90 hours. The app uses ``config.sh`` to define the runtime settings. The settings that need to be modified to set up the first cycle, last cycle, forecast length and cycle hour are listed below.

    .. code-block:: bash
 
      FCST_LEN_HRS="90"
      LBC_SPEC_INTVL_HRS="3"
      DATE_FIRST_CYCL="20190712"
      DATE_LAST_CYCL="20190712"
      CYCL_HRS=( "00" )

    Initial condition (IC) and boundary condition (BC) files are created from GFS operational dataset in NEMSIO format.

    .. container:: sphx-glr-footer
       :class: sphx-glr-footer-example


      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2019071200.gfs.nemsio.tar.gz  <https://ufs-case-studies.s3.amazonaws.com/2019071200.gfs.nemsio.tar.gz>`
        
        :download:`Download the script for getting boundary conditions: get_hsup_bc_ic.sh <./get_hsup_bc_ic.sh>`

..............
Case Results
..............

==============================
Hurricane Track and Intensity
==============================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2019Barry/tracker_Barry_ufsv1.png
      :width: 400
      :align: center

      Hurricane tracks from MRW_GFSv16beta (blue line), MRW_GFSv15p2 (red line), and Best Track (black line). The dots are color coded with the vortex maximum 10-m wind speed (WS, kt). 

    * Both MRW_GFSv16beta and MRW_GFSv15p2 generate right-of-track biases. 
    * Hurricane track and intensity simulated by MRW_GFSv15p2 are closer to Best Track compared with MRW_GFSv16beta.


    .. figure:: images/2019Barry/tracker_ws_mslp_Barry.png
      :width: 1200
      :align: center

      Time series of the vortex maximum surface wind speed (WS, left panel) and minimum mean sea level pressure (MSLP, right panel)

    * The peak wind speed at the vortex center in MRW_GFSv15p2 (60 kts) is closer to Best Track (67 kts) compared with MRW_GFSv16beta (50 kts).
    * Both physics suites simulate the minimum sea level pressure relatively well.  

  .. group-tab:: GFS.v16.0.10

     .. figure:: images/2019Barry/tracker_Barry_GFS.v16.0.10.png
      :width: 400
      :align: center

      Hurricane tracks from GFS.v16.0.10 (red line) and Best Track (black line). The dots are color coded with the vortex maximum 10-m wind speed (WS, kt). 

    * GFS.v16.0.10 generates right-of-track bias. 

    .. figure:: images/2019Barry/tracker_ws_mslp_BARRY_GFS.v.16.0.10.png
      :width: 1200
      :align: center

      Time series of the vortex maximum surface wind speed (WS, left panel) and minimum mean sea level pressure (MSLP, right panel)

    * The time variation of maximum wind speed in GFS.v16.0.10 agrees well with Best Track.
    * The minimum sea level pressure reaches to a lower value in GFS.v16.0.10 (982 hPa) compared with Best Track (993 hPa). 

  .. group-tab:: SRW.v1.0

    .. figure:: images/2019Barry/tracker_Barry_srwv1.png
      :width: 400
      :align: center

      Hurricane tracks from SRW_RRFSv1alpha (blue line), SRW_GFSv15p2 (purple dash line), MRW_GFSv15p2 (red line), and Best Track (black line). The dots are color coded with the vortex maximum 10-m wind speed (WS, kt). 

    * Both MRW_GFSv15p2 and SRW_GFSv15p2 generate right-of-track biases. 
    * Hurricane track and intensity simulated by SRW_RRFSv1apha are closer to Best Track compared with SRW_GFSv15p2 and MRW_GFSv15p2.


    .. figure:: images/2019Barry/tracker_ws_mslp_Barry_srwv1.png
      :width: 1200
      :align: center

      Time series of the vortex maximum surface wind speed (WS, left panel) and minimum mean sea level pressure (MSLP, right panel)

    * The peak wind speeds at the vortex center in MRW_GFSv15p2 (58 kts) and SRW_RRFSv1alpha (58 kts) are closer to Best Track (67 kts) compared to SRW_GFSv15p2 (52 kts).
    * Both physics suites simulate the minimum sea level pressure relatively well. The results from SRW App v1.0 slightly overestimate the minimum sea level pressure. 


====================================
Comparison with Satellite Data
====================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2019Barry/Satellite_OLR.png
      :width: 1600
      :align: center

      Simulated outgoing longwave radiation (OLR) at the top of atmosphere (TOA) from MRW_GFSv16beta and MRW_GFSv15p2, and infrared images from `NASA Worldview <https://worldview.earthdata.nasa.gov/>`_ at the forecast hour of 72.

    * Comparison with satellite product also indicates a right-of-track error
    * Lower OLR near the tropical cyclone (TC) center suggests more clouds in MRW_GFSv15p2 than in MRW_GFSv16beta 

=============================================
Hovmöller diagram of 850 hPa WS after Landfall
=============================================
.. tabs::
  .. group-tab:: MRW.v1.0

    .. figure:: images/2019Barry/Radial_WS_TimeSeries.png
      :width: 1600
      :align: center

      Hovmöller diagram of wind speed and 850 hPa and the radius of maximum wind (RMW, white line) after landfall

    * The low-level wind speed in GFS model is smaller than GFS_ANL.
    * The MRW_GFSv16beta has the largest inner core size. MRW_GFS15p2 has similar inner core sizes and GFS_ANL.
    * Hurricane intensity attenuates faster in the model compared with Best Track after landfall.
      
......................
Summary and Discussion
......................

The exacerbated right-of-track bias exists in both GFS.v16.0.10 and MRW_GFSv16beta compared with GFSv15p2. The right-of-track bias is likely associated with overactive convection and vortex tilt. This tends to induce convergence towards that excessive convection and leads to track bias (`Lybarger et al. 2020 <https://dtcenter.org/sites/default/files/events/2020/2-lybarger-nick.pdf>`_).
Hurricane track and intensity simulated by RRFSv1apha are closer to Best Track compared to the results from GFSv15p2 in SRW App v1.0. The SRW App forecasts have shorter duration because of limitations in the availability of lateral boundary conditions for longer lead times.

**References**

Lybarger N. D., Kalina E., and Newman K. (2020). Diagnosing Hurricane Track Errors in the UFS Short-Range Weather Application (SRW). *The First UFS Users' Workshop*, July 27-29, 2020. [`Link <https://dtcenter.org/sites/default/files/events/2020/2-lybarger-nick.pdf>`_]
