from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
from tkinter import filedialog
import os

class AdvanceStudentManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title('STUDENT MANAGEMENT SYSTEM')
        self.root.geometry('1530x790+0+0')

        #====== 1st image=====
        img = Image.open("college_images/7th.jpg")
        img = img.resize((460, 160), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)

        self.btn_1=Button(self.root,image=self.photoimage,cursor='hand2',command=self.open_img_1)
        self.btn_1.place(x=0,y=0,width=460,height=160)

        # ====== 2nd image=====
        img_2 = Image.open("college_images/5th.jpg")
        img_2 = img_2.resize((460, 160), Image.ANTIALIAS)
        self.photoimage_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 = Button(self.root, image=self.photoimage_2, cursor='hand2',command=self.open_img_2)
        self.btn_2.place(x=460, y=0, width=460, height=160)

        # ====== 3rd image=====
        img_3 = Image.open("college_images/6th.jpg")
        img_3 = img_3.resize((460, 160), Image.ANTIALIAS)
        self.photoimage_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 = Button(self.root, image=self.photoimage_3, cursor='hand2',command=self.open_img_3)
        self.btn_3.place(x=920, y=0, width=460, height=160)

        #===========background image=====================

        img_4 = Image.open("college_images/university.jpg")
        img_4 = img_4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimage_4 = ImageTk.PhotoImage(img_4)

        bg_lbl =Label(self.root, image=self.photoimage_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0, y=160, width=1530, height=710)

        #=================title label=================
        lbl_title=Label(bg_lbl,text='STUDENT MANAGEMENT SYSTEM',font=('times new roman',37,"bold"),bg='white',fg='blue')
        lbl_title.place(x=0, y=0, width=1530, height=50)

        #============M  ANAGE FRAME=======
        Manage_fram=Frame(bg_lbl,bd=2,relief=RIDGE,bg='white')
        Manage_fram.place(x=15, y=55, width=1340, height=475)

        #==============left frame================
        DataLeftFrame=LabelFrame(Manage_fram,bd=4,relief=RIDGE,padx=2,text='Student Information',font=('times new roman',12,"bold"),bg='white',fg='blue')
        DataLeftFrame.place(x=10, y=10, width=660, height=455)

        #===============images in left frame========

        img_5 = Image.open("college_images/3rd.jpg")
        img_5 = img_5.resize((650, 120), Image.ANTIALIAS)
        self.photoimage_5 = ImageTk.PhotoImage(img_5)

        bg_lbl = Label(DataLeftFrame, image=self.photoimage_5, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=0, width=650, height=120)

        # ==============current course information in left frame================
        st_lbl_info_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text='Current Course Information',
                                   font=('times new roman', 12, "bold"), bg='white', fg='blue')
        st_lbl_info_frame.place(x=0, y=120, width=650, height=110)

        #=============labels &combos in current course labelframe==============

        lbl_dep=Label(st_lbl_info_frame,text='Department:',bg='white',font=('times new roman',12,'bold'))
        lbl_dep.grid(row=0,column=0,padx=2,sticky="w")

        self.var_dep=StringVar()
        combo_dep=ttk.Combobox(st_lbl_info_frame,textvariable=self.var_dep,width=17,font=('times new roman',12,'bold'),state='readonly')
        combo_dep['values']=('Select Department','Computer','Civil','IT')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky="w")

        # Course
        lbl_course = Label(st_lbl_info_frame, text='Course:', bg='white', font=('times new roman', 12, 'bold'))
        lbl_course.grid(row=0, column=2, padx=2,pady=10, sticky="w")

        self.var_course = StringVar()
        combo_course = ttk.Combobox(st_lbl_info_frame,textvariable=self.var_course, width=17, font=('times new roman', 12, 'bold'), state='readonly')
        combo_course['values'] = ('Select Course', 'FE', 'SE', 'TE','BE')
        combo_course.current(0)
        combo_course.grid(row=0, column=3, padx=2, pady=10, sticky="w")

        # year
        lbl_Year = Label(st_lbl_info_frame, text='Department:', bg='white', font=('times new roman', 12, 'bold'))
        lbl_Year.grid(row=1, column=0, padx=2, pady=10, sticky="w")

        self.var_year = StringVar()
        combo_year = ttk.Combobox(st_lbl_info_frame,textvariable=self.var_year, width=17, font=('times new roman', 12, 'bold'), state='readonly')
        combo_year['values'] = ('Select Year', '2020-21', '2021-22', '2022-23', '2023-24')
        combo_year.current(0)
        combo_year.grid(row=1, column=1, padx=2,  sticky="w")

        # semester
        lbl_semster = Label(st_lbl_info_frame, text='Semester:', bg='white', font=('times new roman', 12, 'bold'))
        lbl_semster.grid(row=1, column=2, padx=2, pady=10, sticky="w")

        self.var_semester = StringVar()
        combo_semester = ttk.Combobox(st_lbl_info_frame,textvariable=self.var_semester, width=17, font=('times new roman', 12, 'bold'), state='readonly')
        combo_semester['values'] = ('Select Semester', 'Semester-1','Semester-2')
        combo_semester.current(0)
        combo_semester.grid(row=1, column=3, padx=2, pady=10, sticky="w")

        # ==============Student Class information in left frame================
        stu_class_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text='Student Class Information',
                                       font=('times new roman', 12, "bold"), bg='white', fg='blue')
        stu_class_frame.place(x=0, y=228, width=650, height=200)

        #=================labels & combos in studentclass information===============
        #id
        lbl_id = Label(stu_class_frame, text='StudentID:', bg='white', font=('times new roman', 11, 'bold'))
        lbl_id.grid(row=0, column=0, padx=2, pady=2, sticky="w")

        self.var_std_id = StringVar()
        id_entry=ttk.Entry(stu_class_frame,textvariable=self.var_std_id,font=('times new roman', 12, 'bold'),width=22)
        id_entry.grid(row=0, column=1, padx=2, pady=2, sticky="w")

        # student name
        lbl_student = Label(stu_class_frame, text='Student Name:', bg='white', font=('times new roman', 11, 'bold'))
        lbl_student.grid(row=0, column=2, padx=2, pady=2, sticky="w")

        self.var_std_name = StringVar()
        txt_student = ttk.Entry(stu_class_frame,textvariable=self.var_std_name, font=('times new roman', 12, 'bold'), width=22)
        txt_student.grid(row=0, column=3, padx=2, pady=2, sticky="w")

        # Division
        lbl_div = Label(stu_class_frame, text='Division:', bg='white', font=('times new roman', 11, 'bold'))
        lbl_div.grid(row=1, column=0, padx=2, pady=2, sticky="w")

        self.var_div = StringVar()
        div_entry = ttk.Combobox(stu_class_frame,textvariable=self.var_div, font=('times new roman', 12, 'bold'), width=20)
        div_entry['values']=('Select Division','A','B','C')
        div_entry.current(0)
        div_entry.grid(row=1, column=1, padx=2, pady=2, sticky="w")

        # roll
        lbl_roll = Label(stu_class_frame, text='Roll No.', bg='white', font=('times new roman', 11, 'bold'))
        lbl_roll.grid(row=1, column=2, padx=2, pady=2, sticky="w")

        self.var_roll = StringVar()
        txt_roll = ttk.Entry(stu_class_frame,textvariable=self.var_roll, font=('times new roman', 11, 'bold'), width=22)
        txt_roll.grid(row=1, column=3, padx=2, pady=2, sticky="w")

        # gender
        lbl_gender = Label(stu_class_frame, text='Gender:', bg='white', font=('times new roman', 11, 'bold'))
        lbl_gender.grid(row=2, column=0, padx=2, pady=2, sticky="w")

        self.var_gender = StringVar()
        com_txt_gender = ttk.Combobox(stu_class_frame,textvariable=self.var_gender, font=('times new roman', 12, 'bold'), width=20)
        com_txt_gender['values'] = ('Select Gender', 'Male', 'Female', 'Other')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2, column=1, padx=2, pady=2, sticky="w")

        # dob
        lbl_dob = Label(stu_class_frame, text='DOB:', bg='white', font=('times new roman', 11, 'bold'))
        lbl_dob.grid(row=2, column=2, padx=2, pady=2, sticky="w")

        self.var_dob = StringVar()
        txt_dob = ttk.Entry(stu_class_frame,textvariable=self.var_dob, font=('times new roman', 12, 'bold'), width=22)
        txt_dob.grid(row=2, column=3, padx=2, pady=2, sticky="w")

        # email
        lbl_email = Label(stu_class_frame, text='Email:', bg='white', font=('times new roman', 11, 'bold'))
        lbl_email.grid(row=3, column=0, padx=2, pady=2, sticky="w")

        self.var_email = StringVar()
        txt_email = ttk.Entry(stu_class_frame,textvariable=self.var_email, font=('times new roman', 12, 'bold'), width=22)
        txt_email.grid(row=3, column=1, padx=2, pady=2, sticky="w")

        # phone
        lbl_phone = Label(stu_class_frame, text='Phone No:', bg='white', font=('times new roman', 11, 'bold'))
        lbl_phone.grid(row=3, column=2, padx=2, pady=2, sticky="w")

        self.var_phone = StringVar()
        txt_phone = ttk.Entry(stu_class_frame,textvariable=self.var_phone, font=('times new roman', 12, 'bold'), width=22)
        txt_phone.grid(row=3, column=3, padx=2, pady=2, sticky="w")

        # address
        lbl_address = Label(stu_class_frame, text='Address:', bg='white', font=('times new roman', 11, 'bold'))
        lbl_address.grid(row=4, column=0, padx=2, pady=2, sticky="w")

        self.var_address = StringVar()
        txt_address = ttk.Entry(stu_class_frame,textvariable=self.var_address, font=('times new roman', 12, 'bold'), width=22)
        txt_address.grid(row=4, column=1, padx=2, pady=2, sticky="w")

        # teacher
        lbl_teacher = Label(stu_class_frame, text='Teacher Name:', bg='white', font=('times new roman', 11, 'bold'))
        lbl_teacher.grid(row=4, column=2, padx=2, pady=2, sticky="w")

        self.var_teacher = StringVar()
        txt_teacher = ttk.Entry(stu_class_frame,textvariable=self.var_teacher, font=('times new roman', 12, 'bold'), width=22)
        txt_teacher.grid(row=4, column=3, padx=2, pady=2, sticky="w")

        #==========button frame===================
        button_frame = Frame(DataLeftFrame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=395, width=640, height=30)

        btn_add=Button(button_frame,text='Save',width=17,font=('arial', 11, "bold"), bg='blue', fg='white',cursor='hand2',command=self.add_data)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update = Button(button_frame, text='Update',width=17, font=('arial', 11, "bold"), bg='blue', fg='white', cursor='hand2',command=self.update)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(button_frame, text='Delete',width=17, font=('arial', 11, "bold"), bg='blue', fg='white', cursor='hand2',command=self.delete)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(button_frame, text='Reset',width=17, font=('arial', 11, "bold"), bg='blue', fg='white', cursor='hand2',command=self.reset_date)
        btn_reset.grid(row=0, column=3, padx=1)


        # ==============Right frame================
        DataRightFrame = LabelFrame(Manage_fram, bd=4, relief=RIDGE, padx=2, text='Student Information',
                                   font=('times new roman', 12, "bold"), bg='white', fg='blue')
        DataRightFrame.place(x=670, y=10, width=660, height=455)

        img_6 = Image.open("college_images/6th.jpg")
        img_6 = img_6.resize((650, 170), Image.ANTIALIAS)
        self.photoimage_6 = ImageTk.PhotoImage(img_6)

        bg_lbl = Label(DataRightFrame, image=self.photoimage_6, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=0, width=650, height=170)

        #===================search frame inside right frame====================
        search_frame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, padx=2, text='Search Student Information',
                                    font=('times new roman', 12, "bold"), bg='white', fg='blue')
        search_frame.place(x=0, y=160, width=650, height=60)

        search_by = Label(search_frame, text='Search by',fg='red', bg='black', font=('arial', 12, 'bold'))
        search_by.grid(row=0, column=0, padx=2, sticky="w")

        # search combo
        self.var_combo_search=StringVar()
        combo_txt_search = ttk.Combobox(search_frame, width=15,textvariable=self.var_combo_search, font=('arial', 12, 'bold'), state='readonly')
        combo_txt_search['values'] = ('Select Option', 'roll', 'phone', 'student_id')
        combo_txt_search.current(0)
        combo_txt_search.grid(row=0, column=1, padx=5,sticky="w")

        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame,textvariable=self.var_search, font=('arial', 11, 'bold'), width=20)
        txt_search.grid(row=0, column=2, padx=5, sticky="w")

        #========search frame buttons===================

        btn_search = Button(search_frame, text='Search', width=9, font=('arial', 11, "bold"), bg='blue', fg='white',cursor='hand2',command=self.search_data)
        btn_search.grid(row=0, column=3, padx=5)

        btn_showall = Button(search_frame, text='ShowAll', width=9, font=('arial', 11, "bold"), bg='blue', fg='white',cursor='hand2',command=self.fetch_data)
        btn_showall.grid(row=0, column=4, padx=5)

        #===================student table====================
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0, y=220, width=650, height=210)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=('dep','course','year','sem','id','name','div','roll','gender',
                    'dob','email','phone','address','teacher'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.bind('<ButtonRelease>',self.get_cursor)

        self.student_table.heading('dep', text='Department')
        self.student_table.column('dep', width=100)

        self.student_table.heading('course', text='Course')
        self.student_table.column('course', width=100)

        self.student_table.heading('year', text='Year')
        self.student_table.column('year', width=100)

        self.student_table.heading('sem', text='Semester')
        self.student_table.column('sem', width=100)

        self.student_table.heading('id', text='ID')
        self.student_table.column('id', width=100)

        self.student_table.heading('name', text='Name')
        self.student_table.column('name', width=100)

        self.student_table.heading('div', text='Division')
        self.student_table.column('div', width=100)

        self.student_table.heading('roll', text='Roll No')
        self.student_table.column('roll', width=100)

        self.student_table.heading('gender', text='Gender')
        self.student_table.column('gender', width=100)

        self.student_table.heading('dob', text='DOB')
        self.student_table.column('dob', width=100)

        self.student_table.heading('email', text='Email')
        self.student_table.column('email', width=100)

        self.student_table.heading('phone', text='Phone')
        self.student_table.column('phone', width=100)

        self.student_table.heading('address', text='Address')
        self.student_table.column('address', width=100)

        self.student_table.heading('teacher', text='Teacher')
        self.student_table.column('teacher', width=100)

        self.student_table['show']='headings'
        self.student_table.pack(fill=BOTH,expand=1)

        self.fetch_data()

    def add_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password='123@abc', database='stm')
                cur = con.cursor()
                # to insert in db
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                  self.var_dep.get(),
                                                                                  self.var_course.get(),
                                                                                  self.var_year.get(),
                                                                                  self.var_semester.get(),
                                                                                  self.var_std_id.get(),
                                                                                  self.var_std_name.get(),
                                                                                  self.var_div.get(),
                                                                                  self.var_roll.get(),
                                                                                  self.var_gender.get(),
                                                                                  self.var_dob.get(),
                                                                                  self.var_email.get(),
                                                                                  self.var_phone.get(),
                                                                                  self.var_address.get(),
                                                                                  self.var_teacher.get()

                                                                                                        ))
                con.commit()
                messagebox.showinfo("Success", "Student has been added",parent=self.root)
                con.close()
                self.fetch_data()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password='123@abc', database='stm')
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor(self,event):

        cursor_row=self.student_table.focus()
        contants=self.student_table.item(cursor_row)
        row=contants['values']
        self.var_dep.set(row[0]),
        self.var_course.set(row[1]),
        self.var_year.set(row[2]),
        self.var_semester.set(row[3]),
        self.var_std_id.set(row[4]),
        self.var_std_name.set(row[5]),
        self.var_div.set(row[6]),
        self.var_roll.set(row[7]),
        self.var_gender.set(row[8]),
        self.var_dob.set(row[9]),
        self.var_email.set(row[10]),
        self.var_phone.set(row[11]),
        self.var_address.set(row[12]),
        self.var_teacher.set(row[13])

    def update(self):
        if self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to Update this Student Data',parent=self.root)
                if update>0:
                    con = pymysql.connect(host="localhost", user="root", password='123@abc', database='stm')
                    cur = con.cursor()
                    cur.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,"
                                "gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s where student_id=%s",
                                                                                    (
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_std_name.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_std_id.get()
                                                                                      ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Record Successfully Updated", parent=self.root)
                    self.fetch_data()
                    con.close()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)

    def delete(self):
        if self.var_std_id=='':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                ans = messagebox.askyesno('Update', 'Are you sure to Delete this Student Data', parent=self.root)
                if ans>0:
                    con = pymysql.connect(host="localhost", user="root", password='123@abc', database='stm')
                    cur = con.cursor()
                    cur.execute("delete from student where student_id=%s", self.var_std_id.get(),)

                else:
                    if not ans:
                        return
                con.commit()
                con.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Student Data has been Deleted", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def reset_date(self):
        self.var_dep.set('Select Department'),
        self.var_course.set('Select Course'),
        self.var_year.set('Select Year'),
        self.var_semester.set('Select Semester'),
        self.var_std_id.set(''),
        self.var_std_name.set(''),
        self.var_div.set('Select Division'),
        self.var_roll.set(''),
        self.var_gender.set('Select Gender'),
        self.var_dob.set(''),
        self.var_email.set(''),
        self.var_phone.set(''),
        self.var_address.set(''),
        self.var_teacher.set('')

    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error", "Please Select option", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password='123@abc', database='stm')
                cur = con.cursor()
                cur.execute("select * from student where " +str(self.var_combo_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('', END, values=row)
                    con.commit()
                con.close()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def open_img_1(self):
        file=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open Images',filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All File","*.*")))
        img1 = Image.open(file)
        img_browse = img1.resize((460, 160), Image.ANTIALIAS)#jetna size first image ka liya hai.
        self.photoimg_browse = ImageTk.PhotoImage(img_browse)
        self.btn_1.config(image=self.photoimg_browse)

    def open_img_2(self):
        file=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open Images',filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All File","*.*")))
        img2 = Image.open(file)
        img2_browse = img2.resize((460, 160), Image.ANTIALIAS)#jetna size first image ka liya hai.
        self.photoimg2_browse = ImageTk.PhotoImage(img2_browse)
        self.btn_2.config(image=self.photoimg2_browse)

    def open_img_3(self):
        file=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open Images',filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All File","*.*")))
        img3 = Image.open(file)
        img3_browse = img3.resize((460, 160), Image.ANTIALIAS)#jetna size first image ka liya hai.
        self.photoimg3_browse = ImageTk.PhotoImage(img3_browse)
        self.btn_3.config(image=self.photoimg3_browse)

if __name__ == '__main__':
    root=Tk()
    app=AdvanceStudentManagementSystem(root)
    root.mainloop()
