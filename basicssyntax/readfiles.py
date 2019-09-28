import os, fnmatch

print(fnmatch.filter(os.listdir('C:\\automation\\pycharmprojects\\PythonTutorial\\basicssyntax\\files'),
                     'owner_*20190704*.clt'))