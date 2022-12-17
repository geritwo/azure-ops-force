import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient

AZURE_RESOURCE_GROUP="ImageDataMiner"
AZURE_DATA_FACTORY_NAME="FlickrFlipprADF"


def main():
    client = DataFactoryManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=os.getenv('AZURE_SUBSCRIPTION_ID')
    )

    response = client.linked_services.list_by_factory(
        resource_group_name=AZURE_RESOURCE_GROUP,
        factory_name=AZURE_DATA_FACTORY_NAME,
    )
    for item in response:
        print(item)


if __name__ == "__main__":
    main()