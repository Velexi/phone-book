from tkinter import *
from tkinter import ttk  
from controller import Controller

root=Tk()
root.title("Annuaire")
root.geometry("550x250")

lblNom = Label(root, text="Nom :", font = ("Arial",12))
lblNom.place(x=5, y=50, width=125)
nom=StringVar()
saisieNom = Entry(root, textvariable=nom)
saisieNom.place(x=140, y=50, width=175)

#Label Prenom
lblPrenom = Label(root, text="Prenom :", font = ("Arial",12))
lblPrenom.place(x=5, y=75, width=125)
prenom=StringVar()
saisiePrenom = Entry(root, textvariable=prenom)
saisiePrenom.place(x=140, y=75, width=175)

#Label Telephone
lblTelephone = Label(root, text="Telephone :", font = ("Arial",12))
lblTelephone.place(x=5, y=100, width=125)
telephone=StringVar()
saisieTelephone = Entry(root, textvariable=telephone)
saisieTelephone.place(x=140, y=100, width=175)

#Label Adresse
lblAdresse = Label(root, text = "Adresse :", font = ("Arial",12))
lblAdresse.place(x=5, y=125, width=125)
adresse=StringVar()
saisieAdresse = Entry(root, textvariable=adresse)
saisieAdresse.place(x=140, y=125, width=350)

#Label Ville
lblVille = Label(root, text = "Ville :", font = ("Arial",12))
lblVille.place(x=5, y=150,width=125)
ville=StringVar()
saisieVille = Entry(root, textvariable=ville)
saisieVille.place(x=140, y=150, width=175)

#Bouton Chercher
btnChercher = Button(root, text = "Chercher", command = lambda: Controller.re(nom,saisiePrenom,saisieTelephone,saisieAdresse,saisieVille))
btnChercher.place(x=160, y=185)

#Bouton Inserer
btnInserer = Button(root, text = "Inserer", command = lambda: Controller.insert(saisieNom,saisiePrenom,saisieAdresse,saisieVille,saisieTelephone))
btnInserer.place(x=250, y=185)

#Bouton Effacer
btnEffacer = Button(root, text ="Effacer", command = lambda: Controller.delete_fields(saisieNom,saisiePrenom,saisieTelephone,saisieAdresse,saisieVille))
btnEffacer.place(x=325, y=185)

root.mainloop()
