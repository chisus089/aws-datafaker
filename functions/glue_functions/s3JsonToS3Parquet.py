mport sys
import os
import boto3
import json
from pandas import DataFrame
from awswrangler import catalog
from awswrangler.s3 import to_parquet


ENV_VARS = sys.argv
FILE_KEY = ENV_VARS[18]
print(ENV_VARS)
print(FILE_KEY)

def read_json_s3():
    s3 = boto3.resource('s3')
    content_object = s3.Object('aws-root-main-datafaker-json-trigger', f'hdfs/hdfs-fakedatabase/json/{FILE_KEY}')
    
    file_content = content_object.get()['Body'].read().decode('utf-8')
    return json.loads(file_content)

def write_to_aws(json_data, database_name='fake_database'):

    dataframe = DataFrame.from_dict(json_data,orient='index').T

    catalog.create_database(database_name,exist_ok=True)
    
    to_parquet(df=dataframe,
               path='s3://aws-root-main/hdfs/hdfs-fakedatabase/parquet/', 
               dataset=True, 
               mode="append",
               database=database_name,
               table='fake_db')
               
if __name__ == "__main__":
    write_to_aws(read_json_s3())