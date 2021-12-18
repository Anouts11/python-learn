from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
import random

def addstudent():
    def submitadd():
        id = idval.get()
        fullname = fullnameval.get()
        username = usernameval.get()
        studentId = studentIdval.get()
        extraInfo = extraInfoval.get()
        updateddate = time.strftime("%d/%m/%Y")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,fullname,username,studentId,extraInfo,addeddate,updateddate))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions','Id {} Fullname {} Added sucessfully.. and want to clean the form'.format(id,fullname),parent=addroot)
            if(res==True):
                idval.set('')
                fullnameval.set('')
                usernameval.set('')
                studentIdval.set('')
                extraInfoval.set('')
        except:
            messagebox.showerror('Notifications','Id Already Exist try another id...',parent=addroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
            studenmttable.insert('',END,values=vv)

    addroot = Toplevel(master=root)
    addroot.grab_set()
    addroot.geometry('500x350+600+200')
    addroot.title("student bazaga ma'lumot qo'shish")
    addroot.config(bg='#8C92AC')
    addroot.iconbitmap('./img/student.ico')
    addroot.resizable(False,False)

    #Text in center
    malumot_label = Label(addroot, text="Ma'lumot qo'shish",font = ('calibre',15,'normal'),bg='#8C92AC',relief=FLAT)
    malumot_label.place(x=10, y=10)
    #--------------------------------------------------- Add studenmt Labels
    idlabel = Label(addroot,text='ID',font = ('calibre',12,'normal'),bg='#8C92AC',relief=FLAT)
    idlabel.place(x=300,y=50)
    full_name_label = Label(addroot, text="Full Name",font = ('calibre',12,'normal'),bg='#8C92AC',relief=FLAT)
    full_name_label.place(x=300, y=100)
    username_label = Label(addroot, text="Username",font = ('calibre',12,'normal'),bg='#8C92AC',relief=FLAT)
    username_label.place(x=300, y=150)
    student_id_label = Label(addroot, text="student ID",font = ('calibre',12,'normal'),bg='#8C92AC',relief=FLAT)
    student_id_label.place(x=300, y=200)
    extra_info_label = Label(addroot, text="Qo'shimcha ma'lumot",font = ('calibre',12,'normal'),bg='#8C92AC',relief=FLAT)
    extra_info_label.place(x=300, y=250)

    ##----------------------------------------------------------- Add student Entry
    idval = StringVar()
    fullnameval = StringVar()
    usernameval = StringVar()
    studentIdval = StringVar()
    extraInfoval = StringVar()

    identry = Entry(addroot,width=30, font = ('calibre',13,'normal'),textvariable=idval)
    identry.place(x=10,y=50)
    full_name = Entry(addroot, width=30,font = ('calibre',13,'normal'), textvariable=fullnameval)
    full_name.place(x=10, y=100)
    username = Entry(addroot, width=30,font = ('calibre',13,'normal'), textvariable=usernameval)
    username.place(x=10, y=150)
    student_id = Entry(addroot, width=30,font = ('calibre',13,'normal'), textvariable=studentIdval )
    student_id.place(x=10, y=200)
    extra_info = Entry(addroot, width=30,font = ('calibre',13,'normal'), textvariable=extraInfoval)
    extra_info.place(x=10, y=250) 
    ############------------------------- add button
    fayl_qoshish_btn = Button(addroot, text="Fayl Qo'shish",font = ('calibre',10,'normal'), borderwidth=1, bg='#008000', fg='#ffffff')
    fayl_qoshish_btn.place(x=10, y=300)


    qoshish_haqida_label = Label(addroot, text=("Tanlangan fayl: "),font = ('calibre',10,'normal'),bg='#8C92AC',relief=FLAT)
    qoshish_haqida_label.place(x=130, y=300)

    qoshish_btn = Button(addroot, text="Qo'shish",font = ('calibre',12,'normal'), borderwidth=1, bg='#008000', fg='#ffffff', command=submitadd)
    qoshish_btn.place(x=350, y=300)



    addroot.mainloop()

def searchstudent():
    def search():
        id = idval.get()
        fullname = fullnameval.get()
        username = usernameval.get()
        studentId = studentIdval.get()
        extraInfo = extraInfoval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if(id != ''):
            strr = 'select *from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studenmttable.insert('', END, values=vv)
        elif(fullname != ''):
            strr = 'select *from studentdata1 where name=%s'
            mycursor.execute(strr,(fullname))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studenmttable.insert('', END, values=vv)
        elif(username != ''):
            strr = 'select *from studentdata1 where username=%s'
            mycursor.execute(strr,(username))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studenmttable.insert('', END, values=vv)
        elif(studentId != ''):
            strr = 'select *from studentdata1 where studentId=%s'
            mycursor.execute(strr,(studentId))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studenmttable.insert('', END, values=vv)
        elif(extraInfo != ''):
            strr = 'select *from studentdata1 where extraInfo=%s'
            mycursor.execute(strr,(extraInfo))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studenmttable.insert('', END, values=vv)
        
        elif(addeddate != ''):
            strr = 'select *from studentdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studenmttable.insert('', END, values=vv)

    searchroot = Toplevel(master=root)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='firebrick1')
    # searchroot.iconbitmap('mana.ico')
    searchroot.resizable(False,False)
    #--------------------------------------------------- Add studenmt Labels
    idlabel = Label(searchroot,text='Enter Id : ',bg='gold2',font=('times',20,'bold'),relief=FLAT,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    usernamelabel = Label(searchroot,text='Enter Username : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    usernamelabel.place(x=10,y=130)

    studentIdlabel = Label(searchroot,text='Enter studentId : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    studentIdlabel.place(x=10,y=190)

    extraInfolabel = Label(searchroot,text='Enter ExtraInfo : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    extraInfolabel.place(x=10,y=250)

    datelabel = Label(searchroot,text='Enter Date : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    ##----------------------------------------------------------- Add student Entry
    idval = StringVar()
    fullnameval = StringVar()
    usernameval = StringVar()
    studentIdval = StringVar()
    extraInfoval = StringVar()   
    dateval = StringVar()

    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=fullnameval)
    nameentry.place(x=250,y=70)

    usernamevalentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=usernameval)
    usernamevalentry.place(x=250,y=130)

    studentIdentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=studentIdval)
    studentIdentry.place(x=250,y=190)

    extraInfoentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=extraInfoval)
    extraInfoentry.place(x=250,y=250)

    dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    ############------------------------- add button
    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='red',command=search)
    submitbtn.place(x=150,y=480)



    searchroot.mainloop()
def deletestudent():
    cc = studenmttable.focus()
    content = studenmttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenmttable.insert('', END, values=vv)


def updatestudent():
    def update():
        id = idval.get()
        fullname = fullnameval.get()
        username = usernameval.get()
        studentId = studentIdval.get()
        extraInfo = extraInfoval.get()
        date = dateval.get()
        udate = udateval.get()

        strr = 'update studentdata1 set fullname=%s,username=%s,studentId=%s,extraInfo=%s,date=%s,udate=%s where id=%s'
        mycursor.execute(strr,(fullname,username,studentId,extraInfo,date,udate,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
            studenmttable.insert('', END, values=vv)

    updateroot = Toplevel(master=root)
    updateroot.grab_set()
    updateroot.geometry('500x350+600+200')
    updateroot.title("student bazada ma'lumot o'zgartirish")
    updateroot.config(bg='#8C92AC')
    updateroot.iconbitmap('./img/student.ico')
    updateroot.resizable(False,False)

    #Text in center
    malumot_label = Label(updateroot, text="Ma'lumot o'zgartirish",font = ('calibre',15,'normal'),bg='#8C92AC',relief=FLAT)
    malumot_label.place(x=10, y=10)
    #--------------------------------------------------- Add studenmt Labels
    idlabel = Label(updateroot,text='ID',font = ('calibre',12,'normal'),bg='#8C92AC',relief=FLAT)
    idlabel.place(x=300,y=50)
    full_name_label = Label(updateroot, text="Full Name",font = ('calibre',12,'normal'),bg='#8C92AC',relief=FLAT)
    full_name_label.place(x=300, y=100)
    username_label = Label(updateroot, text="Username",font = ('calibre',12,'normal'),bg='#8C92AC',relief=FLAT)
    username_label.place(x=300, y=150)
    student_id_label = Label(updateroot, text="student ID",font = ('calibre',12,'normal'),bg='#8C92AC',relief=FLAT)
    student_id_label.place(x=300, y=200)
    extra_info_label = Label(updateroot, text="Qo'shimcha ma'lumot",font = ('calibre',12,'normal'),bg='#8C92AC',relief=FLAT)
    extra_info_label.place(x=300, y=250)

    ##----------------------------------------------------------- Add student Entry
    idval = StringVar()
    fullnameval = StringVar()
    usernameval = StringVar()
    studentIdval = StringVar()
    extraInfoval = StringVar()

    identry = Entry(updateroot,width=30, font = ('calibre',13,'normal'),textvariable=idval)
    identry.place(x=10,y=50)
    full_name = Entry(updateroot, width=30,font = ('calibre',13,'normal'), textvariable=fullnameval)
    full_name.place(x=10, y=100)
    username = Entry(updateroot, width=30,font = ('calibre',13,'normal'), textvariable=usernameval)
    username.place(x=10, y=150)
    student_id = Entry(updateroot, width=30,font = ('calibre',13,'normal'), textvariable=studentIdval )
    student_id.place(x=10, y=200)
    extra_info = Entry(updateroot, width=30,font = ('calibre',13,'normal'), textvariable=extraInfoval)
    extra_info.place(x=10, y=250) 
    ############------------------------- add button
    fayl_qoshish_btn = Button(updateroot, text="Fayl Qo'shish",font = ('calibre',10,'normal'), borderwidth=1, bg='#008000', fg='#ffffff')
    fayl_qoshish_btn.place(x=10, y=300)


    qoshish_haqida_label = Label(updateroot, text=("Tanlangan fayl: "),font = ('calibre',10,'normal'),bg='#8C92AC',relief=FLAT)
    qoshish_haqida_label.place(x=130, y=300)

    qoshish_btn = Button(updateroot, text="O'zgartirish",font = ('calibre',12,'normal'), borderwidth=1, bg='#008000', fg='#ffffff', command=update)
    qoshish_btn.place(x=350, y=300)
    idval = StringVar()
    fullnameval = StringVar()
    usernameval = StringVar()
    studentIdval = StringVar()
    extraInfoval = StringVar()
    dateval = StringVar()
    udateval = StringVar()  

    # ##----------------------------------------------------------- Add student Entry
    idval = StringVar()
    fullnameval = StringVar()
    usernameval = StringVar()
    studentIdval = StringVar()
    extraInfoval = StringVar()
    dateval = StringVar()
    udateval = StringVar()
    
    cc = studenmttable.focus()
    content = studenmttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        fullnameval.set(pp[1])
        usernameval.set(pp[2])
        studentIdval.set(pp[3])
        extraInfoval.set(pp[4])
        dateval.set(pp[5])
        udateval.set(pp[6])

    updateroot.mainloop()
def showstudent():
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
        studenmttable.insert('', END, values=vv)

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenmttable.get_children()
    id,fullname,username,studentId,extraInfo,addeddate,updateddate=[],[],[],[],[],[],[]
    for i in gg:
        content = studenmttable.item(i)
        pp = content['values']
        id.append(pp[0]),fullname.append(pp[1]),username.append(pp[2]),studentId.append(pp[3]),extraInfo.append(pp[4]),
        addeddate.append(pp[5]),updateddate.append(pp[6])
    dd = ['Id','Fullname','Username','studentId','extraInfo','Added Date','Updated Date']
    df = pandas.DataFrame(list(zip(id,fullname,username,studentId,extraInfo,addeddate,updateddate)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))


def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
        root.destroy()


###################################################################################Connecttion of Database
def Connectdb():
    def submitdb():
        global con,mycursor
        # host = hostval.get()
        # user = userval.get()
        # password = passwordval.get()
        host = 'localhost'
        user = 'root'
        password = 'root'
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem4'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem4'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,fullname varchar(50),username varchar(50),studentId varchar(30),extraInfo varchar(100),date varchar(50),udate varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected connected to the database ....',parent=dbroot)
            
            
            

        except:
            strr = 'use studentmanagementsystem4'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database ....',parent=dbroot)
            strr = 'select * from studentdata1'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studenmttable.insert('', END, values=vv)
        dbroot.destroy()



    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('350x200+600+200')
    dbroot.iconbitmap('./img/student.ico')
    dbroot.config(bg='#8C92AC')
    dbroot.resizable(False,False)
    #-------------------------------Connectdb Labels
    
    # full_name_label = Label(addroot, text="Full Name",font = ('calibre',12,'normal'))
    # full_name_label.place(x=300, y=100)

    hostlabel = Label(dbroot,text="Enter Host : ",font=('calibre',12,'normal'),bg='#8C92AC',relief=FLAT,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",font=('calibre',12,'normal'),bg='#8C92AC',relief=FLAT,anchor='w')
    userlabel.place(x=10,y=60)

    passwordlabel = Label(dbroot,text="Enter Password : ",font=('calibre',12,'normal'),bg='#8C92AC',relief=FLAT,anchor='w')
    passwordlabel.place(x=10,y=110)

    #-------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    hostentry = Entry(dbroot, width=20, font=('calibre',13,'normal'),textvariable=hostval)
    hostentry.place(x=150,y=10)

    userentry = Entry(dbroot,width=20,font=('calibre',13,'normal'),textvariable=userval)
    userentry.place(x=150,y=60)

    passwordentry = Entry(dbroot,width=20,font=('calibre',13,'normal'),textvariable=passwordval)
    passwordentry.place(x=150,y=110)

    #-------------------------------- Connectdb button
    submitbutton = Button(dbroot,text='Submit',font=('calibre',12,'normal'),width=10,borderwidth=1, bg='#008000', fg='#ffffff', command=submitdb)
    submitbutton.place(x=120,y=160)

    dbroot.mainloop()


##########################################################################################################

# root = Tk()
# root.title('Student Management System')
# root.config(bg='gold2')
# root.geometry('1174x700+200+50')
# # root.iconbitmap('mana.ico')
# root.resizable(False,False)
# ############################################################################################################  Frames
# ##---------------------------------------------------------------------------- dataentry frame

# DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
# DataEntryFrame.place(x=10,y=80,width=500,height=600)

# addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
#                 activeforeground='white',command=addstudent)
# addbtn.pack(side=TOP,expand=True)

# searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
#                 activeforeground='white',command=searchstudent)
# searchbtn.pack(side=TOP,expand=True)

# deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
#                 activeforeground='white',command=deletestudent)
# deletebtn.pack(side=TOP,expand=True)

# updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
#                 activeforeground='white',command=updatestudent)
# updatebtn.pack(side=TOP,expand=True)

# showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
#                 activeforeground='white',command=showstudent)
# showallbtn.pack(side=TOP,expand=True)

# exportbtn = Button(DataEntryFrame,text='6. Export data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
#                 activeforeground='white',command=exportstudent)
# exportbtn.pack(side=TOP,expand=True)

# exitbtn = Button(DataEntryFrame,text='7.  Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
#                 activeforeground='white',command=exitstudent)
# exitbtn.pack(side=TOP,expand=True)

# ##-----------------------------------------------------------Show data frame
# ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
# ShowDataFrame.place(x=550,y=80,width=620,height=600)

# ##-------------------------------------------------  Showdataframe
# style = ttk.Style()
# style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
# style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')
# scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
# scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
# studenmttable = Treeview(ShowDataFrame,columns=('Id','Fullname','Username','studentId','ExtraInfo','Added Date','Updated Date'),
#                          yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
# scroll_x.pack(side=BOTTOM,fill=X)
# scroll_y.pack(side=RIGHT,fill=Y)
# scroll_x.config(command=studenmttable.xview)
# scroll_y.config(command=studenmttable.yview)
# studenmttable.heading('Id',text='Id')
# studenmttable.heading('Fullname',text='Fullname')
# studenmttable.heading('Username',text='Username')
# studenmttable.heading('studentId',text='studentId')
# studenmttable.heading('ExtraInfo',text='ExtraInfo')
# studenmttable.heading('Added Date',text='Added Date')
# studenmttable.heading('Updated Date',text='Updated Date')
# studenmttable['show'] = 'headings'
# studenmttable.column('Id',width=100)
# studenmttable.column('Fullname',width=200)
# studenmttable.column('Username',width=200)
# studenmttable.column('studentId',width=300)
# studenmttable.column('ExtraInfo',width=200)
# studenmttable.column('Added Date',width=150)
# studenmttable.column('Updated Date',width=150)
# studenmttable.pack(fill=BOTH,expand=1)


# ################################################################################################################## ConnectDatabaseButton
# connectbutton = Button(root,text='Connect To Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2',
#                        activebackground='blue',activeforeground='white',command=Connectdb)
# connectbutton.place(x=930,y=0)
root = Tk()
root.title('student baza')
root.geometry('1200x800+200+50')
root.iconbitmap('./img/student.ico')
root.resizable(False,False)

 # create a search box label
search_box = Entry(root, width=20,font = ('calibre',15,'normal'))
search_box.insert(0, "Qidirish...")        
search_box.place(x=500,y=25,anchor='center')

#create a search box button
search_btn_image = PhotoImage(file = r"./img/searchicon1.png")
search_box_btn = Button(root, image=search_btn_image, borderwidth=2)
search_box_btn.place(x=630,y=25,anchor='center')

#adding new user button
add_info_btn = Button(root, text="Ma'lumot Qo'shish",font = ('calibre',13,'normal'), borderwidth=1, bg='#008000', fg='#ffffff', command=addstudent)
add_info_btn.place(x=830,y=25,anchor='center')

connectbutton = Button(root, text="Bazaga ulash",font = ('calibre',13,'normal'), borderwidth=1, bg='#008000', fg='#ffffff', command=Connectdb)
connectbutton.place(x=1000,y=25,anchor='center')

displayInfobutton = Button(root, text="To'liq ma'lumot",font = ('calibre',13,'normal'), borderwidth=1, bg='#008000', fg='#ffffff', command=Connectdb)
displayInfobutton.place(x=80,y=25,anchor='center')

editInfobutton = Button(root, text="O'zgartirish",font = ('calibre',13,'normal'), borderwidth=1, bg='#008000', fg='#ffffff', command=updatestudent)
editInfobutton.place(x=250,y=25,anchor='center')


############################################################################################################  Frames
ShowDataFrame = Frame(root,relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=0,y=80,width=1200,height=675)
style = ttk.Style()
style.configure('Treeview.Heading',font=('calibre',15,'normal'))
style.configure('Treeview',font=('times',15,'bold'),foreground='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenmttable = Treeview(ShowDataFrame,columns=('Id','Fullname','Usename','studentID','ExtraInfo','Addeddate'),
                            yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenmttable.xview)
scroll_y.config(command=studenmttable.yview)
studenmttable.heading('Id',text='Id')
studenmttable.heading('Fullname',text='Fullname')
studenmttable.heading('Usename',text='Usename')
studenmttable.heading('studentID',text='student ID')
studenmttable.heading('ExtraInfo',text='ExtraInfo')
studenmttable.heading('Addeddate',text='Added date')
studenmttable['show'] = 'headings'
studenmttable.column('Id',width=50)
studenmttable.column('Fullname',width=300)
studenmttable.column('Usename',width=200)
studenmttable.column('studentID',width=100)
studenmttable.column('ExtraInfo',width=300)
studenmttable.column('Addeddate',width=100)
studenmttable.pack(fill=BOTH,expand=1)
# showstudent()


root.mainloop()