import socket
import json
from os import system

system('clear')

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6000
BUFFER = 2048
SERVER_ADDRESS = HOST + ':' + str(PORT)
CONNECTED_CLIENTS = []

with socket.socket() as host_socket:
    try:
        host_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host_socket.bind((HOST, PORT))
        print('Server hosted on ' + SERVER_ADDRESS)
        host_socket.listen(1)
        connection, address = host_socket.accept()
        print('Connection from ' + address[0] + ':' + str(address[1]) + '\n')

        while True:
            print('[0] Stop server')
            print('[1] Receive clock settings')
            print('[2] Edit clock settings')
            command = int(input('Input command #: '))

            if command == 0:  # Disconnect
                connection.send('disconnect'.encode('ascii'))
                print('COMMAND SENT: Disconnect')
                break
            elif command == 1:  # Receive clock settings
                connection.send('send_settings'.encode('ascii'))
                print('COMMAND SENT: Receive clock settings')

                # Receives the JSON string and converts into a Python dictionary
                clock_settings = json.loads(connection.recv(BUFFER))

                # Prints clock settings in a neat manner
                for category in clock_settings:
                    print(str(category).upper() + ':')
                    for key in clock_settings[category]:
                        print('- ' + key + ': ' + str(clock_settings[category][key]) + '\n')
            elif command == 2:  # Edit clock settings
                connection.send('edit_settings'.encode('ascii'))
                print('COMMAND SENT: Edit clock settings ')

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
                system('clear') 
            else:
                print('Error: Please input valid number')
                system('clear')

    except socket.error as error:
        print(str(error))

