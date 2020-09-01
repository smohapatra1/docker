#!/usr/bin/python
#https://www.robinwieruch.de/docker-macos
import os
import subprocess
import cmd
import time
#import pdb; pdb.set_trace() # Running script in debug mode 
#Install docker 
#brew update
#Uninstall the docker if its installed
#sudo brew remove docker 
#Install Docker 
#brew install docker
#Install other dendencies 
#Install Virtual Box 
#Start the Docker-Machine
#Print the env variables
# 
#The above will start the docker service
#Check the version - should retrun the docker version e.g Docker version 18.09.7, build 2d0083d
#docker-machine delete <>
#docker --version 
def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print (p.stdout)
print ("Installing docker....")
subprocess_cmd('brew update ; brew remove docker ; brew remove docker-machine ; brew cask install docker ; brew install docker-machine ; brew cask install virtualbox ; docker --version ; docker-machine create --driver virtualbox docker-test ; docker-machine ls ; docker-machine start docker-test ; docker-machine ls ; docker-machine stop docker-test; docker-machine env docker-test ; eval $(docker-machine env docker-test) ; docker run hello-world ') 

