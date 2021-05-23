import tkinter as tk
from PIL import ImageTk
import PIL
from tkinter import*
from tkinter import ttk
import mysql.connector
root = tk.Tk()
root.title("Kütüphane")


same=True
n=0.3


def kutuphane():
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFF9C4",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    table_frame=Frame(root,bd=4,relief=RIDGE,bg='#e03456')
    table_frame.place(x=300,y=100,width=950,height=600)

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)    
    kutuphane_table=ttk.Treeview(table_frame,columns=("Kütüphane İd","İsim","Adres No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=kutuphane_table.xview)
    scroll_x.config(command=kutuphane_table.yview)
    kutuphane_table.heading("Kütüphane İd",text="Kütüphane İd")
    kutuphane_table.heading("İsim",text="İsim")
    kutuphane_table.heading("Adres No",text="Adres No")
    
    kutuphane_table['show']='headings'
    kutuphane_table.column("Kütüphane İd",width=300)
    kutuphane_table.column("İsim",width=300)
    kutuphane_table.column("Adres No",width=300)
    kutuphane_table.pack()

    quitBtn = Button(root,text="<- Menüye Geri Dön",bg='#455A64', fg='white',font=("arial",15,"bold"),command=empMenu)
    quitBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)


def kitap_işlemleri():
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    

    girilen= StringVar()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)


    
    manage_frame=Frame(root,bd=4,relief=RIDGE,bg="#e03456").place(x=20,y=100,width=500,height=560)
    manage_title=Label(manage_frame,text="Kitap Bilgileri",fg="white",bg="#e03456",font=("times new roman",20,"bold")).place(x=25,y=110)


    kitapisbnbilgi=StringVar()
    kitapBaslik=StringVar()
    kitapYayinevi=StringVar()
    kitapkutuphaneid=StringVar()
           
            
    label_roll=Label(manage_frame,text="ISBN",fg="white",bg="#e03456",font=("times new roman",20,"bold")).place(x=25,y=150)
    txt_roll=Entry(manage_frame,bd=5,relief=GROOVE,textvariable=kitapisbnbilgi,font=("times new roman",15,"bold")).place(x=180,y=150)

    label_roll=Label(manage_frame,text="Başlık",bg="#e03456",fg="white",font=("times new roman",20,"bold")).place(x=25,y=200)
    txt_roll=Entry(manage_frame,bd=5,relief=GROOVE,textvariable=kitapBaslik,font=("times new roman",15,"bold")).place(x=180,y=200)

    label_roll=Label(manage_frame,text="Yayınevi",bg="#e03456",fg="white",font=("times new roman",20,"bold")).place(x=25,y=250)
    txt_roll=Entry(manage_frame,bd=5,relief=GROOVE,textvariable=kitapYayinevi,font=("times new roman",15,"bold")).place(x=180,y=250)

    label_roll=Label(manage_frame,text="Kütüphane",bg="#e03456",fg="white",font=("times new roman",20,"bold")).place(x=25,y=300)
    txt_roll=Entry(manage_frame,bd=5,width=20,relief=GROOVE,textvariable=kitapkutuphaneid,font=("times new roman",15,"bold")).place(x=180,y=300)


    button_frame=Frame(manage_frame,bd=4,relief=RIDGE, bg="#e03456").place(x=10,y=480,width=430)
    updatebtn=Button(button_frame,text="Güncelle",width=10,height=2).place(x=200,y=500)
    deletebtn=Button(button_frame,text="Sil",width=10,height=2).place(x=300,y=500)
    
        
    detail_frame=Frame(root,bd=4,relief=RIDGE,bg="#e03456").place(x=550,y=100,width=800,height=560)
    search_label=Label(detail_frame,text="Ara",bg="#e03456",fg="white",font=("times new roman",24,"bold")).place(x=580,y=105)

    widget_var = tk.StringVar()

    vlist=["ISBN", "Yazar", "Kategori"]
    
    
    combo_search=ttk.Combobox(detail_frame,values=vlist,font=("times new roman",15,"bold"),state='readonly')
    combo_search.set("Pick an option")
    combo_search.pack(padx =5,pady=5)


    combo_search.place(x=680,y=112)



    txt_search=Entry(detail_frame,textvariable=girilen,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE).place(x=920,y=112)

    def arama():

        cnx = mysql.connector.connect(user='root', password='1234',
        host='127.0.0.1',
        database='sakila')

        cursor = cnx.cursor()

        secilen=combo_search.get()
        print(secilen)

        metin=girilen.get()
        
        if secilen == "ISBN":
            kitapgetir()
            
    def kitapgetir():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()

        mycursor.execute("SELECT * from kitap_tablosu WHERE kitap_isbn = '%s'" % girilen.get())

        rows=mycursor.fetchall()

        if len(rows) !=0:
            kitap_table.delete(*kitap_table.get_children())
            for row in rows:
                kitap_table.insert("",END,values=row)
            conn.commit()
        conn.close()

    def tumkitapgetir():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()
        mycursor.execute("SELECT * from kitap_tablosu ")
        rows=mycursor.fetchall()

        if len(rows) !=0:
            kitap_table.delete(*kitap_table.get_children())
            for row in rows:
                kitap_table.insert("",END,values=row)
            conn.commit()
        conn.close()

    def yazarbilgialma():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()

        mycursor.execute("SELECT * from kitap_tablosu WHERE kitap_isbn = '%s'" % girilen.get())

        rows=mycursor.fetchall()

        if len(rows) !=0:
            kitap_table.delete(*kitap_table.get_children())
            for row in rows:
                kitap_table.insert("",END,values=row)
            conn.commit()
        conn.close()

    def addbook():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()
        sql="insert into kitap_tablosu (kitap_isbn,kitap_baslik,kitap_yayinevi,kitap_kutuphane_id) values (%s,%s,%s,%s)"
        val=(kitapisbnbilgi.get(),kitapBaslik.get(),kitapYayinevi.get(),kitapkutuphaneid.get())
        mycursor.execute(sql,val)
        conn.commit()
        kitabi_getir()
        conn.close()

    def kitabi_getir():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()
        mycursor.execute("select * from kitap_tablosu")
        rows=mycursor.fetchall()
        if len(rows) !=0:
            kitap_table.delete(*kitap_table.get_children())
            for row in rows:
                kitap_table.insert("",END,values=row)
            conn.commit()
        conn.close()  

    def yazitemizle():
        kitapisbnbilgi.set("")
        kitapBaslik.set("")
        kitapYayinevi.set("")
        kitapkutuphaneid.set("")
        
    
    clearbtn=Button(button_frame,text="Temizle",command=yazitemizle,width=10,height=2).place(x=400,y=500)
    
    addbtn=Button(button_frame,text="Ekle",command=addbook,width=10,height=2).place(x=100,y=500)

    search_button=Button(detail_frame,text="Ara",command=arama,width=10,pady=5).place(x=1100,y=112)
    show_allbtn=Button(detail_frame,text="Tüm Kitapları Göster",command=tumkitapgetir,width=15,pady=5).place(x=1200,y=112)

    quitBtn = Button(root,text="<- Menüye Geri Dön",bg='#455A64', fg='white',font=("arial",15,"bold"),command=empMenu)
    quitBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)
    
    table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg='#e03456')
    table_frame.place(x=560,y=170,width=780,height=480)

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)    
    kitap_table=ttk.Treeview(table_frame,columns=("ISBN","Başlık","Yayınevi","Kütüphane İd"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=kitap_table.xview)
    scroll_x.config(command=kitap_table.yview)
    kitap_table.heading("ISBN",text="ISBN")
    kitap_table.heading("Başlık",text="Başlık")
    kitap_table.heading("Yayınevi",text="Yayınevi")
    kitap_table.heading("Kütüphane İd",text="Kütüphane İd")
    kitap_table['show']='headings'
    kitap_table.pack() 


    
def alinan_kitaplar():
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)


    
    table_frame=Frame(root,bd=4,relief=RIDGE,bg='#e03456')
    table_frame.place(x=300,y=170,width=900,height=480)

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)    
    kitap_table=ttk.Treeview(table_frame,columns=("Emanet No","Alış Tarihi","Teslim Tarihi","Üye İd","ISBN","Kütüphane İd"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=kitap_table.xview)
    scroll_x.config(command=kitap_table.yview)
    kitap_table.heading("Emanet No",text="Emanet No")
    kitap_table.heading("Alış Tarihi",text="Alış Tarihi")
    kitap_table.heading("Teslim Tarihi",text="Teslim Tarihi")
    kitap_table.heading("Üye İd",text="Üye İd")
    kitap_table.heading("ISBN",text="ISBN")
    kitap_table.heading("Kütüphane İd",text="Kütüphane İd")
    kitap_table['show']='headings'
    kitap_table.column("Emanet No",width=145)
    kitap_table.column("Alış Tarihi",width=145)
    kitap_table.column("Teslim Tarihi",width=145)
    kitap_table.column("Üye İd",width=145)
    kitap_table.column("ISBN",width=145)
    kitap_table.column("Kütüphane İd",width=145)
     
    kitap_table.pack()

    quitBtn = Button(root,text="<- Menüye Geri Dön",bg='#455A64', fg='white',font=("arial",15,"bold"),command=empMenu)
    quitBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)

    





def empMenu():
    
    global headingFrame1,headingFrame2,headingLabel,btn2,Canvas1,labelFrame,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn2.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#f7f1e3",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="MENU", fg='black',font=("Arial",40,"bold"))
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Kitap İşlemleri",bg='black', fg='white',font=("arial",15,"bold"),command=kitap_işlemleri)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Üye-Kitap İşlemleri",bg='black', fg='white',font=("arial",15,"bold"), command=alinan_kitaplar)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="Kütüphaneler",bg='black', fg='white',font=("arial",15,"bold"),command=kutuphane)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="Kategori",bg='black', fg='white',font=("arial",15,"bold"), command=kategori)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    btn5 = Button(root,text="Yazar",bg='black', fg='white',font=("arial",15,"bold"), command = yazar)
    btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn5 = Button(root,text="Adres",bg='black', fg='white',font=("arial",15,"bold"), command = adres)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="<- Geri",bg='#455A64', fg='white',font=("arial",15,"bold"), command=uye)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)


def quit():
    root.destroy()




def uye():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    
    Canvas1 = Canvas(root)

    kuladkontrol= StringVar()
    kulmailkontrol= StringVar()

    Canvas1.config(bg="#FFF9C4",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Üye Girişi", fg='black',font=("arial",20,"bold"))
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)

    lbl_user=Label(root,text="Kullanıcı Adı",font=("Goudy old style",15,"bold"),fg='gray',bg="white").place(x=400,y=300)
    txt_user=Entry(root,textvariable=kuladkontrol,font=('times new roman',15),bg='lightgray').place(x=400,y=350,width=350,height=35)

    lbl_pass=Label(root,text="Mail",font=("Goudy old style",15,"bold"),fg='gray',bg="white").place(x=400,y=400)
    txt_pass=Entry(root,textvariable=kulmailkontrol,font=('times new roman',15),bg='lightgray').place(x=400,y=450,width=350,height=35)
    
    #btn1 = Button(root,text="Register",bg='black', fg='white')
    #btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)

    def kontrol():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()

        val=(kuladkontrol.get())
        val2=(kulmailkontrol.get())
        
        print(val)
        sql="SELECT uye_adi FROM uye_tablosu WHERE uye_adi = '%s'" % val

        sqls="SELECT uye_mail FROM uye_tablosu WHERE uye_mail = '%s'" % val2
        mycursor.execute(sql)
        uyeadi=mycursor.fetchall()

        mycursor.execute(sqls)
        uyemail=mycursor.fetchall()

        if uyeadi == [('%s' % val,)] and uyemail == [('%s' % val2,)]:
            empMenu()
        
        conn.close()

    
    btn2 = Button(root,text="Giriş Yap",command=kontrol,bg='#455A64', fg='white',font=("arial",15,"bold"))
    btn2.place(relx=0.30,rely=0.8, relwidth=0.18,relheight=0.08)
    
    btn3 = Button(root,text="Çık",bg='#455A64', fg='white',font=("arial",15,"bold"),command=quit)
    btn3.place(relx=0.53,rely=0.8, relwidth=0.18,relheight=0.08)



def kayit():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    
    Canvas1 = Canvas(root)

    mystring= StringVar()
    mystring1= StringVar()
    kullanicisoyad= StringVar()
    kullanicitelefon= StringVar()
    kullanicieposta= StringVar()

    def getvalue():
        print(mystring.get())
        print(mystring1.get())
        print(kullanicisoyad.get())
        print(kullanicitelefon.get())
        print(kullanicieposta.get())


    Canvas1.config(bg="#FFF9C4",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Yeni Üye", fg='black',font=("arial",30,"bold"))
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)

    lbl_uyeid=Label(root,text="Kullanıcı İd",font=("Goudy old style",20,"bold"),fg='gray',bg="white").place(x=400,y=350)
    Entry(root,textvariable=mystring,font=('times new roman',15),bg='lightgray').place(x=550,y=350,width=350,height=35)
    

    
    lbl_ad=Label(root,text="Ad",font=("Goudy old style",20,"bold"),fg='gray',bg="white").place(x=400,y=410)
    txt_ad=Entry(root,textvariable=mystring1,font=('times new roman',15),bg='lightgray').place(x=550,y=410,width=350,height=35)

    lbl_soyad=Label(root,text="Soyad",font=("Goudy old style",20,"bold"),fg='gray',bg="white").place(x=400,y=470)
    txt_soyad=Entry(root,textvariable=kullanicisoyad,font=('times new roman',15),bg='lightgray').place(x=550,y=470,width=350,height=35)

    lbl_tel=Label(root,text="Telefon",font=("Goudy old style",20,"bold"),fg='gray',bg="white").place(x=400,y=530)
    txt_tel=Entry(root,textvariable=kullanicitelefon,font=('times new roman',15),bg='lightgray').place(x=550,y=530,width=350,height=35)

    lbl_eposta=Label(root,text="E-posta",font=("Goudy old style",20,"bold"),fg='gray',bg="white").place(x=400,y=590)
    txt_eposta=Entry(root,textvariable=kullanicieposta,font=('times new roman',15),bg='lightgray').place(x=550,y=590,width=350,height=35)
   
    
    btn3 = Button(root,text="Çık",bg='#455A64', fg='white',command=quit,font=("arial",15,"bold"))
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    backBtn = Button(root,text="<- Geri",bg='#455A64', fg='white',font=("arial",15,"bold"), command=uye)
    backBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)


    def addkayit():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()
        sql="insert into uye_tablosu (uye_id,uye_adi,uye_soyadi,uye_tel,uye_mail,uye_adres_no) values (%s,%s,%s,%s,%s,'15')"
        val=(mystring.get(),mystring1.get(),kullanicisoyad.get(),kullanicitelefon.get(),kullanicieposta.get())
        mycursor.execute(sql,val)
        conn.commit()

        conn.close()

    btn2 = Button(root,text="Kaydet",command=addkayit,bg='black', fg='white',font=("arial",15,"bold"))
    btn2.place(relx=0.53,rely=0.3, relwidth=0.2,relheight=0.1)

    def kayittemizle():
        mystring.set("")
        mystring1.set("")
        kullanicisoyad.set("")
        kullanicitelefon.set("")
        kullanicieposta.set("")

    btn1 = Button(root,text="Temizle",command=kayittemizle,bg='black', fg='white',font=("arial",15,"bold"))
    btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)
    

background_image =PIL.Image.open("kutuphane.png")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight))
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340)      
Canvas1.config(bg="white")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#333945",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="Kütüphane Otomasyonu", fg='black',font=("Arial",30,"bold"))
headingLabel.place(relx=0.15,rely=0.1, relwidth=0.7, relheight=0.7)

btn1 = Button(root,text="Üye Girişi",bg='black', fg='white',command=uye,font=("arial",15,"bold"))
btn1.place(relx=0.25,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="Kayıt Ol",bg='black', fg='white',command=kayit,font=("arial",15,"bold"))
btn2.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)

resim=PhotoImage(file="kutuphane.png")
resim_yeni=resim.subsample(2,2)


background_label = Label(root, image=resim_yeni)
background_label.place(x=550, y=350)

def kategori():
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)


    
    table_frame=Frame(root,bd=4,relief=RIDGE,bg='#e03456')
    table_frame.place(x=300,y=170,width=900,height=480)

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)    
    kitap_table=ttk.Treeview(table_frame,columns=("Kategori İd","Kategori Adı"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=kitap_table.xview)
    scroll_x.config(command=kitap_table.yview)
    kitap_table.heading("Kategori İd",text="Kategori İd")
    kitap_table.heading("Kategori Adı",text="Kategori Adı")
    kitap_table['show']='headings'
    kitap_table.column("Kategori İd",width=450)
    kitap_table.column("Kategori Adı",width=450)
     
    kitap_table.pack()

    quitBtn = Button(root,text="<- Menüye Geri Dön",bg='#455A64', fg='white',font=("arial",15,"bold"),command=empMenu)
    quitBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)

    
def yazar():
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)


    
    table_frame=Frame(root,bd=4,relief=RIDGE,bg='#e03456')
    table_frame.place(x=300,y=170,width=900,height=480)

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)    
    kitap_table=ttk.Treeview(table_frame,columns=("Yazar İd","Adı","Soyadı"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=kitap_table.xview)
    scroll_x.config(command=kitap_table.yview)
    kitap_table.heading("Yazar İd",text="Yazar İd")
    kitap_table.heading("Adı",text="Adı")
    kitap_table.heading("Soyadı",text="Soyadı")
    kitap_table['show']='headings'
    kitap_table.column("Yazar İd",width=300)
    kitap_table.column("Adı",width=300)
    kitap_table.column("Soyadı",width=300)
     
    kitap_table.pack()

    quitBtn = Button(root,text="<- Menüye Geri Dön",bg='#455A64', fg='white',font=("arial",15,"bold"),command=empMenu)
    quitBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)


def adres():
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)


    
    table_frame=Frame(root,bd=4,relief=RIDGE,bg='#e03456')
    table_frame.place(x=300,y=170,width=900,height=480)

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)    
    kitap_table=ttk.Treeview(table_frame,columns=("Adres No","Adres Bilgisi"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=kitap_table.xview)
    scroll_x.config(command=kitap_table.yview)
    kitap_table.heading("Adres No",text="Adres No")
    kitap_table.heading("Adres Bilgisi",text="Adres Bilgisi")
    kitap_table['show']='headings'
    kitap_table.column("Adres No",width=450)
    kitap_table.column("Adres Bilgisi",width=450)
     
    kitap_table.pack()

    quitBtn = Button(root,text="<- Menüye Geri Dön",bg='#455A64', fg='white',font=("arial",15,"bold"),command=empMenu)
    quitBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)

