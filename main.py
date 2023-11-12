import getpass
import os
from dentistas.administrador import login as adminLogin, routeUser
import json
f = open('mensajes.es.json')
messages = json.load(f)
treatments = {}
adminLoginState = False
state = 'welcome'

while True:
    useMode = int(
        input(messages[state]))
    if useMode == 0:
        state = 'adminPwdRequest'
        pwd = getpass.getpass(messages[state])
        adminLoginState = adminLogin(pwd)
        state = "adminLoged" if adminLoginState else "adminNotLoged"
        print(messages[state])
        if adminLoginState == False: continue
        state = "adminActions"
        routeUser(state)


    elif useMode == 1:
        user = input('Indique su DNI')
    elif useMode == 2:
        break
    else:
        print('¡La opción escogida no es correcta!')
    state = 'welcome'
    # break

    os.system('clear')
