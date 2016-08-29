# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# don't put duplicate lines in the history. See bash(1) for more options
export HISTCONTROL=ignoredups
# ... and ignore same sucessive entries.
export HISTCONTROL=ignoreboth

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac




# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_colored_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
#case "$TERM" in
#xterm*|rxvt*)
#    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}: ${PWD/$HOME/~}\007"'
#    ;;
#*)
#    ;;
#esac

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}: ${PWD}\007"'

    # Show the currently running command in the terminal title:
    # http://www.davidpashley.com/articles/xterm-titles-with-bash.html
    show_command_in_title_bar()
    {
        case "$BASH_COMMAND" in
            *\033]0*)
                # The command is trying to set the title bar as well;
                # this is most likely the execution of $PROMPT_COMMAND.
                # In any case nested escapes confuse the terminal, so don't
                # output them.
                ;;
            *)
                echo -ne "\033]0;${USER}@${HOSTNAME}: ${BASH_COMMAND}\007"
                ;;
        esac
    }
    trap show_command_in_title_bar DEBUG
    ;;
*)
    ;;
esac

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

#if [ -f ~/.bash_aliases ]; then
#    . ~/.bash_aliases
#fi

# enable color support of ls and also add handy aliases
if [ "$TERM" != "dumb" ] && [ -x /usr/bin/dircolors ]; then
    eval "`dircolors -b`"
    alias ls='ls --color=auto'
    #alias dir='ls --color=auto --format=vertical'
    #alias vdir='ls --color=auto --format=long'

    #alias grep='grep --color=auto'
    #alias fgrep='fgrep --color=auto'
    #alias egrep='egrep --color=auto'
fi

# some more ls aliases
#alias ll='ls -l'
#alias la='ls -A'
#alias l='ls -CF'

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi

#set cps_project environment variable
CPS_ROOT=/CPS_Project
export CPS_ROOT
CPS_ENV=$CPS_ROOT/ubuntu
export CPS_ENV
JAVA_HOME=~/java_install/jdk1.7.0_45
export JAVA_HOME
JRE_HOME=~/java_install/jdk1.7.0_45/jre
export JRE_HOME
CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export CLASSPATH
TOMCATPATH=~/java_install/apache-tomcat-7.0.47
export TOMCATPATH
#ACE_ROOT=/home/cps/ubuntu12.04_64bit_3rd/ACE_wrappers
ACE_ROOT=/home/cps/CPS_Project/CPS/3rdPartyProgram/ACE
export ACE_ROOT
QTDIR=$CPS_ROOT/CPS/3rdPartyProgram/Qt
export QTDIR
PATH=$CPS_ENV/bin:$JAVA_HOME/bin:$JRE_HOME/bin:$TOMCATPATH/bin:$QTDIR/bin:/usr/X11R6/bin:/usr/local/mysql/bin:$PATH
export PATH
#LD_LIBRARY_PATH=$CPS_ENV/lib:$CPS_ENV/plugin/rules:$CPS_ENV/thirdpartylib:$QTDIR/lib:/usr/X11R6/lib:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=$CPS_ENV/lib:$CPS_ENV/plugin/rules:$CPS_ENV/thirdpartylib:$ACE_ROOT/lib:$QTDIR/lib:/usr/X11R6/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH
NLS_LANG="SIMPLIFIED CHINESE_CHINA.UTF8"
export NLS_LANG
TNS_ADMIN="/CPS_Project/ubuntu/etc"
export TNS_ADMIN
AUDIOSERVER=`hostname`:0.0
export AUDIOSERVER

#export CVSROOT=:ext:lijunda@172.28.111.208:/home/yfgzk
export CVSROOT=:ssh;key='.ssh/lijunda_private.ppk':lijunda@172.28.111.208:/home/yfgzk
export CVS_RSH=ssh
export CPS_PROJECT20

#Add for Oracle DB 
export ORACLE_SID=orcl
export NLS_LANG="SIMPLIFIED CHINESE_CHINA.UTF8"
export ORACLE_BASE=/usr/local/oracle/app/oracle
export ORACLE_HOME=$ORACLE_BASE/product/11.2.0/dbhome_1
export PATH=$PATH:$ORACLE_HOME/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/lib 

export NLS_LANG="SIMPLIFIED CHINESE_CHINA.UTF8"

cd /CPS_Project/ubuntu/bin

