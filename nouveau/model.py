

class Model():
	def __init__(self):
		self.annuaire_dict = {
			"Jones" : {
				"prenom": "Don",
				"adresse": "1 Rue Rivoli",
				"telephone": "0800838383", 
				"ville": "Paris"
			}
		}
	
	def chercher_details(self,nom):
		for key, value in self.annuaire_dict[nom].items():
        		print(f'{key}: {value}')

	def ajouter_personne(self,nom,prenom,adresse,ville,telephone):
		self.annuaire_dict.update({nom : {"prenom": prenom, "adresse": adresse, "ville": ville, "telephone": ville}})




