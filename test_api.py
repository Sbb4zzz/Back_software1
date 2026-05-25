import requests
import json

BASE_URL = "http://localhost:5001"

def test_endpoints():
    print("Testing Mundial 2026 Hub Backend API")
    print("=" * 50)

    # Test root endpoint
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Root endpoint: {response.status_code}")
    except Exception as e:
        print(f"❌ Root endpoint failed: {e}")

    # Test partidos endpoint
    try:
        response = requests.get(f"{BASE_URL}/partidos")
        data = response.json()
        print(f"✅ Partidos endpoint: {response.status_code} - {len(data['partidos'])} partidos")
    except Exception as e:
        print(f"❌ Partidos endpoint failed: {e}")

    # Test registration
    try:
        data = {
            "nombre": "Test User 2",
            "email": "test2@example.com",
            "password": "password123",
            "rol": "aficionado"
        }
        response = requests.post(f"{BASE_URL}/registro", json=data)
        if response.status_code == 201:
            user_data = response.json()
            user_id = user_data['usuario_id']
            print(f"✅ Registration: {response.status_code} - User ID: {user_id}")

            # Test login
            login_data = {"email": "test2@example.com", "password": "password123"}
            login_response = requests.post(f"{BASE_URL}/login", json=login_data)
            print(f"✅ Login: {login_response.status_code}")

            # Test agenda
            agenda_response = requests.get(f"{BASE_URL}/agenda/{user_id}")
            print(f"✅ Agenda: {agenda_response.status_code}")

            # Test abrir paquete
            paquete_response = requests.post(f"{BASE_URL}/album/abrir-paquete/{user_id}")
            print(f"✅ Abrir paquete: {paquete_response.status_code}")

            # Test colección
            coleccion_response = requests.get(f"{BASE_URL}/album/coleccion/{user_id}")
            print(f"✅ Colección: {coleccion_response.status_code}")

        else:
            print(f"❌ Registration failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Registration/Login test failed: {e}")

    print("\n🎉 Backend testing completed!")

if __name__ == "__main__":
    test_endpoints()