import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import font
from threading import Thread
import json
import socket
import time
import ssl

IP_ADDR="98.70.98.60"
PORT=8000

start_time=None
correct_options=[1,3,3,]
my_options=[]
response=[]
def close(self):
        for widget in self.winfo_children():
            widget.destroy()

ssl_context=ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.load_verify_locations("quiz.crt")
ssl_context.check_hostname=False
ssl_context.verify_mode=ssl.CERT_NONE

def transition(window,name):
    close(window)
    start_time=time.time()
    chosen_option1=tk.IntVar()
    chosen_option2=tk.IntVar()
    chosen_option3=tk.IntVar()
    def hover_action(radiobutton):
        radiobutton.configure(font=('Century Gothic',30),text_color='#4287f5',hover_color='blue')

    def leave_action(radiobutton,chosen_option):
        
        radiobutton.configure(font=('Century Gothic',20),text_color='white')
        state = radiobutton.cget("value")
        if(state==chosen_option.get()):
            radiobutton.configure(font=('Century Gothic',30),text_color='#4287f5',hover_color='blue')
        
    
    def prev_qn(qn_tracker,frame1):
        
        if(qn_tracker.get()==1):
            return
        else:
            close(frame1)
            qn_tracker.set(qn_tracker.get()-1)
            value=qn_tracker.get()
            if value==1:
                qn1()
            elif value==2:
                qn2()
            elif value==3:
                qn3()

        
    def next_qn(qn_tracker,frame1):
        close(frame1)
        qn_tracker.set(qn_tracker.get()+1)
        value=qn_tracker.get()
        if value==2:
            qn2()
        elif value==3:
            qn3()
        elif value==4:
            finish(frame1)
        

    def qn1():

        label=ctk.CTkLabel(frame1,text='What is the standard unit\n of data transmission?',font=(('Century Gothic',30)))
        label.pack(pady=10)


        
        option_1 = ctk.CTkRadioButton(frame1, text="Packets",
                                                    value=1,font=(('Century Gothic',20)),
                                                    variable=chosen_option1,
                                                    )
        option_1.pack(pady=10)

        option_1.bind('<Enter>',lambda event:hover_action(option_1))
        option_1.bind('<Leave>',lambda event:leave_action(option_1,chosen_option1))


        option_2 = ctk.CTkRadioButton(frame1, text="Bytes",
                                                    value=2,font=(('Century Gothic',20)),
                                                    variable=chosen_option1,
                                                    )
        option_2.pack(pady=10)

        option_2.bind('<Enter>',lambda event:hover_action(option_2))
        option_2.bind('<Leave>',lambda event:leave_action(option_2,chosen_option1))


        option_3 = ctk.CTkRadioButton(frame1, text="Bits",
                                                    value=3,font=(('Century Gothic',20)),
                                                    variable=chosen_option1,
                                                    )
        option_3.pack(pady=10)

        option_3.bind('<Enter>',lambda event:hover_action(option_3))
        option_3.bind('<Leave>',lambda event:leave_action(option_3,chosen_option1))


        option_4 = ctk.CTkRadioButton(frame1, text="Metre/s",
                                                    value=4,font=(('Century Gothic',20)),
                                                    variable=chosen_option1,
                                                    )
        option_4.pack(pady=10)

        option_4.bind('<Enter>',lambda event:hover_action(option_4))
        option_4.bind('<Leave>',lambda event:leave_action(option_4,chosen_option1))

    def qn2():
        label=ctk.CTkLabel(frame1,text='What is the full form of OSI?',font=(('Century Gothic',30)))
        label.pack(pady=10)


        
        option_1 = ctk.CTkRadioButton(frame1, text="Optical service implementatation",
                                                    value=1,font=(('Century Gothic',20)),
                                                    variable=chosen_option2,
                                                    )
        option_1.pack(pady=10)

        option_1.bind('<Enter>',lambda event:hover_action(option_1))
        option_1.bind('<Leave>',lambda event:leave_action(option_1,chosen_option2))


        option_2 = ctk.CTkRadioButton(frame1, text="open service internet",
                                                    value=2,font=(('Century Gothic',20)),
                                                    variable=chosen_option2,
                                                    )
        option_2.pack(pady=10)

        option_2.bind('<Enter>',lambda event:hover_action(option_2))
        option_2.bind('<Leave>',lambda event:leave_action(option_2,chosen_option2))


        option_3 = ctk.CTkRadioButton(frame1, text="open system interconnnection",
                                                    value=3,font=(('Century Gothic',20)),
                                                    variable=chosen_option2,
                                                    )
        option_3.pack(pady=10)

        option_3.bind('<Enter>',lambda event:hover_action(option_3))
        option_3.bind('<Leave>',lambda event:leave_action(option_3,chosen_option2))


        option_4 = ctk.CTkRadioButton(frame1, text="operating system interface",
                                                    value=4,font=(('Century Gothic',20)),
                                                    variable=chosen_option2,
                                                    )
        option_4.pack(pady=10)

        option_4.bind('<Enter>',lambda event:hover_action(option_4))
        option_4.bind('<Leave>',lambda event:leave_action(option_4,chosen_option2))
    def qn3():
        label=ctk.CTkLabel(frame1,text='Which of the following maintains DNS?',font=(('Century Gothic',30)))
        label.pack(pady=10)


        
        option_1 = ctk.CTkRadioButton(frame1, text="A single server",
                                                    value=1,font=(('Century Gothic',20)),
                                                    variable=chosen_option3,
                                                    )
        option_1.pack(pady=10)

        option_1.bind('<Enter>',lambda event:hover_action(option_1))
        option_1.bind('<Leave>',lambda event:leave_action(option_1,chosen_option3))


        option_2 = ctk.CTkRadioButton(frame1, text="a single computer",
                                                    value=2,font=(('Century Gothic',20)),
                                                    variable=chosen_option3,
                                                    )
        option_2.pack(pady=10)

        option_2.bind('<Enter>',lambda event:hover_action(option_2))
        option_2.bind('<Leave>',lambda event:leave_action(option_2,chosen_option3))


        option_3 = ctk.CTkRadioButton(frame1, text="distributed database system",
                                                    value=3,font=(('Century Gothic',20)),
                                                    variable=chosen_option3,
                                                    )
        option_3.pack(pady=10)

        option_3.bind('<Enter>',lambda event:hover_action(option_3))
        option_3.bind('<Leave>',lambda event:leave_action(option_3,chosen_option3))


        option_4 = ctk.CTkRadioButton(frame1, text="none of the mentioned",
                                                    value=4,font=(('Century Gothic',20)),
                                                    variable=chosen_option3,
                                                    )
        option_4.pack(pady=10)

        option_4.bind('<Enter>',lambda event:hover_action(option_4))
        option_4.bind('<Leave>',lambda event:leave_action(option_4,chosen_option3))

    def finish(frame1):
        label=ctk.CTkLabel(frame1,text='The quiz is over\nWould you like to submit?',font=(('Century Gothic',30)))
        label.pack(pady=10)
        button=ctk.CTkButton(frame1,text='Submit',border_width=2,font=(('Century Gothic',30)),fg_color='transparent',command=submit_func)
        button.pack(pady=20)
    
    def submit_func():
        my_options.append(chosen_option1.get())
        my_options.append(chosen_option2.get())
        my_options.append(chosen_option3.get())
        calculate_marks()
        
    def calculate_marks():
        end_time=time.time()
        marks=0
        for i in range(3):
            if my_options[i]==correct_options[i]:
                marks=marks+1
        time_taken=end_time-start_time
    
        # print(f'chosen options vs correct options:{my_options}\n{correct_options}')
        # print(f'this is your marks:{marks}')
        multi_connect(marks,time_taken)
    
    
    def receive_list(conn):
        received_data = b''
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            received_data += chunk
        return json.loads(received_data.decode())

    def connect_client(marks,time_taken):
        global response
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP_ADDR, PORT))
        client=ssl_context.wrap_socket(client, server_hostname=IP_ADDR)
        data=[name,marks,time_taken]
        # Serialize the array to JSON
        json_data = json.dumps(data)

        # Send the JSON data
        client.sendall(json_data.encode())

      
        received_data = b''
        while True:
            chunk = client.recv(1024)
            if not chunk:
                break
            received_data += chunk
            break

        # print(received_data.decode())
        response=json.loads(received_data.decode())
        
        client.close()
        
        return
   
    def recieve():
        global response
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP_ADDR, PORT))
        client=ssl_context.wrap_socket(client, server_hostname=IP_ADDR)
        data='recieve'

        # Send the JSON data
        client.send(data.encode())
        received_data = b''
        
        chunk = client.recv(1024)
        print(chunk.decode())
        
        # leaderboard=receive_list(client)
        response=json.loads(chunk.decode())
        client.close()
        return

    def recieve_thread():
        thread2 = Thread(target=recieve,daemon=True)
        thread2.start()
        thread2.join()
        table(window,response)

    def multi_connect(marks,time_taken):    
        thread = Thread(target=connect_client,args=(marks,time_taken),daemon=True)
        thread.start()
        thread.join()
        table(window,response)

    def table(window,response):
        close(window)
        style = ttk.Style()
    
        style.theme_use("default")
    
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=40,
                            columnwidth=30,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0,
                            font=('Century Gothic',11)),
        style.map('Treeview', background=[('selected', '#22559b')])
    
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat",
                            font=('Century Gothic',25))
        style.configure("Treeview.insert",
                            background="#565b5e",
                            foreground="white",
                            relief="flat",
                            font=('Century Gothic',15))
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Century Gothic', 11))
        style.map("Treeview.Heading",
                    background=[('active', '#3484F0')])
        style.map("Treeview.insert",
                background=[('active', '#3484F0')])
        style.map("mystyle.Treeview",background=[('active', '#3484F0')])

        table=ttk.Treeview(window,columns=('Name','Marks','Rank'),show='headings',height=15,)
        table.heading('Name',text='Name',)
        table.heading('Marks',text='Marks',)
        table.heading('Rank',text='Rank',)
        table.pack()
        # print(response)
        # inserting values into table
        temp3=len(response)
        for i in response:
           
            i[2]=temp3
            temp3-=1
            for j in i:
                temp=0
                i[temp]=str(i[temp])
                temp+=1
            temp2=0
            table.insert(parent='',index=temp2,values=tuple(i),)
            temp2+=1
        table.column('Name',anchor=tk.CENTER)
        table.column('Marks',anchor=tk.CENTER)
        table.column('Rank',anchor=tk.CENTER)
        button=ctk.CTkButton(window,text="Refresh",font=('Century Gothic',30),width=300,height=40,command=recieve_thread)
        button.pack()
        


        

    
        
    

    frame1=ctk.CTkFrame(window,width=600,height=550)
    frame1.pack_propagate('False')
    frame1.pack()

    qn1()

    qn_tracker=tk.IntVar(value=1)

    button1=ctk.CTkButton(window,text="Previous",font=('Century Gothic',30),width=200,height=40,command=lambda:prev_qn(qn_tracker,frame1))
    button1.pack(side='left')
    button2=ctk.CTkButton(window,text="Next",font=('Century Gothic',30),width=200,height=40,command=lambda:next_qn(qn_tracker,frame1))
    button2.pack(side='right')

def fram1(window):
    Image_original=Image.open('./CN_4.png')
    Image_original=Image_original.convert('RGBA')
    Img_tk=ctk.CTkImage(Image_original,Image_original,size=(400,400))
    Image_original2=Image.open('./quiz.png')
    Image_original2=Image_original2.convert('RGBA')
    Img_tk2=ctk.CTkImage(Image_original2,Image_original2,size=(150,90))


    label=ctk.CTkLabel(window,image=Img_tk,text='',corner_radius=40)
    label.pack()
    label2=ctk.CTkLabel(window,image=Img_tk2,text='',corner_radius=40,width=100,height=100)
    label2.place(x=300,y=300)

    name=tk.StringVar(value='Enter your name')
    entry=ctk.CTkEntry(window,placeholder_text='Enter your name',font=('Century Gothic',30),width=300,height=40,textvariable=name)
    
    entry.pack(pady=30)

    button=ctk.CTkButton(window,text="Start",font=('Century Gothic',30),width=300,height=40,command=lambda:transition(window,name.get()))
    button.pack()

def table2(window,response):
        close(window)



window=ctk.CTk()
window.geometry('650x650+430+50')
window.title('CN Quiz')
ctk.set_appearance_mode('dark')
window.maxsize(650,650)
window.minsize(650,650)


fram1(window)






window.mainloop()