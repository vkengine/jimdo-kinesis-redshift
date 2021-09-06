import boto3
import time
import json

# The kinesis stream I defined in asw console
stream_name_user_event = 'kinesis-firehose-user-event-stream'
stream_name_user_utm = 'kinesis-firehose-user-utm-stream'

k_client = boto3.client('firehose', region_name='eu-central-1')


def lambda_handler(event=None, context=None):
    for i in range(10):

        put_to_stream(i+1)

        # wait for 1 second
        time.sleep(1)


def put_to_stream(count):
    payload_user_utm = {
        "request_id": "fc417c2b-fe7a-4737-afe2-bec49c0ebd6f",
        "request_timestamp": "2020-06-01 00:00:24.000000",
        "cookie_id": "a09c4ca3-d142-4312-ba78-029c3355b8ef",
        "topic": "dolphin_cms.wizard.step.color_palette.set",
        "message": "{\"isAffiliate\":false,\"language\":\"es\",\"isRecommendedPalette\":true,\"color\":\"#6d8d79\",\"paletteIndex\":\"0\",\"workspaceId\":\"ecaca5cd-e23c-4f6d-8ec9-ad8695b378d5\"}",
        "environment": "dolphin_cms",
        "website_id": None,
        "user_account_id": "0f36f200-df29-4fbf-8625-39a88b7f778c",
        "location": "https://cms.jimdo.com/wizard/color-palette/",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
        "referrer": "https://register.jimdo.com/es/product"
    }

    payload_user_event = {
        "request_id": "cbae8544-ab7a-46a5-9253-a5c8f6612115",
        "source": "adwords",
        "medium": "cpc",
        "campaign": "Campaign Brand FR",
        "content": None,
        "term": "jimdo",
        "matchtype": "e",
        "network": "g",
        "ad_id": "12063526619",
        "ad_pos": "1t1",
        "placement": None,
        "placement_category": None,
        "testgroup": None,
        "device": "c"
    }

    k_client.put_record(
        DeliveryStreamName=stream_name_user_event,
        Record={'Data': json.dumps(payload_user_event)}
    )

    k_client.put_record(
        DeliveryStreamName=stream_name_user_utm,
        Record={'Data': json.dumps(payload_user_utm)}
    )

    print(f'Done {count}')


if __name__ == '__main__':
    lambda_handler()
