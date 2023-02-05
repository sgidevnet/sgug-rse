# Initialization script for bash and sh

if [ "$0" = ksh ] ; then
  alias which='(alias; typeset -f) | /usr/bin/which --tty-only --read-alias --read-functions --show-tilde --show-dot'
else
  alias which='(alias; declare -f) | /usr/bin/which --tty-only --read-alias --read-functions --show-tilde --show-dot'
fi
