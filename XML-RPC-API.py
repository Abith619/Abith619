# XML-RPC
#                               Configuration
"""url = insert server URL
db = insert database name
username = 'admin'
password = insert password for your admin user (default: admin)"""

# Test database
import xmlrpc.client
info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
url, db, username, password = info['host'], info['database'], info['user'], info['password']

# Logging in

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()
uid = common.authenticate(db, username, password, {})

# List Records

models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])

# Pagination
models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 10, 'limit': 5})

# Count records
models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])

# Read records
ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'limit': 1})
[record] = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids])
# count the number of fields fetched by default
len(record)

# List record fields
models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})

# Search and read
models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})

# Create records
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner"}])

# Update records
models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {'name': "Newer partner"}])
# get record name after having changed it
models.execute_kw(db, uid, password, 'res.partner', 'name_get', [[id]])

# Delete records
models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
# check if the deleted record is still in the database
models.execute_kw(db, uid, password, 'res.partner', 'search', [[['id', '=', id]]])

#                           Inspection and introspection
#                                                                          ir.model
models.execute_kw(db, uid, password, 'ir.model', 'create', [{
    'name': "Custom Model",
    'model': "x_custom_model",
    'state': 'manual',
}])
models.execute_kw(db, uid, password, 'x_custom_model', 'fields_get', [], {'attributes': ['string', 'help', 'type']})

#                                                                       ir.model.fields
id = models.execute_kw(db, uid, password, 'ir.model', 'create', [{
    'name': "Custom Model",
    'model': "x_custom",
    'state': 'manual',
}])
models.execute_kw(db, uid, password, 'ir.model.fields', 'create', [{
    'model_id': id,
    'name': 'x_name',
    'ttype': 'char',
    'state': 'manual',
    'required': True,
}])
record_id = models.execute_kw(db, uid, password, 'x_custom', 'create', [{'x_name': "test record"}])
models.execute_kw(db, uid, password, 'x_custom', 'read', [[record_id]])
# O/P = 
"""[
    {
        "create_uid": [1, "Administrator"],
        "x_name": "test record",
        "__last_update": "2014-11-12 16:32:13",
        "write_uid": [1, "Administrator"],
        "write_date": "2014-11-12 16:32:13",
        "create_date": "2014-11-12 16:32:13",
        "id": 1,
        "display_name": "test record"
    }
]
"""