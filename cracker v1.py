'''
TODOLIST
    *put the script, dictionary and zip file in the same folder
    *wirte down the zip file name
    *write down the dic. file name
    '''

import zipfile

zFile = zipfile.ZipFile('ramadan.zip') #write your zip file name..
passFile = open('passlist.txt') #use your own dic. file if the name is diff. remeber to wirite it here.
for line in passFile.readlines():
    password = x.strip()
    try:

        zFile.extractall(pwd=password)
        print('[+] Password = ' + password)
        exit(0)
    except Exception:
        pass