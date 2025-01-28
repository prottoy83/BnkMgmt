import tkinter

def loginBox():
    back_col = "#fafafa"

    root = tkinter.Tk()

    root.title("Nig bank")
    root.geometry("720x580")
    root.configure(bg=back_col)

    cred = {"method": None, "username": None, "password": None}

    #print(tkinter.font.families())

    def loginFSub():
        cred["method"] = "login"
        cred["username"] = username_entry.get()
        cred["password"] = password_entry.get()
        root.destroy()

    heading = tkinter.Label(root,
                            text ="Welcome, Please Log in to your Account!",
                            background =  back_col,
                            foreground="#171717",
                            font = ('Montserrat', 18),
                            justify="left"
                            ).place(x=100, y=80)


    username_label = tkinter.Label(
        root,
        text="Username:",
        font=('Montserrat', 10),
        background= back_col,  
        foreground="#171717"   
    )
    username_label.place(x=100, y=160)  


    username_entry = tkinter.Entry(
        root,
        font=('Montserrat', 10),  
        bd=0,  
        highlightthickness=1, 
        highlightbackground="#171717", 
        relief="flat",  
        width=30  
    )
    username_entry.place(x=180, y=160, width=360, height=30) 

    password_label = tkinter.Label(
        root,
        text="Password:",
        font=('Montserrat', 10),
        background= back_col,  
        foreground="#171717"   
    )
    password_label.place(x=100, y=220)  


    password_entry = tkinter.Entry(
        root,
        font=('Montserrat', 10),  
        bd=0,  
        highlightthickness=1, 
        highlightbackground="#171717", 
        relief="flat",  
        width=30,
        show="*"
    )
    password_entry.place(x=180, y=220, width=360, height=30) 

    login = tkinter.Button(root,
                        text="Login",
                        command = loginFSub,
                        bg= "#ff511c",
                        fg="#fafafa",
                        relief="flat",
                        font=("Montserrat", 10),
                        activebackground="#ff7043"
                        )
    login.place(x=420,y=280, width=120, height= 30)

    root.mainloop()

    return cred["method"], cred["username"], cred["password"]