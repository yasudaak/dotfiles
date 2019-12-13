#!/bin/bash
set -u
DOT_DIRECTORY="$HOME/dotfiles"

#シンボリックリンクを張る
cd ${DOT_DIRECTORY}

for f in .??*
do
  [[ ${f} = ".git" ]] && continue
  [[ ${f} = ".gitignore" ]] && continue
  ln -snfv ${DOT_DIRECTORY}/${f} ~/${f}
done
echo $(tput setaf 2)Deploy dotfiles.$(tput sgr0)

