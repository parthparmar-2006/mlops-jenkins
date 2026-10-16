import numpy as np

from app import app, model


def test_model_predicts_setosa():
    assert model.predict(np.array([[5.1, 3.5, 1.4, 0.2]]))[0] == "Iris-setosa"


def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
