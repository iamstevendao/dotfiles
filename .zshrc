# Fig pre block. Keep at the top of this file.
[[ -f "$HOME/.fig/shell/zshrc.pre.zsh" ]] && . "$HOME/.fig/shell/zshrc.pre.zsh"

export PATH=/opt/homebrew/bin:$PATH

# Enable mongod.
export PATH="$PATH:/usr/local/opt/mongodb-community/bin";

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/iamstevendao/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/iamstevendao/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/iamstevendao/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/iamstevendao/google-cloud-sdk/completion.zsh.inc'; fi
export PATH="/usr/local/sbin:$PATH"

export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"

# Fig post block. Keep at the bottom of this file.
[[ -f "$HOME/.fig/shell/zshrc.post.zsh" ]] && . "$HOME/.fig/shell/zshrc.post.zsh"
