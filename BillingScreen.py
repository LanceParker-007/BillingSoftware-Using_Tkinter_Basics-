from tkinter import *
import tkinter
# import mysql.connector
import tkinter.messagebox as mb

bill = Tk()
bill.title('BillingScreen')
bill.iconbitmap(
    r"C:\Users\Harsh\Desktop\Softwaress\Teacher\BillingSoftware\bilicon.ico")
bill.geometry('1920x1080+0+0')
# bill.resizable(width=FALSE, height=FALSE)
bill.config(background='gold3')

# logoImage = PhotoImage(file='Logo.png')
# photologo = Label(bill, image=logoImage, bd=10, bg='gold3',
#   relief=SUNKEN).place(x=300, y=10)
SoftwareName = Label(bill, text='Billing Software', bg='gold3', font=(
    'times new roman', 100, 'bold'), pady=3).place(x=500, y=0)
# _____________________Variables____________________
# ________________--Main Course
FP = IntVar()
PIZ = IntVar()
PB = IntVar()
GJ = IntVar()
# ______________Drinks___________

MD = IntVar()
CC = IntVar()
MZ = IntVar()
F = IntVar()

# ________________Total Bil__________
TotalBill = StringVar()

# _______________CustomerDetails

CN = StringVar()
PN = StringVar()
# _________________________Total Bill Calculation_______


def TotalAmount():
    TotalBill.set(str((FP.get()*100) + (PIZ.get()*200) +
                      (PB.get()*50) + (GJ.get()*60) +
                      (MD.get()*40) + (CC.get()*35) +
                      (MZ.get()*30)+(F.get()*35)))

# ___________________________Entry into Database________________________


def EnterDetails():
    conn = mysql.connector.connect(
        host='localhost', password='', user='root', db='billingsoftware')
    cr = conn.cursor()
    if(CN.get() == '' or PN.get() == '' or TotalBill.get() == ''):
        mb.showinfo('Alert', 'Please fill the details !!')
    else:
        cr.execute("insert into customerdetails(Name,MobileNumber,TotalBill) values('" +
                   CN.get()+"','"+PN.get()+"','"+TotalBill.get()+"')")
        conn.commit()
        mb.showinfo("Success", "Your data is inserted ...")

# ______________________________Clear Function_____________


def ClearAll():
    FP.set(0)
    PIZ.set(0)
    PB.set(0)
    GJ.set(0)

    MD.set(0)
    CC.set(0)
    MZ.set(0)
    F.set(0)

    CN.set("")
    PN.set("")
    TotalBill.set("")


# ___________________Customer Frame____________
F1 = LabelFrame(bill, text='Customer Details', bd=10, font=(15), bg='gold3')
F1.place(x=0, y=180, relwidth=1)
cname_lbl = Label(F1, text='Customer Name :- ', font=('times new roman',
                                                      20, 'bold'), bg='gold3').grid(row=0, column=0, padx=5, pady=5)
cname_txt = Entry(F1, width=20, textvariable=CN, font='arial 15', bd=5,
                  relief=SUNKEN).grid(row=0, column=1, padx=3, pady=3)

cphone_lbl = Label(F1, text='Mobile Number :- ', font=('times new roman',
                                                       20, 'bold'), bg='gold3').grid(row=0, column=2, padx=5, pady=5)
cphone_txt = Entry(F1, width=20, textvariable=PN, font='arial 15', bd=5,
                   relief=SUNKEN).grid(row=0, column=4, padx=3, pady=3)

cBill_lbl = Label(F1, text='Toal Bill :- ', font=('times new roman',
                                                  20, 'bold'), bg='gold3').grid(row=0, column=5, padx=0, pady=5)
cBill_txt = Entry(F1, width=20, textvariable=TotalBill, font='arial 15', bd=5,
                  relief=SUNKEN).grid(row=0, column=6, padx=3, pady=3)

bill_btn = Button(F1, text='Calculate Bill', width=16, bd=5,
                  font='arial 15', command=TotalAmount).grid(row=0, column=7, padx=20, pady=10)
# Main Courses________________
F2 = LabelFrame(bill, text='Main Course Menu', bd=5, font=(15), bg='gold3')
F2.place(x=0, y=275, width=765, height=500)

FullPlate_lbl = Label(F2, text='Full Plate :- ', font=('courier', 30, 'bold'),
                      bg='gold3').grid(row=0, column=0, padx=10, pady=15, sticky='w')

FullPlate_txt = Entry(F2, width=20, textvariable=FP, font=('times new roman', 20),
                      bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

Pizza_lbl = Label(F2, text='Pizza :- ', font=('courier', 30, 'bold'),
                  bg='gold3').grid(row=1, column=0, padx=10, pady=15, sticky='w')

Pizza_txt = Entry(F2, width=20, textvariable=PIZ, font=('times new roman', 20),
                  bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

PavBhaji_lbl = Label(F2, text='Pav Bhaji :- ', font=('courier', 30, 'bold'),
                     bg='gold3').grid(row=2, column=0, padx=10, pady=15, sticky='w')

PavBhaji_txt = Entry(F2, width=20, textvariable=PB, font=('times new roman', 20),
                     bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

Gulab_lbl = Label(F2, text='Gulab Jamun :- ', font=('courier', 30, 'bold'),
                  bg='gold3').grid(row=3, column=0, padx=10, pady=15, sticky='w')

Gulab_txt = Entry(F2, width=20, textvariable=GJ, font=('times new roman', 20),
                  bd=7, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

ClearAll_btn = Button(F2, text='Clear All', width=30, bd=10, bg='yellow', relief=GROOVE,
                      font='arial 25', command=ClearAll).place(y=390, relwidth=1)

# ______________________________Drinks______________________________

F3 = LabelFrame(bill, text='Drinks Menu', bd=5, font=(15), bg='gold3')
F3.place(x=766, y=275, width=765, height=500)

MountainDew_lbl = Label(F3, text='Mountain Dew :- ', font=('courier', 30, 'bold'),
                        bg='gold3').grid(row=0, column=0, padx=20, pady=15, sticky='w')

MountainDew_txt = Entry(F3, width=20, textvariable=MD, font=('times new roman', 20),
                        bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

Coke_lbl = Label(F3, text='Coca-Cola :- ', font=('courier', 30, 'bold'),
                 bg='gold3').grid(row=1, column=0, padx=20, pady=15, sticky='w')
Coke_txt = Entry(F3, width=20, textvariable=CC, font=('times new roman', 20),
                 bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

Mazza_lbl = Label(F3, text='Mazza :- ', font=('courier', 30, 'bold'),
                  bg='gold3').grid(row=2, column=0, padx=20, pady=15, sticky='w')

Mazza_txt = Entry(F3, width=20, textvariable=MZ, font=('times new roman', 20),
                  bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

Fanta_lbl = Label(F3, text='Fanta :- ', font=('courier', 30, 'bold'),
                  bg='gold3').grid(row=3, column=0, padx=20, pady=15, sticky='w')

Fanta_txt = Entry(F3, width=20, textvariable=F, font=('times new roman', 20),
                  bd=7, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

PrintBill_btn = Button(F3, text='Print Bill', width=30, bd=10, bg='orange', relief=GROOVE,
                       font='arial 25', command=EnterDetails).place(y=390, relwidth=1)

# Footer___________________
Term_lbl = Label(bill, bd=5, text='Copyright under My Stores.....').place(
    x=0, y=774, relwidth=1)

bill.mainloop()
