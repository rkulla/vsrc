
Vsrc 1.0 by Ryan Kulla (rkulla AT gmail DOT com).
Homepage: http://vsrc.sourceforge.net/


Description
===========
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


Usage
=====
Command-line: $ python vsrc.py <module> 
Interactive mode: >>> import vsrc
                  >>> vsrc.vsrc('<module>')


Examples
========
To see the "socket" module's corresponding socket.py source file, type:
    $ python vsrc.py socket
or from within Python's interactive-mode, type:
    >>> import vsrc
    >>> vsrc.vsrc('socket')
and vsrc will automatically find socket.py--which, if you use Linux, would 
be something like /usr/lib/python/socket.py-- and load in your viewer.

To seek out and view Pygame's sprite module's source code, type:
    $ ./vsrc.py pygame.sprite
or:
    >>> from vsrc import vsrc
    >>> vsrc('pygame.sprite')

To view a Python source file from the current directory, do:
    >>> vsrc('foo')
as long as you have a file called 'foo.py' in the current dir.


License
=======
BSD


Copyright
========= 
Copyright (c) 2003-2009 Ryan Kulla
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above
  copyright notice, this list of conditions and the following
  disclaimer in the documentation and/or other materials provided
  with the distribution.
3. The name of the author may not be used to endorse or promote 
  products derived from this software without specific prior 
  written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

