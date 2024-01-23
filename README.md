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


