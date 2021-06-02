.. 2020DNRInversionCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. _2020 Denver Radiation Inversion:
2020 Denver Radiation Inversion
=====================================
Radiation inversion usually happens at night due to the surface radiative cooling.  

..............................
Model Configuration and Datasets
..............................
.. tabs::
  .. group-tab:: MRW.v1.0

    The case runs are initialized at 12z Apr 29, 2020 with 120 hours forecasting. The corresponding namelist options that need to be changed are listed below. The app uses ``./xmlchange`` to change the runtime settings. The settings that need to be modified to set up the start date, start time, and run time are listed below.

    .. code-block:: bash
 
      ./xmlchange RUN_STARTDATE=2020-04-29,START_TOD=43200,STOP_OPTION=nhours,STOP_N=120


    Initial condition (IC) files are created from GFS operational dataset in NEMSIO format. Sounding profiles can be downloaded from the `University of Wyoming <http://weather.uwyo.edu/upperair/sounding.html>`_.

    .. container:: sphx-glr-footer
        :class: sphx-glr-footer-example



      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2020042912.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2020042912.gfs.nemsio.tar.gz>`

  .. group-tab:: GFS.v16.0.10

    The GFS model EMC global workflow points to the most up-to-date GFS model development code. The GFS.v16.0.10 is tested in C768 (~13km) resolution and in 128 vertical levels. It uses two scripts, ``setup_expt_fcstonly.py`` and ``setup_workflow_fcstonly.py`` to set up the mode simulation date and case directories.

    The case runs are initialized at 12z Apr 29, 2020 with 120 hours forecasting. The settings that need to be modified to set up the start date and directories are listed below. 

    .. code-block:: bash
 
      ./setup_expt_fcstonly.py --pslot 2020DNRInversion --configdir /PATH/TO/YOUR/GLOBAL/WORKFLOW/parm/config --idate 2020042912 --edate 2020042912 --res 768 --comrot /PATH/TO/YOUR/EXP/DIR/comrot --expdir /PATH/TO/YOUR/EXP/OUTPUT/expdir 

    The account and simulation duration time can be set up in ``/expdir/2020DNRInversion/config.base`` file. 

    .. code-block:: bash

      ./setup_workflow_fcstonly.py --expdir /PATH/TO/YOUR/OUTPUT/expdir/2020DNRInversion

    Next step is to go to ``/expdir/2020DNRInversion`` to submit the run by

    .. code-block:: bash
   
      crontab 2020DNRInversion.crontab 
  .. group-tab:: SRW.v1.0

    The case runs are initialized at 12z Apr 29, 2020 with 90 hours forecasting. The app uses ``config.sh`` to define the runtime settings. The settings that need to be modified to set up the first cycle, last cycle, forecast length and cycle hour are listed below.

    .. code-block:: bash

      FCST_LEN_HRS="90"
      LBC_SPEC_INTVL_HRS="3"
      DATE_FIRST_CYCL="20190429"
      DATE_LAST_CYCL="20190429"
      CYCL_HRS=( "12" )


    Initial condition (IC) and boundary condition (BC) files are created from GFS operational dataset in NEMSIO format.

    .. container:: sphx-glr-footer
        :class: sphx-glr-footer-example


      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2020042912.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2020042912.gfs.nemsio.tar.gz>`
        :download:`Download boundary condition files: 2020042912_bc.gfs.nemsio.tar.gz <https://ufs-case-studies.s3.amazonaws.com/2020042912_bc.gfs.nemsio.tar.gz>`

..............
Case Results
..............

======================================================
Skew-T Log-P Plot
======================================================

The Skew-T Log-P plot is created using the script adapted from `SHARPpy <https://sharppy.github.io/SHARPpy/index.html>`_. The steps for using the SHARPpy scripting in Python programming language is `here <https://sharppy.github.io/SHARPpy/scripting.html>`_. 

.. tabs::

  .. group-tab:: MRW.v1.0

    .. figure:: images/2020DNRInversion/2020042912_f024_DNR_MRWvsObs_indices.png
      :width: 1200
      :align: center

      Skew-T Log-P plot from observed and simulated sounding profiles. Indices including K-index and lapse rate are shown in the bottom.

    * The two physics compsets, MRW_GFSv15p2 and MRW_GFSv16beta, underestimate the temperature inversion strength with a warmer near surface temperature.  

  .. group-tab:: GFS.v16.0.10

    .. figure:: images/2020DNRInversion/2020042912_f024_DNR_GFS.v16.0.10vsObs_indices.png
      :width: 400
      :align: center

      Skew-T Log-P plot from observed and simulated sounding profiles. Indices including K-index and lapse rate are shown in the bottom.
    
    * GFS.v16.0.10 underestimates the temperature inversion strength with a warmer near surface temperature.

  .. group-tab:: SRW.v1.0

    .. figure:: images/2020DNRInversion/2020042912_f024_DNR_SRWvsObs_indices.png
      :width: 1200
      :align: center

      Skew-T Log-P plot from observed and simulated sounding profiles. Indices are shown in the bottom.

    * The physics suite SRW_GFSv15p2 underestimates the temperature inversion strength with a warmer near surface temperature.  
    * The temperature inversion strength is well captured in SRW_RRFSv1alpha.  
 
......................
Summary and Discussion
......................

The 2020 Denver Radiation Inversion results show that the GFS model lacks skills in forecasting the boundary layer temperature inversion for MRW_GFSv15p2, MRW_GFSv16beta, and GFS.v16.0.10, with a warmer near-surface temperature. 
The inversion is well captured by physics suite RRFSv1alpha in SRW App.
