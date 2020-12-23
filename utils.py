def build_url(endpoint):
    '''Return URL string, endpoint should not without slash like '/URL' but just 'URL\''''
    return f'https://api.megaventory.com/v2017a/{endpoint}'


# Product
def build_product(SKU, description, sales_price=0.00, purchase_price=0.00):
    '''Return a new product object'''

    return {
        'mvProduct': {
            'ProductSKU': SKU,
            'ProductDescription': description,
            'ProductSellingPrice': sales_price,
            'ProductPurchasePrice': purchase_price
        },
        'mvRecordAction': 'Insert',
    }


# Client
def build_client(name, email, shipping_address, phone):
    '''Return a new client object'''

    return {'mvSupplierClient': {
        'SupplierClientName': name,
        'SupplierClientEmail': email,
        'SupplierClientShippingAddress1': shipping_address,
        'SupplierClientPhone1': phone
    },
        'mvRecordAction': 'Insert'
    }


# Warehouse
def build_warehouse(name, abbreviation, address):
    '''Return a new warehouse object'''

    return {'mvInventoryLocation': {
        'InventoryLocationName': name,
        'InventoryLocationAbbreviation': abbreviation,
        'InventoryLocationAddress': address
    },
        'mvRecordAction': 'Insert'
    }
