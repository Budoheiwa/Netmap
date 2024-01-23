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

First you need to enable the DBMS from Neo4j Desktop interface. Then go to folder **network-mapping-neo4j**. In the terminal, use the command:
```
ip a
ifconfig
```
> It allows you to see which network interfaces you want to use


