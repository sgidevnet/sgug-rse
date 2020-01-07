#!/usr/sgug/bin/bash


SGUG_ROOT=/usr/sgug
SGUG_BIN=$SGUG_ROOT/bin
SGUG_LIB=$SGUG_ROOT/lib32

export PATH=$SGUG_BIN:/usr/bin:/bin:/usr/sbin:/usr/bsd
export LD_LIBRARYN32_PATH=$SGUG_LIB:/usr/lib32:/lib32:/usr/lib:/lib
#export LD_LIBRARYN32_PATH=/usr/lib32:/lib32:/usr/lib:/lib
export PKG_CONFIG_PATH=$SGUG_LIB/pkgconfig
export MANPATH=$SGUG_ROOT/man:/usr/share/catman/a_man:/usr/share/catman/g_man:/usr/share/catman/p_man:/usr/share/catman/u_man

export PS1='[sgugshell \u@\h \W]\$ '
exec bash --norc -i
