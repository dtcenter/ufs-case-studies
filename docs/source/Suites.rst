.. Suites documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. _Using another physics suite:
Using another physics suite
=====================================

There are occasions when researchers are interested in using another physics suite. This pertains to setting up the suite definition file (SDF), suitable namelists, and specific field table.

..............................
Check if the suite is supported
..............................

The currently supported physics suites for UFS MRW app v1.0, UFS weather model, UFS SRW app v1.0 are shown in the table below. Regarding the UFS weather model, the physics suites supported by the public release of CCPP v5.0 are listed here.

.. table::  Supported physics suites

   +---------------------+----------------+---------------+
   | **MRW.v1.0**        | **CCPP.v5.0**  | **SRW.v1.0**  |
   +=====================+================+===============+
   | GFSv15p2            | GFSv15p2       | GFSv15p2      |
   +---------------------+----------------+---------------+
   | GFSv16beta          | GFSv16beta     | RRFS.v1alpha  |
   +---------------------+----------------+---------------+
   |                     | csawmg         |               |
   +---------------------+----------------+---------------+
   |                     | RRFSv1alpha    |               |
   +---------------------+----------------+---------------+

..............................
Compose another physics suite 
..............................
In addition to the physics suites supported by the public release listed above, it is possible to use Global Workflow to conduct experiments using other suites included in the development branch of `fv3atm <https://github.com/NOAA-EMC/fv3atm>`_, under the directory of `fv3atm/ccpp/suites <https://github.com/NOAA-EMC/fv3atm/tree/develop/ccpp/suites>`_. Example physics suites include `RAP <https://github.com/NOAA-EMC/fv3atm/blob/develop/ccpp/suites/suite_FV3_RAP.xml>`_, `HRRR <https://github.com/NOAA-EMC/fv3atm/blob/develop/ccpp/suites/suite_FV3_HRRR.xml>`_, `RRFS_v1beta <https://github.com/NOAA-EMC/fv3atm/blob/develop/ccpp/suites/suite_FV3_RRFS_v1beta.xml>`_, `GSD_noah <https://github.com/NOAA-EMC/fv3atm/blob/develop/ccpp/suites/suite_FV3_GSD_noah.xml>`_, etc. Note that these physics suites are still in the developmental stage and users need caution to set up the correct namelist and field table. The `CCPP Technical Documentation <https://ccpp-techdoc.readthedocs.io/en/v5.0.0/AddingNewSchemes.html>`_ provides guidance on adding a new scheme and a new SDF.


..............................
Change the namelist
..............................

In MRW app that adopts the Common Infrastructure for Modeling the Earth (CIME) workflow. One can change the namelist through editing the file ``user_nl_ufsatm`` and run ``./case.submit`` to update the namelist (Source: `UFS Medium-Range Weather App Users Guide <https://ufs-mrweather-app.readthedocs.io/en/ufs-v1.0.0/faq.html#how-do-i-change-a-namelist-option-for-chgres-cube-or-the-model>`_).

In Global Workflow to run the up-to-date UFS weather model, the namelist can be changed in ``exglobal_forecast.sh`` under the directory of ``global-workflow/scripts``. 

In SRW app that uses the regional workflow, the namelist parameters are changed in the ``config.sh`` within the ``ush`` directory (Source: `UFS Short-Range Weather App Users Guide <https://ufs-srweather-app.readthedocs.io/en/latest/ConfigWorkflow.html#forecast-parametersl>`_).





