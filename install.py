import subprocess
subprocess.run(["bash","-c","sudo curl -fsSL https://get.docker.com -o get-docker.sh"])
subprocess.run(["bash","-c","sudo sh get-docker.sh"])
subprocess.run(["bash","-c","sudo usermod -aG docker ${USER}"])
subprocess.run(["bash","-c","sudo docker version"])
subprocess.run(["bash","-c","sudo apt-get install libffi-dev libssl-dev && sudo apt install python3-dev && sudo apt-get install -y python3 python3-pip -y"])
subprocess.run(["bash","-c","sudo pip3 install docker-compose"])
print("PLEASE REBOOT OR RELOG")