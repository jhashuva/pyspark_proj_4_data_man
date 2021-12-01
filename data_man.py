from read_data import df
from pyspark.sql.functions import isnan, when, count, col

def display():
    return df.show()

def schema():
    return df.printSchema()

def is_missing():
    return df.select([count(when(isnan(c), c)).alias(c) for c in df.columns]).show()

def describe_data():
    return df.describe().show()

