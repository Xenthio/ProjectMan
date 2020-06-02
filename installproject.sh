#!/bin/zsh
echo "NOTE: Linux users may need to run this script as root.\n"

cp ./project /usr/local/bin/project # copy exectuable over to usr local bin.
chmod +x /usr/local/bin/project # just in case.

# -- make shortcuts and aliases --
ln -s /usr/local/bin/project /usr/local/bin/proj # Shortcut to project by typing proj
ln -s /usr/local/bin/project /usr/local/bin/pman # Shortcut to project by typing pman
ln -s /usr/local/bin/project /usr/local/bin/proman # Shortcut to project by typing proman
ln -s /usr/local/bin/project /usr/local/bin/p # Shortcut to project by typing p --- Do we really need an alias to "p"???
