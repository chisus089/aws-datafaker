<p align="center">
<img src="imgs/logo2.png" alt="bigbyte" width="30%">

# How to generate a 1M random users serverless database in AWS using: Serverless Application Model (AWS SAM) + AWS Glue + AWS Athena + python
</p>

A tutorial on how to build a scalable architecture in AWS to generate random data, using Lambda Functions, S3 storage, AWS Glue, AWS athena and python

The tutorial focuses on: 

1. write data in json format using AWS SAM,
2. create an AWS GlueJob to transform json(read json) to parquet(write parquet),
3. add an AWS LambdaFunction to trigger GlueJob for each json document (write 1 parquet for each 1 json)
4. write data concurrently using AWS SAM mapped function
    + invoke AWS LambdaFunction concurrently
    + start AWS GlueJob concurrently
6. explore data using AWS Athena

The following image represents the pipeline in a graphic way.

<p align="center">
<img src="gifs/AWSDataFakerGif.gif" alt="bigbyte" width="95%">
</p>



## Table Of Contents

- [Generate data](#Generate-data)
    - Install AWS Serverless Application Model
    - Write json data to S3 using faker and AWS SAM Function
    - Deploy AWS SAM function
    - Invoke AWS SAM function

- [Transform data](#Transform-data)
    - Transform json to parquet with AWS Glue
    - Save parquet to S3

- [Trigger process](#Trigger)
    - Create a Lambda function to start AWS Glue Job
    - Create a S3 trigger

- [Test process](#Invoke)
    - Invoke process concurrently using AWS SAM


## Generate-data
#### 1. Install AWS Serverless Application Model

Install [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) 

Create a working folder

`mkdir sam-apps`
`cd sam-apps`

Create a new application using command:

`sam init`

Choose 1, 1, N, choose your python dist (20), 1, N, N, N, choose a project name

A folder with a new SAM application should 

#### 2. Write json data to S3 using faker and AWS SAM Function
    
[Faker](https://pypi.org/project/Faker/) is a Python package that generates fake data.

#### 3. Deploy AWS SAM function
#### 4. Invoke AWS SAM function


## Transform-data
#### 5. Transform json to parquet with AWS Glue
#### 6. Save parquet to S3


## Trigger
#### 7. Create a Lambda function to start AWS Glue Job
#### 8. Create a S3 trigger


## Invoke
#### 9. Invoke process concurrently using AWS SAM




## To-do



## Team

<img src="https://avatars.githubusercontent.com/u/39705698?v=4 " alt="Jesus Martinez" width="30%" style="border-radius: 50%" >

[Jesus Jorge Martinez Rios](https://www.linkedin.com/in/jesusjmartinezr/) 

## [License](https://github.com/chisus089/flight_data_tutorial/blob/main/LICENSE)

© Jesus Jorge Martinez Rios 

[jesus.martinez89@hotmail.com](jesus.martinez89@hotmail.com)