# **docker-and-docker-compose**
this lets you install docker &amp; docker compose in one line

## HOW DOES IT WORK?
- it checks for python3
- it installs (and it automatically makes it so that you dont have to type sudo whenever you run a docker command)

## WARNING
- please restart or log out and back in so that docker can be ran without sudo
- make sure you are on an up to date debian system

---
## **INSTALL SCRIPT**
```
sudo apt-get install -y python3 && sudo curl -sSL https://raw.githubusercontent.com/silverace71/docker-and-docker-compose/main/install.py > install.py && sudo python3 install.py
```
---
### ***CREDIT***
- silverace_71 - writing code (this is my first script) and taking some from pouter
- [ckissane](https://github.com/ckissane) - for helping silverace_71 learn some basic python stuff