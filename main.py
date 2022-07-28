from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_pass():
 letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


 password_letters=[choice(letters) for _ in range(randint(8, 10))]
 password_numbers=[choice(numbers) for _ in range(randint(2,4))]
 password_symbols=[choice(symbols) for _ in range(randint(2,4))]

 password_list = password_symbols+password_numbers+password_letters
 shuffle(password_list)

 password = "".join(password_list)

 password_ip.insert(0,password)
 pyperclip.copy(password)
 #gets copyed automatically
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website=website_ip.get()
    email=email_ip.get()
    password=password_ip.get()
    password_ip.delete(0,END)
    website_ip.delete(0,END)


    if len(website)==0  or len(password)==0:
        messagebox.showinfo(title="warning",message="Add information!!!")

    else:
     message = messagebox.askokcancel(title=website,
                                     message=f"The information you have entered: email: {email}, password: {password}")

     if message:
      with open("savedPass.txt","a") as file:
       file.write(f"website:{website},  email:{email},  password:{password}\n")



# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("password generater")
window.config(padx=40,pady=40)

canvas=Canvas(width=200,height=240)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

website_lb=Label(text="website :")
website_lb.grid(column=0,row=1)
website_ip=Entry(width=35)
website_ip.grid(column=1,row=1,columnspan=2)

email_lb=Label(text="Email/username :")
email_lb.grid(column=0,row=2)
email_ip=Entry(width=35)
email_ip.grid(column=1,row=2,columnspan=2)
email_ip.insert(0,"siddiusha193@gmail.com")

password_lb=Label(text="Password :")
password_lb.grid(column=0,row=3)
password_ip=Entry(width=25)
password_ip.grid(column=1,row=3,columnspan=1)

generate_password=Button(text="Generate password",command=generate_pass)
generate_password.grid(column=2,row=3)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()