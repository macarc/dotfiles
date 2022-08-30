# The following lines were added by compinstall
zstyle :compinstall filename '/home/macarc/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt autocd extendedglob nomatch
bindkey -e
# End of lines configured by zsh-newuser-install

autoload -Uz vcs_info
precmd_vsc_info () { vcs_info }
precmd_functions+=( precmd_vsc_info )

setopt prompt_subst

PROMPT='%/ %(?.%F{green}%(!.#.>)%f.%F{red}%(!.#.>)%f) '
RPROMPT=\$vcs_info_msg_0_

zstyle ':vcs_info:git:*' formats '(%b)'
zstyle ':vcs_info:*' enable git

source /home/macarc/3rd_party/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
