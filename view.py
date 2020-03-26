from tkinter import *
from tkinter import ttk  

class View(Frame):
	def __init__(self,master):
		self.master = master
		self.load_ui()
	
	def load_ui(self):
		#Label Nom
		self.lblNom = Label(root, text="Nom :", font = ("Arial",12))
		self.lblNom.place(x=5, y=50, width=125)
		self.saisieNom = Entry(root)
		self.saisieNom.place(x=140, y=50, width=175)

		#Label Prenom
		self.lblPrenom = Label(root, text="Prenom :", font = ("Arial",12))
		self.lblPrenom.place(x=5, y=75, width=125)
		self.saisiePrenom = Entry(root)
		self.saisiePrenom.place(x=140, y=75, width=175)

		#Label Telephone
		self.lblTelephone = Label(root, text="Telephone :", font = ("Arial",12))
		self.lblTelephone.place(x=5, y=100, width=125)
		self.saisieTelephone = Entry(root)
		self.saisieTelephone.place(x=140, y=100, width=175)

		#Label Adresse
		self.lblAdresse = Label(root, text = "Adresse :", font = ("Arial",12))
		self.lblAdresse.place(x=5, y=125, width=125)
		self.saisieAdresse = Entry(root)
		self.saisieAdresse.place(x=140, y=125, width=350)

		#Label Ville
		self.lblVille = Label(root, text = "Ville :", font = ("Arial",12))
		self.lblVille.place(x=5, y=150,width=125)
		self.saisieVille = Entry(root)
		self.saisieVille.place(x=140, y=150, width=175)

		#Bouton Chercher
		self.btnChercher = Button(root, text = "Chercher")
		self.btnChercher.place(x=160, y=185)

		#Bouton Inserer
		self.btnInserer = Button(root, text = "Inserer")
		self.btnInserer.place(x=250, y=185)

		#Bouton Effacer
		self.btnEffacer = Button(root, text ="Effacer")
		self.btnEffacer.place(x=325, y=185)


if __name__ == "__main__":
	root = Tk()
	root.title("Annuaire")
	root.geometry("550x250")
	v = View(root)
	root.mainloop()
