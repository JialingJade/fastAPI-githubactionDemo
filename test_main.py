#test_main.py
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
	
def test_read_coursecat():
    response = client.get("/tpgateway/coursecat")
    assert response.status_code == 200
    assert response.json() == {"message": "tpgw_read_coursecat"}
	
def test_read_coursesubcat():
    response = client.get("/tpgateway/coursesubcat/1")
    assert response.status_code == 200
    assert response.json() == {"cat_id": 1}
	
def test_read_coursesubcat_bad_catid():
    response = client.get("/tpgateway/coursesubcat/abc")
    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': ['path', 'cat_id'],
                      'msg': 'value is not a valid integer',
                      'type': 'type_error.integer'}]}
    
    
