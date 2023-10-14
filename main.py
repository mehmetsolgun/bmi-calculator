from tkinter import *

window = Tk()
window.title("Vücut-Kitle Endeksi Hesaplama")
window.minsize(width=400, height=400)
window.config(pady= 20)
header = Label(text="Vücut-Kitle Endeksi Hesaplama",font=("Cooper Black", 15, "normal"), pady=20)
header.pack()

def clickbutton():
    kg= kginput.get()
    boy= boyinput.get()
    try:
        kg= int(kg)
        boy= int(boy)
        boy = boy / 100
        bmihesapla = kg / (boy * boy)

        if kg == "":
            sonuc.config(text="Lütfen kilonuzu giriniz.")
        if boy == "":
            sonuc.config(text="Lütfen boyunuzu giriniz.")
        if boy and kg == "":
            sonuc.config(text="Lütfen boyunuzu ve kilonuzu giriniz.")

        if bmihesapla <= 18.5:
            sonuc.config(text=f"V-K Endeksiniz: {bmihesapla:.2f}, Zayıf")
        elif 18.5 < bmihesapla < 25:
            sonuc.config(text=f"V-K Endeksiniz: {bmihesapla:.2f}, Normal kilolu ")
        elif 25 <= bmihesapla < 30:
            sonuc.config(text=f"V-K Endeksiniz: {bmihesapla:.2f}, Fazla kilolu ")
        elif 30 <= bmihesapla < 35:
            sonuc.config(text=f"V-K Endeksiniz: {bmihesapla:.2f}, Obez (1. derece) ")
        elif 35 <= bmihesapla < 40:
            sonuc.config(text=f"V-K Endeksiniz: {bmihesapla:.2f}, Aşırı obez (2. derece)")
        elif 40 <= bmihesapla:
            sonuc.config(text=f"V-K Endeksiniz: {bmihesapla:.2f}, Morbid obez (3. derece) ")
    except:
        sonuc.config(text="Lütfen kilo ve boyu sayı cinsinden giriniz.")







kgtext = Label(text="Kilo (kg):", font=("Arial", 15, "normal"), pady=10)
kgtext.pack()

kginput = Entry()
kginput.pack()

boytext = Label(text="Boy (cm):", font=("Arial", 15, "normal"), pady=10)
boytext.pack()

boyinput= Entry()
boyinput.pack()

hesapla= Button(text="Hesapla", pady=10, width=16, height=1,bg="black",fg="white", command= clickbutton)
hesapla.pack()



sonuc = Label(pady=10, font=("Arial", 15, "normal"))

sonuc.pack()

ben = Label(pady=30, text="Mehmet Solgun",font=("Chiller", 20, "normal"))
ben.pack()

window.mainloop()