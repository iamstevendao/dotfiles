ZSH_THEME="robbyrussell"

# pure
autoload -U promptinit; promptinit
prompt pure
PURE_CMD_MAX_EXEC_TIME=1

source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/iamstevendao/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/iamstevendao/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/iamstevendao/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/iamstevendao/google-cloud-sdk/completion.zsh.inc'; fi

# Iterm2 integration.
test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh" || true

# Enable mongod.
export PATH="$PATH:/usr/local/opt/mongodb-community@4.4/bin";
