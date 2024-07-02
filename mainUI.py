import urllib.request
import random
import tkinter as tk
#import tkMessageBox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import io
import urllib.request
import mysql.connector
from getImdbId import getImdbID
from getDirectorFilmRating import getDirectorFilmRating
from getActorFilmRating import getActorFilmRating
from getMusicDFilmRating import getMusicDFilmRating
from main import getID
from main import image
from predict import predict
import re
import warnings
warnings.filterwarnings('ignore')

# establish connection with the database
mydb = mysql.connector.connect(
  host="localhost",
  user="surya",
  password="1234",
  database="movie success prediction"
)

# create a cursor object to execute SQL queries
mycursor = mydb.cursor()


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None



class getDetails(tk.Frame):

    def __init__(self,root):

        self.dummy = root
        self.test = ImageTk.PhotoImage(Image.open(r"login.jpg"))
        self.imglabel1 = tk.Label(root,  image=self.test, compound='center')
        self.imglabel1.image = self.test
        self.imglabel1.place(relx=0.00, rely=0.0)
        
        self.test = ImageTk.PhotoImage(Image.open(r"bgs1.jpg"))
        self.imglabel1 = tk.Label(root,  image=self.test, compound='center',highlightbackground='black',highlightthickness=8)
        self.imglabel1.image = self.test
        self.imglabel1.place(relx=0.275, rely=0.3,height=380,width=600)
        
        #self.test = ImageTk.PhotoImage(Image.open(r"logo.jpg"))
        #self.imglabel1 = tk.Label(root,  image=self.test, compound='center')
        #self.imglabel1.image = self.test
        #self.imglabel1.place(relx=0.90, rely=.0)
        
        #self.title = tk.Label(root, text="K.V.G College of Engineering")
        #self.title.config(font = "Helvetica 11 bold")
        #self.title.place(relx=0.35, rely=.0)
        #self.title.configure(background='#669999')gghg

        def blink_label(master=None, **kwargs):
            label = tk.Label(master, **kwargs)
            colors = ['red','black','red','black']
            current_color = colors[0]

            def blink():
                nonlocal current_color
                current_color = random.choice(colors)
                label.config(fg=current_color)
                label.after(300, blink)

            label.after(300, blink)
            return label


        self.user = blink_label(root, text="MOVIE SUCCESS PREDICTION",fg='black',highlightbackground='black',highlightthickness=8)
        self.user.config(font = "STCaiyun 50 bold")
        self.user.place(relx=0.2, rely=.1)
        self.user.configure(background='light blue')
        

        
        self.user = tk.Label(root, text="Enter Username",fg='black',highlightbackground='black',highlightthickness=2)
        self.user.config(font = "Arial 18 bold")
        self.user.place(relx=0.3, rely=.4)
        self.user.configure(background='light blue')
        self.username = tk.Text(root)
        self.username.place(relx=.48, rely=.4,height=40, width=250)
        
        self.passw = tk.Label(root, text="Enter Password",fg='black',highlightbackground='black',highlightthickness=2)
        self.passw.config(font = "Arial 18 bold")
        self.password = tk.Entry(root, show="*")
        self.passw.place(relx=0.3, rely=.5)
        self.passw.configure(background='light blue')
        #self.password = tk.Text(root, height=1.25, width=20)
        self.password.place(relx=.48, rely=.5, height=40, width=250)
        
        self.loginButton = tk.Button(root, text="Login", command=self.login,fg="black",highlightcolor='white',activeforeground="white",bd=8,activebackground="black")
        self.loginButton.place(relx=.3, rely=.6, height=40, width=140)
        self.loginButton.configure(background='light blue')
        self.regButton = tk.Button(root, text="Register", command=self.Register,fg="black",highlightcolor='white',activeforeground="white",bd=8,activebackground="black")
        self.regButton.place(relx=.52, rely=.6, height=40, width=140)
        self.regButton.configure(background='light blue')

    def validate_email(self,email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_password(self,password):
        pattern = r'^[a-zA-Z0-9]{10}$'
        return re.match(pattern, password) is not None

    def validate_name(self,name):
        pattern = r'^[a-zA-Z]+$'
        return re.match(pattern, name) is not None

    def login(self):
        global username,password
        username=self.username.get("1.0", "end-1c")
        #password=self.password.get("1.0", "end-1c")
        password=self.password.get()
        query = "SELECT * FROM User WHERE username = '" + username + "' AND password = '" + password + "'" 
        mycursor.execute(query)
        mycursor.fetchall()
        print(mycursor.rowcount)
        #result = mycursor.fetchone()
        if mycursor.rowcount==1:
            self.dashboard()            
        else:
            messagebox.showinfo("Invalid","Invalid username or password.")
            print("Invalid username or password.")
        

        
    def Register(self):
        self.user.destroy()
        self.username.destroy()
        self.passw.destroy()
        self.password.destroy()
        self.loginButton.destroy()
        self.regButton.destroy()

        if self.imglabel1:
            self.imglabel1.destroy()

        self.test = ImageTk.PhotoImage(Image.open(r"register.jpg"))
        self.imglabel2 = tk.Label(self.dummy,  image=self.test, compound='center')
        self.imglabel2.image = self.test
        self.imglabel2.place(relx=0.00, rely=0.0)
        
        self.test = ImageTk.PhotoImage(Image.open(r"bgs2.jpg"))
        self.imglabel1 = tk.Label(self.dummy,  image=self.test, compound='center',highlightbackground='black',highlightthickness=8)
        self.imglabel1.image = self.test
        self.imglabel1.place(relx=0.275, rely=0.3,height=500,width=700)

        #self.test = ImageTk.PhotoImage(Image.open(r"logo.jpg"))
        #self.imglabel1 = tk.Label(self.dummy,  image=self.test, compound='center')
        #self.imglabel1.image = self.test
        #self.imglabel1.place(relx=0.0, rely=.0)
        
        #self.title = tk.Label(self.dummy, text="K.V.G College of Engineering")
        #self.title.config(font = "Helvetica 11 bold")
        #self.title.place(relx=0.35, rely=.0)
        #self.title.configure(background='#669999')
        
        self.user = tk.Label(self.dummy, text="MOVIE SUCCESS PREDICTION",fg='black',highlightbackground='black',highlightthickness=8)
        self.user.config(font = "STCaiyun 50 bold")
        self.user.place(relx=0.2, rely=.1)
        self.user.configure(background='light blue')
        
        #self.user = tk.Label(self.dummy, text="Movie Success Rating Prediction")
        #self.user.config(font = "Helvetica 18 bold")
        #self.user.place(relx=0.2, rely=.1)
        #self.user.configure(background='#669999')
        
        self.user = tk.Label(self.dummy, text="Enter Username")
        self.user.config(font = "Arial 18 bold")
        self.user.place(relx=0.35, rely=.35)
        self.user.configure(background='light blue')
        self.username = tk.Text(self.dummy, height=2, width=20)
        self.username.place(relx=.55, rely=.35)
        self.error_label_username = tk.Label(self.dummy, fg="red")
        self.error_label_username.place(relx=.55, rely=.4)
        
        self.passw = tk.Label(self.dummy, text="Enter Password")
        self.passw.config(font = "Arial 18 bold")
        self.passw.place(relx=0.35, rely=.45)
        self.passw.configure(background='light blue')
        self.password = tk.Text(self.dummy, height=2, width=20)
        self.password.place(relx=.55, rely=.45)
        self.error_label_password = tk.Label(self.dummy, fg="red")
        self.error_label_password.place(relx=.55, rely=.5)

        self.email = tk.Label(self.dummy, text="Enter Email")
        self.email.config(font = "Arial 18 bold")
        self.email.place(relx=0.35, rely=.55)
        self.email.configure(background='light blue')
        self.emailid = tk.Text(self.dummy, height=2, width=20)
        self.emailid.place(relx=.55, rely=.55)
        self.error_label_email = tk.Label(self.dummy, fg="red")
        self.error_label_email.place(relx=.55, rely=.6)
        
        self.name = tk.Label(self.dummy, text="Enter Fullname")
        self.name.config(font = "Arial 18 bold")
        self.name.place(relx=0.35, rely=.65)
        self.name.configure(background='light blue')
        self.fullname = tk.Text(self.dummy, height=2, width=20)
        self.fullname.place(relx=.55, rely=.65)
        self.error_label_fullname = tk.Label(self.dummy, fg="red")
        self.error_label_fullname.place(relx=.55, rely=.7)
        
        self.loginButton = tk.Button(self.dummy, text="Register", command=self.registeruser,fg="black",highlightcolor='white',activeforeground="white",bd=8,activebackground="black")
        self.loginButton.place(relx=.45, rely=.75, height=40, width=150)
        self.loginButton.configure(background='light blue')        

    def registeruser(self):
        global username,password,email,fullname
        username=self.username.get("1.0", "end-1c")
        password=self.password.get("1.0", "end-1c")
        email=self.emailid.get("1.0", "end-1c")
        fullname=self.fullname.get("1.0", "end-1c")
        if self.validate_email(email):
            self.error_label_email.config(text="")
        else:
            self.error_label_email.config(text="Invalid email address")
            
        if self.validate_password(password):
            self.error_label_password.config(text="")
        else:
            self.error_label_password.config(text="Password should conatin 10 letters")

            
        if self.validate_name(fullname):
            self.error_label_fullname.config(text="")   
        else:
            self.error_label_fullname.config(text="Fullname should contain only letters") 

        if self.validate_name(username):
            self.error_label_username.config(text="")    
        else:
            self.error_label_username.config(text="Username should contain only letters")
            print("Invalid username")  
        if self.validate_email(email) and self.validate_password(password) and self.validate_name(fullname) and self.validate_name(username):
            sql = "INSERT INTO user (username,password,email,fullname) VALUES (%s, %s, %s,%s)"
            val = (username,password,email,fullname)
            # execute the query with values
            mycursor.execute(sql, val)
            # commit changes to the database
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            if(mycursor.rowcount==1):
                self.emailid.destroy()
                self.email.destroy()
                self.fullname.destroy()
                self.name.destroy()
                self.dashboard()
            else:
                messagebox.showinfo("Failed","Regiter Faailed Try agian.")

    
    def dashboard(self):
        self.user.destroy()
        self.username.destroy()
        self.passw.destroy()
        self.password.destroy()
        self.loginButton.destroy()
        self.regButton.destroy()
        self.imglabel1.destroy()
        root=self.dummy

        self.test = ImageTk.PhotoImage(Image.open(r"home.jpg"))
        self.imglabel2 = tk.Label(self.dummy,  image=self.test, compound='center')
        self.imglabel2.image = self.test
        self.imglabel2.place(relx=0.00, rely=0.0)

        self.test = ImageTk.PhotoImage(Image.open(r"bgs3.jpg"))
        self.imglabel1 = tk.Label(self.dummy,  image=self.test, compound='center',highlightbackground='black',highlightthickness=8)
        self.imglabel1.image = self.test
        self.imglabel1.place(relx=0.25, rely=0.25,height=530,width=800)

        #self.test = ImageTk.PhotoImage(Image.open(r"logo.jpg"))
        #self.imglabel1 = tk.Label(self.dummy,  image=self.test, compound='center')
        #self.imglabel1.image = self.test
        #self.imglabel1.place(relx=0.0, rely=.0)
        
        #self.title = tk.Label(self.dummy, text="K.V.G College of Engineering")
        #self.title.config(font = "Helvetica 11 bold")
        #self.title.place(relx=0.35, rely=.0)
        #self.title.configure(background='#669999')
        
        #self.user = tk.Label(self.dummy, text="Movie Success Rating Prediction")
        #self.user.config(font = "Helvetica 18 bold")
        #self.user.place(relx=0.2, rely=.1)
        #self.user.configure(background='#669999')
        
        self.user = tk.Label(self.dummy, text="MOVIE SUCCESS PREDICTION",fg='black',highlightbackground='black',highlightthickness=8)
        self.user.config(font = "STCaiyun 50 bold")
        self.user.place(relx=0.2, rely=.1)
        self.user.configure(background='light blue')
        
        self.movie = tk.Label(root, text="Enter Movie Name",fg='black',highlightbackground='black',highlightthickness=2)
        self.movie.config(font = "Arial 18 bold")
        self.movie.place(relx=0.3, rely=.3)
        self.movie.configure(background='light blue')
        self.moviename = tk.Text(self.dummy, height=2, width=20)
        self.moviename.place(relx=.55, rely=.3)
        
        self.director = tk.Label(root, text="Director Name",fg='black',highlightbackground='black',highlightthickness=2)
        self.director.config(font = "Arial 18 bold")
        self.director.place(relx=0.3, rely=.4)
        self.director.configure(background='light blue')
        self.directorname = tk.Text(self.dummy, height=2, width=20)
        self.directorname.place(relx=.55, rely=.4)

        self.hero = tk.Label(root, text="Actor(Hero) Name",fg='black',highlightbackground='black',highlightthickness=2)
        self.hero.config(font = "Arial 18 bold")
        self.hero.place(relx=0.3, rely=.5)
        self.hero.configure(background='light blue')
        self.heroname = tk.Text(self.dummy, height=2, width=20)
        self.heroname.place(relx=.55, rely=.5)

        self.music = tk.Label(root, text="Music Director",fg='black',highlightbackground='black',highlightthickness=2)
        self.music.config(font = "Arial 18 bold")
        self.music.place(relx=0.3, rely=.6)
        self.music.configure(background='light blue')
        self.musicname = tk.Text(self.dummy, height=2, width=20)
        self.musicname.place(relx=.55, rely=.6)
        
        self.year = tk.Label(root, text="Enter Year",fg='black',highlightbackground='black',highlightthickness=2)
        self.year.config(font = "Arial 18 bold")
        self.year.place(relx=0.3, rely=.7)
        self.year.configure(background='light blue')
        self.yeardata = tk.Text(self.dummy, height=2, width=20)
        self.yeardata.place(relx=.55, rely=.7)
        
        #nextButton
        self.nextButton = tk.Button(root, text="Predict", command=self.validateData,fg="black",highlightcolor='white',activeforeground="white",bd=8,activebackground="black")
        self.nextButton.configure(background='light blue')
        self.nextButton.place(relx=.45, rely=.8, height=40, width=150)

    def validateData(self):
        global movie,director,hero,music,year
        director=getDirectorFilmRating(getID(self.directorname.get("1.0", "end-1c")))
        hero=getActorFilmRating(getID(self.heroname.get("1.0", "end-1c")))
        music=getMusicDFilmRating(getID(self.musicname.get("1.0", "end-1c")))
        if director>0 and hero>0 and music>0:
            self.validate(director,hero,music)
        else:
            if director==0:
                messagebox.showinfo("Not Valid","Directorn name not valid")
            elif hero==0:
                messagebox.showinfo("Not Valid","Hero name not valid")
            else:
                messagebox.showinfo("Not Valid","Music director name not valid")
        
        

   
    #def validate(self,movie,year,music,hero,director,durl,hurl,murl):
    def validate(self,directorp,herop,musicp):
        self.test = ImageTk.PhotoImage(Image.open(r"result.jpg"))
        self.imglabel2 = tk.Label(self.dummy,  image=self.test, compound='center')
        self.imglabel2.image = self.test
        self.imglabel2.place(relx=0.00, rely=0.0)

        self.test = ImageTk.PhotoImage(Image.open(r"bgi.jpg"))
        self.imglabel1 = tk.Label(self.dummy,  image=self.test, compound='center',highlightbackground='black',highlightthickness=8)
        self.imglabel1.image = self.test
        self.imglabel1.place(relx=0.1, rely=0.3,height=300,width=280)

        self.test = ImageTk.PhotoImage(Image.open(r"bgi.jpg"))
        self.imglabel1 = tk.Label(self.dummy,  image=self.test, compound='center',highlightbackground='black',highlightthickness=8)
        self.imglabel1.image = self.test
        self.imglabel1.place(relx=0.4, rely=0.3,height=300,width=280)

        self.test = ImageTk.PhotoImage(Image.open(r"bgi.jpg"))
        self.imglabel1 = tk.Label(self.dummy,  image=self.test, compound='center',highlightbackground='black',highlightthickness=8)
        self.imglabel1.image = self.test
        self.imglabel1.place(relx=0.7, rely=0.3,height=300,width=280)

        #self.test = ImageTk.PhotoImage(Image.open(r"bgim.jpg"))
        #self.imglabel1 = tk.Label(self.dummy,  image=self.test, compound='center',highlightbackground='black',highlightthickness=8)
        #self.imglabel1.image = self.test
        #self.imglabel1.place(relx=0.22, rely=0.7,height=150,width=800)

        #self.test = ImageTk.PhotoImage(Image.open(r"logo.jpg"))
        #self.imglabel1 = tk.Label(self.dummy,  image=self.test, compound='center')
        #self.imglabel1.image = self.test
        #self.imglabel1.place(relx=0.0, rely=.0)
        
        #self.title = tk.Label(self.dummy, text="K.V.G College of Engineering")
        #self.title.config(font = "Helvetica 11 bold")
        #self.title.place(relx=0.35, rely=.0)
        #self.title.configure(background='#669999')
        
        #self.user = tk.Label(self.dummy, text="Movie Success Rating Prediction")
        #self.user.config(font = "Helvetica 18 bold")
        #self.user.place(relx=0.2, rely=.1)
        #self.user.configure(background='#669999')
        
        self.user = tk.Label(self.dummy, text="MOVIE SUCCESS PREDICTION",fg='black',highlightbackground='black',highlightthickness=8)
        self.user.config(font = "STCaiyun 30 bold")
        self.user.place(relx=0.35, rely=.05)
        self.user.configure(background='light blue')

        global dn,mn,y,msn,hn,huri,muri,duri
        dn=self.directorname.get("1.0", "end-1c")
        mn=self.moviename.get("1.0", "end-1c")
        y=self.yeardata.get("1.0", "end-1c")
        msn=self.musicname.get("1.0", "end-1c")
        hn=self.heroname.get("1.0", "end-1c")

        huri=image(getID(self.heroname.get("1.0", "end-1c")))
        muri=image(getID(self.musicname.get("1.0", "end-1c")))
        duri=image(getID(self.directorname.get("1.0", "end-1c")))
        
        self.movie.destroy()
        self.moviename.destroy()
        self.director.destroy()
        self.directorname.destroy()
        self.hero.destroy()
        self.heroname.destroy()
        self.music.destroy()
        self.musicname.destroy()
        self.year.destroy()
        self.yeardata.destroy()
        self.yeardata.destroy()
        self.nextButton.destroy()
        root=self.dummy

        self.dir = tk.Label(self.dummy, text="Director")
        self.dir.config(font = "Arial 15 bold")
        self.dir.place(relx=0.165, rely=.32)

        self.raw_data=urllib.request.urlopen(duri).read()
        self.im = Image.open(io.BytesIO(self.raw_data))
        self.im_resized = self.im.resize((120, 120), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.im_resized)
        self.label = tk.Label(root, image=self.photo)
        self.label.place(relx=0.15, rely=.37)
        
        self.dirname = tk.Label(self.dummy, text=dn)
        self.dirname.config(font = "Arial 15 bold")
        self.dirname.place(relx=0.16, rely=.53)
        
        self.dirimdb = tk.Label(self.dummy, text="IMDB :"+str(directorp))
        self.dirimdb.config(font = "Arial 15 bold")
        self.dirimdb.place(relx=0.16, rely=.57)

        self.her = tk.Label(self.dummy, text="Actor(H)")
        self.her.config(font = "Arial 15 bold")
        self.her.place(relx=0.465, rely=.32)

        self.hraw_data=urllib.request.urlopen(huri).read()
        self.him = Image.open(io.BytesIO(self.hraw_data))
        self.him_resized = self.him.resize((120, 120), Image.ANTIALIAS)
        self.hphoto = ImageTk.PhotoImage(self.him_resized)
        self.hlabel = tk.Label(root, image=self.hphoto)
        self.hlabel.place(relx=0.45, rely=.37)
        
        self.hername = tk.Label(self.dummy, text=hn)
        self.hername.config(font = "Arial 15 bold")
        self.hername.place(relx=0.46, rely=.53)
        
        self.herimdb = tk.Label(self.dummy, text="IMDB :"+str(herop))
        self.herimdb.config(font = "Arial 15 bold")
        self.herimdb.place(relx=0.46, rely=.57)

        self.mher = tk.Label(self.dummy, text="Music(D)")
        self.mher.config(font = "Arial 15 bold")
        self.mher.place(relx=0.765, rely=.32)

        self.mraw_data=urllib.request.urlopen(muri).read()
        self.mim = Image.open(io.BytesIO(self.mraw_data))
        self.mim_resized = self.mim.resize((120, 120), Image.ANTIALIAS)
        self.mphoto = ImageTk.PhotoImage(self.mim_resized)
        self.mlabel = tk.Label(root, image=self.mphoto)
        self.mlabel.place(relx=0.75, rely=.37)
        
        self.mhername = tk.Label(self.dummy, text=msn)
        self.mhername.config(font = "Arial 15 bold")
        self.mhername.place(relx=0.76, rely=.53)
        
        self.mherimdb = tk.Label(self.dummy, text="IMDB :"+str(musicp))
        self.mherimdb.config(font = "Arial 15 bold")
        self.mherimdb.place(relx=0.76, rely=.57)

        self.mnam = tk.Label(self.dummy, text="Movie Name",fg='black',highlightbackground='black',highlightthickness=2)
        self.mnam.config(font = "Arial 20 bold")
        self.mnam.place(relx=0.15, rely=.2)
        self.mnam.configure(background='white')

        self.mvm = tk.Label(self.dummy, text=mn,fg='red',highlightbackground='black',highlightthickness=2)
        self.mvm.config(font = "Arial 20 bold")
        self.mvm.place(relx=0.26, rely=.2)
        self.mvm.configure(background='white')

        self.yrd = tk.Label(self.dummy, text="Release Year",fg='black',highlightbackground='black',highlightthickness=2)
        self.yrd.config(font = "Arial 20 bold")
        self.yrd.place(relx=0.7, rely=.2)
        self.yrd.configure(background='white')

        self.yr = tk.Label(self.dummy, text=y,fg='red',highlightbackground='black',highlightthickness=2)
        self.yr.config(font = "Arial 20 bold")
        self.yr.place(relx=0.815, rely=.2)
        self.yr.configure(background='white')

        global predocteddata
        score=predict(herop,directorp,musicp)

        if score>0 and score<5:
            predocteddata="Flop"
        elif score>=5 and score<7:
            predocteddata="Hit"
        elif score>=7 and score<8:
            predocteddata="Super Hit"
        elif score>=8 and score<=10:
            predocteddata="Blockbuster"
            
            
        self.mherimdb = tk.Label(self.dummy, text="Movie Verdict ",fg='black',highlightbackground='black',highlightthickness=2)
        self.mherimdb.config(font = "Arial 20 bold")
        self.mherimdb.place(relx=0.15, rely=.725)
        self.mherimdb.configure(background='white')

        self.mherimdb = tk.Label(self.dummy, text=str(predocteddata),fg='red',highlightbackground='black',highlightthickness=2)
        self.mherimdb.config(font = "Arial 20 bold")
        self.mherimdb.place(relx=0.277, rely=.725)
        self.mherimdb.configure(background='white')
        
        self.mherimdb = tk.Label(self.dummy, text="Rating",fg='black',highlightbackground='black',highlightthickness=2)
        self.mherimdb.config(font = "Arial 20 bold")
        self.mherimdb.place(relx=0.7, rely=.725)
        self.mherimdb.configure(background='white')

        self.mherimdb = tk.Label(self.dummy, text=str(score),fg='red',highlightbackground='black',highlightthickness=2)
        self.mherimdb.config(font = "Arial 20 bold")
        self.mherimdb.place(relx=0.762, rely=.725)
        self.mherimdb.configure(background='white')

        self.backButton = tk.Button(root, text="Back", command=self.dashboard,fg="black",highlightcolor='white',activeforeground="white",bd=8,activebackground="black")
        self.backButton.configure(background='light blue')
        self.backButton.place(relx=.45, rely=.9, height=40, width=150)
        
        label.pack()
        

        def history():
            messagebox.showinfo("History", "\r\n\r\n\r\n   \r\n\r\n\r\n Date:12-2-1290 \r\n\r\n\r\n Ground : 9 ")
            
        #self.nextButton = tk.Button(root, text="Check History", command=history)
        #self.nextButton.configure(background='blue')
        #self.nextButton.place(relx=.41, rely=.85, height=40, width=150)

rt = tk.Tk()
rt.geometry("1920x1080")
rt.title("   Movie Success Rating Prediction")
rt.configure(background='#669999')
getDetails(rt)
rt.mainloop()
