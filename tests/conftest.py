import copy
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Return a TestClient for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Deep-copy and restore the `activities` mapping around each test to ensure isolation."""
    initial = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(initial)
