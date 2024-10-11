from ml_app.train import Model

def test_model():
    model = Model()
    assert model._score() > 0.5  # Example test
