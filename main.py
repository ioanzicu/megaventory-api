import requests


API_KEY = 'a74a5edc5a7c3280@m115629'


def build_url(endpoint):
    '''Return URL string, endpoint should not without slash like '/URL' but just 'URL\''''
    return f'https://api.megaventory.com/v2017a/{endpoint}'


def make_post_request(URL, API_KEY):

    headers = {'Accept': 'application/json'}
    req = ''

    try:
        data = {'APIKEY': API_KEY}
        req = requests.post(url=URL, headers=headers,
                            data=data)

        # req_data = req.text
        req_data = req.json()
        print(f'Data: {req_data}')

    except requests.exceptions.HTTPError as err:
        print(f'HTTP Error: {err}')
    except requests.exceptions.ConnectionError as err:
        print(f'Error Connecting {err}')
    except requests.exceptions.Timeout as err:
        print(f'Timout, try again {err}')
    except requests.exceptions.TooManyRedirects as err:
        print(f'Bad url {err}')
    except requests.exceptions.RequestException as err:
        # Fatal error
        print(f'Fatal Error: {err}')
        raise SystemExit(err)
    except ValueError as err:
        print(f'Decoding JSON has failed')


# /Product/ProductUpdate
def build_product(SKU, description, sales_price=0.0, purchase_price=0.0):
    new_product = {
        'mvProduct': {
            'ProductSKU': SKU,
            'ProductDescription': description,
            'ProductSellingPrice': sales_price,
            'ProductPurchasePrice': purchase_price
        },
        'mvRecordAction': 'Insert'
    }
    return new_product


# /SupplierClient/SupplierClientUpdate
def build_client(name, email, shipping_address, phone):
    return {'mvSupplierClient': {
        'SupplierClientName': name,
        'SupplierClientEmail': email,
        'SupplierClientShippingAddress1': shipping_address,
        'SupplierClientPhone1': phone
    },
        'mvRecordAction': 'Insert'
    }


# /InventoryLocation/InventoryLocationUpdate
def build_warehouse(name, abbreviation, address):
    return {'mvInventoryLocation': {
        'InventoryLocationName': name,
        'InventoryLocationAbbreviation': abbreviation,
        'InventoryLocationAddress': address
    },
        'mvRecordAction': 'Insert'
    }


# Add Product                      /Product/ProductUpdate
product_URL = build_url('Product/ProductUpdate')

make_post_request(product_URL, API_KEY)


# Add Client                       /SupplierClient/SupplierClientUpdate
client_URL = build_url('/SupplierClient/SupplierClientUpdate')

# Add Warehouse                    /InventoryLocation/InventoryLocationUpdate
warehouse_URL = build_url('/InventoryLocation/InventoryLocationUpdate')

# Add Discount                     /Discount/DiscountUpdate
discount_URL = build_url('/Discount/DiscountUpdate')

# Create a Sales Order as Verified /PurchaseOrder/PurchaseOrderUpdate
verified_purchase_URL = build_url('/PurchaseOrder/PurchaseOrderUpdate')
