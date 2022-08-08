import code
from tkinter import *
from tkinter import messagebox
import db
root = Tk()
root.title('Money Manager')
root.geometry('1100x450+300+200')
root.configure(bg = '#fff')
root.resizable(False,False)

def singin():
    username=user.get()
    password=code.get()

    if db.select_user(username, password) !='':
        root.destroy()
        import app
        app.main
    else:
        messagebox.showerror('Invalid','Tài khoản hoặc mật khẩu không chính xác')

def signup_command():
    window=Toplevel(root)
    window.title("Signup")
    window.geometry('1100x450+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)

    def signup():
        username=user.get()
        password=code.get()
        conform_password=conform_code.get()

        if password==conform_password:
            db.insert_user(username, password)
            messagebox.showinfo("Thông tin đăng ký", "Đăng ký tài khoản thành công")
        else:
            messagebox.showerror('Invalid',"Mật khẩu không trùng nhau")
    def sign():
        window.destroy()

    img = PhotoImage(file='E:\\Dell\\Visual Studio\\Code Python\\rsz_background.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)

    frame=Frame(window,width=350,height=390,bg='white')
    frame.place(x=670,y=60)

    heading = Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)

    ##########----------------------------------
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')

    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    ##########----------------------------------
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')

    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)



    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    ##########----------------------------------
    def on_enter(e):
        conform_code.delete(0,'end')
    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0,'Conform Password')

    conform_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0, 'Conform Password')
    conform_code.bind("<FocusIn>",on_enter)
    conform_code.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    ###############--------------------

    Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    label=Label(frame,text='Tôi đã có tài khoản?',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=70,y=340)

    signin = Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=200,y=340)




    window.mainloop()
#################---------    
img = PhotoImage(file = 'E:\\Dell\\Visual Studio\\Code Python\\rsz_background.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=670,y=60)

heading=Label(frame,text='Money Manager',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI',27,'bold'))
heading.place(x=20,y=15)
################-----------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='' :
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#################-------------------------
def on_enter1(e):
    code.delete(0,'end')

def on_leave1(e):
    name=code.get()
    if name=='' :
        code.insert(0,'Password')


code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter1)
code.bind('<FocusOut>',on_leave1)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##########################################

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=singin).place(x=35,y=204)
label=Label(frame,text="Bạn không có tài khoản?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=70,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)




root.mainloop()