import hashlib
from tkinter import *

#main window
root = Tk()
root.title("Encryptor 2.0")
root.config(bg="#444444")
root.geometry("800x300")

#input label
myLabel = Label(root ,text= "ENTER A VALUE", foreground="#88baea", bg="#444444",font = ("Courier 30 bold"))
myLabel.pack()

#input widget
msg = Entry(root, width = 50, bg="#97a1aa", borderwidth = 5)
msg.pack()

#encrypting function(sha256)
def encrypt_sha256():
   encryption = hashlib.sha256(msg.get().encode())
   output = "Encryption in SHA256 :  " + encryption.hexdigest()
   newLabel = Label(root, text = output, bg="#192734", fg="#fff", font= ("helvetica 14"))
   newLabel.pack()

#encrypting function(md5)
def encrypt_md5():
   encryption = hashlib.md5(msg.get().encode())
   output = "Encryption in MD5 :  " + encryption.hexdigest()
   newLabel = Label(root, text = output, bg="#243747", fg="#fff", font= ("helvetica 14"))
   newLabel.pack()

#output button(sha256)
sha256_button = Button(root, text = "SHA256",font= ("callibre 16 bold"),bg="#536878", width = 14, command = encrypt_sha256)
sha256_button.pack()

#output button(md5)
md5_button = Button(root, text = "MD5",font= ("callibre 16 bold"), bg="#536878", width = 14, command = encrypt_md5)
md5_button.pack()

root.mainloop()
