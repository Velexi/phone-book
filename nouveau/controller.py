from model import Model

class Controller():
	def __init__(self):
		self.s=''

	def re(n,p,t,ad,v):
		a = Model()
		s=n.get()
		a.chercher_details(s)
		p.insert(0,a.annuaire_dict[s]["prenom"])
		t.insert(0,a.annuaire_dict[s]["telephone"])
		ad.insert(0,a.annuaire_dict[s]["adresse"])
		v.insert(0,a.annuaire_dict[s]["ville"])
		
		
		
	def delete_fields(n,p,t,a,v):
		n.delete(0,100)
		p.delete(0,100)
		t.delete(0,100)
		a.delete(0,100)
		v.delete(0,100)
	
	def insert(n,p,ad,v,t):
		a = Model()

		nom=n.get()
		prenom=p.get()
		adresse=ad.get()
		ville=v.get()
		telephone=t.get()
		
		a.ajouter_personne(nom,prenom,adresse,ville,telephone)
	



