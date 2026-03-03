def test_signup_adds_participant_and_prevents_duplicates(client):
    # pick an existing activity
    activities_resp = client.get("/activities")
    assert activities_resp.status_code == 200
    activities = activities_resp.json()
    activity_name = next(iter(activities.keys()))

    email = "alice@example.com"

    # register successfully
    resp = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert resp.status_code == 200

    # verify via GET that participant was added
    activities_after = client.get("/activities").json()
    participants = activities_after[activity_name].get("participants", [])
    assert email in participants

    # registering again should return 400 (already registered)
    resp_dup = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert resp_dup.status_code == 400
