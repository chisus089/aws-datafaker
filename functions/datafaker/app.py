from datetime import datetime, timedelta
from random import randint, random
from uuid import uuid4
from faker import Faker
from uuid import uuid4
import json
import boto3    

BUCKET = 'aws-root-main-datafaker-json-trigger'

def gen_datetime(min_year=2020, max_year=datetime.today().year):
    """
    generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    """

    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    response = start + (end - start) * random()
    return response


def create_json():
    """
    Generates dummy spark dataframe.
    """
    fake = Faker()
    fake_age = randint(18, 50)
    min_year = datetime.now().year - fake_age
    fake_dob = gen_datetime(min_year=min_year, max_year=min_year).strftime(
        "%Y-%m-%d"
    )
    struct =  {
        "uuid": str(uuid4()),
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.basic_phone_number(),
        "nationality": fake.country(),
        "address": fake.address(),
        "salary": randint(10000, 1000000),
        "age": fake_age,
        "dob": fake_dob,
        "join_date": gen_datetime().isoformat()
    }

    key = struct['join_date'][:10] + "/" + struct['uuid']
    struct['json_path'] = f's3://{BUCKET}/hdfs/hdfs-fakedatabase/json/{key}.json'

    return struct

def save_json_to_s3(json_data):
    """_summary_

    Args:
        json_data (_type_): _description_

    Returns:
        _type_: _description_
    """
    s3 = boto3.resource('s3')
    
    key=json_data['json_path'].split("/")[-2]
    filename=json_data['json_path'].split("/")[-1]
    
    s3object = s3.Object(BUCKET, f'hdfs/hdfs-fakedatabase/json/{key}/{filename}')
    tosave_object = (bytes(json.dumps(json_data).encode('UTF-8')))
    
    s3object.put(Body=tosave_object)

    return tosave_object

def lambda_handler(event, context):
    """_summary_

    Args:
        event (_type_): _description_
        context (_type_): _description_

    Returns:
        _type_: _description_
    """
    json_doc=create_json()
    body=save_json_to_s3(json_doc)

    return body

