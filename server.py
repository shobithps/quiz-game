import socket
import threading
import json
import ssl
import customtkinter as ttk
import tkinter as tk
from tkinter import ttk

IP_ADDR='98.70.98.60'
PORT=8000

clients=[]
leaderboard=[]


ssl_context=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile='quiz.crt', keyfile='quiz.key')

# def leaderboard_update(leaderboard,data):
#     for i in data:
#         leaderboard.append(i)

def convert_integers_to_strings(arr):
                    return [str(num) for num in arr]

def handle_client(client_socket, addr,):
    try:
        while True:
            json_data = client_socket.recv(1024).decode("utf-8")
            if not json_data:
                break
            print(json_data)
            if json_data.strip().lower()=='recieve':
                response = json.dumps(leaderboard) #sending the appended list back to client to display leaderboard
                print(response)
                for i in clients:
                    try:
                        i.sendall(response.encode())
                    except:
                        continue
                return

            data = json.loads(json_data)

            # data=convert_integers_to_strings(data)
            
            leaderboard.append(data)
            # print(leaderboard)
            # appending individual string to array
            
            
            leaderboard.sort(key=lambda x: (x[1], x[2]))

            response = json.dumps(leaderboard) #sending the appended list back to client to display leaderboard
            for i in clients:
                try:
                    i.sendall(response.encode())
                except:
                    continue
    except Exception as e:
        print(f"Error when handling client: {e}")
    finally:
        client_socket.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed")

def run_server(): 

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((IP_ADDR, PORT))
        server.listen(1)
        print(f"Listening on {IP_ADDR}:{PORT}")

        while True:
            client_socket, addr = server.accept()
            client_socket=ssl_context.wrap_socket(client_socket, server_side=True)
            clients.append(client_socket)
            # conn_ssl=ssl_context.wrap_socket(client_socket, server_side=True)
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            thread = threading.Thread(target=handle_client, args=(client_socket, addr,), 
            daemon=True)
            thread.start()
            # print(clients)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()


run_server()