#!/usr/bin/env python

# $Id$

from distutils.core import setup
from distutils.command.install_data import install_data
import distutils.command.build
from distutils.cmd import Command
import glob
import os
import stat

PACKAGE = 'lct'
MAJOR = 0
MINOR = 1
PATCH = 0
VERSION = "%d.%d.%d" % (MAJOR, MINOR, PATCH)

# Pete Shinner's distutils data file fix... from distutils-sig
#  data installer with improved intelligence over distutils
#  data files are copied into the project directory instead
#  of willy-nilly
class smart_install_data(install_data):   
    def run(self):
        # need to change self.install_dir to the library dir
        install_cmd = self.get_finalized_command('install')
        self.install_dir = getattr(install_cmd, 'install_lib')
        return install_data.run(self)

# Function to check timestamps for file creation
def isNewer(src, target):
    if not os.path.exists(target):
        return True
    src_mtime = os.stat(src)[stat.ST_MTIME]
    target_mtime = os.stat(target)[stat.ST_MTIME]
    if src_mtime > target_mtime:
        return True
    else:
        return False

# Function to run command calls
def exec_cmd(cmd):
    import subprocess as sub
    proc = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.STDOUT, shell=True)
    (stdout, stderr) = proc.communicate()
    proc.wait()
    if proc.returncode:
        print stdout
    
def write_version(filename="version.py"):
    vfile = open(os.path.join(PACKAGE, filename), 'w')
    try:
        vfile.write("version='%s'" % VERSION)
    finally:
        vfile.close()
    
# Make a command class to build PyQt/Qt specific stuff
class build_qt(Command):
    description="Build PyQt/Qt resources and UIs"
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Make resources
        """
        qtr = "res/resources.qrc"
        pyqtr = "%s/info/qrc_resources.py" % PACKAGE
        if isNewer(qtr, pyqtr):
            pyrcc_cmd = "pyrcc4 -o %s %s" % (pyqtr, qtr)
            print pyrcc_cmd
            exec_cmd(pyrcc_cmd)
        """
        # Make dialogs
        uidir = 'ui'
        idir = os.path.join('res', uidir)
        ddir = os.path.join(PACKAGE, uidir)
        import dircache
        uifiles = [f for f in dircache.listdir(idir) if f.endswith('.ui')]
        for uifile in uifiles:
            pyuifile = "ui_"+uifile.split('.')[0]+".py"
            uifile = os.path.join(idir, uifile)
            pyuifile = os.path.join(ddir, pyuifile)
            if isNewer(uifile, pyuifile): 
                pyuic_cmd = "pyuic4 -o %s %s" % (pyuifile, uifile)
                print pyuic_cmd
                exec_cmd(pyuic_cmd)

old_cmds = distutils.command.build.build.sub_commands
new_cmds = [('build_qt', None)]
new_cmds.extend([x for x in old_cmds])
distutils.command.build.build.sub_commands = new_cmds

if __name__ == "__main__":
    write_version()
    setup(name = PACKAGE,
          version = VERSION,
          description = 'Lunar Club Tools',
          license = 'MIT Academic',
          cmdclass = {'install_data': smart_install_data,
                      'build_qt': build_qt},
          data_files = [ ('lct/ui', glob.glob('%s/ui/*.ui' % PACKAGE)),
                        ('lct/images', glob.glob('images/*.svg')) ],
                          #('dgspowder/images', glob.glob('images/*.png')+
          package_dir = {'lct': 'lct',
                         'lct.ui': 'lct/ui',
                         'lct.info': 'lct/info'},
          packages = ['lct',
                      'lct.ui',
                      'lct.info'])
          #scripts = ['bin/planet_weight_calc.py'])