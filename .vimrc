set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'nanotech/jellybeans.vim'
Plugin 'sonictemplate-vim'

call vundle#end()            " required
filetype plugin indent on    " required

set tabstop=4
set expandtab
set shiftwidth=4

color jellybeans
set number
set  paste
syntax on
