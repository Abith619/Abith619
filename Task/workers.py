import xmlrpc.client
import socket, ssl
url='http://143.1.1.143:8079'
db='manufacturing'
username='dhilip@xbs.in'
password='Solution@456'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url),allow_none=True,context=ssl._create_unverified_context())
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url),allow_none=True,context=ssl._create_unverified_context())
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
val = models.execute_kw(db, uid, password, 'worker.master', 'create', [{'machine_id': IPAddr,'worker_name':hostname}])
if val:
    print('Woker Created')