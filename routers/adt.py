import os
from fastapi import APIRouter, HTTPException, status
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient
from azure.core.exceptions import ResourceNotFoundError
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix='/acs'
)

router.client = DigitalTwinsClient(os.environ["AZURE_URL"], DefaultAzureCredential())

class Patch(BaseModel):
    op: str
    path: str
    value: object

@router.get("/models")
def get_models():
    models = router.client.list_models()
    payload = []
    for model in models:
        payload.append(model)
    return { "data": payload }

@router.get("/model/${model_id}")
def get_model(model_id: str):
    model = router.client.get_model(model_id)
    print(model)
    return { "data": model }

@router.get("/twins")
def get_twins(query: str):
    twins = router.client.query_twins(query)
    payload = []
    for twin in twins:
        payload.append(twin)
    return { "data": payload }

@router.get("/twin/${twin_id}")
def get_twin(twin_id: str):
    try:
        twin = router.client.get_digital_twin(twin_id)
        return { "data": twin }
    except ResourceNotFoundError as e:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

@router.get("/twin/${twin_id}/relationships")
def get_twin_relationship(twin_id: str):
    relationships = router.client.list_relationships(twin_id)
    payload = []
    for relationship in relationships:
        payload.append(relationship)
    return { "data": payload }

@router.get("/twin/${twin_id}/incoming_relationships/")
def get_twin_incoming_relationships(twin_id: str):
    relationships = router.client.list_incoming_relationships(twin_id)
    payload = []
    for relationship in relationships:
        payload.append(relationship)
    return { "data": payload }

@router.put("/twin/${twin_id}/property")
def update_twin_property(twin_id: str, patches: List[Patch]):
    try:
        payload = []
        for patch in patches:
            payload.append({
                "op": patch.op,
                "path": patch.path,
                "value": patch.value
            })
        router.client.update_digital_twin(twin_id, payload)
        return { "data": "success" }
    except ResourceNotFoundError as e:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

# Tommy
@router.post('/updateViewAngle')
def updateMapView():
    twin_id = "viewAngle"
    # 取得前端傳過來的數值
    patch = [
        {
            "op": "replace",
            "path": "/viewAngle",
            "value": "Human"
        },        
    ]
    router.client.update_digital_twin(twin_id, patch)
    return "success"

@router.get('/getMapView')
def getMapView():
    twin_id = "viewAngle"
    # 取得前端傳過來的數值
    get_twin = router.client.get_digital_twin(twin_id)
    return get_twin["viewAngle"]