import base64
import os,hashlib,time
from colorama import Fore
from pyfiglet import Figlet
from termcolor import colored



print(Fore.BLUE + "**************************************************************************************")
check = Figlet(font='standard')
print(colored(check.renderText('FILE INTEGRITY MODEL'),'blue'))
print(Fore.BLUE + "**************************************************************************************")

Monitor_the_file = [
    {'Path_of_the_Folder': r'C:\Users\dx\Desktop\Testing-for-FIM','recursive': True}
]
files={}
def get_all_files():
    fileslist = []
    for i in Monitor_the_file:
        if os.path.isdir(i['Path_of_the_Folder']):
            if i['recursive']:
                fileslist.extend([os.path.join(root, f) for(root,dirs, files) in os.walk(i['Path_of_the_Folder']) for f in files])
            else:
                fileslist.extend([item for item in os.listdir(i['Path_of_the_Folder']) if os.path.isfile(item)])
        elif os.path.isfile(i['Path_of_the_Folder']):
            fileslist.append(i['Path_of_the_Folder'])
    return fileslist
def get_the_bytes_of_a_file(file):
    return base64.b64encode(open(file,"rb").read())
while True:
    for file in get_all_files():
        sha512_hash = hashlib.sha512()
        with open(file,"rb") as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                sha512_hash.update(byte_block)
        sha512 = sha512_hash.hexdigest()
        if file in files and sha512 != files[file]['sha512']:
            print(Fore.RED + '%s %s has been changed !' % (time.strftime("%Y-%m-%d %H:%M:%S"), file))
        elif file not in files:
            print(Fore.CYAN + '%s %s has been created !' % (time.strftime("%Y-%m-%d %H:%M:%S"), file))
        files[file]={'sha512':sha512, 'bytes':get_the_bytes_of_a_file(file)}
    time.sleep(1)




