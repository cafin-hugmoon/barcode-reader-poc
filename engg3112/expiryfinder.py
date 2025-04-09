import requests

def get_product_details(ean):
    url = f"https://world.openfoodfacts.org/api/v0/product/{ean}.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("status") == 1:
            product = data.get("product")
            name = product.get("product_name")
            quantity = product.get("quantity")
            expiry_date = product.get("expiration_date")  # Field may vary
            return name, quantity, expiry_date
        else:
            return None, None, None
    else:
        print("Error:", response.status_code)
        return None, None, None
    
