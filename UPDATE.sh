#!/bin/sh

DEST="$HOME/bin/noch_less"
cd $DEST

echo '=> Updating to latest version...'

git pull https://github.com/dncrht/noch_less.git

cd lessphp

git pull https://github.com/leafo/lessphp.git

echo '=> Update succeeded!'

cd ~

