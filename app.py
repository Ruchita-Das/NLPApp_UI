from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):
        self.dbo=Database()
        self.root=Tk()
        self.apio=API()
        self.root.title("NLPApp")
        self.root.iconbitmap("Resources/android-icon-192x192.ico")
        self.root.geometry("350x600")
        self.root.configure(bg="#a7e7c3")
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading=Label(self.root,text="NLPApp",bg="#a7e7c3",fg="blue")
        heading.pack(pady=(30,30))
        heading.configure(font=("verdana",24,"bold"))

        label1=Label(self.root,text="Enter email")
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text="Enter password")
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=30,show="*")
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn=Button(self.root,text="Login",height=2,width=30,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text="Not a member?")
        label3.pack(pady=(10, 10))

        redirect_btn = Button(self.root, text="Register Now", height=2, width=30,command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))


    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#a7e7c3', fg='blue')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2,command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        #clear existing gui
        for i in self.root.pack_slaves():
            i.destroy()
    def perform_registration(self):
        name=self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response=self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success', 'Registration successful. You can login now')
        else:
            messagebox.showerror('Error', 'Email already exists')

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('success', 'Login successful')
            self.sentiment_gui()
        else:
            messagebox.showerror('error', 'Incorrect email/password')



    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#a7e7c3', fg='blue')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#a7e7c3', fg='blue')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=20)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg='#a7e7c3',fg='blue')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))


        goback_btn = Button(self.root, text='Go Back', command=self.login_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()  # Get the input text from the UI
        result = self.apio.sentiment_analysis(text)  # Perform sentiment analysis using the API

        txt = ''

        # Check if the result contains the 'scored_labels' key
        if 'scored_labels' in result:
            for label_info in result['scored_labels']:
                label = label_info['label']  # Get the label (e.g., joy, love, etc.)
                score = label_info['score']  # Get the score for that label
                txt += f"{label} -> {score:.4f}\n"  # Format the output to 4 decimal places
        else:
            # Handle the case where 'scored_labels' key is not present
            txt = "Sentiment analysis could not be performed. Please check the input or API response."

        print(txt)  # Print the results
        self.sentiment_result['text'] = txt  # Update the UI with the result


nlp=NLPApp()