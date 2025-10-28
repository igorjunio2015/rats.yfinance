import requests
import json

base_url = "http://localhost:8000"

def test_health():
    """Testa o endpoint de health"""
    response = requests.get(f"{base_url}/health")
    print("Health Check:", response.json())
    return response.status_code == 200

def test_ticker_info():
    """Testa buscar informações de uma ação"""
    data = {"symbol": "AAPL"}
    response = requests.post(f"{base_url}/ticker/info", json=data)
    if response.status_code == 200:
        print("Ticker Info Success:", response.json().get('longName', 'N/A'))
        return True
    else:
        print("Ticker Info Error:", response.text)
        return False

def test_search():
    """Testa busca de ações"""
    response = requests.get(f"{base_url}/market/search/Apple")
    if response.status_code == 200:
        results = response.json()
        print(f"Search Results: {len(results)} items found")
        return True
    else:
        print("Search Error:", response.text)
        return False

if __name__ == "__main__":
    print("🧪 Testando Finance Service...")
    print(f"📡 Base URL: {base_url}")
    print(f"📚 Documentação: {base_url}/docs")
    print(f"✨ Scalar UI: {base_url}/scalar")
    print("-" * 50)
    
    tests = [
        ("Health Check", test_health),
        ("Ticker Info", test_ticker_info), 
        ("Search", test_search)
    ]
    
    for name, test_func in tests:
        try:
            success = test_func()
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"{status} {name}")
        except Exception as e:
            print(f"❌ FAIL {name}: {str(e)}")
        print()