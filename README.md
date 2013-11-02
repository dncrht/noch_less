# What is this?

Noch Less is a handy GUI frontend to keep track and compile LESS files into CSS, such as projects based upon [Bootstrap](http://getbootstrap.com/).

It has been written on PyGTK for *Linux* desktop OSs, requiring very little dependencies.

# How does it work?

Just drag a LESS file into the program's main window. You can add up to 10 files.
Then, *any file change* in the LESS file folder will trigger a recompilation of the CSS.

The user interface allows you to force a compilation, change the destination of the compilation or remove a file from being tracked.

# Aren't there other options available?

At the time of writing this, there was a program called [SimpLESS](http://wearekiss.com/simpless) but the Linux version doesn't exist anymore.

# How do I install it?

Use the installer for Debian-like systems, by running this in your command line shell:
```bash
curl https://raw.github.com/dncrht/noch_less/master/INSTALL.sh | sh
```

It will install the program in *$HOME/bin/noch_less* and it will report you any missing dependencies.

Once installed, it is recommended that you run the updater from time to time:
```bash
curl https://raw.github.com/dncrht/noch_less/master/UPDATE.sh | sh
```

