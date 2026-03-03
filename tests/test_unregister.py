def test_unregister_removes_participant_and_handles_errors(client):
    activities_resp = client.get("/activities")
    activities = activities_resp.json()
    activity_name = next(iter(activities.keys()))

    email = "bob@example.com"

    # ensure registered first
    resp = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert resp.status_code == 200

    # unregister successfully
    resp_del = client.delete(f"/activities/{activity_name}/unregister", params={"email": email})
    assert resp_del.status_code == 200

    # unregistering again should return 400 or 404 (not registered)
    resp_del_again = client.delete(f"/activities/{activity_name}/unregister", params={"email": email})
    assert resp_del_again.status_code in (400, 404)
