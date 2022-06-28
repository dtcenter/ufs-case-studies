.. Hierarchical Testing Framework documentation master file, created by
   sphinx-quickstart on Tue Jun  28 10:14 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. _Hierarchical Testing Framework:
Hierarchical Testing Framework
=====================================

Hierarchical Testing Framework (HTF) refers to test physics innovations using tools ranging in complexity from simple parameterization simulators to complex three-dimensional global models. Unified Forecast System (UFS) Case Studies Platform (Sun et al., 2021) provides a set of cases that reveal the forecast challenges of NOAA’s operational numerical global weather prediction model, the Global Forecast System (GFS). Our catalog of test cases currently contains 10 cases that cover known biases of the GFS operational implementations GFS v15.2 and GFS v16, such as hurricanes, mid-latitude storms, heat waves and cold blast events, and a cold air damming case. We used the 2020 July Convective Available Potential Energy (CAPE) case and the 2020 Cold Air Damming (CAD) cases to perform hierarchical testing of physics innovations. The results were presented to the community at the American Meteorological Society annual meetings (Sun et al., 2022; Pan et al., 2022). 

..............................
2020 July CAPE Case
..............................

For the 2020 CAPE case, we exercised the HTF to investigate the factors that lead to the low CAPE bias. This case was initialized on July 23, 2020 using GFS v15.2 and GFS v16. A large CAPE reservoir appeared over the Great Plains with a warm front passage over the northern Great Plains and no significant synoptic pattern impacting the Southern Great Plains (SGP). A comprehensive evaluation of GFS forecasts was made, focusing on the SGP and verifying against the observational dataset from the Atmospheric Radiation Measurement network. We investigated the large-scale advection fields over a 120 km × 120 km region centered at the SGP central facility site using European Centre for Medium-Range Weather Forecasts Reanalysis v5 (ERA5). Experiments were conducted using the Common Community Physics Package (CCPP) Single Column Model (SCM) to probe the impacts of initial conditions (IC) and surface forcing.

Key findings for the CAPE case are listed below:

- The lower CAPE in GFS is attributed to air at low levels being drier than observed.
- The larger-than-observed Bowen ratio in GFS suggests an incorrect surface energy partitioning associated with soil moisture and soil temperature. 
- GFS v16 exhibits more vertical mixing leading to a deeper boundary layer than v15.2 and observations.
- The drier air in GFSv16 is mostly related to local physics not large-scale advection in this case.
- With realistic IC of vertical profiles and surface fluxes, the GFS v16 physics suite is able to produce the large CAPE.

..............................
2020 Cold Air Damming
..............................

We adopted the latest version of Short-Range Weather (SRWeather) App (version 1.0) to investigate the 2020 CAD case1 developed as part of the UFS Case Studies project to investigate the impact of code updates, horizontal and vertical resolution, and physics suites. The SRWeather App is the foundation for building NOAA’s future convection-allowing Rapid Refresh Forecast System (RRFS). The limited area configuration needs fewer computer resources and can run models in high resolution and cycle frequently. Thus the case studies conducted with the SRWeather App are a useful supplement for the global configuration case studies. The physics suites used in this study, which focuses on the CONUS domain, include GFS v15.2, GFS v16, GFS v17α, and RRFS v1α. The results from UFS SRWeather App were compared with the results from the UFS global configuration. The SRWeather App was also tested with different configurations, such as different versions of the code base, model grid spacing (13 km vs 3 km, 64 levels vs 127 levels), and physics suite employed. The model forecasts were verified against station observations and analysis data. 

The key findings for the CAD case are:

- The spatial pattern of the 2-meter surface temperature field obtained with the SRWeather App is slightly improved over the one obtained with the global configuration.
- Using the code version of April 10 th, 2022 and more vertical levels leads to
- Improvements for this case when using the GFS v16 suite
- Degradation when using the (uncoupled) GFS v17α suite
- When the 3-km horizontal grid spacing configuration is used with the GFS v15.2 and GFS v16 suites (but not with the GFS v17α suite), the cold air is not maintained and the CAD strength is reduced, which is a degradation when compared to experiments conducted at lower resolutions. for
- Sensitivity tests with suite GFS v17α show that changing the land surface model from NoahMP to Noah can cause a northward shift of the cold air.

**References**

Pan, L., Heinzeller, D., Bernardet, L., Sun, X., & Brown, J. M. (2022, January). Surface biases in forecasting extreme events using the Unified Forecast System with different physics suites. 31st Conference on Weather Analysis and Forecasting.

Sun, X., Heinzeller, D., Bernardet, L., Pan, L., & Brown, J. M. (2021, January). Case studies that exemplify known biases of the Unified Forecast System (UFS) Weather Model. 11th Conference on the Transition of Research to Operations.

Sun, X., Heinzeller, D., Bernardet, L., Pan, L., & Brown, J. M. (2022, January). Confronting the low summer CAPE behavior in GFSv16. 12th Conference on the Transition of Research to Operations.

Sun, X., Heinzeller, D., Bernardet, L., Pan, L., Li, W., Turner, D., & Brown, J. M. On the factors leading to the low surface-based CAPE behavior in the Global Forecast System. In preparation.



