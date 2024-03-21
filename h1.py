import tkinter as tk
import socket
import time
from threading import Thread
import json
import ssl

root = tk.Tk()
root.title('quiz page')

ssl_context=ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.load_verify_locations("quiz.crt")
ssl_context.check_hostname=False
ssl_context.verify_mode=ssl.CERT_NONE

def connect_client(data):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8000))
    client=ssl_context.wrap_socket(client, server_hostname='127.0.0.1')

    # Serialize the array to JSON
    json_data = json.dumps(data)

    # Send the JSON data
    client.send(json_data.encode('utf-8'))

    while True:
        response = client.recv(1024)
        response = response.decode('utf-8')
        if response == 'close':
            print('Closing the connection')
            break
        
    client.close()
    print()


class QuizPage(tk.Toplevel):
    def __init__(self, master=None, name=""):
        super().__init__(master)
        self.title("Quiz Page")
        self.geometry("400x600")
        self.configure(bg="#F5F5F5")
        
        self.questions = [
            "1. What is the capital of France?",
            "2. What is the largest planet in our solar system?",
            "3. Who wrote 'To Kill a Mockingbird'?"
        ]

        self.options = [
            ["Paris", "Rome", "London", "Berlin"],
            ["Jupiter", "Saturn", "Earth", "Mars"],
            ["Harper Lee", "J.K. Rowling", "Stephen King", "Ernest Hemingway"]
        ]

        self.correct_answers = ["Paris", "Jupiter", "Harper Lee"]
        
        self.selected_options = [tk.StringVar() for _ in range(3)]

        self.start_time = None
        self.name = name

        self.create_widgets()

    def create_widgets(self):
        heading_label = tk.Label(self, text="Welcome to the Quiz", font=("Helvetica", 16), bg="#F5F5F5", fg="#333333")
        heading_label.pack(pady=10)

        for i in range(3):
            question_label = tk.Label(self, text=self.questions[i], font=("Helvetica", 12), bg="#F5F5F5", fg="#333333")
            question_label.pack(pady=5, anchor="w")

            for j in range(4):
                option_radio_button = tk.Radiobutton(self, text=self.options[i][j], variable=self.selected_options[i], value=self.options[i][j], font=("Helvetica", 10), bg="#F5F5F5", fg="#333333", indicator=0)
                option_radio_button.pack(pady=2, padx=20, anchor="w")

        submit_button = tk.Button(self, text="Submit", font=("Helvetica", 12), bg="#FF6347", fg="#FFFFFF", activebackground="#32CD32", activeforeground="#FFFFFF", bd=0,
            command=Thread(target=self.calculate_marks, daemon=True).start)
        submit_button.pack(pady=20, padx=20, ipadx=10, ipady=5)

        self.start_time = time.time()

    def calculate_marks(self):
        end_time = time.time()
        time_taken = end_time - self.start_time

        correct_count = 0
        for i in range(3):
            if self.selected_options[i].get() == self.correct_answers[i]:
                correct_count += 1
        print("Total Marks:", correct_count, time_taken)

        data = [self.name, correct_count, time_taken]
        connect_client(data)
        self.destroy()


def start_quiz():
    name = entry.get()  # Get the name entered by the user
    app = QuizPage(name=name)
    app.mainloop()

    
label = tk.Label(root, text="Welcome to the Quiz", bg="#FFFFFF", fg="#333333", font=("Helvetica", 16))
label.pack(pady=20)

entry = tk.Entry(root)
entry.config(bg="#F5F5F5")
entry.config(fg="#333333", font=("Helvetica", 12))
entry.insert(0, "Enter your name")
entry.pack()

button = tk.Button(root, text="Start Quiz", bg="#008080", fg="#FFFFFF", font=("Helvetica", 12), command=start_quiz)
button.pack(pady=10)

root.mainloop()
