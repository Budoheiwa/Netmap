# Requirements

Before using the Network mapping project, you need some **requirements**:
- Install Kali Linux OS [https://www.kali.org/get-kali/](https://www.kali.org/get-kali/#kali-platforms).

- Make sure that all is update with the command: 
```
sudo apt update && sudo apt upgrade
```
> Especially Python language

- To be sure that **Python has the best version**, you can see its version with `which python3` in the **terminal**.

- Install docker with the command:
```
sudo apt install -y docker.io
sudo systemctl enable docker --now
```
> Now you can get started with using docker, with sudo.

- If you want to add yourself to the docker group to use docker without sudo, an additional step is needed:
```
sudo usermod -aG docker $USER
```
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
> It allows you to see which network interfaces you want to use to sniff packets in your current network.

Make sure to enter your network interface in the interface list of `capture.py`.

![image](https://github.com/Budoheiwa/network-mapping-neo4j/assets/156065416/6b2b7653-8dac-4e21-a452-67cd720752ac)
To run the script, do:
```
sudo chmod +x capture.py
sudo python3 capture.py
```
Then in `bdd_graph.py`, make sure to put the correct url link to connect to Neo4j Database and credentials for authentification.
![image](https://github.com/Budoheiwa/network-mapping-neo4j/assets/156065416/6bdc4252-c546-40d3-8563-a65d6a1b5c1c)

To run the script, do:
```
sudo chmod +x bdd_graph.py
sudo python3 bdd_graph.py
```





