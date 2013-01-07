vsrc
====

Vsrc is a developer tool that finds and displays a module's Python source
file by searching the Module Search Path, which means the list of directories
given by sys.path, the current directory, PYTHONPATH, and the installation-
dependent default path. Therefore, Vsrc can find standard modules (like 
'string' and 'os.path'), 3rd-party modules (like pygame), and user-defined 
modules. Vsrc works from both the command-line and from inside of Python's
interactive mode.

Note that not all modules include Python source, for example, 'sys' is a 
C Built-in. If a .py file for the module is found, it's displayed after first
checking the value of the optional environment variable VSRC_VIEWER. If 
VSRC_VIEWER isn't set, then Vsrc will attempt to use the "less" pager (if it
exists in the system PATH), otherwise it uses "more".

The value of VSRC_VIEWER can be any viewer you like, such as a normal text 
editor like vim or notepad, or a pager program like less or more.  

Vsrc is platform-independent.

Since Vsrc 0.1 (which was created July 16th, 2003) Vsrc has been rewritten
as of July 30th, 2009 and includes some changes...

It now uses VSRC_VIEWER as an environment variable, instead of PAGER.

It now will work in Windows using cmd.exe. The default viewer it uses is
less.exe, if you have it in your path, otherwise it uses more.exe (which 
comes with Windows) but you can also create a VSRC_VIEWER environment 
variable to use another viewer, such as notepad. To get less.exe, visit
http://gnuwin32.sourceforge.net/packages/less.htm. If you get the setup
program it will install less.exe into C:\Program Files\GnuWin32\bin. Make
sure you add this directory to your Windows %PATH%. 

Installing
==========
The preferred way is to use install it from pypi using pip::

    $ pip install vsrc

this way you can install it into any virtualenv's you might have. Or into
your main python installation (by running: sudo pip install vsrc). And you'll
also be able to uninstall it with:

    $ pip uninstall vsrc

If you want to run it manually from source code, you can download the tarball
from pypi or clone from https://github.com/rkulla/vsrc.git and run::

    $ sudo python setup.py install

this will install the command-line script 'vsrc' in your bin directory and it
will install the vsrc.py module into your dist-packages directory.

Usage
=====
Typical usage looks like this::

    Command-line: $ python vsrc.py <module> 
    Interactive mode: >>> import vsrc
                    >>> vsrc.vsrc('<module>')


Examples
========
To see the "socket" module's corresponding socket.py source file, type::

    $ python vsrc.py socket

or from within Python's interactive-mode, type::

    >>> import vsrc
    >>> vsrc.vsrc('socket')

and vsrc will automatically find socket.py--which, if you use Linux, would 
be something like /usr/lib/python/socket.py-- and load in your viewer.

To seek out and view Pygame's sprite module's source code, type::

    $ ./vsrc.py pygame.sprite

or::

    >>> from vsrc import vsrc
    >>> vsrc('pygame.sprite')

To view a Python source file from the current directory, do::

    >>> vsrc('foo')

as long as you have a file called 'foo.py' in the current dir.
