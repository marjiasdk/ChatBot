from tkinter import Tk, Text, Entry, Button, PhotoImage, END
from openAI_chatbot import Chatbot

def send_message(event=None):
    user_message = user_entry.get()
    
    # END is used to insert the text at the end of the text widget
    chat_log.insert(END, "User: " + user_message + "\n")
    bot_response = Chatbot.get_response(user_message)
    chat_log.insert(END, "Bot: " + bot_response + "\n")
    user_entry.delete(0, END)

root = Tk()
root.title("Chatbot")
root.geometry("400x500")

# config can have the following parameters: bg, fg, font, padx, pady, etc.
root.config(bg="light blue")
root.resizable(width=False, height=False)


icon_image = PhotoImage(file="Images/chatbot.png")
root.iconphoto(False, icon_image)

# Text() is used to display text in multiple lines
chat_log = Text(root, width=50, height=28)
chat_log.pack()

# Entry() is used to display text in a single line
user_entry = Entry(root, width=50, borderwidth=2)
user_entry.pack(side="left", padx=10, pady=10)

# Bind the Enter key to the send_message function
user_entry.bind("<Return>", send_message)

# Button() is used to create a button
submit_button = Button(root, width=20, text="Send", command=send_message)
submit_button.pack(side="right", padx=10, pady=10)

root.mainloop()
