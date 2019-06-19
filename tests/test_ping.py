import json


def test_ping(client):
    """Test that the application is running"""

    res = client.get('/')
    assert res.status_code == 200
    res_data = json.loads(res.data)
    assert res_data['status'] == 'success'
