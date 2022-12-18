import os
import json

from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient

AZURE_RESOURCE_GROUP = "ImageDataMiner"
AZURE_DATA_FACTORY_NAME = "FlickrFlipprADF"
AZURE_SUBSCRIPTION_ID = os.getenv('AZURE_SUBSCRIPTION_ID')


def get_linked_services(client):
    linked_services = client.linked_services.list_by_factory(
        resource_group_name=AZURE_RESOURCE_GROUP,
        factory_name=AZURE_DATA_FACTORY_NAME,
    )

    return linked_services


def main():
    client = DataFactoryManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=AZURE_SUBSCRIPTION_ID
    )

    linked_services_details = get_linked_services(client)
    for l in linked_services_details:
        s = str(l).split(', \'properties\':')[0].replace('\'', '\"') + "}"
        j = json.loads(s)
        print(j['name'])

    test_endpoint = f"https://management.azure.com/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourcegroups/" \
                    f"{AZURE_RESOURCE_GROUP}/providers/Microsoft.DataFactory/factories/{AZURE_RESOURCE_GROUP}/" \
                    f"testConnectivity?api-version=2018-06-01"

    payload = '{"linkedService":' \
              '{"type":"LinkedServiceReference",' \
              '"referenceName":"AzureBlobStorage1"},' \
              '"activityId":"3a966aae-b74f-4d71-a964-931cdf0e44e1",' \
              '"tags":{},' \
              '"userAgent":"Madrid"}'


if __name__ == "__main__":
    main()
