import boto3
import psycopg2
import os
import logging
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

logger = logging.getLogger(__name__)

access_key = os.getenv('access_key_id')
secret_access_key = os.getenv('secret_access_key')
file_name_event = 's3://jimdo-user-event/2021/09/06/02/kinesis-firehose-user-utm-stream-1-2021-09-06-02-32-06-5b39f574-09d3-4675-be7d-dc4a12ceb67b'


def load_to_tables(connection):
    user_utm_table = f"""
    COPY events FROM '{file_name_event}'
    access_key_id '{access_key}'
    secret_access_key '{secret_access_key}'
    REGION 'eu-central-1' 
    FORMAT JSON 'auto';
    """

    cur = connection.cursor()
    cur.execute(user_utm_table)
    connection.commit()

    logger.info("data added")


def db_connection():
    RS_PORT = 5439
    RS_USER = 'username'
    DATABASE = 'jimdo'
    CLUSTER_ID = 'jimdo-redshift-cluster'
    RS_HOST = 'jimdo-redshift-cluster.c6ewv4ndpwpt.eu-central-1.redshift.amazonaws.com'

    session = boto3.session.Session(profile_name='buildyourjazz')
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


def lambda_handler(event=None, context=None):
    conn = db_connection()
    load_to_tables(conn)


if __name__ == '__main__':
    lambda_handler()
