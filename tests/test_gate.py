from fastapi.testclient import TestClient
from mlgitops.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'desired': 'champion', 'live': 'champion'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'desired': 'champion', 'live': 'challenger'}).json()
    assert bad["passed"] is False
    assert "alias_drift" in bad["failed"]
