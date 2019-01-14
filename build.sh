#!/bin/bash

sudo apt-get update -y

# vim
sudo apt-get install vim -y
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
cp -r .vimrc ~/.vimrc

# pwntools
sudo apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential -y
sudo pip install --upgrade pip
sudo pip install --upgrade pwntools

# gdb
sudo apt-get install gdb
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit
echo "DONE! debug your program with gdb and enjoy"
cd ~/
git clone https://github.com/scwuaptx/Pwngdb.git 
cp ~/Pwngdb/.gdbinit ~/

# compiler gcc&g++
sudo apt-get install gcc g++ -y
sudo apt-get install gcc-multilib g++-multilib -y

