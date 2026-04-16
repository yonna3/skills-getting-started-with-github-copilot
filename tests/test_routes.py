def test_root_redirects_to_static_ui(client):
    # Arrange

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_expected_data(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    data = response.json()
    assert "Chess Club" in data
    assert data["Chess Club"]["description"] == "Learn strategies and compete in chess tournaments"
    assert data["Chess Club"]["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert data["Chess Club"]["max_participants"] == 12
    assert data["Chess Club"]["participants"] == ["michael@mergington.edu", "daniel@mergington.edu"]