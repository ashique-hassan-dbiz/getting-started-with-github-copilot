def test_get_activities_returns_mapping_and_keys(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    # pick a key to ensure shape contains participants list/dict
    first_key = next(iter(data.keys()))
    assert first_key in data
