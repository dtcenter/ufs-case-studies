.. BarryCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



2017 Denver Inversion
=====================================
  
..............................
Model Configuration and Datasets
..............................

The case runs are initialized at 00z Oct 16, 2017 with 120 hours forecasting. The corresponding namelist options that need to be changed are listed below. The app uses ``./xmlchange`` to change the runtime settings. The settings that need to be modified to set up the start date, start time, and run time are listed below.

.. code-block:: bash
 
   ./xmlchange RUN_STARTDATE=2017-10-16,START_TOD=0,STOP_OPTION=nhours,STOP_N=120


Initial condition (IC)  files are created from GFS reanalysis dataset in nemsio format. Sounding profiles can be downloaded from the `University of Wyoming <http://weather.uwyo.edu/upperair/sounding.html>`_.

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download initial condition files: 2017101600.gfs.nemsio.tar.gz <https://domain.invalid/>`
..............
Case Results
..............

======================================================
Skew-T Log-P Plot
======================================================


.. figure:: images/2017101700_84z_DNR_GFS_Obs_indices.png
  :width: 1200
  :align: center

  Skew-T Log-P plot from observed and simulated sounding profiles
