import json

import requests_unixsocket

session = requests_unixsocket.Session()
r = session.get('http+unix://%2Frun%2Fpodman%2Fpodman.sock/v2.0.0/libpod/info')
print(json.dumps(r))
