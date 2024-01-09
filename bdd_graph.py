import pyshark
from py2neo import Graph, Node, Relationship

#Ouvrir le fichier pcap avec PyShark
capture = pyshark.FileCapture('capturestocker.pcap')

#Initialiser la base de données Neo4j
graph = Graph('bolt://localhost:7689', auth=('neo4j','accessgranted'))

#Supprimer les noeuds et relations de l'ancienne BDD
graph.run('MATCH (n) DETACH DELETE n')
graph.run('MATCH ()-[r]->() DELETE r')

#Supprimer la contrainte existante avant de la recréer
graph.run('DROP CONSTRAINT constraint_41aff76b')

#Définir la contrainte d'unicité sur l'étiquette "IP" et la propriété "address"
graph.run('CREATE CONSTRAINT FOR (ip:IP) REQUIRE ip.address IS UNIQUE')

for packet in capture:
	if 'IP' in packet:
		#Extraction des informations pertinentes
		src_ip = str(packet.ip.src)
		dst_ip = str(packet.ip.dst)
		protocol = str(packet.transport_layer)
		src_port = int(packet[protocol].srcport)
		dst_port = int(packet[protocol].dstport)
		
		#Création d'un dictionnaire pour sstocker les données
		packet_data = {'protocol': protocol, 'dst_port' : dst_port}
		
		#Création des noeuds pour les adresses IP source et destination
		src_node = Node('IP', **{'address': src_ip})
		dst_node = Node('IP', **{'address': dst_ip})
		
		#Création de la relation CONNECT_TO entre les noeuds
		conn_rel = Relationship(src_node, 'CONNECT_TO', dst_node, **packet_data)
		
		#Ajout des noeuds et de la relation à la BDD Neo4j
		graph.merge(src_node, 'IP', 'address')
		graph.merge(dst_node, 'IP', 'address')
		graph.merge(conn_rel)
	
#Fermer la capture de paquets
capture.close()
		
		

