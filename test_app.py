from app import app

def test_home():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.data.decode("utf-8") == "Hello from CI/CD pipeline!"
