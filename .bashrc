shopt -s dotglob

#疑似treeコマンド
alias tree="pwd;find . | sort | sed '1d;s/^\.//;s/\/\([^/]*\)$/|--\1/;s/\/[^/|]*/| /g'"

#cdコマンドにls結果を表示する
function cdls(){
 \cd $1
 ls;
}
alias cd=cdls

#プロンプトの表示をカスタマイズ
export PS1='\[\e[36m\]\w\[\e[0m\]\[\e[1m\]$(__git_ps1 " (%s)") \[\e[0m\] \n\$ '

#コマンドの履歴
export HISTSIZE=1000

#git branch を表示する
#https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh
source ~/dotfiles/.git-prompt.sh

#英語表示
#export LANG=en_US

#日本語表示
export LANG='ja_JP.UTF-8'
export LC_ALL='ja_JP.UTF-8'
export LC_MESSAGES='ja_JP.UTF-8'

#lsの結果に色をつける
#alias ls="ls --color=always"

#ssh接続したときにtmuxを起動する
if [[ ! -n $TMUX ]]; then
    tmux new-session
fi

#vimrcの設定が読み込まれない対策
alias tmux='tmux -2'

#bashrcの読み込み
#source ~/.bashrc
