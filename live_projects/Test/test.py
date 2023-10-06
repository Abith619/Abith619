import xmlrpc.client

url = 'https://limgro-staging-9294758.dev.odoo.com/'
db = 'limgro-staging-9294758'
username = 'abithraj.s@insoft.com'
password = 'abith@456'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

backup_id = models.execute_kw(db, uid, password, 'ir.backup', 'create', [{
    'name': 'Odoo Backup',
    'description': 'Backup Description',
}])

models.execute_kw(db, uid, password, 'ir.backup', 'backup', [[backup_id]])

print('Database backup created successfully.')
