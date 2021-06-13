import tkinter as tk
from PIL import ImageTk
import PIL
import re
from tkinter import*
from tkinter import ttk
import mysql.connector
from datetime import datetime
from tkinter import messagebox
root = tk.Tk()
root.title("Kütüphane")


same=True
n=0.3

global uyeid


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
    kutuphane_table=ttk.Treeview(table_frame,columns=("Kütüphane İd","İsim","Adres No","Adres"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=kutuphane_table.xview)
    scroll_x.config(command=kutuphane_table.yview)
    kutuphane_table.heading("Kütüphane İd",text="Kütüphane İd")
    kutuphane_table.heading("İsim",text="İsim")
    kutuphane_table.heading("Adres No",text="Adres No")
    kutuphane_table.heading("Adres",text="Adres")
    
    kutuphane_table['show']='headings'
    kutuphane_table.column("Kütüphane İd",width=150)
    kutuphane_table.column("İsim",width=300)
    kutuphane_table.column("Adres No",width=200)
    kutuphane_table.column("Adres",width=300)
    kutuphane_table.pack()


    conn = mysql.connector.connect(user='root', password='1234',
    host='127.0.0.1',
    database='sakila')

    mycursor = conn.cursor()

    
    mycursor.execute("SELECT kutuphane_tablosu.kutuphane_id,kutuphane_tablosu.kutuphane_isim,adres_tablosu.adres_no,adres_tablosu.adres_bilgisi " \
    "FROM kutuphane_tablosu " \
    "INNER JOIN adres_tablosu ON kutuphane_tablosu.kutuphane_adres_no=adres_tablosu.adres_no")

    rows=mycursor.fetchall()

    if len(rows) !=0:
        kutuphane_table.delete(*kutuphane_table.get_children())
        for row in rows:
            kutuphane_table.insert("",END,values=row)
        conn.commit()
    conn.close()


    

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


    
    #manage_frame=Frame(root,bd=4,relief=RIDGE,bg="#e03456").place(x=20,y=100,width=500,height=560)
    #manage_title=Label(manage_frame,text="Kitap Bilgileri",fg="white",bg="#e03456",font=("times new roman",20,"bold")).place(x=25,y=110)


    kitapisbnbilgi=StringVar()
    kitapBaslik=StringVar()
    kitapYayinevi=StringVar()
    kitapkutuphaneid=StringVar()
           
            
    '''label_roll=Label(manage_frame,text="ISBN",fg="white",bg="#e03456",font=("times new roman",20,"bold")).place(x=25,y=150)
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
    
    '''    
    detail_frame=Frame(root,bd=4,relief=RIDGE,bg="#e03456").place(x=300,y=100,width=930,height=560)
    search_label=Label(detail_frame,text="Ara",bg="#e03456",fg="white",font=("times new roman",24,"bold")).place(x=320,y=105)


    vlist=["ISBN", "Yazar", "Kategori"]
    
    
    combo_search=ttk.Combobox(detail_frame,values=vlist,font=("times new roman",15,"bold"),state='readonly')
    combo_search.set("Pick an option")
    combo_search.pack(padx =5,pady=5)


    combo_search.place(x=400,y=112)



    txt_search=Entry(detail_frame,textvariable=girilen,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE).place(x=650,y=112)

    def arama():

        cnx = mysql.connector.connect(user='root', password='1234',
        host='127.0.0.1',
        database='sakila')

        cursor = cnx.cursor()

        secilen=combo_search.get()

        metin=girilen.get()
        
        if secilen == "ISBN":
            kitapgetir()
        elif secilen =="Yazar":
            yazararama()
        elif secilen =="Kategori":
            kategoriarama()

    
    def kategoriarama():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()

        #mycursor.execute("SELECT kategori_id FROM kategori_tablosu WHERE kategori_adi = '%s'" % girilen.get())

        #rows2=mycursor.fetchall()

        #for row in rows2:
        #    print("data row=(%s)" %str(row[0]))

        
        #mycursor.execute("SELECT kitap_tablosu.kitap_isbn,kitap_tablosu.kitap_baslik,kitap_tablosu.kitap_yayinevi,kitap_tablosu.kitap_kutuphane_id FROM (( kitap_tablosu INNER JOIN kategorikitap_tablosu ON kitap_tablosu.kitap_isbn=kategorikitap_tablosu.ktk_kitap_isbn) INNER JOIN kategori_tablosu ON kategorikitap_tablosu.ktk_kategori_id='%s')" %str(row[0]))




        mycursor.execute("SELECT kitap_tablosu.kitap_isbn,kitap_tablosu.kitap_baslik,kitap_tablosu.kitap_yayinevi,kitap_tablosu.kitap_kutuphane_id " \
    "FROM kitap_tablosu " \
    "INNER JOIN kategorikitap_tablosu ON kitap_tablosu.kitap_isbn=kategorikitap_tablosu.ktk_kitap_isbn " \
    "INNER JOIN kategori_tablosu ON kategorikitap_tablosu.ktk_kategori_id=kategori_tablosu.kategori_id WHERE kategori_tablosu.kategori_adi='%s'" % girilen.get())


        
        

        rows=mycursor.fetchall()

        if len(rows) !=0:
            kitap_table.delete(*kitap_table.get_children())
            for row in rows:
                kitap_table.insert("",END,values=row)
            conn.commit()
        conn.close()

        




    def yazararama():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()

        text=girilen.get()

        
        girilen_bolme=text.split(" ")


        
        mycursor.execute("SELECT yazar_id FROM yazar_tablosu WHERE yazar_ad = '%s' AND yazar_soyad = '%s'" % (girilen_bolme[0],girilen_bolme[1]))

        rows2=mycursor.fetchall()

        for row in rows2:
            print("data row=(%s)" %str(row[0]))

        mycursor.execute("SELECT kitap_tablosu.kitap_isbn,kitap_tablosu.kitap_baslik,kitap_tablosu.kitap_yayinevi,kitap_tablosu.kitap_kutuphane_id FROM ((kitap_tablosu INNER JOIN kitapyazar_tablosu ON kitap_tablosu.kitap_isbn=kitapyazar_tablosu.kty_kitap_isbn) INNER JOIN yazar_tablosu ON kitapyazar_tablosu.kty_yazar_id='%s')" % str(row[0]))

        rows=mycursor.fetchall()
        
        if len(rows) !=0:
            kitap_table.delete(*kitap_table.get_children())
            for row in rows:
                kitap_table.insert("",END,values=row)
            conn.commit()
        conn.close()


            
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
        
    
    #clearbtn=Button(button_frame,text="Temizle",command=yazitemizle,width=10,height=2).place(x=400,y=500)
    
    #addbtn=Button(button_frame,text="Ekle",command=addbook,width=10,height=2).place(x=100,y=500)

    search_button=Button(detail_frame,text="Ara",command=arama,width=10,pady=5).place(x=1000,y=112)
    show_allbtn=Button(detail_frame,text="Tüm Kitapları Göster",command=tumkitapgetir,width=15,pady=5).place(x=850,y=112)

    quitBtn = Button(root,text="<- Menüye Geri Dön",bg='#455A64', fg='white',font=("arial",15,"bold"),command=empMenu)
    quitBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)
    
    table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg='#e03456')
    table_frame.place(x=310,y=170,width=900,height=480)

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

    #yenieklenen
    manage_frame=Frame(root,bd=4,relief=RIDGE,bg="#e03456").place(x=20,y=100,width=500,height=560)
    manage_title=Label(manage_frame,text="Alınan Kitaplar",fg="white",bg="#e03456",font=("times new roman",20,"bold")).place(x=25,y=110)

    


    
    table_frame=Frame(root,bd=4,relief=RIDGE,bg='#e03456')
    table_frame.place(x=560,y=100,width=780,height=580)



    emanetNo=StringVar()

    an=datetime.now()
    alisTarihi=datetime.strftime(an, '%Y-%m-%d')


    
    teslimTarihi=StringVar()
    uyeID=StringVar()
    kitapISBN=StringVar()
    kutuphaneID=StringVar()



    #label_roll=Label(manage_frame,text="Format:Yıl-Ay-Gün",fg="white",bg="#e03456",font=("times new roman",20,"bold")).place(x=25,y=150)
    #txt_roll=Entry(manage_frame,bd=5,relief=GROOVE,textvariable=emanetNo,font=("times new roman",15,"bold")).place(x=200,y=150)

    label_roll=Label(manage_frame,text="ISBN",bg="#e03456",fg="white",font=("times new roman",20,"bold")).place(x=25,y=200)
    txt_roll=Entry(manage_frame,bd=5,relief=GROOVE,textvariable=kitapISBN,font=("times new roman",15,"bold")).place(x=200,y=200)

    #label_roll=Label(manage_frame,text="Alış Tarihi",bg="#e03456",fg="white",font=("times new roman",20,"bold")).place(x=25,y=250)
    #txt_roll=Entry(manage_frame,bd=5,relief=GROOVE,textvariable=alisTarihi,font=("times new roman",15,"bold")).place(x=200,y=250)

    #label_roll=Label(manage_frame,text="Teslim Tarihi",bg="#e03456",fg="white",font=("times new roman",20,"bold")).place(x=25,y=300)
    #txt_roll=Entry(manage_frame,bd=5,relief=GROOVE,textvariable=teslimTarihi,font=("times new roman",15,"bold")).place(x=200,y=300)



    button_frame=Frame(manage_frame,bd=4,relief=RIDGE, bg="#e03456").place(x=10,y=480,width=430)
    #addbtn=Button(button_frame,text="Ekle",command=addkitap,width=10,height=2).place(x=100,y=500)
    #updatebtn=Button(button_frame,text="Güncelle",command=alinankitapGuncelle,width=10,height=2).place(x=200,y=500)
    #deletebtn=Button(button_frame,text="Sil",command=alinankitapSil,width=10,height=2).place(x=300,y=500)
    #clearbtn=Button(button_frame,text="Temizle",command=alinanSil,width=10,height=2).place(x=400,y=500)




    

    
    

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)    
    kitap_table=ttk.Treeview(table_frame,columns=("Emanet No","Alış Tarihi","Teslim Tarihi","Üye İd","ISBN","Kütüphane İd","Kitap Adı","Yazar Adı","Yazar Soyadı","Kütüphane Adı"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
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
    kitap_table.heading("Kitap Adı",text="Kitap Adı")
    kitap_table.heading("Yazar Adı",text="Yazar Adı")
    kitap_table.heading("Yazar Soyadı",text="Yazar Soyadı")
    kitap_table.heading("Kütüphane Adı",text="Kütüphane Adı")
    kitap_table['show']='headings'
    kitap_table.column("Emanet No",width=100)
    kitap_table.column("Alış Tarihi",width=100)
    kitap_table.column("Teslim Tarihi",width=100)
    kitap_table.column("Üye İd",width=70)
    kitap_table.column("ISBN",width=60)
    kitap_table.column("Kütüphane İd",width=90)
    kitap_table.column("Kitap Adı",width=100)
    kitap_table.column("Yazar Adı",width=100)
    kitap_table.column("Yazar Soyadı",width=100)
    kitap_table.column("Kütüphane Adı",width=100)
     
    kitap_table.pack()
    #kitap_table.bind("<ButtonRelease-1>",kitap_getCursor)
    #alinankitabi_getir()

    quitBtn = Button(root,text="<- Menüye Geri Dön",bg='#455A64', fg='white',font=("arial",15,"bold"),command=empMenu)
    quitBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)



    

    def addkitap():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()
        #sql2="select uyeler.uye_id,alinan_kitaplar.kutuphane_id from uyeler INNER JOIN alinan_kitaplar on uyeler.uye_id=alinan_kitaplar.uye_id"
        #sql="select from uyeler,kutuphaneler,uye-kutuphane where uye-kutuphane.uye_id=uyeler.uye_id and uye-kutuphane.kutuphane_id=kutuphaneler.kutuphane_id"
        #mycursor.execute(sql2)
        #sql="insert into alinan_kitaplar (alis_tarihi,teslim_tarihi,uye_id,isbn,kutuphane_id) select (uye_id,kutuphane_id) from uye-kutuphane where uye-kutuphane.uye_id=alinan_kitaplar.uye_id and uye-kutuphane.kutuphane_id=alinan_kitaplar.kutuphane_id"
        #sql="(insert into (uye_id,isbn,alis_tarihi,teslim_tarihi,kutuphane_id) select from alinan_kitaplar where uye_id=%s and kutuphane_id=%s)"


        mycursor.execute("SELECT ADDDATE('%s', INTERVAL 2 MONTH)" % alisTarihi)

        degisken=mycursor.fetchall()

        for row in degisken:
            teslimtarihi=str(row[0])


        mycursor.execute("SELECT kitap_kutuphane_id FROM kitap_tablosu WHERE kitap_isbn='%s'" % kitapISBN.get())

        degisken2=mycursor.fetchall()

        for row in degisken2:
            kutuphaneid=str(row[0])



        sql="insert into alinan_tablosu (alinan_uye_id,alinan_kitap_isbn,alinan_alis_tarihi,alinan_teslim_tarihi,alinan_kutuphane_id) values (%s,%s,%s,%s,%s)"
        val=(uyeid,kitapISBN.get(),alisTarihi,teslimtarihi,kutuphaneid)
        mycursor.execute(sql,val)




        mycursor.execute("SELECT alinan_emanet_no FROM alinan_tablosu WHERE alinan_kitap_isbn='%s'" % kitapISBN.get())

        rows=mycursor.fetchall()

        for row in rows:
            emanetnosu=str(row[0])


        sqlkomut="INSERT INTO uyekitap_tablosu (uye_id,emanet_no) VALUES (%s,%s)"
        val=(uyeid,emanetnosu)
        mycursor.execute(sqlkomut,val)


        

        conn.commit()
        alinankitabi_getir()
        conn.close()

    def alinankitabi_getir():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()

        mycursor.execute("SELECT alinan_tablosu.alinan_emanet_no,alinan_tablosu.alinan_alis_tarihi,alinan_tablosu.alinan_teslim_tarihi,alinan_tablosu.alinan_uye_id,alinan_tablosu.alinan_kitap_isbn,alinan_tablosu.alinan_kutuphane_id,kitap_tablosu.kitap_baslik,yazar_tablosu.yazar_ad,yazar_tablosu.yazar_soyad,kutuphane_tablosu.kutuphane_isim " \
      "FROM alinan_tablosu INNER JOIN kitap_tablosu ON alinan_tablosu.alinan_kitap_isbn=kitap_tablosu.kitap_isbn " \
      "INNER JOIN kitapyazar_tablosu ON kitap_tablosu.kitap_isbn=kitapyazar_tablosu.kty_kitap_isbn " \
      "INNER JOIN yazar_tablosu ON kitapyazar_tablosu.kty_yazar_id=yazar_tablosu.yazar_id " \
      "INNER JOIN kutuphane_tablosu ON kitap_tablosu.kitap_kutuphane_id=kutuphane_tablosu.kutuphane_id WHERE alinan_tablosu.alinan_uye_id='%s'" % uyeid)


        rows=mycursor.fetchall()
        if len(rows) !=0:
                kitap_table.delete(*kitap_table.get_children())
        for row in rows:
                kitap_table.insert("",END,values=row)



        conn.commit()
        conn.close()

    def kitap_getCursor(root):
        cursor_row=kitap_table.focus()
        veriler=kitap_table.item(cursor_row)
        row=veriler['values']
        kitapISBN.set(row[2])
        alisTarihi.set(row[3])
        teslimTarihi.set(row[4])

    #def alinankitapSil():
    #    conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
    #    mycursor=conn.cursor()
    #    mycursor.execute("delete from alinan_tablosu where alinan_kitap_isbn=%s",[kitapISBN.get()])
    #    conn.commit()
    #    alinankitabi_getir()
    #    alinanSil()
    #    conn.close()
    
    #def alinankitapGuncelle():
    #    conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
    #    mycursor=conn.cursor()
    #    mycursor.execute("update alinan_tablosu set alinan_emanet_no=%s,alinan_uye_id=%s,alinan_alis_tarihi=%s,alinan_teslim_tarihi=%s,alinan_kutuphane_id=%s where alinan_kitap_isbn=%s",(1,45,alisTarihi.get(),teslimTarihi.get(),1,kitapISBN.get()))
    #    conn.commit()
    #    alinankitabi_getir()
    #    conn.close()
    
    def alinanSil():
        kitapISBN.set("")
        alisTarihi.set("")
        teslimTarihi.set("")



    kitap_table.bind("<ButtonRelease-1>",kitap_getCursor)
    alinankitabi_getir()
    

    addbtn=Button(button_frame,text="Ekle",command=addkitap,width=10,height=2).place(x=100,y=500)    
    #updatebtn=Button(button_frame,text="Güncelle",command=alinankitapGuncelle,width=10,height=2).place(x=200,y=500)
    #deletebtn=Button(button_frame,text="Sil",command=alinankitapSil,width=10,height=2).place(x=300,y=500)
    clearbtn=Button(button_frame,text="Temizle",command=alinanSil,width=10,height=2).place(x=400,y=500)




def kitapIade():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1,kitapIsbn,kitapBaslik,kitapYayinevi,kitapIade_table
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)


    manage_frame=Frame(root,bd=4,relief=RIDGE,bg="#e03456").place(x=450,y=10,width=600,height=100)
    manage_title=Label(manage_frame,text="İade edilecek kitabın ISBN bilgisini giriniz.",fg="white",bg="#e03456",font=("times new roman",20,"bold")).place(x=455,y=15)

    kitapIsbn=StringVar()

    txt_roll=Entry(manage_frame,bd=5,relief=GROOVE,textvariable=kitapIsbn,font=("times new roman",15,"bold")).place(x=620,y=55)

    

    
        
    
    table_frame=Frame(root,bd=4,relief=RIDGE,bg='#e03456')
    table_frame.place(x=300,y=100,width=900,height=580)

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)    
    kitapIade_table=ttk.Treeview(table_frame,columns=("Üye İd","Üye Adı","Üye Soyadı","ISBN","Kitap Adı"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=kitapIade_table.xview)
    scroll_x.config(command=kitapIade_table.yview)
    #kitapIade_table.heading("Id",text="Id")
    kitapIade_table.heading("Üye İd",text="Üye İd")
    kitapIade_table.heading("Üye Adı",text="Üye Adı")
    kitapIade_table.heading("Üye Soyadı",text="Üye Soyadı")
    kitapIade_table.heading("ISBN",text="ISBN")
    kitapIade_table.heading("Kitap Adı",text="Kitap Adı")
    kitapIade_table['show']='headings'
    #kitapIade_table.column("Id",width=145)
    kitapIade_table.column("Üye İd",width=145)
    kitapIade_table.column("Üye Adı",width=145)
    kitapIade_table.column("Üye Soyadı",width=145)
    kitapIade_table.column("ISBN",width=145)
    kitapIade_table.column("Kitap Adı",width=145)
    #Iadekitabi_getir()
    kitapIade_table.pack()

    #iadeBtn = Button(root,text="İade Et",bg='#455A64', fg='white',font=("arial",15,"bold"),command=kitapTeslim)
    #iadeBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    
    #quitBtn = Button(root,text="<- Menüye Geri Dön",bg='#455A64', fg='white',font=("arial",15,"bold"),command=empMenu)
    #quitBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)

    def Iadekitabi_getir():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()
        mycursor.execute("SELECT uyekitap_tablosu.uye_id,uye_tablosu.uye_adi,uye_tablosu.uye_soyadi,alinan_tablosu.alinan_kitap_isbn,kitap_tablosu.kitap_baslik " \
    "FROM uyekitap_tablosu " \
    "INNER JOIN alinan_tablosu ON uyekitap_tablosu.emanet_no=alinan_tablosu.alinan_emanet_no " \
    "INNER JOIN uye_tablosu ON uyekitap_tablosu.uye_id=uye_tablosu.uye_id " \
    "INNER JOIN kitap_tablosu ON alinan_tablosu.alinan_kitap_isbn=kitap_tablosu.kitap_isbn WHERE uyekitap_tablosu.uye_id='%s'" % uyeid)
        rows=mycursor.fetchall()
        if len(rows) !=0:
            kitapIade_table.delete(*kitapIade_table.get_children())
            for row in rows:
                kitapIade_table.insert("",END,values=row)

        #if len(rows) ==0:
        #    teksilme()

        def teksilme():

            kitapIade_table.delete(*kitapIade_table.get_children())

            value=[' ',' ',' ',' ',' ']

            for row in value:
                kitapIade_table.insert("",END,values=row)

        if len(rows) ==0:
            teksilme()

        
        conn.commit()
        conn.close()

    Iadekitabi_getir()
    
    #def teksilme():
    #
    #   kitapIade_table.delete(*kitapIade_table.get_children())
    #
    #    value=[' ',' ',' ',' ',' ']
    #
    #   for row in value:
    #        kitapIade_table.insert("",END,values=row)

        
        




    def kitapTeslim():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()

        mycursor.execute("SELECT alinan_emanet_no FROM alinan_tablosu WHERE alinan_kitap_isbn='%s'" % kitapIsbn.get())

        rows2=mycursor.fetchall()

        for row in rows2:
            emanetno=str(row[0])

        
        
        mycursor.execute("delete from uyekitap_tablosu where emanet_no='%s'" % emanetno)
        #rows=mycursor.fetchall()
        #if len(rows) !=0:
        #    kitapIade_table.delete(*kitapIade_table.get_children())


        mycursor.execute("delete from alinan_tablosu where alinan_uye_id=%s AND alinan_kitap_isbn=%s",(uyeid,kitapIsbn.get()))
    
        conn.commit()
        Iadekitabi_getir()
        conn.close()
    
    iadeBtn = Button(root,text="İade Et",bg='#455A64', fg='white',font=("arial",15,"bold"),command=kitapTeslim)
    iadeBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    
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



    btn6=Button(root,text="Kitap İade",bg='black', fg='white',font=("arial",15,"bold"),command=kitapIade)
    btn6.place(relx=0.28,rely=0.85, relwidth=0.45,relheight=0.1)

    backBtn = Button(root,text="<- Geri",bg='#455A64', fg='white',font=("arial",15,"bold"), command=uye)
    backBtn.place(relx=0.8,rely=0.9, relwidth=0.18,relheight=0.08)
    


    
    #backBtn = Button(root,text="<- Geri",bg='#455A64', fg='white',font=("arial",15,"bold"), command=uye)
    #backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)


def quit():
    root.destroy()




def uye():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    #global uyeid
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


    def giris():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()
        mycursor.execute("select uye_adi,uye_mail from uye_tablosu")
        rows=mycursor.fetchall()

        for row in rows:
            if(row[0]==kuladkontrol.get() and row[1]==kulmailkontrol.get()):
                return True

            conn.commit()
        conn.close()




    

    def kontrol():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()

        val=(kuladkontrol.get())
        val2=(kulmailkontrol.get())
        
        print(val)
        sql="SELECT uye_adi FROM uye_tablosu WHERE uye_adi = '%s'" % val

        sqls="SELECT uye_mail FROM uye_tablosu WHERE uye_mail = '%s'" % val2
        mycursor.execute(sql)
        rows=mycursor.fetchall()


        for row in rows:
            uyeadi=str(row[0])


        mycursor.execute(sqls)
        uyemail=mycursor.fetchall()



        sqll="SELECT uye_id FROM uye_tablosu WHERE uye_adi='%s' AND uye_mail='%s'" % (val,val2)

        mycursor.execute(sqll)

        uyeidokuma=mycursor.fetchall()

        for row in uyeidokuma:
            globals()['uyeid'] = str(row[0])



        print(uyeid)

        
        if uyeadi == '%s' % val and uyemail == [('%s' % val2,)]:
            empMenu()        


        #if uyeadi == [('%s' % val,)] and uyemail == [('%s' % val2,)]:
        #    empMenu()
        
        conn.close()


    def menuyegiris():
        if(giris()):
            kontrol()
        else:
            messagebox.showwarning("Hata","Giriş başarısız!")
        
    
    btn2 = Button(root,text="Giriş Yap",command=menuyegiris,bg='#455A64', fg='white',font=("arial",15,"bold"))
    btn2.place(relx=0.30,rely=0.8, relwidth=0.18,relheight=0.08)
    
    btn3 = Button(root,text="Çık",bg='#455A64', fg='white',font=("arial",15,"bold"),command=quit)
    btn3.place(relx=0.53,rely=0.8, relwidth=0.18,relheight=0.08)



#print(uyeid)

def kayit():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    
    Canvas1 = Canvas(root)

    uyead= StringVar()
    uyesoyad= StringVar()
    uyetelefon= StringVar()
    uyeeposta= StringVar()
    uyeadres= StringVar()

    


    Canvas1.config(bg="#FFF9C4",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Yeni Üye", fg='black',font=("arial",30,"bold"))
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)

    lbl_ad=Label(root,text="Ad",font=("Goudy old style",20,"bold"),fg='gray',bg="white").place(x=400,y=350)
    Entry(root,textvariable=uyead,font=('times new roman',15),bg='lightgray').place(x=550,y=350,width=350,height=35)
    

    
    lbl_soyad=Label(root,text="Soyad",font=("Goudy old style",20,"bold"),fg='gray',bg="white").place(x=400,y=410)
    txt_soyad=Entry(root,textvariable=uyesoyad,font=('times new roman',15),bg='lightgray').place(x=550,y=410,width=350,height=35)

    lbl_telefon=Label(root,text="Telefon",font=("Goudy old style",20,"bold"),fg='gray',bg="white").place(x=400,y=470)
    txt_telefon=Entry(root,textvariable=uyetelefon,font=('times new roman',15),bg='lightgray').place(x=550,y=470,width=350,height=35)

    lbl_eposta=Label(root,text="E-posta",font=("Goudy old style",20,"bold"),fg='gray',bg="white").place(x=400,y=530)
    txt_eposta=Entry(root,textvariable=uyeeposta,font=('times new roman',15),bg='lightgray').place(x=550,y=530,width=350,height=35)

    lbl_adres=Label(root,text="Adres",font=("Goudy old style",20,"bold"),fg='gray',bg="white").place(x=400,y=590)
    txt_adres=Entry(root,textvariable=uyeadres,font=('times new roman',15),bg='lightgray').place(x=550,y=590,width=350,height=35)


    def checkUser():

        if len(uyeeposta.get())>7:
            if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",uyeeposta.get()):
                return True
            else:
                messagebox.showwarning("Uyarı","Geçersiz mail")
                return False
    
    
        if uyead.get() == '':
            messagebox.showerror("Hata","Kullanıcı adı alanı boş bırakılamaz")
        elif uyesoyad.get() == '':
            messagebox.showerror("Hata","Kullanıcı soyad alanı boş bırakılamaz")
        elif not(uyetelefon.get().isdigit()):
            messagebox.showerror("Hata","Telefon alanı numara olamlıdır")
        elif uyetelefon.get() == '':
            messagebox.showerror("Hata","Kullanıcı id alanı numara olmalıdır")
        elif len(uyetelefon.get())!= 11:
             messagebox.showerror("Hata","Telefon alanı 11 karakter içermelidir")
        elif uyeeposta.get() == '':
            messagebox.showerror("Hata","Mail alanı boş bırakılamaz")
        elif uyeadres.get() == '':
            messagebox.showerror("Hata","Adres alanı boş bırakılamaz")
         
        else:
            messagebox.showinfo("Uyarı","Mail çok kısa")



   
    
    btn3 = Button(root,text="Çık",bg='#455A64', fg='white',command=quit,font=("arial",15,"bold"))
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    backBtn = Button(root,text="<- Geri",bg='#455A64', fg='white',font=("arial",15,"bold"), command=uye)
    backBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)




    def verikontrol():

        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()
        mycursor.execute("select uye_mail from uye_tablosu")
        rows=mycursor.fetchall()

        for row in rows:
            if((row[0]==uyeeposta.get())):
                messagebox.showerror("Hata",uyeeposta.get() + " mail adresi sistemde mevcut")
                return False
                
                

        if(checkUser()):
            addkayit()
            messagebox.showinfo("Geçerli","Kayıt Başarılı")




        

    
    def addkayit():
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="sakila")
        mycursor=conn.cursor()
        sql="insert into uye_tablosu (uye_adi,uye_soyadi,uye_tel,uye_mail,uye_adres_no) values (%s,%s,%s,%s,%s)"
        val=(uyead.get(),uyesoyad.get(),uyetelefon.get(),uyeeposta.get(),uyeadres.get())
        mycursor.execute(sql,val)
        conn.commit()

        conn.close()

    btn2 = Button(root,text="Kaydet",command=verikontrol,bg='black', fg='white',font=("arial",15,"bold"))
    btn2.place(relx=0.53,rely=0.3, relwidth=0.2,relheight=0.1)

    def kayittemizle():
        uyead.set("")
        uyesoyad.set("")
        uyetelefon.set("")
        uyeeposta.set("")
        uyeadres.set("")

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


    conn = mysql.connector.connect(user='root', password='1234',
    host='127.0.0.1',
    database='sakila')

    mycursor = conn.cursor()

    
    mycursor.execute("SELECT * FROM kategori_tablosu")
    rows=mycursor.fetchall()

    if len(rows) !=0:
        kitap_table.delete(*kitap_table.get_children())
        for row in rows:
            kitap_table.insert("",END,values=row)
        conn.commit()
    conn.close()



    

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


    conn = mysql.connector.connect(user='root', password='1234',
    host='127.0.0.1',
    database='sakila')

    mycursor = conn.cursor()

    
    mycursor.execute("SELECT * FROM yazar_tablosu")
    rows=mycursor.fetchall()

    if len(rows) !=0:
        kitap_table.delete(*kitap_table.get_children())
        for row in rows:
            kitap_table.insert("",END,values=row)
        conn.commit()
    conn.close()


    

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


    conn = mysql.connector.connect(user='root', password='1234',
    host='127.0.0.1',
    database='sakila')

    mycursor = conn.cursor()

    
    mycursor.execute("SELECT * FROM adres_tablosu")
    rows=mycursor.fetchall()

    if len(rows) !=0:
        kitap_table.delete(*kitap_table.get_children())
        for row in rows:
            kitap_table.insert("",END,values=row)
        conn.commit()
    conn.close()
    

    quitBtn = Button(root,text="<- Menüye Geri Dön",bg='#455A64', fg='white',font=("arial",15,"bold"),command=empMenu)
    quitBtn.place(relx=0.3,rely=0.9, relwidth=0.18,relheight=0.08)

