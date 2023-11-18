import getpass
import os
from dentistas.administrador import login as adminLogin, routeUser
import json
import time
f = open('mensajes.es.json')
messages = json.load(f)
adminLoginState = False
state = 'welcome'

while True:
    userResponse = input(messages[state])
    useMode = int(userResponse if userResponse.isnumeric() else -1)
    if useMode == 0:
        state = 'adminPwdRequest'
        pwd = getpass.getpass(messages[state])
        adminLoginState = adminLogin(pwd)
        state = "adminLoged" if adminLoginState else "adminNotLoged"
        print(messages[state])
        if adminLoginState == False:
            state = "welcome"
            continue
        state = "adminActions"
        routeUser(state)

    elif useMode == 1:
        user = input('Indique su DNI')
    elif useMode == 2:
        break
    else:
        state = "errorMessage"
        print(messages[state])
        time.sleep(5)
        
    state = 'welcome'
    # break

    os.system('clear')
