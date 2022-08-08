from calendar import month
from email.mime import message
from tkinter import messagebox
from tkinter import ttk
import db
from tkinter import *
from tkinter.ttk import *
from functools import partial

months=["Hiển thị giao dịch","Tất cả giao dịch",1,2,3,4,5,6,7,8,9,10,11,12]

LARGE_FONT = ("Verdana", 32)

class MoneyManager:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.main_window()

    ### hiển thị các hàm để cập nhật cơ sở dữ liệu và thêm vào hoặc xóa#
    def added(self, boxaile):
        messagebox.showinfo("Thông tin giao dịch", "Giao dịch đã được nhập")
        return
    def delete(self, boxaile):
        messagebox.showinfo("Thông tin giao dịch", "Giao dịch đã bị xóa")
        return

    def display_all(self, database):
        select_all = database
        return select_all

    def insert(self, database, val1, val2, val3):
        goods = val1.get()
        price = val2.get()
        date = val3.get()
        insertion = database(goods, price, date)
        return insertion

    def find_expense(self, database, val1, val2, val3):
        goods = val1.get()
        price = val2.get()
        date  = val3.get() 
        find = database(goods, price, date)
        if find =='' :
            find = "Khong tim thay giao dich"
        return find

    def delete_expense(self,database, val1, val2):
        goods = val1.get()
        price = val2.get()
        delete = database(goods, price)
        return delete

    ###Cửa sổ chính###
    def main_window(self):

        button1 = Button(self.frame, text="Khoản thu nhập", command=self.incomes)
        button1.pack(ipadx=15, ipady=5, fill='both',side='left')

        button2 = Button(self.frame, text="Khoản chi tiêu", command=self.expenses)
        button2.pack(ipadx=15, ipady=5, fill='both',side='left')

        button3 = Button(self.frame, text="Khoản vay",command=self.loan)
        button3.pack(ipadx=15, ipady=5, fill='both',side='right')

        button4 = Button(self.frame, text="Giao dịch khác", command=self.other)
        button4.pack(ipadx=15, ipady=5, fill='both', side='right')

        

    ###Cac chuc nang###
    def incomes(self):


        top = Toplevel(self.frame)
        top.title('Khoản thu nhập')
        l1 = Label(top, text="Tên loại thu nhập").grid(row = 1, column = 0, sticky = W, pady = 2)
        l2 = Label(top, text="Số tiền").grid(row = 2, column = 0, sticky = W, pady = 2)
        l3 = Label(top, text="Ngày giao dịch").grid(row = 3, column = 0, sticky = W, pady = 2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        #BUTTONS###

        B1 = Button(top, text="Nhập giao dịch", command=lambda: (text.delete(0.0, END), self.insert(db.insert_incomes,e1,e2,e3), self.added(top)))
        B1.grid(row=1, column=3, sticky=EW)

        def comboclick(e):
            if C1.get() =="Tất cả giao dịch":
                text.delete(1.0, END)
                text.insert(END,self.display_all(db.select_all_incomes()))
            else:
                text.delete(1.0, END)
                text.insert(END, self.display_all(db.select_incomes_bymonth(int(C1.get()))))
       
        C1= Combobox(top,values=months)
        C1.current(0)
        C1.bind("<<ComboboxSelected>>", comboclick)
        C1.grid(row=0, column=3, sticky=EW)

        B2 = Button(top, text="Tìm giao dịch", command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_incomes, e1,e2,e3))))
        B2.grid(row=2, column=3, sticky=EW)

        B3 = Button(top, text="Xóa giao dịch", command=lambda: (text.delete(0.0, END), self.delete_expense(db.delete_incomes, e1,e2), self.delete(top)))
        B3.grid(row=3, column=3, sticky=EW)

        B4 = Button(top, text="Xóa bảng thông tin", command=lambda: (text.delete(0.0, END)))
        B4.grid(row=4, column=3, sticky=EW)

        B5= Button(top, text="Menu chính", command=top.destroy)
        B5.grid(row=5, column=3, sticky=SE)

    def expenses(self):
        top = Toplevel(self.frame)
        top.title('Khoản chi tiêu')
        l1 = Label(top, text="Tên loại chi tiêu").grid(row=1, column=0, sticky=W, pady=2)
        l2 = Label(top, text="Số tiền").grid(row=2, column=0, sticky=W, pady=2)
        l3 = Label(top, text="Ngày giao dịch").grid(row=3, column=0, sticky=W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # BUTTONS###

        B1 = Button(top, text="Nhập giao dịch", command=lambda: (text.delete(0.0, END), self.insert(db.insert_expenses,e1,e2,e3), self.added(top)))
        B1.grid(row=1, column=3, sticky=EW)

        def comboclick(e):
            if C1.get() =="Tất cả giao dịch":
                text.delete(1.0, END)
                text.insert(END,self.display_all(db.select_all_expenses()))
            else:
                text.delete(1.0, END)
                text.insert(END, self.display_all(db.select_expenses_bymonth(int(C1.get()))))

        C1= Combobox(top,values=months)
        C1.current(0)
        C1.bind("<<ComboboxSelected>>", comboclick)
        C1.grid(row=0, column=3, sticky=EW)

        B2 = Button(top, text="Tìm giao dịch", command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_expenses, e1,e2,e3))))
        B2.grid(row=2, column=3, sticky=EW)

        B3 = Button(top, text="Xóa giao dịch", command=lambda: (text.delete(0.0, END), self.delete_expense(db.delete_expenses, e1,e2), self.delete(top)))
        B3.grid(row=3, column=3, sticky=EW)

        B4 = Button(top, text="Xóa bảng thông tin", command=lambda: (text.delete(0.0, END)))
        B4.grid(row=4, column=3, sticky=EW)

        B5= Button(top, text="Menu chính", command=top.destroy)
        B5.grid(row=5, column=3, sticky=SE)

    def loan(self):
        top = Toplevel(self.frame)
        top.title('Khoản vay')
        l1 = Label(top, text="Tên loại Khoản vay").grid(row=1, column=0, sticky=W, pady=2)
        l2 = Label(top, text="Giá tiền").grid(row=2, column=0, sticky=W, pady=2)
        l3 = Label(top, text="Ngày giao dịch").grid(row=3, column=0, sticky=W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # BUTTONS###
        B1 = Button(top, text="Nhập giao dịch", command=lambda: (text.delete(0.0, END), self.insert(db.insert_loan,e1,e2,e3), self.added(top)))
        B1.grid(row=1, column=3, sticky=EW)

        def comboclick(e):
            if C1.get() =="Tất cả giao dịch":
                text.delete(1.0, END)
                text.insert(END,self.display_all(db.select_all_loan()))
            else:
                text.delete(1.0, END)
                text.insert(END, self.display_all(db.select_loan_bymonth(int(C1.get()))))

        C1= Combobox(top,values=months)
        C1.current(0)
        C1.bind("<<ComboboxSelected>>", comboclick)
        C1.grid(row=0, column=3, sticky=EW)

        B2 = Button(top, text="Tìm giao dịch", command=lambda: (text.delete(1.0, END), text.insert(END, self.find_loan(db.select_loan, e1,e2,e3))))
        B2.grid(row=2, column=3, sticky=EW)

        B3 = Button(top, text="Xóa giao dịch", command=lambda: (text.delete(0.0, END), self.delete_loan(db.delete_loan, e1,e2), self.delete(top)))
        B3.grid(row=3, column=3, sticky=EW)

        B4 = Button(top, text="Xóa bảng thông tin", command=lambda: (text.delete(0.0, END)))
        B4.grid(row=4, column=3, sticky=EW)

        B5= Button(top, text="Menu chính", command=top.destroy)
        B5.grid(row=5, column=3, sticky=SE)

    def other(self):
        top = Toplevel(self.frame)
        top.title('Giao dịch khác')
        l1 = Label(top, text="Tên khoản giao dịch").grid(row=1, column=0, sticky=W, pady=2)
        l2 = Label(top, text="Giá tiền").grid(row=2, column=0, sticky=W, pady=2)
        l3 = Label(top, text="Ngày giao dịch").grid(row=3, column=0, sticky=W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # BUTTONS###

        B1 = Button(top, text="Nhập giao dịch", command=lambda: (text.delete(0.0, END), self.insert(db.insert_other,e1,e2,e3), self.added(top)))
        B1.grid(row=1, column=3, sticky=EW)

        def comboclick(e):
            if C1.get() =="Tất cả giao dịch":
                text.delete(1.0, END)
                text.insert(END,self.display_all(db.select_all_other()))
            else:
                text.delete(1.0, END)
                text.insert(END, self.display_all(db.select_other_bymonth(int(C1.get()))))

        C1= Combobox(top,values=months)
        C1.current(0)
        C1.bind("<<ComboboxSelected>>", comboclick)
        C1.grid(row=0, column=3, sticky=EW)

        B2 = Button(top, text="Tìm giao dịch", command=lambda: (text.delete(1.0, END), text.insert(END, self.find_other(db.select_other, e1,e2,e3))))
        B2.grid(row=2, column=3, sticky=EW)

        B3 = Button(top, text="Xóa giao dịch", command=lambda: (text.delete(0.0, END), self.delete_other(db.delete_expenses, e1,e2), self.delete(top)))
        B3.grid(row=3, column=3, sticky=EW)

        B4 = Button(top, text="Xóa bảng thông tin", command=lambda: (text.delete(0.0, END)))
        B4.grid(row=4, column=3, sticky=EW)

        B5= Button(top, text="Menu chính", command=top.destroy)
        B5.grid(row=5, column=3, sticky=SE)


def main():
    root = Tk()
    root.geometry('600x315')
    root.title("Money Manager")
    #background
    img1 = PhotoImage(file = "E:\\Dell\\Visual Studio\\Code Python\\rsz_background.png")
    label1 = Label(root,image = img1,background='white')
    label1.place(x=0,y=0)
    MoneyManager(root)
    root.mainloop()


main()
