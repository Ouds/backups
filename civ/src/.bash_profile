# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PYTHONPATH=$HOME/ThinkerUnion/Civilization:$HOME/lib:$PYTHONPATH
export PYTHONPATH

PATH=$HOME/bin:$HOME/lib/python2.6/site-packages/django/bin:$PYTHONPATH:$PATH
export PATH

# PYTHONHOME=$PYTHONHOME:$HOME/lib/python2.6
# export PYTHONHOME

DJANGO_SETTINGS_MODULE=tu.settings
export DJANGO_SETTINGS_MODULE

unset USERNAME
