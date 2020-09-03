.. BarryCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Introduction
=====================================

Challenges for accurate weather prediction still exist in numerical models. To facilitate the development and improvement of the NOAA `Unified Forecast System (UFS) <https://ufscommunity.org/>`_ Weather Model (WM), case studies are needed based on these forecast challenges. There are several known model biases in the UFS WM. These known biases include but are not limited to progressive synoptic patters, degraded tropical cyclone tracks, and incapability to simulate stable boundary layer structures.

This document provides case studies evaluation results for the UFS Weather Model using `UFS Medium Range Weather (MRW) App <https://ufs-mrweather-app.readthedocs.io/en/latest/index.html>`_ and `NOAA Enviromental Model Center (EMC) Global Workflow <https://github.com/NOAA-EMC/global-workflow/wiki>`_. It should be noted that this is an ongoing effort that is aligned with the model public release and model development. Namely these evaluation results only apply to specific model versions.

.. tabs::
  .. group-tab:: Medium-Range Weather (MRW) App 

	The `UFS Medium Range Weather (MRW) App <https://ufs-mrweather-app.readthedocs.io/en/latest/index.html>`_ uses the `Common Infrastructure for Modeling the Earth (CIME) workflow <https://esmci.github.io/cime/versions/ufs_release_v1.0/html/index.html>`_ that incorporates pre-processing software, forecast model, and post-processor. The app serves as a useful tool to conduct the UFS WM runs. The latest evaluation results are based on physics compsets of ``GFSv15p2`` and ``GFSv16beta`` employed in UFS Medium Range Weather App *v1.0*, hereafter referred to as MRW_GFSv15p2 and MRW_GFSv16beta, respectively.
  
  .. group-tab:: Global Workflow

	The `Global Workflow <https://github.com/NOAA-EMC/global-workflow>`_ developed by `NOAA EMC <https://www.emc.ncep.noaa.gov/emc_new.php>`_ is a superstructure that supports the Finite-Volume on a Cubed-Sphere Global Forecast System (FV3GFS) development. It includes submodules that points to the most up-to-date GFS model development codes. Case study results are updated each time the physics innovations are included in the GFS model between two subsequent public releases.

The goal of this ongoing effort is to provide the community, as well as the physics development team, with a model testing platform where they can use the resources to conduct model runs and evaluate the model performance for representative meteorological cases. These case studies will provide insights for future model developments in aim to improve NOAA numerical weather forecasts. 

The case catalogue in this documentation are created based on the known biases of the UFS WM. This is a list that we are updating diligently. Please come back to check updates anytime.



