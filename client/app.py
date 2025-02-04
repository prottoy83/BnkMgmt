from conn import connectS
from auth import loginBox
import json

method, username, password = loginBox()

authData = {"method": method,
            "username": username,
            "password": password}
authData = json.dumps(authData)

connectS(authData.encode())

authTF = True

