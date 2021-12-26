# Udacity Data Engineer Nanodegree Capstone Project: I94 Immigration Dataset Analysis

### Introduction

This is a capstone project for data engineering nano degree at Udacity. I have used 3 datasets including the 2016-09 I94 Immigration data together to complete the project. The main purpose of this project is to firs understand the datasets and design the data model then pre-process the data into desirable format. After that, the data is stored into a durable storage on cloud, which in this project AWS S3 has been used as the data lake for housing the parquet files. Finally data is loaded into a data warehouse for further analysis, which in this project AWS Redshift has been used for this purpose. In this project, after spending some time on understanding the datasets, I have come up the solution and process as mentioned above.

### Datasets
I've worked with three datasets to complete the project. The main dataset will include data on immigration to the United States, and supplementary datasets will include data on airport codes, U.S. city demographics, and temperature data. 

- I94 Immigration Data: This data comes from the US National Tourism and Trade Office. A data dictionary is included in the workspace. [This](https://www.trade.gov/national-travel-and-tourism-office) is where the data comes from. There's a sample file to take a look at the data in csv format before reading it all in. 
- World Temperature Data: This dataset came from Kaggle. You can read more about it [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data).
- U.S. City Demographic Data: This data comes from OpenSoft. You can read more about it [here](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/).

### Files
- i94_apr16_sub.parquet the raw parquet format data file for i94 immigration data 
- Capstone Project.ipynb the scripts I wrote for the project as well as the query results
- Capture.PNG the star schema diagram screenshot used for this project
- dwh.cfg contains AWS connection information
- GlobalLandTemperaturesByState.csv the World Temperature Data aggregated by states
- I94_SAS_Labels_Descriptions.SAS A data dictionary for I94 Immigration Data
- immigration_data_sample.csv a sample file to take a look at the data in csv format before reading it all in. 
- us-cities-demographics-updated.csv updated based on the original U.S. City Demographic Data for poviting the population for races into its own columns
- dictionary data dictionary for data model for each field, brief description of what the data is and where it came from
- AWS_Module.py contains AWS variables for connection and user defined functions for created Redshift cluster
- SQL_Statement.py contains the sql queries for creating tables on Redshift
- README.md provides discussion on the process and decisions

#### Fact Table
- fact_i94_records - i94 records for this project
cicid, i94yr, i94mon, i94cit, i94res, i94port, i94_port_city, i94_port_state, arrdate, i94mode, i94addr, depdate, i94bir, i94visa, biryear, gender, insnum , airline, visatype

#### Dimension Tables
- dim_us_city_demographics - us-cities-demographics data
City, State, Median_Age, Male_Population, Female_Population, Total_Population, Number_of_Veterans, Foreign_born, Average_Household_Size, State_Code,
American_Indian_and_Alaska_Native, Hispanic_or_Latino, White, Asian, Black_or_African_American
- dim_time - date of records in i94_records broken down into specific units
date, day, week, month, year, weekday
- dim_temperature - GlobalLandTemperaturesByState
Average_Temperature, Average_Temperature_Uncertainty, state, Country


#### How to Run
1. Write AWS correct keys on dl.cfg file
2. Execute Capstone Project.ipynb from jupiter notebook
