import requests

# Replace with your API key
api_key = "your_api_key_here"

# Barcode to search for
barcode = "5010029204209"  # Replace with the barcode you want to search

# URL for the API endpoint
url = f"https://api.ean-search.org/api?token={api_key}&op=barcode-lookup&ean={barcode}"

# Send an HTTP GET request to the API
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract and print product information
if data.get('status') == 'success':
    product_info = data.get('product')
    print("Product Description:", product_info.get('description', 'Description not available'))
else:
    print("Failed to fetch product information.")