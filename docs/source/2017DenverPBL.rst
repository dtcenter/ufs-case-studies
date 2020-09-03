.. 2017DNRInversionCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



2017 Denver Inversion
=====================================
  
..............................
Model Configuration and Datasets
..............................
.. tabs::
  .. group-tab:: MRW.v1.0

    The case runs are initialized at 00z Oct 16, 2017 with 120 hours forecasting. The corresponding namelist options that need to be changed are listed below. The app uses ``./xmlchange`` to change the runtime settings. The settings that need to be modified to set up the start date, start time, and run time are listed below.

    .. code-block:: bash
 
      ./xmlchange RUN_STARTDATE=2017-10-16,START_TOD=0,STOP_OPTION=nhours,STOP_N=120


    Initial condition (IC) files are created from GFS operational dataset in NEMSIO format. Sounding profiles can be downloaded from the `University of Wyoming <http://weather.uwyo.edu/upperair/sounding.html>`_.

    .. container:: sphx-glr-footer
        :class: sphx-glr-footer-example



      .. container:: sphx-glr-download sphx-glr-download-python

        :download:`Download initial condition files: 2017101600.gfs.nemsio.tar.gz <https://domain.invalid/>`

  .. group-tab:: GFS.v16.0.10

    The GFS model EMC global workflow points to the most up-to-date GFS model development code. The GFS.v16.0.10 is tested in C768 (~13km) resolution and in 128 vertical levels. It uses two scripts, ``setup_expt_fcstonly.py`` and ``setup_workflow_fcstonly.py`` to set up the mode simulation date and case directories.

    The case runs are initialized at 00z Oct 16, 2017 with 120 hours forecasting. The settings that need to be modified to set up the start date and directories are listed below. 

    .. code-block:: bash
 
      ./setup_expt_fcstonly.py --pslot 2017DNRInversion --configdir /PATH/TO/YOUR/GLOBAL/WORKFLOW/parm/config --idate 2017101600 --edate 2017101600 --res 768 --comrot /PATH/TO/YOUR/EXP/DIR/comrot --expdir /PATH/TO/YOUR/EXP/OUTPUT/expdir 

    The account and simulation duration time can be set up in ``/expdir/2017DNRInversion/config.base`` file. 

    .. code-block:: bash

      ./setup_workflow_fcstonly.py --expdir /PATH/TO/YOUR/OUTPUT/expdir/2017DNRInversion

    Next step is to go to ``/expdir/2017DNRInversion`` to submit the run by

    .. code-block:: bash
   
      crontab 2017DNRInversion.crontab 
..............
Case Results
..............

======================================================
Skew-T Log-P Plot
======================================================

The Skew-T Log-P plot is created using the script adapted from `SHARPpy <https://sharppy.github.io/SHARPpy/index.html>`_. The steps for using the SHARPpy scripting in Python programming language is `here <https://sharppy.github.io/SHARPpy/scripting.html>`_.

.. tabs::
  .. group-tab:: MRW.v1.0
  
    .. figure:: images/2017101700_84z_DNR_GFS_Obs_indices.png
      :width: 1200
      :align: center

      Skew-T Log-P plot from observed and simulated sounding profiles. Indices including K-index and lapse rate are shown in the bottom.

  .. group-tab:: GFS.v16.0.10
  
    .. figure:: images/2017101700_84z_DNR_16.0.10.vsObs_indices.png
      :width: 400
      :align: center

      Skew-T Log-P plot from observed and simulated sounding profiles. Indices including K-index and lapse rate are shown in the bottom.


