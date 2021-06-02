.. BarryCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Introduction
=====================================

Challenges for accurate weather prediction still exist in numerical models. This catalog of case studies aims at facilitating the development and improvement of NOAA operational modeling systems by making available datasets and codes that allow researchers to configure and run the `Unified Forecast System (UFS) <https://ufscommunity.org/>`_ for a number of cases that represent known biases of the NOAA operational Global Forecast System (GFS).

The catalog offers both global and limited-area domain configurations of the case studies to provide flexibility to users. Given this catalog's current focus on GFS biases, at this time, both global and limited-area configurations use the operational GFS horizontal grid spacing of approximately 13 km. Two types of global configurations are available, both of which focus on suites ``GFS.v15p2`` (used in the GFS v15 implemented operationally in June 2019) and ``GFS.v16beta`` (associated with the GFS v16 implemented operationally in March 2021).

- The UFS Medium-Range Weather (MRW) Application (App) public release, which contains stable and well tested code. It should be noted that the public release code precedes the operational implementation of GFS v16 and therefore does not reflect the final updates that are part of the operational implementation.
- UFS Global Workflow, which invokes the most up-to-date source codes and housed in the `ufs-weather-model <https://github.com/ufs-community/ufs-weather-model>`_ GitHub repository.

The limited area configurations of the case studies use the UFS Short-Range Weather (SRW) Application (App), which employs suites ``GFS.v15p2`` and ``RRFS.v1alpha``. An operational implementation of the SRW App is planned for 2024. 

The known biases and development priorities related to GFS v15 (`Stan et al. 2019 <https://drive.google.com/file/d/1rdFPbY28d7cRrcShy0uo4Mtqwh3BSzYg/view>`_) and GFS v16 (presented by `Yang 2020 <https://ufscommunity.org/wp-content/uploads/2020/10/UFS_Webnair_GFSv16_20201022_FanglinYang.pdf>`_) have been summarized below. The known bugs in the SRW App 1.0 can be found at `SRW App website <https://github.com/ufs-community/ufs-srweather-app/wiki/Release-Notes-and-Known-Bugs>`_. 

.. tabs::
  .. group-tab:: GFS.v15 

    - Less skillful hurricane track forecasts for strong storms in the Atlantic basin
    - Progressive with synoptic patterns
    - Extreme 2-m temperature biases in the mid-west region in the warm season
    - Cold bias in the lower troposphere and near the surface in the winter season
    - Precipitation dry bias for moderate rainfall
    - Struggle to capture boundary layer inversions    
  .. group-tab:: GFS.v16

    - Increased right-of-track bias for tropical cyclones (TC) at longer lead times at North Atlantic
    - Larger TC False Alarm Rate in the western North Atlantic
    - Exacerbated low instability bias, which is largely related to dry soil moisture
    - Poor representation of radiation inversions
  .. group-tab:: RRFS.v1alpha

    - More skillful hurricane track forecasts for strong storms in the Atlantic basin
    - Weak hurricane intensity forecasts
    - Unstable signal over mountain area
    - Slightly skillful cold air damming forecast
    - The heat wave signal is too strong
   
.. tabs::
  .. group-tab:: Medium-Range Weather (MRW) App 

	The `UFS Medium Range Weather (MRW) App <https://ufs-mrweather-app.readthedocs.io/en/latest/index.html>`_ uses the `Common Infrastructure for Modeling the Earth (CIME) workflow <https://esmci.github.io/cime/versions/ufs_release_v1.0/html/index.html>`_ that incorporates pre-processing software, forecast model, and post-processor. The app serves as a useful tool to conduct the UFS WM runs. The latest evaluation results are based on physics suites of ``GFSv15p2`` and ``GFSv16beta`` employed in UFS Medium Range Weather App *v1.0* (MRW.v1.0), hereafter referred to as MRW_GFSv15p2 and MRW_GFSv16beta, respectively.
  
  .. group-tab:: Global Workflow

	The `Global Workflow <https://github.com/NOAA-EMC/global-workflow>`_ developed by `NOAA EMC <https://www.emc.ncep.noaa.gov/emc_new.php>`_ is a superstructure that supports the Finite-Volume on a Cubed-Sphere Global Forecast System (FV3GFS) development. It includes submodules that points to the most up-to-date GFS model development codes located in the `ufs-weather-model <https://github.com/ufs-community/ufs-weather-model>`_ GitHub repository. Case study results are continually updated when substantial physics innovations are included and GitHub tags (e.g., ``GFS.v16.0.10``) are created between two subsequent public releases.

  .. group-tab:: Short-Range Weather (SRW) App 

	The `UFS Short Range Weather (SRW) App <https://ufs-srweather-app.readthedocs.io/en/latest/index.html>`_ uses the `regional workflow` that incorporates pre-processing software, forecast model, and post-processor. The app serves as a useful tool to conduct the UFS Weather Model (WM) runs. The latest evaluation results are based on physics suites of ``GFSv15p2`` and ``RRFSv1alpha`` employed in UFS Short Range Weather App *v1.0* (SRW.v1.0), hereafter referred to as SRW_GFSv15p2 and SRW_RRFSv1alpha, respectively.
  
The goal of this ongoing effort is to provide the community, as well as the physics development team, with a model testing platform where they can use the resources to conduct model runs and evaluate the model performance for representative meteorological cases. These case studies will provide insights for future model developments and aim at improving NOAA numerical weather forecasts. It should be noted that this is an ongoing effort that is aligned with the model public release and model development. Namely these evaluation results only apply to specific model versions. Timeline of physics frozen date in different model versions, including both UFS MRW/SRW App suites and ufs-weather-model GitHub tags, are shown below:

.. figure:: images/timeline_Apr2021.png
   :scale: 20%
   :align: center

   Timeline of physics frozen date

The case catalog in this documentation was created based on the known biases of GFS model. This is a list that we are updating diligently. Please come back to check updates anytime.


**References**

Stan C., Yang F., and Harris L. (2019). UFS Development Goals and Priorities for Medium-Range and S2S Applications. *Unified Forecast System Community*. [`Link <https://drive.google.com/file/d/1rdFPbY28d7cRrcShy0uo4Mtqwh3BSzYg/view>`_]

Yang F. (2020). Development and evaluation of NCEP's Global Forecast System Version 16. *Unified Forecast System Community Webinar*, Oct 22, 2020. [`Link <https://ufscommunity.org/wp-content/uploads/2020/10/UFS_Webnair_GFSv16_20201022_FanglinYang.pdf>`_]


