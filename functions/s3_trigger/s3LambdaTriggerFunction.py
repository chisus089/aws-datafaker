# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


class GlueWrapper:
    """Encapsulates AWS Glue actions."""

    def __init__(self):
        """
        :param glue_client: A Boto3 Glue client.
        """
        self.glue_client = boto3.client("glue")


    def start_job_run(self, name, file_key):
        """
        Starts a job run. A job run extracts data from the source, transforms it,
        and loads it to the output bucket.

        :param name: The name of the job definition.
        :param input_database: The name of the metadata database that contains tables
                               that describe the source data. This is typically created
                               by a crawler.
        :param input_table: The name of the table in the metadata database that
                            describes the source data.
        :param output_bucket_name: The S3 bucket where the output is written.
        :return: The ID of the job run.
        """

        # The custom Arguments that are passed to this function are used by the
        # Python ETL script to determine the location of input and output data.
        response = self.glue_client.start_job_run(
            JobName=name,
            Arguments={
                "--FILE_KEY": file_key
            },
        )

        return response["JobRunId"]

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        gw = GlueWrapper()
        job_name="s3JsonToS3Parquet"
        folder=key.split("/")[-2]
        filename=key.split("/")[-1]
        file=f"{folder}/{filename}"
        gw.start_job_run(name=job_name, file_key=file)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
              
