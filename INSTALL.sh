#!/bin/sh

DEST="$HOME/bin/noch_less"

. .config/user-dirs.dirs

echo '=> Meeting requeriments...'

hash apt-get 2> /dev/null || { echo >&2 "This installer is for Debian Linux only."; exit 1; }

hash git 2> /dev/null || { echo >&2 "Missing dependency! Please install with:\n\n  sudo apt-get install git"; exit 1; }
hash php 2> /dev/null || { echo >&2 "Missing dependency! Please install with:\n\n  sudo apt-get install php5-cli"; exit 1; }
hash inotifywait 2> /dev/null || { echo >&2 "Missing dependency! Please install with:\n\n  sudo apt-get install inotify-tools"; exit 1; }
dpkg -l | grep python-gtk2 > /dev/null || { echo >&2 "Missing dependency! Please install with:\n\n  sudo apt-get install python-gtk2"; exit 1; }

echo "=> Installing noch_less into $DEST ... "

mkdir -p $DEST
cd $DEST

echo '=> Downloading latest version...'

git clone https://github.com/dncrht/noch_less.git .

git clone https://github.com/leafo/lessphp.git

echo '=> Creating desktop shortcut...'

sed noch_less.desktop -e "s%~%$HOME%g" > $XDG_DESKTOP_DIR/noch_less.desktop

echo '=> Installation succeeded!'

cd ~

