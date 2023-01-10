# Azure Digital Twin Backend

This project is build for poxy of azure services, which include digital twins and communication sevices. The project is built by FastAPI and Azure ADK of each services.

## Prerequisite

We use pipenv as the packaging tool for Python, so if you don't have pipenv, please install pipenv first.


```sh
pip install pipenv
```

Install the required packages from Pipfile.

```sh
pipenv install
```

Create .env to provide connection information for azure digital twins and azure communication services.

|Variable|Description|
|:-|--|
| COMMUNICATION_SERVICES_CONNECTION_STRING| This string provide enpoint and api key for communication services. You can find it at key section of the resourse from the Azure portal. |
| HOLOLENS_ACS_TOKEN | *(optional)* This is the identity of HoloLens2 for communication services. |
| WEB_ACS_TOKEN | *(optional)* This is the identity of webpage for communication services. |
| AZURE_URL | Endpoint of Azure Digital Twins |
| AZURE_TENANT_ID | Azure tenant id |
| AZURE_CLIENT_ID | Azure client id |
| AZURE_CLIENT_SECRET | Azure client secret |