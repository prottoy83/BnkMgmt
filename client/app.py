from conn import connectS
from auth import loginBox

method, username, password = loginBox()

authData = [username, password]

connectS(method, authData)