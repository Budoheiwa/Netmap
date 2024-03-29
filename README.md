# Requirements

Before using the Network mapping project, you need some **requirements**:
- Install Kali Linux OS [https://www.kali.org/get-kali/](https://www.kali.org/get-kali/#kali-platforms).

- Make sure that all is update with the command: 
```
sudo apt update && sudo apt upgrade
```
> Especially Python language

- To be sure that **Python has the best version**, you can see its version with `which python3` in the **terminal**.

> The final thing is to **logout and in again**

- Install Neo4j Graph Database Desktop [https://neo4j.com/download/](https://neo4j.com/download/)
> For further information about how to install the software, there is a manual for each OS [neo4j-desktop-manual](https://neo4j.com/docs/desktop-manual/current/installation/download-installation/)

After installing, you need to configure the **DBMS (Database Management System)**. It allows you to connect to its server, store data and display them by graph:

![image](https://github.com/Budoheiwa/network-mapping-neo4j/assets/156065416/3e09dba9-857a-4790-976d-ceccffe86fd0)
> It is essential that you set up the right **bolt port number** and **https port number**.

# How to use Network mapping project

First you need to enable the DBMS from Neo4j Desktop interface. Then go to folder **network-mapping-neo4j** and use the python script `capture.py` to sniff packets. But before that, in a terminal, use the command:
```
ip a
ifconfig
```
> It allows you to see which **network interfaces** you want to use to sniff packets in your current network.

Make sure to enter your network interface in the interface list of `capture.py`.

![image](https://github.com/Budoheiwa/network-mapping-neo4j/assets/156065416/6b2b7653-8dac-4e21-a452-67cd720752ac)
To run the script, do:
```
sudo chmod +x capture.py
sudo python3 capture.py
```
Then in `bdd_graph.py`, make sure to put the correct **url link** to connect to **Neo4j Database** and **credentials for authentification**.
![image](https://github.com/Budoheiwa/network-mapping-neo4j/assets/156065416/6bdc4252-c546-40d3-8563-a65d6a1b5c1c)

To run the script, do:
```
sudo chmod +x bdd_graph.py
sudo python3 bdd_graph.py
```
Then run the python script `webserver.py`:
```
sudo chmod +x webserver.py
sudo python3 webserver.py
```
> This allows you to create a webserver, run it and display data from Neo4j database with a **graphical interface**.

![image](https://github.com/Budoheiwa/network-mapping-neo4j/assets/156065416/98d00e68-ae17-4f0e-85c2-4fd2095e2bca)
![image](https://github.com/Budoheiwa/network-mapping-neo4j/assets/156065416/1e3f28c1-0ef6-4aba-8935-de8bc9094a57)
Make sure to enter the right **credentials** for connecting to Neo4j Database, and define at **which port** the webserver runs to. 

