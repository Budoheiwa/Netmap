import pyshark
from py2neo import Graph, Node, Relationship

capture = pyshark.FileCapture('capturestocker.pcap')

graph = Graph('bolt://localhost:7687', auth=('neo4j', 'accessgranted'))

graph.run('MATCH (n) DETACH DELETE n')
graph.run('MATCH ()-[r]->() DELETE r')

constraint_name = 'constraint_41aff76b'
drop_constraint_query = f'DROP CONSTRAINT {constraint_name} IF EXISTS'
graph.run(drop_constraint_query)

create_constraint_query = 'CREATE CONSTRAINT FOR (ip:IP) REQUIRE ip.address IS UNIQUE'
graph.run(create_constraint_query)

for packet in capture:
    if 'IP' in packet:
        src_ip = str(packet.ip.src)
        dst_ip = str(packet.ip.dst)
        protocol = str(packet.transport_layer)
        src_port = int(packet[protocol].srcport)
        dst_port = int(packet[protocol].dstport)

        packet_data = {'protocol': protocol, 'dst_port': dst_port}

        src_node = Node('IP', **{'address': src_ip})
        dst_node = Node('IP', **{'address': dst_ip})

        conn_rel = Relationship(src_node, 'CONNECT_TO', dst_node, **packet_data)

        graph.merge(src_node, 'IP', 'address')
        graph.merge(dst_node, 'IP', 'address')
        graph.merge(conn_rel)

capture.close()
