export PATH=/opt/homebrew/bin:$PATH
export PATH=/usr/local/share/npm/bin:$PATH
export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin/"
export PATH=/Users/iamstevendao/.meteor:$PATH

# --- python and pyenv ---------
export PYENV_ROOT="$HOME/.pyenv"
alias python="python3"
alias pip="pip3"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
# ------------------------------

eval "$(starship init zsh)"

[[ -s $HOME/.nvm/nvm.sh ]] && . $HOME/.nvm/nvm.sh

# --- zsh plugins ------
. $HOME/z.sh
source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh
export GPG_TTY=\$(tty)

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
