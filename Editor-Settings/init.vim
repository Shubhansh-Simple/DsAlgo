call plug#begin('~/.config/nvim/plugged/')

Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }

call plug#end()


set mouse=a
set wildmode=longest,list
set ttyfast
set hlsearch
colo molokai
set smartcase	" Enable smart-case search
set ignorecase	" Always case-insensitive
set incsearch	" Searches for strings incrementally
set cursorline
set linebreak   "Break lines at word (requires Wrap lines)
set smarttab
set smartindent
set showbreak=--> " Wrap-broken line prefix
set showmatch   " Highlight matching brace
"set errorbells  " Beep or flash screen on errors
set visualbell  " Use visual bell (no beeping))""")"")"
set shortmess+=c
set cursorcolumn


"Tabs Capital T to open new blank tab
nnoremap <Tab> gt
nnoremap <S-Tab> gT
nnoremap <silent> <S-t> :tabnew<CR>
nnoremap <silent> <C-f> :FZF <CR>
nnoremap <silent> <C-d> :set background=dark  \| echo 'Dark Version' <CR>
nnoremap <silent> <C-l> :set background=light \| echo 'Light Version'<CR>



