import socket
import json
from time import sleep
from os import system

system('clear')

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6000
BUFFER = 2048
CLIENT_ADDRESS = HOST + ':' + str(PORT)
RECONNECT_TIME = 10  # Seconds

def connect_to_server():
    with socket.socket() as client_socket:
        while True:
            try:
                client_socket = socket.socket()
                print('STATUS: Connecting to ' + CLIENT_ADDRESS)
                
                client_socket.connect((HOST, PORT))
                print('STATUS: Connected to ' + CLIENT_ADDRESS)

                print('STATUS: Listening for commands...')

                while True:
                    command = client_socket.recv(BUFFER).decode('ascii')
                    if command == 'disconnect':
                        print('COMMAND RECEIVED: Disconnect')
                        break
                    elif command == 'send_settings':
                        print('COMMAND RECEIVED: Send clock settings')

                        # Reads from 'settings.json' 
                        with open('settings.json', 'r') as json_file:
                            # Loads the JSON file into a Python object
                            clock_settings = json.load(json_file)

                            # Sends the JSON Python object as an encoded string
                            client_socket.send(json.dumps(clock_settings).encode('ascii'))
                    elif command == 'edit_settings':
                        print('COMMAND RECEIVED: Edit clock settings')
                        
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

            except ConnectionError:
                print('ERROR: Reconnecting to server in 10 seconds...')
                sleep(RECONNECT_TIME)
