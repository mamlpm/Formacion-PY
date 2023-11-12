from dotenv import load_dotenv
import os
import json
import pprint
load_dotenv()
f = open('mensajes.es.json')
messages = json.load(f)
registeredInformation = ['Nombre', 'Precio', 'Moneda']
treatments = {
    1: {'Nombre': 'Endodoncia', 'Precio': 1000, 'Moneda': 'EUR'},
    2: {'Nombre': 'Empaste', 'Precio': 900, 'Moneda': 'EUR'},
    3: {'Nombre': 'Limpieza', 'Precio': 50, 'Moneda': 'EUR'},
    4: {'Nombre': 'Implante', 'Precio': 3000, 'Moneda': 'EUR'},
}


def inputUpsertValues(state, treatmentToUpdate={}):
    toReturn = {}
    for key in registeredInformation:
        value = input(messages[state + key])
        emptyText = value.strip() == ''
        if state == 'insert':
            toReturn[key] = 'EUR' if key == 'Moneda' and emptyText else 0 if key == 'Precio' and emptyText else int(
                value) if key == 'Precio' else value
        else:
            toReturn[key] = treatmentToUpdate[key] if emptyText else int(
                value) if key == 'Precio' else value
    return toReturn


def insert(state='insert'):
    dictToInsert = inputUpsertValues(state)
    treatments[len(treatments) + 1] = dictToInsert
    return


def get(state='get'):
    pprint.pprint(treatments)
    if state == 'get':
        input(messages['pressAnyKey'])
    return treatments


def getById(id, state='getById'):
    return treatments[id]


def update(state='update'):
    get(state)
    keyToUpdate = int(input(messages["updateQuestion"]))
    if keyToUpdate > len(treatments):
        print(messages['outOfRangeError'])
        return
    itemToUpdate = getById(keyToUpdate)
    print('Actualizando el siguiente tratamiento: ', itemToUpdate)
    values = inputUpsertValues(state, itemToUpdate)
    treatments[keyToUpdate] = values
    return


def delete(state='delete'):
    get(state)
    keyToDelete = int(input(messages["updateQuestion"]))
    confirmation = input(messages['confirmationMessage'])
    if confirmation != 'n':
        treatments.pop(keyToDelete)
    return


def login(insertedPassword):
    return insertedPassword == os.environ.get('admin-pass')


def routeUser(state):
    while True:
        option = int(input(messages[state]))
        if option == 0:
            insert()
        elif option == 1:
            get()
        elif option == 2:
            update()
        elif option == 3:
            delete()
        elif option == 4:
            return False
