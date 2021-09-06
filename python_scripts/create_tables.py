import boto3
import psycopg2
import logging

logger = logging.getLogger(__name__)


def create_tables(connection):
    user_utm_table = """
    CREATE TABLE IF NOT EXISTS public.utm
        (
            request_id VARCHAR(56) NOT NULL  ENCODE zstd
            ,source VARCHAR(255) NOT NULL  ENCODE zstd
            ,medium VARCHAR(255) NOT NULL  ENCODE zstd
            ,campaign VARCHAR(255)   ENCODE zstd
            ,content VARCHAR(255)   ENCODE zstd
            ,term VARCHAR(255)   ENCODE zstd
            ,matchtype VARCHAR(255)   ENCODE zstd
            ,"network" VARCHAR(255)   ENCODE zstd
            ,ad_id VARCHAR(255)   ENCODE zstd
            ,ad_pos VARCHAR(255)   ENCODE zstd
            ,placement VARCHAR(255)   ENCODE zstd
            ,placement_category VARCHAR(255)   ENCODE zstd
            ,testgroup VARCHAR(255)   ENCODE zstd
            ,device VARCHAR(255)   ENCODE zstd
        )
    """

    user_event_table = """
    CREATE TABLE IF NOT EXISTS public.events
        (
            request_id CHAR(36) NOT NULL
            ,request_timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL
            ,cookie_id CHAR(36) NOT NULL
            ,topic VARCHAR(1024) NOT NULL
            ,message VARCHAR(3128)
            ,environment VARCHAR(30)
            ,website_id CHAR(36)
            ,user_account_id CHAR(36)
            ,"location" VARCHAR(5000)
            ,user_agent VARCHAR(1024)
            ,referrer VARCHAR(500)
        )
    """

    cur = connection.cursor()
    cur.execute(user_event_table)
    cur.execute(user_utm_table)
    conn.commit()

    logger.info("tables created")


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


if __name__ == '__main__':
    conn = db_connection()
    create_tables(conn)
