import os, sys
import progressbar
from files_manage import *
os.system('cls')
from subprocess import Popen, PIPE

#files = dir_to_list(os.getcwd())
files = getListOfFiles(os.getcwd())
for i in progressbar.progressbar(range(len(files))):
    file = files[i]
    #if not (os.path.exists(file + '.xml') or os.path.exists(file)):
    if file.endswith('.bin.ktid'):
        #c = f'F:\\AOC\\_extracted\\KIDSSystemResource\\kidsobjdb\\fid_utility.exe {file}'
        p = Popen(['fid_utility.exe', file, '>nul'], stdin=PIPE, shell=True)
        p.communicate(input='\n'.encode())
        #break