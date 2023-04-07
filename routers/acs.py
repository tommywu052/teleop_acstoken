import os
from fastapi import APIRouter
from azure.communication.identity import CommunicationIdentityClient, CommunicationUserIdentifier

router = APIRouter(
    prefix='/acs'
)

connection_string = os.environ["COMMUNICATION_SERVICES_CONNECTION_STRING"]

# Instantiate the identity client
router.client = CommunicationIdentityClient.from_connection_string(connection_string)

HOLOLENS_ACS_TOKEN = os.environ["HOLOLENS_ACS_TOKEN"]
WEB_ACS_TOKEN = os.environ["WEB_ACS_TOKEN"]

@router.get("/user/hololens")
def get_acs_user():
    return HOLOLENS_ACS_TOKEN

@router.get("/user/web")
def get_acs_user():
    return WEB_ACS_TOKEN

@router.get("/token/hololens")
def get_acs_token():
    identity = CommunicationUserIdentifier(HOLOLENS_ACS_TOKEN)
    token_result = router.client.get_token(identity, ["voip"])
    return token_result[0]

@router.get("/token/web")
def get_acs_token():
    identity = CommunicationUserIdentifier(WEB_ACS_TOKEN)
    token_result = router.client.get_token(identity, ["voip"])
    return token_result[0]

@router.get("/grpcall/createuser")
def get_grpcall_createuser():
    identity = router.client.create_user()
    return identity.properties['id']

@router.get("/grpcall/tokenbyid/{userid}")
def get_grpcall_tokenbyid(userid:str):
    identity = CommunicationUserIdentifier(userid)
    token_result = router.client.get_token(identity, ["voip"])
    return token_result[0]

@router.get("/grpcall/idtoken")
def get_grpcall_idtoken():
    identity = router.client.create_user()
    token_result = router.client.get_token(identity, ["voip"])
    return token_result[0]