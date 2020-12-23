import requests
import json
from utils import build_url, build_client, build_product, build_warehouse

API_KEY = 'b2bdcde7751b01c7@m115629'


def make_post_request(URL, API_KEY, data):

    headers = {'Accept': 'application/json'}
    params = {'APIKEY': API_KEY}

    try:
        print(json.dumps(data), end='\n\n')

        response = requests.post(
            url=URL, headers=headers, params=params, data=json.dumps(data))

        if response:
            try:
                response_json = response.json()
                if response_json['ResponseStatus']['ErrorCode'] == "400":
                    print(
                        f'Request Failed, Error: {response_json["ResponseStatus"]}')
                else:
                    print(
                        f'Data: {response_json}')

            except ValueError as err:
                print(f'Decoding JSON has failed')
        else:
            print(f'Something went wrong, STATUS CODE: {response.status_code}')

    except requests.exceptions.HTTPError as err:
        print(f'HTTP Error: {err}')
    except requests.exceptions.ConnectionError as err:
        print(f'Error Connecting {err}')
    except requests.exceptions.Timeout as err:
        print(f'Timout, try again {err}')
    except requests.exceptions.TooManyRedirects as err:
        print(f'Bad url {err}')
    except requests.exceptions.RequestException as err:
        print(f'Fatal Error: {err}')
        raise SystemExit(err)


# Add Product                      /Product/ProductUpdate
product_URL = build_url('Product/ProductUpdate')
new_product = build_product('1112256', 'Nike shoes', 99.99, 44.99)

make_post_request(product_URL, API_KEY, new_product)


# Add Client                       /SupplierClient/SupplierClientUpdate
client_URL = build_url('/SupplierClient/SupplierClientUpdate')

# Add Warehouse                    /InventoryLocation/InventoryLocationUpdate
warehouse_URL = build_url('/InventoryLocation/InventoryLocationUpdate')

# Add Discount                     /Discount/DiscountUpdate
discount_URL = build_url('/Discount/DiscountUpdate')

# Create a Sales Order as Verified /PurchaseOrder/PurchaseOrderUpdate
verified_purchase_URL = build_url('/PurchaseOrder/PurchaseOrderUpdate')
