from tkinter import *
import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='',database='student')
if conn.is_connected():
    print('CONNECTED')
cursor=conn.cursor()
class sql:

    def __init__(self,root):
        root.title('INSERTION')
        self.m=Menu()
        root.config(menu=self.m)
        self.m1=Menu(root,tearoff=0)
        self.m.add_cascade(label='CHANGE',menu=self.m1)
        self.m1.add_command(label='DELETE',command=self.delete)
        self.m1.add_command(label='UPDATE',command=self.update)
        self.m1.add_command(label='RETRIEVE',command=self.retrieve)
        self.m.add_cascade(label='EXIT',command=root.destroy)
        self.f2=Frame(root,height=400,width=450,bg='peachpuff')
        self.f2.propagate(0)
        self.f2.pack()
        self.l1=Label(self.f2,text='ENTER ID:',fg='black',font='bold',bg='peachpuff').place(x=50,y=70)
        self.l2=Label(self.f2,text='ENTER NAME:',fg='black',font='bold',bg='peachpuff').place(x=50,y=110)
        self.l3=Label(self.f2,text='ENTER ROLLNO:',fg='black',font='bold',bg='peachpuff').place(x=50,y=150)
        self.l4=Label(self.f2,text='ENTER FEES:',fg='black',font='bold',bg='peachpuff').place(x=50,y=190)
        self.e1=Entry(self.f2,width=20,bg='white')
        self.e1.place(x=230,y=70)
        self.e2=Entry(self.f2,width=25,bg='white')
        self.e2.place(x=230, y=110)
        self.e3=Entry(self.f2,width=20,bg='white')
        self.e3.place(x=230,y=150)
        self.e4=Entry(self.f2,bg='white',width=20)
        self.e4.place(x=230,y=190)
        self.b2=Button(self.f2,bg='skyblue',fg='black',text='INSERT',font='bold',command=self.insert1)
        self.b2.place(x=90,y=280)
    def insert1(self):
        self.var1=self.e1.get()
        self.var2=self.e2.get()
        self.var3=self.e3.get()
        self.var4=self.e4.get()
        try:
            cursor.execute("Insert into class values('"+str(self.var1)+"','"+str(self.var2)+"','"+str(self.var3)+"','"+str(self.var4)+"')")
            l1=Label(self.f2,text='INSERTED',bg='peachpuff',fg='black').place(x=100,y=210)
            conn.commit()
        except:
            conn.rollback()
            print('ROLLBACK')
        self.e1.delete(0,'end')
        self.e2.delete(0,'end')
        self.e3.delete(0,'end')
        self.e4.delete(0,'end')
    def delete(self):
        self.root3=Tk()
        self.root3.title('DELETE')
        self.f3=Frame(self.root3,height=300,width=400,bg='blue')
        self.f3.propagate(0)
        self.f3.pack()
        L=Label(self.f3,text='Enter the ID to delete data:',fg='black').place(x=40,y=60)
        self.E=Entry(self.f3,width=20,bg='white')
        self.E.place(x=220,y=60)
        B=Button(self.f3,text='DELETE',bg='red',fg='white',command=self.dele)
        B.place(x=50,y=130)
    def dele(self):
        v1=self.E.get()
        try:
            cursor.execute("delete from class where id='"+v1+"'")
            l=Label(self.f3,text='DELETED',fg='black',bg='white').place(x=120,y=160)
            conn.commit()
        except:
            l2=Label(self.f3,text='UNABLE TO DELETE',fg='black',bg='white').place(x=120,y=160)
            conn.rollback()
        self.E.delete(0,'end')
        self.root3.mainloop()
    def retrieve(self):
        self.root4=Tk()
        self.root4.title('GET')
        self.f4=Frame(self.root4,height=480,width=500,bg='white')
        self.f4.propagate(0)
        self.f4.pack()
        l=Label(self.f4,text='Enter ID to retrieve data:').place(x=40,y=60)
        self.e5=Entry(self.f4,width=20,bg='white',fg='black')
        self.e5.place(x=220,y=60)
        B=Button(self.f4,text='GET',bg='darkgreen',fg='white',command=self.ret).place(x=50,y=100)
    def ret(self):
        v=self.e5.get()
        a2=['ID is:','Name is:','Rollno is:','Fees is:']
        try:
            cursor.execute("select * from class where id='" + v + "'")
            a = cursor.fetchone()
            print(a)
            for i in range(4):
                l = Label(self.f4,text=a2[i]+str(a[i]),font='bold', fg='black').place(x=80, y=200+i*35)
            conn.commit()
        except:
            l2=Label(self.f4,text='NOT FOUND',fg='black').place(x=80,y=200)
            print('ROLLBACK')
            conn.rollback()
        self.e5.delete(0,'end')
        self.root4.mainloop()
    def update(self):
        self.root5=Tk()
        self.root5.title('UPDATE')
        self.f5=Frame(self.root5,height=400,width=450,bg='skyblue')
        self.f5.propagate(0)
        self.f5.pack()
        l=Label(self.f5,text='Enter ID to update data:',bg='white').place(x=30,y=50)
        self.e6=Entry(self.f5,width=20,bg='white',fg='black')
        self.e6.place(x=200,y=50)
        self.b0=Button(self.f5,text='CLICK',bg='yellow',command=self.up)
        self.b0.pack(padx=4,pady=4)
        self.b0.place(x=50, y=90)
    def up(self):
        c=0
        r2=[]
        self.v=self.e6.get()
        cursor.execute('select id from class')
        r = cursor.fetchone()
        while r is not None:
            r2.append(r[0])
            r=cursor.fetchone()
        print(self.v)
        for i in range(len(r2)):
            if (int(r2[i]) == int(self.v)):
                c = c + 1
        if(c!=0):
         self.b0.destroy()
         a=['ENTER NEW ID:','ENTER NEW NAME:','ENTER NEW ROLLNO:','ENTER NEW FEES']
         for i in range(4):
            l=Label(self.f5,text=a[i]).place(x=30,y=90+i*30)
         self.e7=Entry(self.f5,width=20,bg='white')
         self.e8=Entry(self.f5,width=30,bg='white')
         self.e9=Entry(self.f5,width=20,bg='white')
         self.e10=Entry(self.f5,width=20,bg='white')
         self.e7.place(x=150,y=90)
         self.e8.place(x=150,y=120)
         self.e9.place(x=160,y=150)
         self.e10.place(x=150,y=180)

         b=Button(self.f5,text='UPDATE',bg='pink',command=self.u).place(x=50,y=250)
        else:
            l=Label(self.f5,text='WRONG ID!',bg='red',fg='white').place(x=70,y=200)

    def u(self):
        v2 = self.e7.get()
        v3 = self.e8.get()
        v4 = self.e9.get()
        v5 = self.e10.get()
        try:
            cursor.execute("update class set id='" + v2 + "',name='" + v3 + "',rollno='" + v4 + "',fees='" + v5 + "'where id='" + self.v + "'")
            l = Label(self.f5, text='UPDATED', fg='black', bg='skyblue').place(x=100, y=200)
            conn.commit()
        except:
            l = Label(self.f5, text='ERROR', fg='black', bg='skyblue').place(x=100, y=200)
            conn.rollback()
        self.e6.delete(0,'end')
        self.e7.delete(0,'end')
        self.e8.delete(0,'end')
        self.e9.delete(0,'end')
        self.e10.delete(0,'end')
        self.root5.mainloop()
root=Tk()
sql(root)
root.mainloop()
cursor.close()
conn.close()