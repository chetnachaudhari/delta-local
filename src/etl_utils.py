import pyspark.sql.functions as F
from pyspark.sql.functions import *
from pyspark.sql.types import *


class DataTransformer:

    def jsonToDataFrame(json, schema=None):
        reader = spark.read
        if schema:
            reader.schema(schema)
        return reader.json(sc.parallelize([json]))

    


    

class DataframeComparator:

    def test_schema(df1: DataFrame, df2: DataFrame, check_nullable=True):
        field_list = lambda fields: (fields.name, fields.dataType, fields.nullable)
        fields1 = [*map(field_list, df1.schema.fields)]
        fields2 = [*map(field_list, df2.schema.fields)]
        if check_nullable:
            res = set(fields1) == set(fields2)
        else:
            res = set([field[:-1] for field in fields1]) == set([field[:-1] for field in fields2])
        return res
    
    def test_data(df1: DataFrame, df2: DataFrame):
        data1 = df1.collect()
        data2 = df2.collect()
        return set(data1) == set(data2)