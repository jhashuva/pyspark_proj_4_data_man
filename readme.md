# Pyspark Project 4 
This project is related to spark data processing. Data has been taken from:
[Github](https://github.com/databricks/Spark-The-Definitive-Guide/tree/master/data/flight-data/csv).

This project tends to analyze the data interms of:
- Display first few records of the data.
- Display schema of the data.
- Display missing values.
- Display count, min, mean, max of each field.

## `requirments.txt`

- pyspark
- findspark

## `init_context.py`
It initializes the Spark session and Spark context.

## `read_data.py`
Reads the data from `Data` Folder and store it into Pyspark Data Frame.

## `data_man.py`
Here all data manipulations would happen.

## `main.py`

Connect the customer to the project and testing information.