#!/usr/bin/python
#https://www.robinwieruch.de/docker-macos
import os
import subprocess
import cmd
import time
#import pdb; pdb.set_trace() # Running script in debug mode 
#Install docker 
#sudo brew update
#Uninstall the docker if its installed
#sudo brew remove docker docker-engine docker.io
#sudo apt autoremove docker docker-engine docker.io # To remove all dependancies 
#Install Docker 
#sudo apt install docker.io
#Enable Docker 
#sudo systemctl enable docker
#Bellow steps to unmask docker
#If you get the this error - Failed to start docker.service: Unit docker.service is masked.
# sudo systemctl list-unit-files | grep docker
# sudo systemctl unmask docker.service
# sudo systemctl unmask docker.socket
#Start Docker 
#sudo systemctl start docker
#OR
#sudo systemctl start docker.service
# The above will start the docker service
#Check the version - should retrun the docker version e.g Docker version 18.09.7, build 2d0083d
#docker --version 
def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print (p.stdout)
print ("Installing docker....")
subprocess_cmd('brew update ; brew remove docker docker-engine docker.io ; brew -y install docker ; brew install docker-machine; brew cask install virtualbox ; brew install docker-compose ; docker-machine create --driver virtualbox default ; docker-machine ls ; docker-machine start default ; docker-machine ls ; docker-machine stop default; docker-machine env default ; eval $(docker-machine env default) ; docker run hello-world ') 

