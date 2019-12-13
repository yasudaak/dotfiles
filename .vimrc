"
"                                ___           ___           ___
"      ___                      /\  \         /\  \         /\__\
"     /\  \        ___         |::\  \       /::\  \       /:/  /
"     \:\  \      /\__\        |:|:\  \     /:/\:\__\     /:/  /
"      \:\  \    /:/__/      __|:|\:\  \   /:/ /:/  /    /:/  /  ___
"  ___  \:\__\  /::\  \     /::::|_\:\__\ /:/_/:/__/___ /:/__/  /\__\
" /\  \ |:|  |  \/\:\  \__  \:\~~\  \/__/ \:\/:::::/  / \:\  \ /:/  /
" \:\  \|:|  |   ~~\:\/\__\  \:\  \        \::/~~/~~~~   \:\  /:/  /
"  \:\__|:|__|      \::/  /   \:\  \        \:\~~\        \:\/:/  /
"   \::::/__/       /:/  /     \:\__\        \:\__\        \::/  /
"    ~~~~           \/__/       \/__/         \/__/         \/__/
"

"バックスペースが効かなくなる対策
set backspace=indent,eol,start

"行番号表示
set number

"タイトルをウィンドウ枠に表示
set title

"ステータスラインを常に表示
set laststatus=2

"現在のモードを表示
set showmode

"打ったコマンドをステータスラインの下に表示
set showcmd

"ステータスラインの右側にカーソルの現在位置を表示する
set ruler

"クリップボードにコピーする
set clipboard&
set clipboard^=unnamedplus

"エンコーディング
set encoding=UTF-8

"保存時に行末の空白を除去する
autocmd BufWritePre * :%s/\s\+$//ge

" ~/.vimrc を保存したときにリロードする（source コマンドで変更を反映する）
autocmd BufWritePost  ~/.vimrc  so ~/.vimrc

"Control + e でPythonファイルを実行
autocmd BufNewFile,BufRead *.py nnoremap <C-e> :!python3 % <enter>

"Control + d でCSSファイルをminifyして.minファイルに保存する
"autocmd BufNewFile,BufRead *.css nnoremap <C-d> ggVG <S-j> :w %:r.min.%:e <enter> <undo>
"air-lineのバッファと:tabnewの違い
":e hogeで開いて:bnで次のファイル:bpで前のファイル

"常に自動補完を表示して一番上を選択する
"set pasteと干渉する
"set completeopt=menuone
"for k in split("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_",'\zs')
"  exec "imap <expr> " . k . " pumvisible() ? '" . k . "' : '" . k . "\<C-X>\<C-P>\<C-N>'"
"endfor

"ファイル名補完
set wildmenu wildmode=longest,full

"/を打ったあとの文字を入力タイミングからリアルタイムで検索してくれる。
set incsearch

"検索結果をハイライトして表示してくれる。
set hlsearch

"これが有効だと画面の端っこまで文字がいっても改行してくれません。
set nowrap

"文字列を検索してて、一番オシリ（もしくはアタマ）まで検索したときに先頭まで戻って検索するかの設定です。
set wrapscan

"文字列の検索時に大文字と小文字を区別しないで検索します。
set ignorecase

"ignorecaseと組み合わせて使うことで、小文字で検索した時は区別しなくなります。
set smartcase

"tabを押した時にtabではなくスペースを入れてくれる設定です。
"この設定を入れてたとしても、
"Control + v　をおした後にtabを押すことで　でtabを入力することができます。これ、小技です。
set expandtab

"tabをスペースいくつ分にするか
set tabstop=2

"<<や>>を入力したときに挿入されるtabがスペースいくつ分かを設定できる
"例えばshift + v を押して複数行を選択させた状態で、>>と入力するとそれを一気にインデントすることが可能
set shiftwidth=2

"補完メニューの高さ
set pumheight=10

"外部でファイルに変更がされた場合は読みなおす
set autoread

" ファイル保存時にバックアップファイルを作らない
set nobackup

" ファイル編集中にスワップファイルを作らない
set noswapfile

"ビープ音すべてを無効にする
set visualbell t_vb=

"エラーメッセージの表示時にビープを鳴らさない
set noerrorbells

"スクロールする時に下が見えるようにする
set scrolloff=5

":terminalしたときに下に開く
set splitbelow

"terminalを起動
"autocmd VimEnter * :terminal

"ESCで検索ハイライトを消す
"nnoremap <ESC> :nohlsearch <CR>

":qを:qaに変えた
"nnoremap :q :qa

"行単位で移動する
nnoremap j gj
nnoremap k gk

"ファイルを閉じてもUndoを有効にする
if has('persistent_undo')
  set undodir=~/.vim/undo
  set undofile
endif

"カッコの補完
"inoremap { {}
"inoremap ( ()
"inoremap < <>

"入力モードでのカーソル移動
"imap <C-k> <Up>
"imap <C-j> <Down>
"imap <C-l> <Left>
"imap <C-h> <Right>


"---onedark---

"Use 24-bit (true-color) mode in Vim/Neovim when outside tmux.
"If you're using tmux version 2.2 or later, you can remove the outermost $TMUX check and use tmux's 24-bit color support
"(see < http://sunaku.github.io/tmux-24bit-color.html#usage > for more information.)
if (empty($TMUX))
  if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
  endif
  "For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
  "Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
  " < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >
  if (has("termguicolors"))
    set termguicolors
  endif
endif

"---onedark---


"---Vundle---
"自動でVundleをインストールする
if empty(glob('~/dotfiles/.vim/bundle/Vundle.vim'))
  echo "Installing Vundle.."
  echo ""
  silent !curl -fLo ~/.vim/bundle/Vundle.vim --create-dirs https://github.com/VundleVim/Vundle.vim.git
  echo "Installing Plugin.."
  echo ""
  autocmd VimEnter * :PluginInstall <enter>
endif

set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'valloric/youcompleteme'
Plugin 'joshdick/onedark.vim'

call vundle#end()
filetype plugin indent on

colorscheme onedark
syntax on


"Setting up Vundle - the vim plugin bundler
"    let iCanHazVundle=1
"    let Vundle=expand('~/.vim/bundle/Vundle.vim')
"    if !isdirectory(Vundle)
"        echo "Installing Vundle.."
"        echo ""
"        silent !mkdir -p ~/.vim/bundle
"        silent !git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
"        let iCanHazVundle=0
"    endif
"    if iCanHazVundle == 0
"        echo "Installing Vundles, please ignore key map error messages"
"        echo ""
"        :PluginInstall
"    endif

"---Vundle---


"---vim-airline---
"カラースキーム
"let g:airline_theme = 'minimalist'

"表示するもの
let g:airline_left_sep=''
let g:airline_right_sep=''

" タブバーのカスタマイズを有効にする
let g:airline#extensions#tabline#enabled = 1

" タブバーの右領域を非表示にする
let g:airline#extensions#tabline#show_splits = 0
let g:airline#extensions#tabline#show_tab_type = 0
let g:airline#extensions#tabline#show_close_button = 0

"ディレクトリ表示
let g:airline_section_b = '%-0.10{getcwd()}'

"ファイル名表示
"let g:airline_section_a = 'mode'
let g:airline_section_a = airline#section#create(['mode'])
let g:airline_section_b = ''
let g:airline_section_c = ''
let g:airline_section_x = airline#section#create(['branch'])
let g:airline_section_y = airline#section#create(['filetype'])
"let g:airline_section_z = ''
"---vim-airline---


"---NERDTree---
"ファイルを選択したらNERDTreeを閉じる
let NERDTreeQuitOnOpen = 1

"隠しファイルを表示する
"let NERDTreeShowHidden = 1

"Press ? for helpを表示しない
let NERDTreeMinimalUI=1

"ブックマークを表示する
"let g:NERDTreeShowBookmarks=1

"引数なしでvimを開いたらNERDTreeを起動、
"引数ありならNERDTreeは起動せず、引数で渡されたファイルを開く。
autocmd vimenter * if !argc() | NERDTree | endif

"他のバッファをすべて閉じた時にNERDTreeが開いていたらNERDTreeも一緒に閉じる。
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
"autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

"ディレクトリ表示記号を変更
"let g:NERDTreeDirArrowExpandable = '▸'
"let g:NERDTreeDirArrowCollapsible = '▾'
"---NERDTree---


"---YouCompleteMe---
"YouCompleteMeの設定
let g:ycm_use_clangd = 0

"補完をエンターキーで選択する
let g:ycm_key_list_stop_completion = [ '<C-y>', '<Enter>' ]
"---YouCompleteMe---
