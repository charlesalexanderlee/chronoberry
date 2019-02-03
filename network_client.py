import socket
import json
from os import system

system('clear')

HOST = socket.gethostname()
PORT = 6000
BUFFER = 2048

with socket.socket() as client_socket:
    try:
        client_socket = socket.socket()
        client_socket.connect((HOST, PORT))

        # Reads from 'settings.json' 
        with open('settings.json', 'r') as json_file:
            # Loads the JSON file into a Python object
            clock_settings = json.load(json_file)
            
            # Sends the JSON Python object as an encoded string
            client_socket.send(json.dumps(clock_settings).encode('ascii'))

        # Receives new clock settings and wrties to clock
            clock_settings = json.loads(client_socket.recv(BUFFER))

        # Writes new clock settings to 'settings.json'
        with open('settings.json', 'w') as json_file:
            json.dump(clock_settings, json_file, sort_keys=False, indent=4, separators=(',', ': '))
            
    except socket.error as error:
        print(str(error))
