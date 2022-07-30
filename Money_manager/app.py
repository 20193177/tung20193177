import db
from tkinter import *
from tkinter.ttk import *
from functools import partial


LARGE_FONT = ("Verdana", 32)

class MoneyManager:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.main_window()

    ### hiển thị các hàm để cập nhật cơ sở dữ liệu và thêm vào hoặc xóa#
    def added(self, boxaile):
        myLabel = Label(boxaile, text="Giao dịch đã được thêm")
        myLabel.grid(row=4, column=0)

    def delete(self, boxaile):
        myLabel = Label(boxaile, text="Giao dịch đã bị xóa")
        myLabel.grid(row=4, column=0)

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
        button1.pack()

        button2 = Button(self.frame, text="Khoản chi tiêu", command=self.expenses)
        button2.pack()

        button3 = Button(self.frame, text="Khoản vay",command=self.loan)
        button3.pack()

        button4 = Button(self.frame, text="Giao dịch khác", command=self.other)
        button4.pack()

        button5 = Button(self.frame, text="EXIT", command=exit)
        button5.pack()

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

        B1 = Button(top, text="Nhập giao dịch", command=lambda: (self.insert(db.insert_incomes,e1,e2,e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Hiển thị giao dịch", command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_incomes()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Tìm giao dịch", command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_incomes, e1,e2,e3))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Xóa giao dịch", command=lambda: (self.delete_expense(db.delete_incomes, e1,e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5= Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)


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

        B1 = Button(top, text="Nhập giao dịch",
                    command=lambda: (self.insert(db.insert_expenses, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Hiển thị giao dịch", command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_expenses()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Tìm giao dịch", command=lambda: (
        text.delete(1.0, END), text.insert(END, self.find_expense(db.select_expenses, e1, e2,e3))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Xóa giao dịch",
                    command=lambda: (self.delete_expense(db.delete_expenses, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

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

        B1 = Button(top, text="Nhập giao dịch",
                    command=lambda: (self.insert(db.insert_loan, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Hiển thị giao dịch", command=lambda: (
        text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_loan()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Tìm giao dịch", command=lambda: (
        text.delete(1.0, END), text.insert(END, self.find_expense(db.select_loan, e1, e2,e3))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Xóa giao dịch",
                    command=lambda: (self.delete_expense(db.delete_loan, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

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

        B1 = Button(top, text="Nhập giao dịch",
                    command=lambda: (self.insert(db.insert_other, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Hiển thị giao dịch", command=lambda: (
            text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_other()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Tìm giao dịch", command=lambda: (
            text.delete(1.0, END), text.insert(END, self.find_expense(db.select_other, e1, e2, e3))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Xóa giao dịch",
                    command=lambda: (self.delete_expense(db.delete_other, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)


def main():
    root = Tk()
    root.geometry('250x200')
    root.title("Money Manager")
    MoneyManager(root)
    root.mainloop()


main()
