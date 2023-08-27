from tkinter import  *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
import pymysql
from tkinter import messagebox

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title('GUI Analog Clock')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#021e2f')

        #==========background colors==============
        self.left_lbl = Label(self.root, bg='#08a3D2', bd=0)
        self.left_lbl.place(x=0, y=0, width=600, relheight=1)

        self.right_lbl = Label(self.root, bg='#031F3C', bd=0)
        self.right_lbl.place(x=600, y=0, relwidth=1, relheight=1)

        #================FRAMES================
        login_frame=Frame(self.root,bg='white')
        login_frame.place(x=250,y=100,width=800,height=500)

        login_title=Label(login_frame,text='LOGIN HERE',font=('times new roman',30,'bold'),bg='white',fg='#08A3D2').place(x=250,y=50)

        email_title = Label(login_frame, text='EMAIL ADDRESS', font=('times new roman',18, 'bold'), bg='white',fg='gray').place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=('times new roman', 15),bg='lightgray')
        self.txt_email.place(x=250, y=180,width=350,height=35)

        pass_ = Label(login_frame, text='PASSWORD', font=('times new roman', 18, 'bold'), bg='white',fg='gray').place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=('times new roman', 15), bg='lightgray')
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, text='Register new Account?',font=('times new roman',14),bg='white',bd=0,fg='#B00857',cursor='hand2',command=self.register_window).place(x=250,y=320)
        btn_login = Button(login_frame, text='Login', font=('times new roman', 20,'bold'), fg='white',
                         bg='#B00857', cursor='hand2',command=self.login).place(x=250, y=380,width=180,height=40)


        #======= clock================
        self.lbl=Label(self.root,text='\nMycode Clock',font=('Book Antiqua',25,'bold'),compound=BOTTOM,fg='white',bg='#081923',bd=0)
        self.lbl.place(x=90,y=120,width=350,height=450)
        # self.clock_image()
        self.working()

    #==============functions================

    def clock_image(self,hr,min_,sec_):
        clock=Image.new('RGB',(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #for clock Image
        bg=Image.open('Images/c.png')
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        #Formula to rortate the clock anticlockwise
        #angle_in_radians = angle_in_degrees * math.pi/180
        #line_length=100
        #center_x=250
        #center_y=250
        #x2 or end_x=center_x - line_lenght * math.cos(angle_in_radians)
        # y2 or end_y=center_y - line_lenght * math.sin(angle_in_radians)

        #===for hour line====
        #(x1,y1,x2,y2)
        draw.line((200,200,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill='#DF005E',width=4)

        # ===for minuts line====
        # draw.line((200, 200, 280, 210), fill='blue', width=3)
        draw.line((200, 200, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill='white', width=3)
        # ===for second line====
        # draw.line((200, 200, 300, 240), fill='green', width=3)
        draw.line((200, 200, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill='yellow', width=2)

        draw.ellipse((195,195,210,210),fill='#1AD5D5')


        clock.save('Images/clock_new.png')

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        #make the angle of h,m,s
        hr= (h/12)*360
        min_=(m/60)*360
        sec_ = (s/ 60)*360
        self.clock_image(hr,min_,sec_)
        self.img = ImageTk.PhotoImage(file="Images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get()=='' or self.txt_pass_.get()=='':
            messagebox.showerror('Error','All fields are Required',parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',database='employee')
                cur=con.cursor()
                cur.execute('select * from employee where email=%s and password=%s',(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Invalid Email and Password', parent=self.root)
                else:
                    messagebox.showinfo('Success', 'Welcome', parent=self.root)
                    self.root.destroy()
                    import Student
                con.close()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)





root=Tk()
obj=login_window(root)
root.mainloop()