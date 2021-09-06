import boto3
import psycopg2
import os
import logging
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

logger = logging.getLogger(__name__)

access_key = os.getenv('access_key_id')
secret_access_key = os.getenv('secret_access_key')
redshift_access_key = os.getenv('redshift_access_key')
redshift_access_key_secret = os.getenv('redshift_access_key_secret')
RS_HOST = os.getenv('RS_HOST')
RS_PORT = os.getenv('RS_PORT')
RS_USER = os.getenv('RS_USERNAME')
DATABASE = os.getenv('DATABASE')

s3_event_bucket = os.getenv('event_bucket')
s3_utm_bucket = os.getenv('utm_bucket')
bucket_region = os.getenv('bucket_region')


def load_to_tables(connection, list_of_files):
    utm_files = list_of_files['utm']
    event_files = list_of_files['event']
    cur = connection.cursor()

    for file in utm_files:
        file_name_utm = f's3://{s3_utm_bucket}/{file}'

        user_utm_table = f"""
            COPY utm FROM '{file_name_utm}'
            access_key_id '{access_key}'
            secret_access_key '{secret_access_key}'
            REGION '{bucket_region}' 
            FORMAT JSON 'auto';
            """

        cur.execute(user_utm_table)

    print('utm file loaded')

    for file in event_files:
        file_name_event = f's3://{s3_event_bucket}/{file}'

        user_event_table = f"""
            COPY events FROM '{file_name_event}'
            access_key_id '{access_key}'
            secret_access_key '{secret_access_key}'
            REGION '{bucket_region}' 
            FORMAT JSON 'auto';
            """

        cur.execute(user_event_table)

    print('event file added')

    connection.commit()

    print('data added')


def db_connection():
    CLUSTER_ID = RS_HOST.split('.')[0]

    session = boto3.session.Session(aws_access_key_id=redshift_access_key,
                                    aws_secret_access_key=redshift_access_key_secret)
    client = session.client('redshift')

    cluster_creds = client.get_cluster_credentials(DbUser=RS_USER,
                                                   DbName=DATABASE,
                                                   ClusterIdentifier=CLUSTER_ID,
                                                   AutoCreate=False)

    try:
        conn = psycopg2.connect(
            host=RS_HOST,
            port=RS_PORT,
            user=cluster_creds['DbUser'],
            password=cluster_creds['DbPassword'],
            database=DATABASE
        )
        return conn
    except psycopg2.Error:
        logger.exception('Failed to open database connection.')


def get_list_of_files_from_s3(s3_keys):
    year = s3_keys['year']
    month = s3_keys['month']
    day = s3_keys['day']
    hour = s3_keys['hour']

    key = f'{year}/{month}/{day}/{hour}/'

    session = boto3.Session(aws_access_key_id=access_key,
                            aws_secret_access_key=secret_access_key)

    s3 = session.resource('s3')
    event_bucket = s3.Bucket(s3_event_bucket)
    utm_bucket = s3.Bucket(s3_utm_bucket)

    event_files = []
    utm_files = []

    for files in event_bucket.objects.filter(Prefix=key):
        event_files.append(files.key)

    for files in utm_bucket.objects.filter(Prefix=key):
        utm_files.append(files.key)

    print('files fetched')
    return {'utm': utm_files, 'event': event_files}


def lambda_handler(event=None, context=None):
    files = get_list_of_files_from_s3(event)
    conn = db_connection()
    load_to_tables(conn, files)


# if __name__ == '__main__':
#     # this should come from cron job that schedules this lambda eg: airflow
#     payload = {'year': '2021', 'month': '09',
#                'day': '06', 'hour': '21'}
#
#     lambda_handler(event=payload)
