def test_root_redirects_to_static_index(client):
    # disable auto-following redirects so we can assert the redirect response
    resp = client.get("/", follow_redirects=False)
    assert resp.status_code in (302, 307)
    assert resp.headers.get("location") == "/static/index.html"


def test_static_index_served(client):
    resp = client.get("/static/index.html")
    assert resp.status_code == 200
    assert "<" in resp.text  # crude check that HTML was returned
