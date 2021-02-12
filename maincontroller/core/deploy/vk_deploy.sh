#!/bin/sh
unzip vkparsers/deploy/vk_project.zip -d ~/
sudo rm -rf vkparsers/deploy/vk_project.zip
cd parsingServer/
sudo apt-get -y  install python3
sudo apt-get -y  remove python3-pip
sudo apt-get -y  install python3-pip
pip3 install -r requirements.txt
python3 manage.py runserver 0:$1 &
