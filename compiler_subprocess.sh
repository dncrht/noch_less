#!/bin/sh

while true; do

    echo "compiling $2 into $3"
    $1 $2 > $3

    DIR_TO_WATCH=${2%/*}

    inotifywait -q -q -e 'close_write' --exclude '^\..*\.sw[px]*$|4913|~$' $DIR_TO_WATCH

done
