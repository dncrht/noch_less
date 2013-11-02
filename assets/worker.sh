#!/bin/sh

while true ; do
	 
		php ~/Web/lessphp/recompilador.php $1
			
			if [ $? -eq 128 ] ; then
					    exit
					    	fi
						 
						#
						# Assuming the build succeeded, run the program in the background, then loop
						# back to inotify.
						#
						 
							if [ $? -eq 0 ] ; then
										PID="$!"
												sleep 0.1
													else
																PID=""
																	fi
																	 
																		inotifywait -q -q -e 'close_write' --exclude '^\..*\.sw[px]*$|4913|~$' .
																		 
																		#
																		# ... so now a "save" has happened. If the program is running, kill it, then
																		# loop back to run the build.
																		#
																		 
																			if [ "$PID" ] ; then
																						kill $PID
																							fi
																							 
																						done

