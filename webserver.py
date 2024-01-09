from flask import Flask, render_template
from py2neo import Graph

#Générer l'application FLASK
app = Flask(__name__)

#Etablir une connexion avec la BDD Neo4j
graph = Graph('bolt://localhost:7689', auth=('neo4j','accessgranted'))

#URL pour démarrer la session comme principale
@app.route('/')
def webserver():

	#Définir la requête pour obtenir les informations nécessaires
	query = 'MATCH (s:IP)-[r:CONNECT_TO]->(d:IP) return s, r, d'
	result = graph.run(query)
	
	#Définir les listes Nodes et Edges
	nodes = []
	edges = []
	
	for record in result:
		source = record['s']
		target = record['d']
		relation = record['r']
		#Afficher les valeurs si toutes sont affichées
		print('Source: {}, Destination: {}, Connexion: {}'.format(source,target,relation))
		
		#On ajoute les informations obtenues dans les listes
		nodes.append({'id':source['address'], 'label':source['address']})
		nodes.append({'id':target['address'], 'label':target['address']})
		edges.append({'id':source['address']+'-'+target['address'],'from':source['address'], 'to':target['addresss'],'info':relation})
		
	#On affiche les listes si elles sont remplies
	print('Nodes',nodes)
	print('Edges',edges)
	
	#On supprime les doublons pour les nodes et edges
	nodes = [dict(s) for s in set(frozenset(d.items()) for d in nodes)]
	edges = [dict(s) for s in set(frozenset(d.items()) for d in edges)]
	
	#On importe les données Nodes et Edges dans un fichier index.html avec la fonction render_template de Flask
	return render_template('index_test.html', nodes=nodes, edges=edges)
	
#On lance l'application
if __name__=='__main__':
	app.run(port=5001)
