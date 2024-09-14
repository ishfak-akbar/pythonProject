from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import Databasehotel
import datetime
import time
from datetime import datetime, timedelta


# Frontend
class Hotel:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Database Management System")
        self.root.geometry("1350x800+0+0")
        MainFrame = Frame(self.root)
        MainFrame.grid()
        TopFrame = Frame(MainFrame, bd=10, bg='#088f8f', width=1350, height=550, relief=RIDGE)
        TopFrame.pack(side=TOP)
        TopFramex = Frame(TopFrame, bd=1, bg='#088f8f', width=1250, height=50, padx=2, relief=RIDGE)
        TopFramex.pack(side=TOP)
        LeftFrame = Frame(TopFrame, bg='#088f8f', bd=5, width=500, height=800, relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        RightFrame = Frame(TopFrame, bd=10, bg='#088f8f', width=890, height=1000, relief=RIDGE)
        RightFrame.pack(side=RIGHT)
        RightFrame1 = Frame(RightFrame, bd=5, width=890, height=50, padx=0, relief=RIDGE)
        RightFrame1.grid(row=0, column=0)
        RightFrame2 = Frame(RightFrame, bd=5, width=890, height=250, padx=0, relief=RIDGE)
        RightFrame2.grid(row=1, column=0)
        RightFrame3 = Frame(RightFrame, bg='#088f8f', bd=5, width=890, height=400, padx=0, relief=RIDGE)
        RightFrame3.grid(row=2, column=0)
        BottomFrame = Frame(MainFrame, bg='#088f8f', bd=9, width=1280, height=150, padx=2, relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)

        global hd
        CusID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Nationality = StringVar()
        DOB = StringVar()
        ProveOfID = StringVar()
        Gender = StringVar()
        DateIn = StringVar()
        DateOut = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        RoomExtNo = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        PaidTax = StringVar()
        TotalDays = StringVar()

        DateIn.set(time.strftime("%d/%m/%Y"))
        DateOut.set(time.strftime("%d/%m/%Y"))

        x = random.randint(1190, 8746)
        randomRef = str(x)
        CusID.set("Hotel" + randomRef)

        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Database Management Systems",
                                                "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExtNo.set("")
            TotalCost.set("")
            ProveOfID.set("")
            TotalDays.set("")
            Nationality.set("")
            Gender.set("")

            self.txtCusID.delete(0, END)
            self.txtDOB.delete(0, END)
            self.txtFirstname.delete(0, END)
            self.txtSurname.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtEmail.delete(0, END)
            self.txtPostCode.delete(0, END)
            self.txtMobile.delete(0, END)
            self.txtDateIn.delete(0, END)
            self.txtDateOut.delete(0, END)
            self.txtPaidTax.delete(0, END)
            self.txtSubTotal.delete(0, END)
            self.txtTotalCost.delete(0, END)

            DateIn.set(time.strftime("%d/%m/%Y"))
            DateOut.set(time.strftime("%d/%m/%Y"))

            x = random.randint(1111, 9999)
            randomRef = str(x)
            CusID.set("Hotel" + randomRef)

        def addData():
            if (len(CusID.get()) != 0):
                Databasehotel.addHotelRec(CusID.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(),
                                          Mobile.get(), Nationality.get(), ProveOfID.get(), DateIn.get(), DateOut.get(),
                                          Email.get())

                lstHotel.delete(0, END)
                lstHotel.insert(END, (
                    CusID.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(), Mobile.get(),
                    Nationality.get(), ProveOfID.get(), DateIn.get(), DateOut.get(), Email.get()))

        def DisplayData():
            lstHotel.delete(0, END)

            for row in Databasehotel.viewData():
                lstHotel.insert(END, row, str(""))

        def HotelRec(event):
            global hd
            searchHdb = lstHotel.curselection()[0]
            hd = lstHotel.get(searchHdb)

            self.txtCusID.delete(0, END)
            self.txtCusID.insert(END, hd[1])
            self.txtFirstname.delete(0, END)
            self.txtFirstname.insert(END, hd[2])
            self.txtSurname.delete(0, END)
            self.txtSurname.insert(END, hd[3])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, hd[4])
            self.cboGender.delete(0, END)
            self.cboGender.insert(END, hd[5])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, hd[6])
            self.cboNationality.delete(0, END)
            self.cboNationality.insert(END, hd[7])
            self.cboProveOfID.delete(0, END)
            self.cboProveOfID.insert(END, hd[8])
            self.txtDateIn.delete(0, END)
            self.txtDateIn.insert(END, hd[9])
            self.txtDateOut.delete(0, END)
            self.txtDateOut.insert(END, hd[10])
            self.txtEmail.delete(0, END)
            self.txtEmail.insert(END, hd[11])

        def DeleteData():
            if CusID.get():
                Databasehotel.deleteRec(hd[0])
                Reset()
                DisplayData()

        '''
        def DeleteData():
            global hd
            searchHdb = lstHotel.curselection()[0]
            hd = lstHotel.get(searchHdb)
            if (len(CusID.get()) != 0):
                Databasehotel.deleteRec(hd[0])
                Reset()
                DisplayData()
        '''
        '''
        def DeleteData(self):
            # Assuming you're using a listbox to select a guest
            selected_item = self.listbox.curselection()  # Get selected item index
            if selected_item:
                guest_id = self.listbox.get(selected_item[0])  # Get ID from selected item
                Databasehotel.deleteRec(guest_id)  # Call delete function with ID
            else:
                # Handle case of no selection
                messagebox.showerror("Error", "Please select a guest to delete")
        '''

        def searchDatabase():
            lstHotel.delete(0, END)
            for row in Databasehotel.searchData(CusID.get(), Firstname.get(), Surname.get(), Address.get(),
                                                Gender.get(), Mobile.get(), Nationality.get(), ProveOfID.get(),
                                                DateIn.get(), DateOut.get(), Email.get()):
                lstHotel.insert(END, row, str(""))

        def update():
            if (len(CusID.get()) != 0):
                Databasehotel.deleteRec(hd[0])

            if (len(CusID.get()) != 0):
                Databasehotel.addStdRec(CusID.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(),
                                        Mobile.get(), Nationality.get(), ProveOfID.get(), DateIn.get(), DateOut.get(),
                                        Email.get())
                lstHotel.delete(0, END)
                lstHotel.insert(END, (
                    CusID.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(), Mobile.get(),
                    Nationality.get(), ProveOfID.get(), DateIn.get(), DateOut.get(), Email.get()))

        def TotalCostandAddData():
            addData()
            InDate = DateIn.get()
            OutDate = DateOut.get()
            try:
                Indate = datetime.strptime(InDate, "%d/%m/%Y")
                Outdate = datetime.strptime(OutDate, "%d/%m/%Y")
                TotalDays.set(abs(Outdate - Indate).days)
            except ValueError as e:  # Catch potential format issues
                print("Invalid date format. Please enter dates in DD/MM/YYYY format.")
            if (Meal.get() == "Breakfast" and RoomType.get() == "Single"):
                q1 = float(17)
                q2 = float(34)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "£" + str('%.2f' % ((q5) * 0.09))
                ST = "£" + str('%.2f' % ((q5)))
                TT = "£" + str('%.2f' % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                self.txtPaidTax.delete(0, END)
                self.txtPaidTax.insert(0, Tax)
                self.txtSubTotal.delete(0, END)
                self.txtSubTotal.insert(0, ST)
                self.txtTotalCost.delete(0, END)
                self.txtTotalCost.insert(0, TT)
            elif (Meal.get() == "Breakfast" and RoomType.get() == "Double"):
                q1 = float(34)
                q2 = float(45)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "£" + str('%.2f' % ((q5) * 0.09))
                ST = "£" + str('%.2f' % ((q5)))
                TT = "£" + str('%.2f' % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                self.txtPaidTax.delete(0, END)
                self.txtPaidTax.insert(0, Tax)
                self.txtSubTotal.delete(0, END)
                self.txtSubTotal.insert(0, ST)
                self.txtTotalCost.delete(0, END)
                self.txtTotalCost.insert(0, TT)
            elif (Meal.get() == "Breakfast" and RoomType.get() == "Family"):
                q1 = float(17)
                q2 = float(34)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "£" + str('%.2f' % ((q5) * 0.09))
                ST = "£" + str('%.2f' % ((q5)))
                TT = "£" + str('%.2f' % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                # Update the entry fields here
                self.txtPaidTax.delete(0, END)
                self.txtPaidTax.insert(0, Tax)
                self.txtSubTotal.delete(0, END)
                self.txtSubTotal.insert(0, ST)
                self.txtTotalCost.delete(0, END)
                self.txtTotalCost.insert(0, TT)
            elif (Meal.get() == "Lunch" and RoomType.get() == "Single"):
                q1 = float(17)
                q2 = float(34)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "£" + str('%.2f' % ((q5) * 0.09))
                ST = "£" + str('%.2f' % ((q5)))
                TT = "£" + str('%.2f' % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                # Update the entry fields here
                self.txtPaidTax.delete(0, END)
                self.txtPaidTax.insert(0, Tax)
                self.txtSubTotal.delete(0, END)
                self.txtSubTotal.insert(0, ST)
                self.txtTotalCost.delete(0, END)
                self.txtTotalCost.insert(0, TT)
            elif (Meal.get() == "Lunch" and RoomType.get() == "Double"):
                q1 = float(17)
                q2 = float(34)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "£" + str('%.2f' % ((q5) * 0.09))
                ST = "£" + str('%.2f' % ((q5)))
                TT = "£" + str('%.2f' % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                # Update the entry fields here
                self.txtPaidTax.delete(0, END)
                self.txtPaidTax.insert(0, Tax)
                self.txtSubTotal.delete(0, END)
                self.txtSubTotal.insert(0, ST)
                self.txtTotalCost.delete(0, END)
                self.txtTotalCost.insert(0, TT)
            elif (Meal.get() == "Lunch" and RoomType.get() == "Family"):
                q1 = float(17)
                q2 = float(34)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "£" + str('%.2f' % ((q5) * 0.09))
                ST = "£" + str('%.2f' % ((q5)))
                TT = "£" + str('%.2f' % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                # Update the entry fields here
                self.txtPaidTax.delete(0, END)
                self.txtPaidTax.insert(0, Tax)
                self.txtSubTotal.delete(0, END)
                self.txtSubTotal.insert(0, ST)
                self.txtTotalCost.delete(0, END)
                self.txtTotalCost.insert(0, TT)
            elif (Meal.get() == "Dinner" and RoomType.get() == "Single"):
                q1 = float(17)
                q2 = float(34)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "£" + str('%.2f' % ((q5) * 0.09))
                ST = "£" + str('%.2f' % ((q5)))
                TT = "£" + str('%.2f' % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                # Update the entry fields here
                self.txtPaidTax.delete(0, END)
                self.txtPaidTax.insert(0, Tax)
                self.txtSubTotal.delete(0, END)
                self.txtSubTotal.insert(0, ST)
                self.txtTotalCost.delete(0, END)
                self.txtTotalCost.insert(0, TT)
            elif (Meal.get() == "Dinner" and RoomType.get() == "Double"):
                q1 = float(17)
                q2 = float(34)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "£" + str('%.2f' % ((q5) * 0.09))
                ST = "£" + str('%.2f' % ((q5)))
                TT = "£" + str('%.2f' % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                # Update the entry fields here
                self.txtPaidTax.delete(0, END)
                self.txtPaidTax.insert(0, Tax)
                self.txtSubTotal.delete(0, END)
                self.txtSubTotal.insert(0, ST)
                self.txtTotalCost.delete(0, END)
                self.txtTotalCost.insert(0, TT)
            elif (Meal.get() == "Dinner" and RoomType.get() == "Family"):
                q1 = float(17)
                q2 = float(34)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "£" + str('%.2f' % ((q5) * 0.09))
                ST = "£" + str('%.2f' % ((q5)))
                TT = "£" + str('%.2f' % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                # Update the entry fields here
                self.txtPaidTax.delete(0, END)
                self.txtPaidTax.insert(0, Tax)
                self.txtSubTotal.delete(0, END)
                self.txtSubTotal.insert(0, ST)
                self.txtTotalCost.delete(0, END)
                self.txtTotalCost.insert(0, TT)

        # =============================================Widget--TopFrame==========================================
        self.lblCusID = Label(TopFramex, font=("lucida calligraphy", 20, 'bold'), bg='#1c1c1c', fg='white',
                              text="GRAND METRO INN", padx=457, pady=1)
        self.lblCusID.grid(row=0, column=0, sticky=W)
        self.txtCusID = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=CusID)
        self.txtCusID.grid(row=0, column=1, pady=3, padx=20)

        # =============================================Widget==========================================
        self.lblCusID = Label(LeftFrame, font=("calibri", 13, 'bold'), bg='#088f8f', text="Customer Ref:", padx=1,
                              pady=5)
        self.lblCusID.grid(row=0, column=0, sticky=W)
        self.txtCusID = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=CusID)
        self.txtCusID.grid(row=0, column=1, pady=3, padx=20)

        self.lblFirstname = Label(LeftFrame, font=("calibri", 13, 'bold'), bg='#088f8f', text="First Name:", padx=1,
                                  pady=5)
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=Firstname)
        self.txtFirstname.grid(row=1, column=1, pady=3, padx=20)

        self.lblSurname = Label(LeftFrame, font=("calibri", 13, 'bold'), bg='#088f8f', text="Surname:", padx=1, pady=5)
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=Surname)
        self.txtSurname.grid(row=2, column=1, pady=3, padx=20)

        self.lblAddress = Label(LeftFrame, font=('calibri', 13, 'bold'), bg='#088f8f', text="Address: ", padx=1, pady=5)
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame, font=('calibri', 13, 'bold'), width=18, textvariable=Address)
        self.txtAddress.grid(row=3, column=1, pady=3, padx=20)

        self.lblDOB = Label(LeftFrame, font=("calibri", 13, 'bold'), bg='#088f8f', text="Date of Birth:", padx=2,
                            pady=5)
        self.lblDOB.grid(row=4, column=0, sticky=W)
        self.txtDOB = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=DOB)
        self.txtDOB.grid(row=4, column=1, pady=3, padx=20)

        self.lblPostCode = Label(LeftFrame, font=("calibri", 13, 'bold'), bg='#088f8f', text="PostCode:", padx=2,
                                 pady=5)
        self.lblPostCode.grid(row=5, column=0, sticky=W)
        self.txtPostCode = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=PostCode)
        self.txtPostCode.grid(row=5, column=1, pady=3, padx=20)

        self.lblMobile = Label(LeftFrame, font=("calibri", 13, 'bold'), bg='#088f8f', text="Mobile:", padx=2, pady=5)
        self.lblMobile.grid(row=6, column=0, sticky=W)
        self.txtMobile = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=Mobile)
        self.txtMobile.grid(row=6, column=1, pady=3, padx=20)

        self.lblEmail = Label(LeftFrame, font=("calibri", 13, 'bold'), bg='#088f8f', text="Email:", padx=2, pady=5)
        self.lblEmail.grid(row=7, column=0, sticky=W)
        self.txtEmail = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=Email)
        self.txtEmail.grid(row=7, column=1, pady=3, padx=20)
        '''
        self.lblNationality = Label(LeftFrame, font=("arial", 12, 'bold'), text="Nationality:", padx=2, pady=2)
        self.lblNationality.grid(row=8, column=0, sticky=W)
        self.txtNationality = Entry(LeftFrame, font=("arial", 12, 'bold'), width=18)
        self.txtNationality.grid(row=8, column=1, pady=3, padx=20)
        '''
        self.lblNationality = Label(LeftFrame, font=('calibri', 13, 'bold'), bg='#088f8f', text="Nationality:", padx=2,
                                    pady=5)
        self.lblNationality.grid(row=8, column=0, sticky=W)
        self.cboNationality = ttk.Combobox(LeftFrame, textvariable=Nationality, state='readonly',
                                           font=('calibri', 13, 'bold'), width=16)
        self.cboNationality['value'] = (' ', 'Bangladeshi', 'British', 'American', 'Canadian', 'Europian')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=8, column=1, pady=3, padx=2)
        '''
        self.lblGender = Label(LeftFrame, font=("calibri", 13, 'bold'),bg='lightblue', text="Gender:", padx=2, pady=5)
        self.lblGender.grid(row=9, column=0, sticky=W)
        self.txtGender = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=Gender)
        self.txtGender.grid(row=9, column=1, pady=3, padx=20)
        '''
        self.lblGender = Label(LeftFrame, font=('calibri', 13, 'bold'), bg='#088f8f', text="Gender:", padx=2, pady=5)
        self.lblGender.grid(row=9, column=0, sticky=W)
        self.cboGender = ttk.Combobox(LeftFrame, textvariable=Gender, state='readonly', font=('calibri', 13, 'bold'),
                                      width=16)
        self.cboGender['value'] = (' ', 'Male', 'Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=9, column=1, pady=3, padx=2)

        self.lblDateIn = Label(LeftFrame, font=("calibri", 13, 'bold'), bg='#088f8f', text="Check In Date:", padx=2,
                               pady=5)
        self.lblDateIn.grid(row=10, column=0, sticky=W)
        self.txtDateIn = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=DateIn)
        self.txtDateIn.grid(row=10, column=1, pady=3, padx=20)

        self.lblDateOut = Label(LeftFrame, font=("calibri", 13, 'bold'), bg='#088f8f', text="Check Out Date:", padx=2,
                                pady=5)
        self.lblDateOut.grid(row=11, column=0, sticky=W)
        self.txtDateOut = Entry(LeftFrame, font=("calibri", 13, 'bold'), width=18, textvariable=DateOut)
        self.txtDateOut.grid(row=11, column=1, pady=3, padx=20)

        self.lblProveOfID = Label(LeftFrame, font=('calibri', 13, 'bold'), bg='#088f8f', text="Type of ID:", padx=2,
                                  pady=5)
        self.lblProveOfID.grid(row=12, column=0, sticky=W)
        self.cboProveOfID = ttk.Combobox(LeftFrame, textvariable=ProveOfID, state='readonly',
                                         font=('calibri', 13, 'bold'), width=16)
        self.cboProveOfID['value'] = (' ', 'Pilot Licence', 'Driving Licence', 'Student ID', 'Passport')
        self.cboProveOfID.current(0)
        self.cboProveOfID.grid(row=12, column=1, pady=3, padx=2)

        self.lblMeal = Label(LeftFrame, font=('calibri', 13, 'bold'), bg='#088f8f', text="Meal:", padx=2, pady=5)
        self.lblMeal.grid(row=13, column=0, sticky=W)
        self.cboMeal = ttk.Combobox(LeftFrame, textvariable=Meal, state='readonly', font=('calibri', 13, 'bold'),
                                    width=16)
        self.cboMeal['value'] = (' ', 'Breakfast', 'Lunch', 'Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13, column=1, pady=3, padx=2)

        self.lblRoomType = Label(LeftFrame, font=('calibri', 13, 'bold'), bg='#088f8f', text="Room Type:", padx=2,
                                 pady=5)
        self.lblRoomType.grid(row=14, column=0, sticky=W)
        self.cboRoomType = ttk.Combobox(LeftFrame, textvariable=RoomType, state='readonly',
                                        font=('calibri', 13, 'bold'),
                                        width=16)
        self.cboRoomType['value'] = ('', 'Single', 'Double', 'Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14, column=1, pady=3, padx=2)

        self.lblRoomNo = Label(LeftFrame, font=('calibri', 13, 'bold'), bg='#088f8f', text="Room No:", padx=2, pady=5)
        self.lblRoomNo.grid(row=15, column=0, sticky=W)
        self.cboRoomNo = ttk.Combobox(LeftFrame, textvariable=RoomNo, state='readonly', font=('calibri', 13, 'bold'),
                                      width=16)
        self.cboRoomNo['value'] = ('', '001', '002', '003', '004', '005', '006')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=15, column=1, pady=3, padx=2)

        self.lblRoomExtNo = Label(LeftFrame, font=('calibri', 13, 'bold'), bg='#088f8f', text="Room Ext. No:", padx=2,
                                  pady=5)
        self.lblRoomExtNo.grid(row=16, column=0, sticky=W)
        self.cboRoomExtNo = ttk.Combobox(LeftFrame, textvariable=RoomExtNo, state='readonly',
                                         font=('calibri', 13, 'bold'), width=16)
        self.cboRoomExtNo['value'] = ('', '101', '102', '103', '104', '105', '106')
        self.cboRoomExtNo.current(0)
        self.cboRoomExtNo.grid(row=16, column=1, pady=3, padx=2)

        # =============================================Widget==========================================
        self.lblLabel = Label(RightFrame1, font=('arial', 10, 'bold'), bg='#088f8f', padx=18, pady=19,
                              text="CustomerRef       FirstName      Surname       Address       Gender      Mobile      Nationality      ProveOfID      DateIn      DateOut      Email")
        self.lblLabel.grid(row=0, column=0, columnspan=19)
        scrollbar = Scrollbar(RightFrame2)
        scrollbar.grid(row=0, column=1, sticky='ns')
        lstHotel = Listbox(RightFrame2, width=96, height=17, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        lstHotel.bind('<<ListboxSelect>>', HotelRec)
        lstHotel.grid(row=0, column=0, padx=7, sticky='nsew')
        scrollbar.config(command=lstHotel.xview)

        # =============================================Widget==========================================
        self.lblDays = Label(RightFrame3, font=('arial', 13, 'bold'), text="No of Days:", bg='#088f8f', padx=10, pady=7)
        self.lblDays.grid(row=0, column=0, sticky=W)
        self.txtDays = Entry(RightFrame3, font=('arial', 12, 'bold'), width=82, textvariable=TotalDays, justify=LEFT)
        self.txtDays.grid(row=0, column=1, pady=3, padx=20)

        self.lblPaidTax = Label(RightFrame3, font=('arial', 13, 'bold'), bg='#088f8f', text="Paid Tax:", padx=10,
                                pady=7)
        self.lblPaidTax.grid(row=1, column=0, sticky=W)
        self.txtPaidTax = Entry(RightFrame3, font=('arial', 12, 'bold'), width=82)
        self.txtPaidTax.grid(row=1, column=1, pady=3, padx=20)

        self.lblSubTotal = Label(RightFrame3, font=('arial', 13, 'bold'), bg='#088f8f', text="Subtotal:", padx=10,
                                 pady=7)
        self.lblSubTotal.grid(row=2, column=0, sticky=W)
        self.txtSubTotal = Entry(RightFrame3, font=('arial', 12, 'bold'), width=82)
        self.txtSubTotal.grid(row=2, column=1, pady=3, padx=20)

        self.lblTotalCost = Label(RightFrame3, font=('arial', 13, 'bold'), bg='#088f8f', text="Total Cost:", padx=10,
                                  pady=7)
        self.lblTotalCost.grid(row=3, column=0, sticky=W)
        self.txtTotalCost = Entry(RightFrame3, font=('arial', 12, 'bold'), width=82)
        self.txtTotalCost.grid(row=3, column=1, pady=3, padx=20)

        # ==============================================BUTTONS=====================================================
        self.btnTotalandAddData = Button(BottomFrame,
             bg='#1c1c1c', bd=4,
             font=('arial', 16, 'bold'), width=14,
             fg='white', height=2, pady=5,
             text="AddNew/Total",
             command=TotalCostandAddData).grid(row=0, column=0, padx=7, pady=10)


        self.btnDisplay = Button(BottomFrame,
             bd=4, bg='#1c1c1c',
             font=('arial', 16, 'bold'),fg='white',
             width=14,height=2, pady=5,
             text="Display",
             command=DisplayData).grid(row=0, column=1,padx=7, pady=10)

        #self.btnUpdate = Button(BottomFrame, bd=4,  bg='lightcoral',font=('arial', 16, 'bold'), width=12, height=2,pady=5, text="Update",command=update).grid( row=0, column=2, padx=4, pady=1)
        self.btnDelete = Button(BottomFrame, bd=4, bg='#1c1c1c',
                                font=('arial', 16, 'bold')
                                , fg='white', width=14, height=2, pady=5, text="Delete",
                                command=DeleteData).grid(row=0, column=3, padx=7, pady=10)
        self.btnSearch = Button(BottomFrame, bd=4, bg='#1c1c1c', font=('arial', 16, 'bold'), fg='white', width=14,
                                height=2, pady=5, text="Search",
                                command=searchDatabase).grid(row=0, column=4, padx=7, pady=10)
        self.btnReset = Button(BottomFrame, bd=4, bg='#1c1c1c', font=('arial', 16, 'bold'), fg='white', width=14,
                               height=2, pady=5, text="Reset",
                               command=Reset).grid(row=0, column=5, padx=7, pady=10)
        self.btnExit = Button(BottomFrame, bd=4, bg='#c30010', font=('arial', 16, 'bold'),
                              fg='white', width=14,
                              height=2, pady=5, text="Exit",
                              command=iExit).grid(row=0, column=6, padx=7, pady=10)


if __name__ == '__main__':
    root = Tk()
    application = Hotel(root)
    root.state('zoomed')
    root.mainloop()
