.. BarryCase documentation master file, created by
   sphinx-quickstart on Mon Jul  6 13:31:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Introduction
=====================================

Challenges for accurate weather prediction still exist in numerical models. To facilitate the development and improvement of the NOAA `Unified Forecast System (UFS) <https://ufscommunity.org/>`_ Weather Model (WM), case studies are needed based on these forecast challenges. There are several known model biases in the UFS WM. These known biases include but are not limited to progressive synoptic patters, degraded tropical cyclone tracks, and incapability to simulate stable boundary layer structures.

This document provides case studies evaluation results for the UFS WM using the `UFS Medium Range Weather App <https://ufs-mrweather-app.readthedocs.io/en/latest/index.html>`_. The app uses a workflow that incorporates pre-processing software, forecast model, and post-processor. The app serves as a useful tool to conduct the UFS WM runs. It should be noted that this is an ongoing effort that is aligned with the model development and model public release. Namely these evaluation results only apply to specific model versions. The latest evaluation results are based on physics compsets of ``GFSv15p2`` and ``GFSv16beta`` employed in UFS Medium Range Weather App *v1.0*.

The goal of this ongoing effort is to provide the community with a model testing platform where they can use the resources to conduct model runs and evaluate the model performance for representative meteorological cases. These case studies will provide insights for future model developments in aim to improve NOAA numerical weather forecasts. 

The case catalogue in this documentation are created based on the known biases of the UFS WM. This is a list that we are updating diligently. Please come back to check updates anytime.



