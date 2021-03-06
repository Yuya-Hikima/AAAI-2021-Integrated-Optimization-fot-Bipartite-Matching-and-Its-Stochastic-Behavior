# AAAI2021-Integrated-Optimization-for-Bipartite-Matching-and-Its-Stochastic-Behavior

## Overview
This repository contains the codes for the experiments performed in the following papers:
  
Yuya Hikima, Yasunori Akagi, Hideaki Kim, Masahiro Kohjima, Takeshi Kurashima, and Hiroyuki Toda. "Integrated Optimization for Bipartite Matching and Its Stochastic Behavior: New Formulation and Approximation Algorithm via Min-cost Flow Optimization." In AAAI, 2021, pages 3796-3805.

In this paper, we conducted two experiments: a crowd-sourcing experiment and a ride-sharing experiment.
Currently, only the crowd-sourcing experiment is shared here, but the ride-sharing experiment will be shared later.

Contents of this repository:
- **README** This file.
- **SOFTWARE LICENSE AGREEMENT FOR EVALUATION** The user must comply with the rules described herein.
- **Crowd-sourcing_experiment folder** It contains the code used in the crowd-sourcing platform experiment and the code needed to set up the experiment, including data downloads.

The data for crowd-sourcing experiments are downloaded from
  
http://dbgroup.cs.tsinghua.edu.cn/ligl/crowddata/ (Relevance Finding dataset).
  
The data are shared by
  
Chris Buckley, Matthew Lease, and Mark D. Smucker. "Overview of the TREC 2010 Relevance Feedback Track (Notebook)." In TREC, 2010.

## Description

The following is a description of what is in each folder.
- **Crowd-sourcing_experiment** 
  - **setup.sh** Script for setting up the experiments
  - **Experiment_paper.sh** Scripts for performing the same experiments as in our paper
  - **Experiment_test.sh** Scripts for small experiments to see if our codes work
  - **bin** Folder containing the python code needed for the crowd-sourcing experiments
    - **data_download.py** It is executed by setup.sh to download the real data.
    - **generate_reward_matrix.py** It is executed by setup.sh to make simulation data from the real data.
    - **experiment_Sigmoid.py** It is executed by Experiment.sh or Experiment_test.sh to perform experiments using simulated data when using Sigmoid functions as acceptance probability functions. The first argument is \phi (active rate of workers), and the second is \psi (active rate of tasks).
    - **experiment_PL.py** Experimental code It is executed by Experiment.sh or Experiment_test.sh to perform experiments using simulated data when using piecewise linear functions as acceptance probability functions.
  - **data** Folder where the downloaded data is stored
  - **work** Folder where the simulation data is stored
    - **Reward_matrix** Data containing w_et in the paper, generated by experiment_crowdsourcing_gurobi.py.
    - **trec-rf10-data.csv** Converted csv data from the downloaded data
  - **results** Folder where the results are stored
    - **Average_result_XX_phi=YY_psi=ZZ.csv** The data containig results for a given parameter set

## Requirement
Codes were implemented in Python 3.6.8.

## Usage
We explain how to perform **Crowd-sourcing experiments.** 

1. Go to the Crowd-sourcing_experiment folder, make "results", "data" and "work" folder, and then, run "bash setup.sh."
2. Run "bash Experiment_test.sh" and see the results in the "results" folder to see if the code works.
3. Run "bash Experiment_paper.sh" and see the results in the "results." Note that this code takes a long time to execute and is not parallelized.
  
If you want to set parameters yourself, go to the Crowd-sourcing_experiment/bin folder and run "python3 experiment_Sigmoid.py YY ZZ." The first argument is \phi (active rate of workers), and the second is \psi (active rate of tasks).

## Licence
You must follow the terms of the "SOFTWARE LICENSE AGREEMENT FOR EVALUATION."
Be sure to read it.

## Author
Yuya Hikima wrote this text.
If you have any problems, please contact yuya.hikima at gmail.com.
