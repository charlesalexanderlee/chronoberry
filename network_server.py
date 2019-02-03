import socket
import json
from os import system

system('clear')

HOST = socket.gethostname()
PORT = 6000
BUFFER = 2048

with socket.socket() as host_socket:
    try:
        host_socket.bind((HOST, PORT))
        host_socket.listen(1)
        connection, address = host_socket.accept()

        # Receives the JSON string and converts into a Python dictionary
        clock_settings = json.loads(connection.recv(BUFFER))
        
        # Prints clock settings in a neat manner
        for category in clock_settings:
            print(str(category).upper() + ':')
            for key in clock_settings[category]:
                print('- ' + key + ': ' + str(clock_settings[category][key]))
            print('')

        # Changes a setting of the clock
        category = input('Change category: ')
        key = input('Change key: ')
        value = input('Input new value: ')
        clock_settings[category][key] = value

        # Sends new settings to the clock
        connection.send(json.dumps(clock_settings).encode('ascii'))
    
    except socket.error as error:
        print(str(error))
