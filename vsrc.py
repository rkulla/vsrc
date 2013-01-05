#!/usr/bin/env python
# Version 0.1 written: July 16, 2003
# Version 1.0 written: July 29, 2009
# Homepage: http://vsrc.sourceforge.net/
"""
vsrc.py 1.0 by Ryan Kulla (rkulla AT gmail DOT com).

Description: Vsrc finds and displays a module's Python source
             file by searching the Module Search Path, which
             means the list of directories given by sys.path,
             the current directory, PYTHONPATH, and the
             installation-dependent default path. Therefore,
             Vsrc can find standard modules (like 'string'
             and 'os.path'), 3rd-party modules (like pygame),
             and user-defined modules. Vsrc works from both
             the command-line and from inside of Python's
             interactive mode.

             Note that not all modules include Python source,
             for example, 'sys' is a C Built-in.

             If a .py file for the module is found, it's
             displayed after first checking the value of the
             optional environment variable VSRC_VIEWER. If
             VSRC_VIEWER isn't set, then vsrc attempts to use
             the "less" pager (if it exists in the system
             PATH), otherwise it uses "more".

             The value of VSRC_VIEWER can be any viewer you
             like, such as a normal text editor like vim or
             notepad, or a pager program like less or more.

             Vsrc is platform-independent.

Usage: python vsrc.py <module>

Examples: To seek out the "socket" module's corresponding socket.py
          source file, type:
              $ python vsrc.py socket
          or from within interactive-mode, type:
              >>> import vsrc
              >>> vsrc.vsrc('socket')
"""


__author__ = "Ryan Kulla (rkulla AT gmail DOT com)"
__version__ = "1.0"


import os
import subprocess
import sys


def in_path(what):
    """

    Scan the system PATH to see if the file exists there.
    Return the path name of the file if the file exists.
    Return false if the file doesn't' exist.
    """
    for dir in os.environ['PATH'].split(os.pathsep):
        fpath = r'%s' % (dir + os.sep + what)
        if os.path.exists(fpath):
            return dir
    return False


def my_import(name):
    """Make __import__ import "package.module" formatted names."""
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def vsrc(module_name=None):
    """Find a module's Python source file and open it in a viewer app."""

    viewer = None

    try:
        mod = my_import(module_name)
        try:
            mod_path = mod.__file__
        except:
            sys.stderr.write("No source file found for module: %s\n" %
                              module_name)
            return

        # Change .pyc to .py:
        if mod_path[-1] == 'c':
            mod_path = mod_path[:-1]
    except ImportError, err:
        sys.stderr.write('%s\n' % err)
        return

    # Figure out which viewer to use:
    try:
        # Use the value of the VSRC_VIEWER environment variable, if it exists:
        viewer_env = os.environ['VSRC_VIEWER']
        if sys.platform.lower().startswith('win') and not\
           viewer_env.lower().endswith('.exe'):
            viewer_env += '.exe'

        # If not an absolute path, check if it exists in PATH:
        if viewer_env.find(os.sep) == -1:
            if in_path(viewer_env):
                viewer = viewer_env
        elif os.path.isfile(viewer_env):
            viewer = viewer_env

        if viewer is None:
            viewer = get_default_viewer()
    except KeyError:
        viewer = get_default_viewer()

    # Open the source file in the viewer:
    if mod_path.endswith('.py'):
        subprocess.call(viewer + ' ' + mod_path, shell=True)
    else:
        sys.stderr.write("No Python source found, just: %s\n" % mod_path)


def get_default_viewer():
    """

    If the user has the "less" pager in their PATH, return that.
    Otherwise, return "more".
    """

    if in_path('less'):
        return 'less'
    else:
        return 'more'


def main():
    """Process the command line."""

    try:
        vsrc(sys.argv[1])
    except:
        sys.stderr.write("%s requires one argument (a module name)\n" %
                          sys.argv[0])


if __name__ == '__main__':
    main()
