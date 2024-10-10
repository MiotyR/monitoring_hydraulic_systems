# Monitoring hydraulic systems
This repository is about predicting the valve condition of hydraulic systems.

## Description
The project is part of the predictive maintenance of a factory. The goal is to identify valve conditions from data captured by sensors. <br>
Data is time series and represents two features: 
* FS1 = Volume flow, stored in FS1.txt
* PS2 = Pressure, stored in PS2.txt 
<br>
The valve condition is the second column of the file profile.txt. It is a variable with 4 different categories representing its state by a percentage of switching behavior.<br> 
The dataset contains 2205 raw process sensor data, there is no missing value.
For more details, please refer to UCI data description (https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems)

The notebook consists of training a model K-Nearest Neighbors combined with Dynamic Time Warping to calculate the distance between two time series.

## Getting Started
* Make sure that you have Jupyter Notebook installed 
* Use requirements.txt to install packages needed for the project
* Run the command for local web application 
```
streamlit run app.py
```
