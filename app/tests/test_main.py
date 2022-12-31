from fastapi.testclient import TestClient
from ..main import app, Msg, Record

client = TestClient(app)

def test_getRoot():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == Msg(message='Hello World')

def test_getItems():
        resp = client.get("/items/2?q=qval2")
        assert resp.status_code == 200
        assert resp.json() == Record(item_id=2, q='qval2', extra_field='extra val')
