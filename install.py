import os, shutil, sys

applicationName = 'generic'
installerVersion = '1.1.1'
downloadDir = os.path.dirname(os.path.realpath(__file__))

class directory():
    def __init__(self, path, overwrite):
        self.path = path
        self.files = []
        self.overwrite = overwrite

    def addFile(self, file):
        self.files.append(file)

directories = {
    'desktop': directory(os.path.expandvars('%USERPROFILE%\\Desktop\\buildPython'), True)
    }

for file in ['LICENSE', 'README.md']:
    directories['desktop'].addFile(file)

def version():
    print('Using {} installer version {}.'.format(applicationName, installerVersion))

if len(sys.argv) > 1:
    if sys.argv[1] == 'version':
        version()
else:
    for k in list(directories.keys()):
        print('Processing directory {}.'.format(k))
        d = directories[k]
        if d.overwrite:
            #Check if %LOCALAPPDATA%\Programs\gitBack exists
            #if so, delete it
            if os.path.exists(d.path):
                print('Removing directory {}.'.format(d.path))
                shutil.rmtree(d.path)

        #Create d.path
        print('Creating directory {}.'.format(d.path))
        os.mkdir(d.path)

        #copy the necessary files to d.path
        for file in d.files:
            print('Copying {} to {} ... '.format(file, d.path), end = '')
            shutil.copy(file, d.path)
            print('Done.')