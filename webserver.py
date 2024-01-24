from flask import Flask, render_template
from py2neo import Graph

app = Flask(__name__)

graph = Graph('bolt://localhost:7687', auth=('neo4j','accessgranted'))

@app.route('/')
def webserver():

	query = 'MATCH (s:IP)-[r:CONNECT_TO]->(d:IP) return s, r, d'
	result = graph.run(query)
	
	nodes = []
	edges = []
	
	for record in result:
		source = record['s']
		target = record['d']
		relation = record['r']
		print('Source: {}, Destination: {}, Connexion: {}'.format(source,target,relation))
		
		nodes.append({'id':source['address'], 'label':source['address']})
		nodes.append({'id':target['address'], 'label':target['address']})
		edges.append({'id':source['address']+'-'+target['address'],'from':source['address'], 'to':target['address'],'info':relation})
		
	print('Nodes',nodes)
	print('Edges',edges)
	
	nodes = [dict(s) for s in set(frozenset(d.items()) for d in nodes)]
	edges = [dict(s) for s in set(frozenset(d.items()) for d in edges)]
	
	return render_template('index_cyber.html', nodes=nodes, edges=edges)
	
if __name__=='__main__':
	app.run(port=5001)
