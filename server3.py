import socket
import threading
import json
import tkinter as tk
import ssl

ssl_context=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile='quiz.crt', keyfile='quiz.key')

def handle_client(client_socket, addr):
    try:
        while True:
            json_data = client_socket.recv(1024).decode("utf-8")
            if not json_data:
                break
            data = json.loads(json_data)
            print(f"Received data from {addr}: {data}")
            
            leaderboard.append(data)
            
            leaderboard.sort(key=lambda x: (x[1], x[2]))
            
            response = f"Echo: {data}"
            client_socket.send(response.encode("utf-8"))
    except Exception as e:
        print(f"Error when handling client: {e}")
    finally:
        client_socket.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed")

def run_server():
    server_ip = "127.0.0.1" 
    port = 8000  

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((server_ip, port))
        server.listen()
        print(f"Listening on {server_ip}:{port}")

        while True:
            client_socket, addr = server.accept()
            conn_ssl=ssl_context.wrap_socket(client_socket, server_side=True)
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            thread = threading.Thread(target=handle_client, args=(conn_ssl, addr,), daemon=True)
            thread.start()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()

leaderboard_window = tk.Tk()
leaderboard_window.title("Quiz Leaderboard")

leaderboard_listbox = tk.Listbox(leaderboard_window)
leaderboard_listbox.pack(expand=True, fill=tk.BOTH)

leaderboard = []

def update_leaderboard():
    leaderboard_listbox.delete(0, tk.END)
    
    for rank, participant in enumerate(leaderboard, start=1):
        leaderboard_listbox.insert(tk.END, f"Rank: {rank}, Name: {participant[0]}, Score: {participant[1]}, Time: {participant[2]}")

    leaderboard_window.after(1000, update_leaderboard)

update_leaderboard()

run_server()

leaderboard_window.mainloop()
