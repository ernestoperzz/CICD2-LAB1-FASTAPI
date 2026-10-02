def user_payload(uid=1, name="Ernesto", email="g00436110@atu.ie", age=21, student_id="S0436110"):
    return {
        "userid": uid,
        "name": name,
        "email": email,
        "age": age,
        "student_id": student_id
    }

def test_create_user_returns_201(client):
    response = client.post("api/users", json=user_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["userid"] == 1
    assert data["name"] == "Ernesto"
    assert data["email"] == "g00436110@atu.ie"


def test_duplicate_user_id_returns_409(client):
    client.post("/api/users", json =user_payload(uid=2))

    response = client.post("/api/users", json = user_payload(uid=2))

    assert response.status_code == 409
    assert "exists" in response.json()["detail"].lower()
