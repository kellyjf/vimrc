call plug#begin("~/.vim/plugged")
"Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'scrooloose/nerdTree'
Plug 'bling/vim-airline'
call plug#end()

"let g:deoplete#enable_at_startup = 1

nmap <C-n> :NERDTreeToggle<CR>
source ~/.vimrc
