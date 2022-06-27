call plug#begin('~/.config/nvim/data/plugged')

" Language plugins
Plug 'neovim/nvim-lspconfig'
Plug 'prettier/vim-prettier'

Plug 'tidalcycles/vim-tidal'
Plug 'alaviss/nim.nvim'
Plug 'edwinb/idris2-vim'
Plug 'ziglang/zig.vim'
Plug 'neovimhaskell/haskell-vim'
Plug 'tidalcycles/vim-tidal'
Plug 'bakpakin/fennel.vim'

" Theme
Plug 'morhetz/gruvbox'
Plug 'vim-airline/vim-airline'
Plug 'nvim-treesitter/nvim-treesitter', { 'do': 'TSUpdate' }

" Other plugins
Plug 'easymotion/vim-easymotion'
Plug 'windwp/nvim-autopairs'
Plug 'jreybert/vimagit'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'pechorin/any-jump.vim'
Plug 'mattn/emmet-vim'

call plug#end()

:lua require('l')

" let g:prettier#autoformat_require_pragma = 0
" let g:prettier#autoformat_config_present = 1

syntax on
filetype plugin indent on
let g:gruvbox_italic=1
set background=dark
set nofoldenable
colorscheme gruvbox

let g:tidal_target = "terminal"
" let g:zig_fmt_autosave = 0

nnoremap <Space> <Nop>
let mapleader=" "
let maplocalleader=" "

" let g:ctrlp_map = '<Leader>p'
" let g:ctrlp_user_command = ['.git', 'cd %s && git ls-files -co --exclude-standard']

nnoremap <C-s> :w<Enter>
nnoremap <C-p> :GFiles<CR>

nnoremap <C-Q> :q<Enter>

tnoremap <Esc> <C-\><C-n>

map tt <Plug>(easymotion-prefix)

nnoremap ; :
nnoremap : ;

nnoremap <C-n> <C-w>h
nnoremap <C-e> <C-w>j
nnoremap <C-i> <C-w>k
nnoremap <C-o> <C-w>l

nnoremap <C-l> <C-o>
nnoremap <C-k> <C-i>

nnoremap n h
nnoremap N H
vnoremap n h
vnoremap N M
nnoremap e j
nnoremap E J
vnoremap e j
vnoremap E J
nnoremap i k
nnoremap I K
vnoremap i k
vnoremap I K
nnoremap o l
nnoremap O L
vnoremap o l
vnoremap O L

nnoremap l o
nnoremap L O
vnoremap l o
vnoremap L O
nnoremap j n
nnoremap J N
vnoremap j n
vnoremap J N
nnoremap h e
nnoremap H E
vnoremap h e
vnoremap H E
nnoremap k i
nnoremap K I
vnoremap k i
vnoremap K I
