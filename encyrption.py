from tkinter import *
from tkinter import messagebox
import base64
import os
def decrypt():
    password=code.get()

    if password=="aaaa":
        s2=Toplevel(screen)
        s2.title("decryption")
        s2.geometry("400x200")
        s2.configure(bg="#00bd56")

        message=t1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(s2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        t2=Text(s2, font="Rpbote 10" , bg="white",relief=GROOVE,wrap=WORD,bd=0)
        t2.place(x=10,y=40,width=380,height=150)

        t2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("Decryption","Input Password")

    elif password !="aaaa":
        messagebox.showerror("Decryption","Invalid Password")
def encrypt():
    password=code.get()

    if password=="aaaa":
        s1=Toplevel(screen)
        s1.title("encryption")
        s1.geometry("400x200")
        s1.configure(bg="#ed3833")

        message=t1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(s1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        t2=Text(s1, font="Rpbote 10" , bg="white",relief=GROOVE,wrap=WORD,bd=0)
        t2.place(x=10,y=40,width=380,height=150)

        t2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("Encryption","Input Password")

    elif password !="aaaa":
        messagebox.showerror("Encryption","Invalid Password")
    

    

def main_screen():
    global screen
    global code
    global t1
    screen=Tk()
    screen.geometry("375x398")
    screen.title("encrypt app")
    image_icon=PhotoImage(file="encyrpt.png")
    screen.iconphoto(False, image_icon)
    def reset():
        code.set("")
        t1.delete(1.0,END)
    Label(text="Enter text for encryption and decryption",fg="black",font=("arial",13)).place(x=10, y=10)
    t1=Text(font="Robote 20", bg ="white",relief=GROOVE,wrap=WORD,bd =0)
    t1.place(x=10,y=50,width=355,height=100)
    Label(text="Enter key for encryption and decryption",fg="black",font=("arial", 13)).place(x=10,y=170)
    code =StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="ENCRYPT", height="2",width=23, bg="#ed3833",fg="white",bd=0, command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT", height="2",width=23, bg="#00bd56",fg="white",bd=0, command=decrypt).place(x=200,y=250)
    Button(text="RESET", height="2",width=50, bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)
    screen.mainloop()
    
main_screen()
