import os, shutil, sys

class directory():
    def __init__(self, path):
        self.path = path
        self.files = []

    def addFile(file):
        self.files.append(file)

applicationName = 'generic'
downloadDir = os.path.dirname(os.path.realpath(__file__))

directories = {
    'config': directory(os.path.expandvars('%APPDATA%\\gitBackConfig')),
    'install': directory(os.path.expandvars('%LOCALAPPDATA%\\Programs\\gitBack'))
    }

configFiles = []
installFiles = ['LICENSE', 'README.md', 'gitBack.exe', 'usage.txt']

_version = '1.1.0'

def version():
    print('Using gitBack installer version {}.'.format(_version))

if len(sys.argv) > 1:
    if sys.argv[1] == 'version':
        version()
else:
    #If not, create it
    if not os.path.exists(configDir):
        print('Creating config directory.')
        os.mkdir(configDir)

    #Check if %LOCALAPPDATA%\Programs\gitBack exists
    #if so, delete it
    if os.path.exists(installDir):
        print('Removing install directory.')
        shutil.rmtree(installDir)

    #Create installDir
    print('Creating install directory.')
    os.mkdir(installDir)

    #copy the necessary files to installDir
    for file in configFiles:
        print('Copying {} to {} ... '.format(file, configDir), end = '')
        shutil.copy(file, configDir)
        print('Done.')

    for file in installFiles:
        print('Copying {} to {} ... '.format(file, installDir), end = '')
        shutil.copy(file, installDir)
        print('Done.')