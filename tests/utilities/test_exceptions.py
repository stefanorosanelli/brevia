"""Exceptions module tests"""
from fastapi.testclient import TestClient
from fastapi import FastAPI
from brevia.routers import collections_router
from brevia.utilities.exceptions import register_exception_handler

app = FastAPI()
app.include_router(collections_router.router)
client = TestClient(app)
register_exception_handler(app)


def test_exception_handler():
    """Test register_exception_handler method"""
    body = '{"name": "test_collection", "cmetadata": {}}'
    response = client.post('/collections', headers={}, content=body)

    assert response.status_code == 422
    json = response.json()
    assert json['status_code'] == 422
    assert json['data'] is None
    assert 'Field required' in json['message']
