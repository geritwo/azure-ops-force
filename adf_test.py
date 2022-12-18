import os
import json

from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient

AZURE_RESOURCE_GROUP = "ImageDataMiner"
AZURE_DATA_FACTORY_NAME = "FlickrFlipprADF"


def get_linked_services(client):
    linked_services = client.linked_services.list_by_factory(
        resource_group_name=AZURE_RESOURCE_GROUP,
        factory_name=AZURE_DATA_FACTORY_NAME,
    )

    return linked_services


def main():
    client = DataFactoryManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=os.getenv('AZURE_SUBSCRIPTION_ID')
    )

    linked_services_details = get_linked_services(client)
    for l in linked_services_details:
        s = str(l).split(', \'properties\':')[0].replace('\'', '\"') + "}"
        j = json.loads(s)
        print(j['name'])


if __name__ == "__main__":
    main()
