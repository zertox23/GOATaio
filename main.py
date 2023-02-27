from GradientGen import PrintGradient, PrintLinearGradient
import random
from listset import listset
import datetime
import os
import time
import requests
import json as js  
import re 
import hashlib
import platform
from bs4 import BeautifulSoup
from download import download
import os
import socket
from discord import SyncWebhook
from colorama import Fore 
import tkinter.filedialog as fd
import ctypes

import json as js
def get_val(val):
    with open("settings.json","r",errors="ignore") as f:
        k  = js.load(f)
    if k["SETTINGS"]['Auto login'] == "True" or k["SETTINGS"]['Auto login'] == True:
        return True
    else:
        return False

def change_val(change,val):
    with open("settings.json","r",errors="ignore") as f:
        k  = js.load(f)
    k["SETTINGS"][f"{val}"] = change
    with open("settings.json","w",errors="ignore") as f:
        js.dump(k,f)
    return True



def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

class counter():
    def __init__(self):
        count = 0  

website = ""


bl, ree, lr, wh, gr, cy, lb, res, ma, lm, lc, ye = Fore.BLUE, Fore.RED, Fore.LIGHTRED_EX, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.RESET, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX, Fore.YELLOW



NAME ='''
  ▄▀  ████▄ ██     ▄▄▄▄▀     ██   ▄█ ████▄ 
▄▀    █   █ █ █ ▀▀▀ █        █ █  ██ █   █ 
█ ▀▄  █   █ █▄▄█    █        █▄▄█ ██ █   █ 
█   █ ▀████ █  █   █         █  █ ▐█ ▀████ 
 ███           █  ▀             █  ▐       
              █                █           
             ▀                ▀            
'''
    
NAME = center(NAME)

os.system("cls")    
'''
CAPTURE_REMOVER DONE [FINISHED]
'''

def send_to_webhook(webhook,message):
        webhook = SyncWebhook.from_url(webhook)
        webhook.send(message)

def f1(func):
    
    def wrapper(*args, **kwargs): 
        try:
            name = socket.gethostname()
            privateIp = socket.gethostbyname(socket.gethostname())
            func(*args, **kwargs)
        except Exception as E:
            try:
                msg = f"```TIME:{str(datetime.datetime.now())[:-7].replace(':','-')}\nERORR HAPPENED:{E}\nNAME:{name}\nPRIVATE IP: {privateIp}\nFUNC={str(func).split('at')[0]}```"
                with open("errors.txt", "a",errors="ignore") as errors:
                    errors.write(f"TIME:{str(datetime.datetime.now())[:-7].replace(':','-')}  ERORR HAPPENED:{E}\n")
                    send_to_webhook(message=msg,webhook="")
            except:
                pass

    return wrapper

def getcombo(title="FILE"):
    try:
        fileo  = fd.askopenfile(title=title,filetypes=[('Text files', '*.txt')]).name.replace('"','')
    except:
            fileo  = None
    return fileo

@f1
def password_limit(limit):
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\PASSWORD_MINIMUM")
    except:
            pass
    combo = getcombo('combo-file')
    combo = open(combo, "r",errors="ignore",encoding="utf-8")
    apropriate = []
    for line in combo:
        password = line.split(":")[1]
        if len(password)>=int(limit):
            apropriate.append(line.strip())
    namy =  '[Minimum - PASSWORD] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\PASSWORD_MINIMUM\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
        for line in apropriate:
            file.write(str(line).strip()+"\n")
@f1
def password_hex(limits):
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\PASSWORD_HEX")
    except:
            pass
    combo = getcombo('combo-file')
    combo = open(combo, "r",errors="ignore",encoding="utf-8")
    good = []
    for line in combo:
        password = line.split(":")[1]
        for character in password:
            if character in limits:
                good.append(line.strip())
                break
            else:
                pass 
    namy = '[PASSWORD - HEX] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\PASSWORD_HEX\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
        for line in good:
            file.write(line.strip()+"\n")
                


@f1
def capture_remover():
    combo=getcombo('combo-file')
    start_time = time.time()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\CAPTURE_REMOVER")
    except:
            pass
    newc = []
    combo = open(combo,"r",errors="ignore",encoding="utf-8")
    for line in combo:
        try:
            user = line.split(":")[0]
            password = str(line.split(":")[1]).split(' ')[0]
            data = user.strip()+":"+password.strip()
            newc.append(data.strip())
        except:
            pass 

    combo.close()
    namy =  '[CAPTURE_REMOVED] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'


    with open(os.getcwd()+"\\results\\CAPTURE_REMOVER\\"+namy,"a",encoding="utf-8",errors="ignore") as f:
        
        for line in newc:
                f.write(line.strip()+"\n")
'''
CAPTURE_REMOVER DONE [FINISHED]
'''
@f1
def domain_changer(dom):
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\DOMAIN_CHANGER")
        except:
            pass
        newc = []
        combo=getcombo('combo-file')
        combo = open(combo,"r",errors="ignore",encoding="utf-8")
        newc = []
        try:
                for line in combo:
                        user = line.split("@")[0]
                        password = line.split(":")[1]
                        new = user.strip()+dom.strip()+":"+password.strip()
                        newc.append(new.strip())
        except:
                pass
        namy =  '[DOMAIN - CHANGER] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\DOMAIN_CHANGER\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                for line in newc:
                        file.write(line.strip()+"\n")
@f1
def ComboLineCounter():
        combo = getcombo('combo-file')
        combo = open(combo, "r",errors="ignore",encoding="utf-8")
        c = []
        for line in combo:
                c.append(line.strip())
        print(f"\n{gr}YOUR COMBO HAVE: {format(len(c),',')} LINES")
        input(f"\n{ree}PRESS ANY THING TO COUNTINUE:")
@f1
def reverser():
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\COMBO_REVERSER")
        except:
            pass
        combo = getcombo('combo-file')
        combo = open(combo, "r",errors="ignore",encoding="utf-8")
        newc = []
        try:
                for line in combo:

                        usr = line.split(":")[0]
                        password = line.split(":")[1]
                        reversed=(f"{password.strip()}:{usr.strip()}")
                        newc.append(reversed.strip())
        except:
                pass 

        namy =  '[DOMAIN - CHANGER] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\COMBO_REVERSER\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                for line in newc:
                        file.write(line.strip()+"\n")
@f1
def combo_sorter():
        combo=getcombo('combo-file')
        combo = open(combo, "r",errors="ignore",encoding="utf-8")
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\COMBO_SORTER")
        except:
            pass
        sorted = []
        for line in combo:
                sorted.append(line)
        namy =  '[COMBO - SORTER] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        sorted.sort()
        with open(os.getcwd()+"\\results\\COMBO_SORTER\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                for line in sorted:
                        file.write(line.strip()+"\n")
                
@f1
def email_extracor():
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\EMAIL_EXTRACTOR")
        except:
            pass
        newc = []
        combo = getcombo('combo-file')
        combo = open(combo, "r",errors="ignore",encoding="utf-8")
        for line in combo:
            try:
                email = line.split(":")[0]
                newc.append(email.strip())
            except:
                pass
        namy =  '[EMAIL - EXTRACTOR] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\EMAIL_EXTRACTOR\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                for line in newc:
                        file.write(line.strip()+"\n")
@f1
def password_extracor():
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\PASSWORD_EXTRACTOR")
        except:
            pass
        newc = []
        combo = getcombo('combo-file')
        combo = open(combo, "r",errors="ignore",encoding="utf-8")
        for line in combo:
            try:
                email = line.split(":")[1]
                newc.append(email.strip())
            except:
                pass
        namy =  '[PASSWORD - EXTRACTOR] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\PASSWORD_EXTRACTOR\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                for line in newc:
                        file.write(line.strip()+"\n")
@f1
def shuffle():
    combo=getcombo('combo-file')
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\SHUFFLE_LIST")
    except:
            pass
    
    combo = open(combo,"r",errors="ignore",encoding="utf-8")
    listt = combo.readlines()

    random.shuffle(listt)
    namy = '[SHUFFlED] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\SHUFFLE_LIST\\"+namy,"a",encoding="utf-8",errors="ignore") as f:
        for line in listt:
            f.write(line.strip()+"\n") 
@f1
def remove_dupes():
    combo=getcombo('combo-file')
    start_time = time.time()
    combo = open(combo,"r",errors="ignore",encoding="utf-8")
    listt = combo.readlines()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\REMOVE_DUPES")
    except:
            pass
    nodupe = listset(listt)
    namy = '[REMOVED DUPES] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\REMOVE_DUPES\\"+namy,"a",encoding="utf-8",errors="ignore") as f:
        for line in nodupe:
            f.write(line.strip()+"\n")

@f1
def CLEANER():
    combo=getcombo('combo-file')
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\ALL_CLEANER")
    except:
            pass
    combo = open(combo,"r",errors="ignore",encoding="utf-8")
    listt = combo.readlines()
    random.shuffle(listt)
    nodupe = listset(listt)
    newlist = []
    for line in nodupe:
        if line == "" or line == " ":
            pass
        else:
             newlist.append(line.strip())


    namy = '[CLEAN - RANDOMIZED] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\ALL_CLEANER\\"+namy,"a",encoding="utf-8",errors="ignore") as f:
        for line in nodupe:
            f.write(line.strip()+"\n")
@f1
def filter_combo_by_domain(domain):
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\DOMAIN_FILTRER")
        except:
            pass
        try:
            domain = domain.replace("@","")
        except:
            pass 
        combo=getcombo('combo-file')
        combo = open(combo,"r",errors="ignore",encoding="utf-8")
        newc = []
        try:
                for line in combo:
                        doma= str(line.split("@")[1]).split(":")[0]
                        if str(doma) == str(domain):
                                newc.append(line.strip())
        
        except:
                pass 

        try:
                namy = '[FILTER - DOMAIN] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
                with open(os.getcwd()+"\\results\\DOMAIN_FILTRER\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                        for line in newc:
                                file.write(line.strip()+"\n")
        except:
                pass 


            

    
@f1
def LQTOHQ():
    combo=getcombo('combo-file')
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\LQTOHQ")
    except:
            pass
    combo = open(combo,"r",errors="ignore",encoding="utf-8")
    listt = []
    for line in combo:
                    try:
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"!"+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"123"+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"1"+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip()+"!"+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip()+"123"+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip()+"1"+"\n")
                            listt.append(line)
                    except:
                        pass


    try:
        random.shuffle(listt)
    except:
        pass
    
    namy = '[LQ to HQ] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\LQTOHQ\\"+namy,"a",encoding="utf-8",errors="ignore")as f:
        for line in listt:
            f.write(line.strip()+"\n")    
@f1
def get_pagetypes():
    filename=getcombo('dorks-file')
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\SKIDED_PAGETYPES")
    except:
            pass
    try:
        dorks = open(filename,"r",errors="ignore",encoding="utf-8")
        pagetypes = []
        for dork in dorks:
            try:
                pagetype = re.findall(r'\?.*?\=',dork)
                pagetypes.append(pagetype[1])
            except:
                pass 
        namy = '[PAGE-TYPES] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\SKIDED_PAGETYPES\\"+namy,"a",encoding="utf-8",errors="ignore") as f:            
            random.shuffle(pagetypes)
            nodupe = listset(pagetypes)
            print(nodupe)
            for line in nodupe:
                f.write(line.strip()+"\n")
    except:
            pass
    @f1
    def get_pageformats():
        filename=getcombo("dorks-file")
        try:
                os.mkdir(os.getcwd()+"\\results")
        except:
                pass
        try:
                os.mkdir(os.getcwd()+"\\results\\SKIDED_PAGEFORMATS")
        except:
                pass
        dorks = open(filename,"r",errors="ignore",encoding="utf-8")
        pageformats = []
        for dork in dorks:
            try:
                pageformat = re.findall(r'\.[A-Za-z0-9]{,}\?',dork.strip('\n'))[0]
                pageformats.append(str(pageformat))
            except:
                pass
        namy = '[PAGE-FORMATS] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\SKIDED_PAGEFORMATS\\"+namy,"a",encoding="utf-8",errors="ignore") as f:
            random.shuffle(pageformats)
            nodupe = listset(pageformats)
            for line in nodupe  :
                f.write(line.strip()+"\n")

    def EP_TO_UP():
        filename=getcombo()
        try:
                os.mkdir(os.getcwd()+"\\results")
        except:
                pass
        try:
                os.mkdir(os.getcwd()+"\\results\\EP_TO_UP")
        except:
                pass
        combo = open(filename,"r",errors="ignore",encoding="utf-8")
        combo = combo.readlines()
        newcombo = []
        for line in combo:
            try:
                user = line.split("@")[0]
                password= line.split(":")[1]
                new=(f"{user.strip()}:{password.strip()}")
                newcombo.append(new.strip())
            except:
                pass
        namy = '[EP-UP] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\EP_TO_UP\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
            for line in newcombo:
                file.write(line.strip()+"\n")


    def is_salesforce_id(string):
        pattern = r"001[A-Z0-9]{15}"
        match = re.search(pattern, string)
        if match:
            return True
        else:
            return False


    @f1 
    def domain_sorter():
        filename=getcombo('combo-file')
        print(colorama.Fore.GREEN+"Plese Wait...")
        start_time = time.time()
        try:
                os.mkdir(os.getcwd()+"\\results")
        except:
                pass
        try:
                os.mkdir(os.getcwd()+f"\\results\\DOMAIN_SORTER")
        except:
                pass
        combo = open(filename,"r",errors="ignore",encoding="utf-8")
        filename = filename.removesuffix(".txt")
        sorted_domains = []
        try:
            for line in combo:
                try:
                        domain= str(line.split("@")[1]).split(":")[0]
                        with open(os.getcwd()+f"\\results\\DOMAIN_SORTER\\{domain}.txt","a",encoding="utf-8",errors="ignore") as f:
                                f.write(line.strip()+"\n")
                except:
                    pass
            dir = os.listdir(os.getcwd()+f"\\results\\DOMAIN_SORTER\\")
            dict_info = {} 
            for item in dir:
                with open(os.getcwd()+f"\\results\DOMAIN_SORTER\\"+item.strip(),errors="ignore") as l: 
                    k = l.readlines()
                item = item.replace(".txt","")
                dict_info[item] = int(len(k))
        except:
            pass
            
        d1 =[]
        d2 = []
        result = sorted(dict_info.items() , key=lambda t : t[1])
        for name,value in result:
                d1.append(name)
                d2.append(value)
        d_1 = d1[-10:]
        d_2 = d2[-10:]
        from matplotlib import pyplot as plt
        plt.figure(facecolor='#363636')
        ax = plt.axes()
    
        # Setting the background color of the
        # plot using set_facecolor() method
        ax.set_facecolor("#363636")
        ax.set_xlabel("x-label", color="red")
        ax.tick_params(axis='x', colors='red')
        ax.tick_params(axis='y',colors='red')
        ax.set_xlabel('x-label',color='red')    
        plt.xticks(rotation=90)
        plt.bar(d_1,d_2)
        plt.tight_layout()
        plt.show()

        
    
        # Setting the background color of the
        # plot using set_facecolor() method
        plt.figure(facecolor='#363636')
        ax = plt.axes()
        ax.set_facecolor("#363636")
        ax.set_xlabel("x-label", color="red")
        ax.tick_params(axis='x', colors='red')
        ax.tick_params(axis='y',colors='red')
        ax.set_xlabel('x-label',color='red')
        plt.xticks(rotation=90)
        plt.bar(d1,d2)
        plt.tight_layout()
        plt.subplots_adjust(
        top=0.969,
        bottom=0.495,
        left=0.08,
        right=0.977,
        hspace=0.2,
        wspace=0.2
    )
        plt.show()
    @f1
    def check_domains():
        os.system('cls')
        start = time.time()
        PrintGradient("#00FFFF","#FF69B4",NAME)
        domainslst = []
        combo = []    
        filename=getcombo('combo-file')
        TP = 0
        cpm = 0
        try:
                os.mkdir(os.getcwd()+"\\results")
        except:
                pass
        try:
                os.mkdir(os.getcwd()+"\\results\\DOMAIN_HUNTER")
        except:
                pass
        namy = '[DOMAIN - HUNTER] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        newcombo = []
        with open(filename, "r",encoding="utf-8",errors="ignore") as file:
            for line in file:
                combo.append(line.strip())  

        with open(os.getcwd()+"\\REQUIRMENTS\\DATA.txt","r",encoding="utf-8",errors="ignore") as file:
            for line in file:
                domainslst.append(line.strip())
        x = 0
        p = 0
        k = len(combo)
        for line in combo:
            p = p+1
            end = time.time()
            total = end-start
            TP = round(total)
            cpm = int(round((p/TP)*60))
            cps =  int(round((p/TP)))   
            domain  = str(line.split("@")[1]).split(":")[0]
            if domain.strip() in domainslst:
                x=x+1
                ctypes.windll.kernel32.SetConsoleTitleW(f"|GOAT-ALLL IN ONE|  |VERSION|:3.8   |MODULE|:(Domain Hunter) |CPS:{format(cps,',')}| |CPM: {format(cpm,',')}| |Hits: {format(x,',')}/{format(k,',')}|  |All: {format(p,',')}/{format(k,',')}| ")
                with open(os.getcwd()+"\\results\\DOMAIN_HUNTER\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                    file.write(line.strip()+"\n")
    import colorama


    @f1
    def Keywords_Cleaner(file=None):
        def clean(file):
            if file is None: filee =  getcombo("keywords")
            else: utf8open = file

            output = []
            blacklisted = ["#", "+", "*", "?", '"', "/", "&", "|", "(", ")", "{", "}", "[", "]", ".", ",", "$", "%", "^", "@", "!", "<", ">", ";", ":"] # +* ?"/&|(){}[].,$#%^@!<>;:
            if file is None:
                input_file = open(filee, "r",errors='ignore')
            else: input_file = utf8open
            for line in input_file:

                        # Remove non ascii
                        line = line.encode("ascii", "ignore").decode()

                        line = line.strip()

                        line = line.replace("\n", "")

                        line = line.replace("\t", "")

                        line = line.replace("_", " ")

                        line = line.replace("-", " ")

                        line = line.replace("\\", "")

                        line = line.replace("  ", " ")

                        line = line.replace("   ", " ")

                        line = line.replace("    ", " ")

                        line = line.replace("     ", " ")

                        for char in blacklisted:
                            line = line.replace(char, "")

                        if len(line) != 0 and line not in output and "amp;" not in line and not line.isdecimal():
                            output.append(line)

            output.sort(key=len)
            d = []
            bad_words = ["http", "www", "com"]
            namy = '[Cleaned - Urls] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
            for line in output:
                if not any(bad_word in line for bad_word in bad_words):
                    if line.count(" ") > 1 and line.count(" ") < 3:
                        if file is None:
                            with open(os.getcwd()+f"\\results\\KEYWORDS_FROM_URLS\\{namy}",'a',encoding="utf-8",errors="ignore") as f: 
                                f.write(line + "\n")
                        else:
                            d.append(line.strip())
            return d        
        
    @f1
    def keywords_from_urls():
        os.system("cls")
        try:
            sys =  input("[!] Clean Keywords after Extraction? (y,n): ").strip().lower()
            os.system("cls")
            if sys == "yes":
                sys = 'y'
            elif sys == "no":
                sys = 'n'
        except:
            sys = "n"
                
        try:
                os.mkdir(os.getcwd()+"\\results")
        except FileExistsError:
                pass
        try:
                os.mkdir(os.getcwd()+f"\\results\\KEYWORDS_FROM_URLS")
        except FileExistsError:
                pass
        links = []
        combo = getcombo("Urls")
        l = 0
        with open(combo,"r",encoding="utf-8",errors="ignore") as f:
            for line in f:
                k=0
                l+=1
                line = line.strip()
                links.append(line)
            keywords = []
            for link in links:  
                keywords.append(re.findall(r'\/[^\/]+\/(.*)\/', link))
            keywordes = []
            for keyword in keywords:
                k +=1
                keywordes.append(keyword)
            if sys == 'y':
                keywordes=Keywords_Cleaner(keywordes)
                

            namy = '[Keywords - Urls] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
            with open(os.getcwd()+f"\\results\\KEYWORDS_FROM_URLS\\{namy}",'a',encoding="utf-8",errors="ignore") as f:
                #keywordes = Keywords_Cleaner(keywordes)
                for line in keywordes:
                    #print("D"+str({len(keywordes)}))
                    try:
                        if type(line) == list:
                            for linee in line:
                                pass
                                f.write(linee+"\n")
                        else:
                            print(line)
                            f.write(line)
                    except:
                        pass

    #!DIDNT FINISH THE PARSER YET
    from my_fake_useragent import UserAgent 
    def random_ua():
            x = UserAgent()
            ua = x.random
            return ua 

    from urllib.parse import urlparse
    from requests.adapters import SOCKSProxyManager
    def Google_Parser():
        results = []
        def geturls(soup,results):
            for d in soup.find_all("div", class_="yuRUbf"):
                    for a in d.find_all('a'):
                        link = a['href']
                        print(f"{link}")
                        upm+=1
                        linkes+=1
                        filter(link)
                        if "translate.google.com" in link:
                            link = link.split("&u=")[1]
                        if link not in results:
                            results.append(link)
                            domain = urlparse(link).netloc
                            try:
                                domain = domain.replace("www.","")
                            except:
                                pass
                            if domain not in blacklist:
                                if '=' in link:
                                    valid+=1
                                    ink+=1
        #url = f"https://www.google.com/search?q={urllib.parse.quote(dork)}&num=50&start={page*10}"
        dorks = getcombo("Dorks")
        dorks = []
        print("socks4\nsocks5\nhttp")
        proxy_type = input("\n!GoatAio:")
        with open(dorks,errors="ignore",encoding='utf-8') as f:
            for line in f:
                dorks.append(line.strip())
        proxypool = getcombo("Proxies")
        proxies = []
        with open(proxypool,errors="ignore",encoding='utf-8') as f:
            for line in f:
                proxies.append(line.strip())
        socks4lst = []
        socks5lst = []
        http = []
        if proxy_type == "1":
            for proxy in proxies:
                socks4 = "socks4://"+str(proxy)
                socks4lst.append(socks4)

        elif proxy_type == "2":
            for proxy in proxies:
                socks5 = "socks5://"+str(proxy)
                socks5lst.append(socks5)
        
        elif proxy_type == "2":
            for proxy in proxies:
                proxies = {
                'http': f'http://{proxy}',
                'https': f'http://{proxy}',}
                http.append(proxies)
        for dork in dorks:
            headerz = {'User-Agent' : f'{random_ua()}'} 
            if proxy_type == "1":
                for i in range(5):
                    i = i-1
                    session = requests.Session()
                    session.mount(random.choice(socks4lst), SOCKSProxyManager)
                    resp = session.get(url = f"https://www.google.com/search?q={urllib.parse.quote(dork)}&num=50&start={i*10}")
                    soup = BeautifulSoup(resp.text, 'html.parser')
                    geturls(soup,results)
                    
    #! THE ABOVE fUNCTION DOSENT WORK 




    @f1
    def lowercase_pass():
        newc=[]
        combo = getcombo('combo-file')
        try:
                os.mkdir(os.getcwd()+"\\results")
        except:
                pass
        try:
                os.mkdir(os.getcwd()+f"\\results\\LOWER_PASSWORD")
        except:
                pass
        
        with open(combo, "r",encoding="utf-8",errors="ignore") as file:
            combo = file.readlines()
        for line in combo:
            password = line.split(":")[1]
            passowrd_low = password.lower()
            line = line.replace(password,passowrd_low)
            newc.append(line)
        namey =     '[Lower - Password] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'    
        with open(os.getcwd()+f"\\results\\LOWER_PASSWORD\\"+namey, "a",encoding="utf-8",errors="ignore") as file:
            for line in newc:
                file.write(line.strip()+"\n")

    @f1
    def upper_password():
        newc=[]
        combo = getcombo('combo-file')
        try:
                os.mkdir(os.getcwd()+"\\results")
        except:
                pass
        try:
                os.mkdir(os.getcwd()+f"\\results\\UPPER_PASSWORD")
        except:
                pass
        
        with open(combo, "r",encoding="utf-8",errors="ignore") as file:
            combo = file.readlines()
        for line in combo:
            password = line.split(":")[1]
            passowrd_upper = password.upper()
            line = line.replace(password,passowrd_upper)
            newc.append(line)
        namey ='[Upper - Password] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+f"\\results\\UPPER_PASSWORD\\"+namey, "a",encoding="utf-8",errors="ignore") as file:
            for line in newc:
                file.write(line.strip()+"\n")
    @f1
    def add_prefix_to_password():
        newc=[]
        combo = getcombo('combo-file')
        prefix = input("Prefix: ")
        try:
                os.mkdir(os.getcwd()+"\\results")
        except:
                pass
        try:
                os.mkdir(os.getcwd()+f"\\results\\PREFIX_PASSWORD")
        except:
                pass
        
        with open(combo, "r",encoding="utf-8",errors="ignore") as file:
            combo = file.readlines()
        for line in combo:
            password = line.split(":")[1]
            passowrd_prefix = str((str(prefix).strip()+str(password).strip())).strip() 
            line = line.replace(password,passowrd_prefix)
            newc.append(line)
        namey ='[Prefix - Password] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+f"\\results\\PREFIX_PASSWORD\\"+namey, "a",encoding="utf-8",errors="ignore") as file:
            for line in newc:
                file.write(line.strip()+"\n")

    @f1
    def add_suffix_to_password():
        newc=[]
        combo = getcombo('combo-file')
        suffix = input("Suffix: ")
        try:
                os.mkdir(os.getcwd()+"\\results")
        except:
                pass
        try:
                os.mkdir(os.getcwd()+f"\\results\\SUFFIX_PASSWORD")
        except:
                pass
        
        with open(combo, "r",encoding="utf-8",errors="ignore") as file:
            combo = file.readlines()
        for line in combo:
            password = line.split(":")[1]
            passowrd_suffix = str((password.strip()+suffix.strip())).strip() 
            line = line.replace(password,passowrd_suffix)
            newc.append(line)
        namey ='[Suffix - Password] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+f"\\results\\SUFFIX_PASSWORD\\"+namey, "a",encoding="utf-8",errors="ignore") as file:
            for line in newc:
                file.write(line.strip()+"\n")




@f1
def Filter_urls():
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
        #cleaned
            os.mkdir(os.getcwd()+f"\\results\\ClEANED_URLS")
    except:
            pass
    combo = getcombo('urls-file')
    with open(combo,"r",encoding="utf-8",errors="ignore") as file:
        URLS = file.readlines()

    bad_urls =            [ 'https://bing',
                            'https://wikipedia',
                            'https://stackoverflow',
                            'https://amazon',
                            'https://google',
                            'https://microsoft',
                            'https://youtube',
                            'https://reddit',
                            'https://quora',
                            'https://telegram',
                            'https://msdn',
                            'https://facebook',
                            'https://apple',
                            'https://twitter',
                            'https://instagram',
                            'https://cracked',
                            'https://nulled',
                            'https://yahoo',
                            'https://gbhackers',
                            'https://github',
                            'https://www.google',
                            'https://docs.microsoft',
                            'https://sourceforge',
                            'https://sourceforge.net',
                            'https://stackoverflow.com',
                            'https://www.facebook',
                            'https://www.bing', 
                            'https://www.bing.com', 
                            'https://www.bing.com/ck/a?!&&p=',
                            'https://bing',
                            'https://wikipedia',
                            'https://stackoverflow',
                            'https://amazon',
                            'https://google',
                            'https://microsoft',
                            'https://youtube',
                            'https://reddit',
                            'https://quora',
                            'https://telegram',
                            'https://msdn',
                            'https://facebook',
                            'https://apple',
                            'https://twitter',
                            'https://instagram',
                            'https://cracked',
                            'https://nulled',
                            'https://yahoo',
                            'https://gbhackers',
                            'https://github',
                            'https://www.google',
                            'https://docs.microsoft',
                            'https://sourceforge',
                            'https://sourceforge.net',
                            'https://stackoverflow.com',
                            'https://www.facebook',
                            'https://www.bing', 
                            'https://www.bing.com', 
                            'https://www.bing.com/ck/a?!&&p=',
                            'https://search.aol.com',
                            'https://search.aol',
                            'https://r.search.yahoo.com',
                            'https://r.search.yahoo',
                            'https://www.google.com',
                            'https://www.google',
                            'https://www.youtube.com',
                            'https://yabs.yandex.ru',
                            'https://www.ask.com',
                            'https://www.bing.com/search?q=',
                            'https://papago.naver.net',
                            'https://papago.naver']
    cleaned = []
    for line in URLS:
        for url in bad_urls:
            if line.startswith(url):
                pass
        else:
            cleaned.append(line)
    cleaned = listset(cleaned)
    namy ='[Cleaned - Urls] {   '+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\ClEANED_URLS\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
        for line in cleaned:
            file.write(line.strip()+"\n")


def write_sqls(namye,lista,date):
    def namy(namy1):
        #f'[{namy1} - Hits] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        return f'[{namy1} - Hits] '.strip()+'{'+str(date)[:-7].replace(':','-')+'}.txt'

    try:
        with open(os.getcwd()+"\\results\\SQL_HITS\\"+namy(namye),"a",encoding="utf-8",errors="ignore") as f:
                        f.write(lista[-1]+"\n")
    except Exception as e:
                    pass
@f1
def SQL_SCANNER():
    namy ='[SQL - Hits] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    hits = []
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
        #cleaned
            os.mkdir(os.getcwd()+f"\\results\\SQL_HITS")
    except:
            pass
    date = datetime.datetime.now()
    combo = getcombo('urls-file')
    with open(combo,"r",encoding="utf-8",errors="ignore") as file:
            start = time.time()
            os.system("cls")
            PrintGradient("#00FFFF","#FF69B4",NAME)
            cpm = "calculating"
            MySQL_hits = []
            MsSQl_hits = []
            PostGRES_hits = []
            Oracle_hits = []
            MariaDb_hits = []
            all_Sql_hits = []
            TP = 0 
            MySQL = 0
            MsSQL = 0
            PostGRES = 0
            Oracle = 0
            MariaDb = 0
            sqls = 0
            Errorr  = 0
            Nonee =0
            retries = 0
            nothing = 0
            import requests
            #ctypes.windll.kernel32.SetConsoleTitleW
            URLS = file.readlines()
            retries2 = len(URLS)
            check = "'"
            for line in URLS:
                if "=" not in line:
                    pass
                else:

                    retries+=1
                    try:
                        checker = requests.post(line + check)
                        if "MySQL" in checker.text or "mysql" in checker.text:
                            hits.append(line.strip())
                            MySQL_hits.append(line.strip())
                            MySQL+=1
                            sqls+=1
                        elif "native client" in checker.text or "Native Client" in checker.text:
                            hits.append(line.strip())
                            MsSQl_hits.append(line.strip())
                            MsSQL+=1
                            sqls+=1
                        elif "syntax error" in checker.text or "Syntax Error" in checker.text:
                            hits.append(line.strip())
                            PostGRES_hits.append(line.strip())
                            PostGRES+=1
                            sqls+=1
                        elif "ORACLE" in checker.text or "oracle" in checker.text:
                            hits.append(line.strip())
                            Oracle_hits.append(line.strip())
                            Oracle+=1
                            sqls+=1
                        elif "MariaDB" in checker.text or "mariadb" in checker.text:
                            hits.append(line.strip())
                            MariaDb_hits.append(line.strip())
                            MariaDB+=1
                            sqls+=1
                        elif "You have an error in your SQL syntax;" in checker.text:
                            hits.append(line.strip())
                            all_Sql_hits.append(line.strip())
                            sqls+=1
                            Nonee+=1
                        else:
                            nothing+=1

                    except:
                        Errorr+=1

                    #os.system("cls")
                    end = time.time()
                    total = end-start
                    TP = round(total)
                    try:
                        cpm = int(round((retries/TP)*60))
                    except:
                        pass
                    os.system("cls")
                    PrintGradient("#00FFFF","#FF69B4",NAME)
                    ctypes.windll.kernel32.SetConsoleTitleW(f"|GOAT-ALLL IN ONE|  |VERSION|:3.8   |MODULE|:(SQLI_SCANNER) STATS= CPM:{cpm}  Nothing:{nothing}   Nones: {Nonee}     MYSQL= {MySQL}   MsSQL: {MsSQL}   PostGRES: {PostGRES}   Oracle: {Oracle}   MariaDB: {MariaDb}    OVR(SQLS): {sqls}    ERORRS: {Errorr}   Checks:{retries}   TimePassed:{TP}")
                    #print(f"\rNothing:{nothing} ||Nones: {Nonee} || MYSQL= {MySQL} || MsSQL: {MsSQL} || PostGRES: {PostGRES} || Oracle: {Oracle} || MariaDB: {MariaDb} || OVR(SQLS): {sqls} || Erros:{Errorr} || Checks:{retries}\r",end="\r")
                    number_format = '{:>4}'
                    number_format2 = '{:<5}'
                    number_format3 = '{:<7}'
                    number_format4 = '{:>7}'
                    number_format5 = '{:<7}'

                    output = f"""\n\n\n{res}  
                                [{cy}MySql                    {ma}{number_format.format(f'{str(MySQL).format(",")}')}{res}]
                                [{cy}MsSql                    {lm}{number_format.format(f'{str(MsSQL).format(",")}')}{res}]
                                [{cy}PostgreSQL               {bl}{number_format.format(f'{str(PostGRES).format(",")}')}{res}]
                                [{cy}Oracle                   {lb}{number_format.format(f'{str(Oracle).format(",")}')}{res}]
                                [{cy}MariaDb                  {gr}{number_format.format(f'{str(MariaDb).format(",")}')}{res}]

                                [CPM: {gr}{number_format2.format(f'{str(cpm).format(",")}')}{res}    Errors: {ree}{number_format3.format(f'{str(Errorr).format(",")}')}{res}]

                                [      {cy}{number_format4.format(f'{str(retries).format(",")}')} {res}/ {cy}{number_format5.format(f'{str(retries2).format(",")}')}{res}      ]"""

                    centered_output=center(output)

                    print(centered_output)
                    
                    
                    
                    
                    write_sqls("All",hits,date)
                    write_sqls("Postgress",PostGRES_hits,date)
                    write_sqls("Oracle",Oracle_hits,date)
                    write_sqls("Mariadb",MariaDb_hits,date)
                    write_sqls("MSsql",MsSQl_hits,date)
                    write_sqls("MYsql",MySQL_hits,date)
                    write_sqls("SQLS_Only",all_Sql_hits,date)

        
                    

        

def get_hwid():
    # Get the CPU name and version
    cpu_name = platform.processor()
    cpu_version = platform.machine()

    # Get the OS name and version
    os_name = platform.system()
    os_version = platform.release()

    # Concatenate the CPU and OS information into a single string
    hwid = f"{cpu_name} ({cpu_version}), {os_name} {os_version}"

    # Return the HWID
    return hwid


            
@f1
def Join_multiple_combos(): 
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+f"\\results\\JOINED_COMBOS")
    except:
            pass
    biglist=[]
    files = []
    combo = getcombo('combo-file (CHOOSE MULTIPLE)')
    for file in combo:
        files.append(file)

    try:
        for line in combo:
            with open(line,"r",encoding="utf-8",errors="ignore") as file:
                biglist.append(file.readlines())
    except:
        pass 
    namy = namy ='[Joined - Combo] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\JOINED_COMBOS"+namy,encoding="utf-8",errors="ignore") as file:
        for line in biglist:
            file.write(line.strip+"\n")



@f1
def get_pagetypes_from_urls():
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\PGT_FROM_URLS")
    except:
            pass
    namy = '[Pagetypes-Urls] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    combo=getcombo('urls-file')
    def redupe(litss):
        nodupe = listset(litss)
        return nodupe
    PageTypes = []
    with open(combo,"r",encoding = "utf-8",errors="ignore") as urls:
        for line in urls.readlines():
            string = line
            match = re.search(r"([^\/\.]*)\.([^\/.]*|[^\/.]*\.|gov\.rw|com\.au|add\.YourOwnDommainExtentionsHereIfItHasMultipleDots|co\.za|ca\.us)\/[^\.]*[^\/]*\.([a-zA-Z1-9]*)\?([^=&]*)=",string)

            if match:
                pre  = match.group()

                string = pre 

                match = re.search(r"\?(.*)", string)

                if match:
                    query_string = match.group(1)
                    if len(query_string) >2: 
                        PageTypes.append(query_string)
                    else:
                        pass 
    pagetypes = redupe(PageTypes)
    with open(os.getcwd()+"\\results\\PGT_FROM_URLS\\"+namy,'a',encoding='utf8',errors='ignore') as file:
        for line in pagetypes:
            file.write(str(line).strip()+"\n")


def get_mainlist(combo,threads):
    lst=[]
    combo=combo
    for line in combo:
        lst.append(line)
    size = len(lst)
    indx = int(size)/int(threads)
    print(indx)
    sublist1 =[]
    mainlist=[]
    for i in lst:
        sublist1.append(i)
        if len(sublist1)==int(indx):
            mainlist.append(sublist1)
            sublist1=[]
        else:
            pass
    return mainlist


def HASH(password):
    """
    Hashes the given password using the SHA-256 algorithm   
    """
    hashed_password = hashlib.sha256(str(password).encode()).hexdigest()
    return hashed_password



def login(username, password,HWID):
    req = requests.get(f"{website}"+f'login/{username.strip()}/{password.strip()}/{HWID}')
    data = req.json()
    status = data["status"]
    if bool(status) == True:
        end_date = data["end_date"]
        return [True,end_date]
    else:
        return False



def register(email, username, password,key,HWID):
    req = requests.get(f"{website}"+f"register/{key}/{email}/{username}/{password}/{HWID}")
    data = req.json()
    status = data["status"]
    if status == True:
        return True
    else:
        return False

def RESETHWID(email, password, HWID):
    req = requests.get(f"{website}"+f"resethwid/{email}/{password}/{HWID}")
    data = req.json()
    status = data["status"]
    if status == True:
        return True
    else:
        return False
    
#! THE COMBO LEECHER
def get_combos():
    os.system('cls')
    PrintGradient("#00FFFF","#FF69B4",NAME)
    target = input("Target: ")
    num = 10
    # making it scrape only the first 10

    # setting up the project making lists so that we can use in BEAUTIFUL SOUP
    pagenum = 1
    outlinkstemp = []
    outlinks = []
    inslinks = []
    n = 1
    newlist = []
    tempins = []
    lastdown = []
    templastdowm = []
    # starting project

    while pagenum < num:  # simple loop to scrape page source
        req = requests.get(
            f"https://sqli.cloud/t/combolists?page={pagenum}")
        src = req.text
        soup = BeautifulSoup(src, "html.parser")
        outs = soup.find_all("a")
        pagenum = pagenum+1

        for link2 in outs:  # simple loop to filter only links from the page source
            if 'href' in link2.attrs:
                outlinkstemp.append((str(link2.attrs['href'])))

        for item in outlinkstemp:  # loop to filter only combolists
            if  target in item or target.capitalize() in item or target.lower() in item:
                outlinks.append(item)
    lenlinks = len(outlinks)

    # making the user choose how many combolists to download
    print(f"Found {lenlinks} Dumpable targeted combos")
    nums = int(input(f"How many combolists to Dump [Max == {lenlinks}]? "))
    while nums > lenlinks:

        nums = input(f"How many combolists to Dump [Max == {lenlinks}]? ")
    num = nums
    list1 = []
    for item in range(int(num)):  # loop to scrape form links and show it to user
        try:
            # choosing random combolist from outlinks
            new = random.choice(outlinks)
            if new in list1:
                new = random.choice(outlinks)
        except:
            pass
        # try and except to stop dupliactes from happening
        list1.append(new)
        n = n+1
        newlist.append(new)
    n = 1
    # appending combolist to "newlist"
    mainlist = get_mainlist(newlist)
    def newbest(newlist):
        for i in newlist:  # loop to print to user the 'newlist' and scraping outer uploadee links
            rein = requests.get(i)
            miaw = i[25:len(i)]
            info = (str(n)+": "+miaw)
            n = n+1
            src = rein.text  # taking page source
            soup = BeautifulSoup(src, "html.parser")  # soup
            ins = soup.find_all("a")  # getting all urls in site
            for link in ins:  # loop to filter only links
                if 'href' in link.attrs:
                    tempins.append((str(link.attrs['href'])))
        
    print("Status [Dumping Combolit]")
    threads = int(input("Threads?: "))
    mainlist = get_mainlist(tempins,threads)
    def lasttask(tempins):           
        for item in tempins:
            if 'upload.ee' in item:
                    inslinks.append(item)
                    for line in inslinks:
                        req = requests.get(line)
                        src = req.text
                        soup = BeautifulSoup(src, "html.parser")
                        link = soup.find_all("a")
                    for link3 in link:
                        if 'href' in link3.attrs:
                            templastdowm.append((str(link3.attrs['href'])))
                    for i in templastdowm:  # getting direct download link
                        if "www.upload.ee/download" in i and i  not in lastdown:
                            lastdown.append(i)
    import threading
    def main(combos):
        thread=[] 
        for combo in combos:
            thread1 =threading.Thread(target=lasttask,args=(combo,))
            thread1.start()
            thread.append(thread1)
        for thread2 in thread:
            thread2.join                        
    main(mainlist)
    n = 1
    try:
        os.mkdir(os.getcwd()+"\\results")
    except:
        pass 
    try:
        os.mkdir(os.getcwd()+f"\\results\\COMBO_DUMPER [{target}]")
    except:
        pass 
    Qualities = ["HQ","MQ","UHQ","Public","SHIT","AWESOME"]
    for url in lastdown:
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW(f"|GOAT-ALLL IN ONE|  |VERSION|:3.8   |MODULE|:(Automatic Combo Dumper) Target: {target}  Load: {n}/{nums}  Quality: {random.choice(Qualities)}")
        PrintGradient("#00FFFF","#FF69B4",NAME)
        print(center(f"""

                        {wh}[{ree}Target{wh}]   {wh}( {ree}{target} {wh})
                        {wh}[{ree}Load{wh}]     {wh}( {ree}{n}/{nums} {wh})        
        
        """))
        try:
            path = download(url, f"{os.getcwd()}\\results\\COMBO_DUMPER [{target}]\\combo_{target}_{n}.txt", replace=True,progressbar=True,verbose=False)
        except:
            pass
        n = n+1
    #combining
    os.chdir(os.getcwd()+f'\\results\\COMBO_DUMPER [{target}]\\')
    ans = ('Do you want to combine all combolists? [y,n]: ')
    if ans.lower() == "yes":
        ans = "y"
    elif ans.lower() == "no":
        "n"
    if ans.lower() == "yes":
        os.system(f"copy /b *.txt {target}_COMBO.txt")
        files = os.listdir()
        for file in files:
            if file == f"{target}_COMBO.txt":
                pass
            else:
                os.remove(file)
    else:
        pass

import math
@f1
def dorkbeg():
    os.system("cls")
    dorkgened = 0
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+f"\\results\\DORK_MAKER")
    except:
            pass
    while True:
        keyword = getcombo("keywords")
        if keyword == None:
            pass
        else:
            break
    pagtyes = getcombo("pagetypes [Close to use the default]") 
    if pagtyes == None:
        pagtypes = [
    "item_id=",
    "page_id=",
    "user_id="
    "PRODUCTID=",
    "openBids=",
    "coId=",
    "ProcedureId=",
    "CA=",
    "coID=",
    "option=",
    "sel=",
    "bo_table=",
    "gameId=",
    "Type=",
    "Report=",
    "type_search=",
    "idxno=",
    "secName=",
    "downloadinstructionsmswordzip=",
    "code=",
    "DId=",
    "pre_box=",
    "USER_ID=",
    "bw_pageId=",
    "lang=",
    "pob_evt=",
    "class=",
    "classid=",
    "Page=",
    "Colour+group=",
    "fileName=",
    "local=",
    "rec=",
    "mid=",
    "subCategoryID=",
    "catIds=",
    "specid=",
    "game_id=",
    "fc=",
    "menuCd=",
    "dbs=",
    "CategoryCode=",
    "ActID=",
    "sid=",
    "pcode=",
    "surl=",
    "panelid=",
    "typeProduitOnglet=",
    "CatId=",
    "idx=",
    "sec=",
    "inst=",
    "sec_no=",
    "link=",
    "blogId=",
    "CATEGORY=",
    "branduid=",
    "doc_id=",
    "language=",
    "Content_ID=",
    "Id=",
    "firstlevel=",
    "Param1=",
    "st=",
    "categoryID=",
    "act=",
    "DataSetCode=",
    "categoryid=",
    "rid=",
    "typeId=",
    "categoryId=",
    "pubno=",
    "ProductId=",
    "path=",
    "id_subsection=",
    "symbol=",
    "includeSSTC=",
    "pt=",
    "articleNo=",
    "num=",
    "cat_no=",
    "g_id=",
    "ToDo=",
    "fold=",
    "kwtag=",
    "bookid=",
    "cat_cd2=",
    "req=",
    "uREC_ID=",
    "cpu=",
    "ro=",
    "board_no=",
    "prod=",
    "PageId=",
    "cat%5B%5D=",
    "pageTitle=",
    "docID=",
    "lan=",
    "ipn=",
    "lg=",
    "fuseaction=",
    "title=",
    "faqcategoryId=",
    "id_concurso=",
    "soc=",
    "FileNum=",
    "RANDOMNUM=",
    "ID=",
    "Dockey=",
    "request=",
    "type=",
    "cam=",
    "platform=",
    "idt=",
    "onlygender=",
    "name=",
    "tabid=",
    "cm_sp=",
    "auto=",
    "ACTION=",
    "cache=",
    "ItemDesc=",
    "discussion=",
    "ids=",
    "TYPE=",
    "id1=",
    "pageID=",
    "forum=",
    "objectgroup_id=",
    "pp011type=",
    "bug_id=",
    "val=",
    "source=",
    "it_id=",
    "svc=",
    "zz=",
    "cmpy_id=",
    "target=",
    "pcid=",
    "ClientID=",
    "promoid=",
    "city_id=",
    "com_board_basic=",
    "IDNews=",
    "rel=",
    "cid=",
    "param=",
    "FILE=",
    "cate_no=",
    "panel=",
    "section=",
    "CategoryId=",
    "ID_LINK=",
    "language_id=",
    "SecID=",
    "catoid=",
    "reset=",
    "ctmid=",
    "nocache=",
    "sub=",
    "app=",
    "topic=",
    "Kind=",
    "coid=",
    "idproduct=",
    "idioma=",
    "gameID=",
    "pos=",
    "pg=",
    "refer=",
    "mod=",
    "ShareTicker=",
    "page_source=",
    "WebSiteID=",
    "returnto=",
    "search=",
    "Product_ID=",
    "do=",
    "show=",
    "boparam::wscontent::loadarticle::permalink=",
    "redirected=",
    "MOD=",
    "id_noticia=",
    "issue=",
    "articleid=",
    "GameID=",
    "from=",
    "uid=",
    "a_id=",
    "s_id=",
    "siteId=",
    "component=",
    "amendCommerceItemId=",
    "menu=",
    "atchFileId=",
    "spName=",
    "nav_id=",
    "raceid=",
    "tid=",
    "consultanswers=",
    "template=",
    "fund=",
    "train_station_id=",
    "method=",
    "fid=",
    "medium=",
    "USParams=",
    "script=",
    "sfvrsn=",
    "idnoticia=",
    "kind=",
    "xmlid=",
    "article_id=",
    "area_id=",
    "Category=",
    "showtopic=",
    "PROGRAM=",
    "main=",
    "include=",
    "europe=",
    "mailtype=",
    "user_id=",
    "sec_id=",
    "list=",
    "portlet=",
    "ver=",
    "tgbn=",
    "_T=",
    "pid=",
    "offset=",
    "pageno=",
    "category=",
    "helpmedothenews11am=",
    "cat=",
    "type_id=",
    "ProductID=",
    "SEC=",
    "ruta_reporte=",
    "la=",
    "photo=",
    "type_id1=",
    "view=",
    "pageNo=",
    "PartnerSpId=",
    "param2=",
    "cat_id=",
    "RootFolder=",
    "subcat=",
    "zstrat=",
    "mcver=",
    "mode=",
    "op=",
    "plik=",
    "lpse=",
    "filePath=",
    "lang_id=",
    "pic=",
    "CFRPart=",
    "fn=",
    "cat_code=",
    "IncludeBlogs=",
    "categorycode=",
    "ACLogoutClicked=",
    "bid=",
    "suBD=",
    "ct=",
    "locator=",
    "Cat2=",
    "Class_ID=",
    "Fun=",
    "bbsid=",
    "item=",
    "vendor_id=",
    "WT=",
    "fileId=",
    "CategoryID=",
    "model=",
    "doc=",
    "courseid=",
    "key=",
    "icid=",
    "ric=",
    "userid=",
    "ref=",
    "Panel=",
    "pageId=",
    "product_id=",
    "page_id=",
    "moduleId=",
    "skin_id=",
    "category1=",
    "BRCHR_VRSN_ID=",
    "GameId=",
    "ArticleID=",
    "style=",
    "Paged=",
    "symb=",
    "IsPstPack=",
    "CatID=",
    "category_id=",
    "_id=",
    "manufacturers_id=",
    "cite=",
    "page=",
    "active=",
    "PageID=",
    "ruta=",
    "evento=",
    "deviceCategory=",
    "query_type=",
    "typeofrhyme=",
    "webfids_type=",
    "TOPIC_ID=",
    "novelid=",
    "categoryPath=",
    "CurrentForm=",
    "topicid=",
    "StatusRequired=",
    "TypeId=",
    "Cat=",
    "contenttypeid=",
    "hash=",
    "product=",
    "PanelID=",
    "file=",
    "mt=",
    "itemID=",
    "PRODUCT_ID=",
    "itemId=",
    "where=",
    "cgid=",
    "resourceID=",
    "APPID=",
    "category_redirect=",
    "isold=",
    "UserID=",
    "projet=",
    "si=",
    "category[]=",
    "productid=",
    "lt=",
    "id=",
    "IdAkrKP=",
    "path=/birthselect.m?sort=",
    "gameid=",
    "displayLevel=",
    "saint_id=",
    "attachType=",
    "qnum=",
    "CAT=",
    "nc=",
    "song=",
    "a_listcnt=",
    "cPath=",
    "open=",
    "no=",
    "item_id=",
    "season=",
    "keyword=",
    "PRID=",
    "action=",
    "abstract_id=",
    "ubb=",
    "route=",
    "cn=",
    "fa=",
    "productID=",
    "degreeName=",
    "urlquery=",
    "CategoryName=",
    "idSectionRacine=",
    "lc=",
    "articleID=",
    "fileticket=",
    "URL=",
    "cboPufNumber=",
    "secID=",
    "fileTask=",
    "ItemId=",
    "tf=",
    "upi=",
    "year=",
    "FIORG=",
    "ItemID=",
    "dest=",
    "dispatch=",
    "productId=",
    "info_id=",
    "qikan_type_id=",
    "tick=",
    "main_page=",
    "site="
    ]
    else:
        pagtypes = []
        with open(pagtyes,"r",encoding="utf8",errors="ignore") as file:
            for line in file:
                pagtypes.append(line.strip())

        
    os.system("cls")
    PrintGradient("#00FFFF","#FF69B4",NAME)
    keywords = []
    with open(keyword,"r",encoding="utf-8",errors='ignore') as f:  
        for line in f:
            keywords.append(line.strip())

    non_repeated = []
    loops = int(input("how many dorks to generate: "))
    # numbers = [1,2,3,4,5,6,7,8,9,10]
    #print("==")
    dorks = []
    d = len(non_repeated)
    time = datetime.datetime.now()
    r = math.ceil(loops/7)
    threads = input("Threads:")
    d = int(math.ceil(r/int(threads))) 
    def generate(r,time):
        dorks = []
        for _ in range(int(math.ceil(r))):
            #ctypes.windll.kernel32.SetConsoleTitleW(f"|GOAT-ALLL IN ONE|  |VERSION|:3.8   |MODULE|:(Dork Generator)  Generated Dorks:{dorkgened}")
            keyword = random.choice(keywords)
            pt1 = random.choice(pagtypes)
            pt2 = random.choice(pagtypes)
            xkeyword = random.choice(keywords)
            dorks.append(f'{keyword} ext:php inurl:{pt1}')#1
            dorks.append(f'{keyword} *{xkeyword} ext:php inurl:{pt1}')#2
            dorks.append(f'{keyword} ~{xkeyword} ext:php inurl:{pt1}')#3
            dorks.append(f'{keyword} ext:php inurl:{pt1}')#4
            dorks.append(f'({keyword}) (ext:php & inurl:{pt1})')#5
            dorks.append(f'({keyword})+ext:php > ({xkeyword}) / inurl:{pt1}')#6
            dorks.append(f'inurl:{pt1} ({keyword} | {xkeyword}) > ext:{pt2}')#7 
            #dorkgened +=30
        non_repeated = listset(dorks)

        namy = '[Dork-Maker] {'+str(time)[:-7].replace(':','-')+'}.txt' 
        with open(os.getcwd()+f"\\results\\DORK_MAKER\\{namy}" , "a", errors="ignore") as f:
            for line in non_repeated:
                    f.write(line+"\n")
    
    def main(threadss,d,time):
        import threading
        thread=[]
        for _ in range(threadss):
            thread1 =threading.Thread(target=generate,args=(d,time))
            thread1.start()
            thread.append(thread1)
        for thread2 in thread:
            thread2.join
    main(int(threads),d,time)


@f1
def auth():
    os.system("cls")
    PrintGradient("#00FFFF","#FF69B4",NAME)
    ctypes.windll.kernel32.SetConsoleTitleW(f"|GOAT-ALLL IN ONE|  |VERSION|:3.8   |MODULE|:(AUTH)")
    print('\n')
    print(f"{wh}[{ree}1{wh}] Login")
    print(f"{wh}[{ree}2{wh}] Register")
    print(f"{wh}[{ree}3{wh}] reset Hwid\n")
    resp = input(f"{wh}[{ree}!{wh}] Goat Aio: ")
    if resp == "3":
        RESETHWID(email=input("email: "),password=input("password: "),HWID=get_hwid())
    if resp == "2":
        #email, username, password,key,HWId
        register(email=input("email: "),username=input("username: "),password=input("password: "),key=input("key: "),HWID=get_hwid())
    if resp == "1":
        response = login(username=input("Username:"),password=input("password:"),HWID=get_hwid())
        #print(response)
        #time.sleep(5)   
        if bool(response[0]) == True:
            while True:
                os.system("cls")
                print("                                     ",end="")
                PrintGradient("#00FFFF","#FF69B4",NAME)
                try:    
                    try:
                        # Current date
                        current_date = datetime.datetime.now()
                        # Target date
                        r = str(response[1].split("T")[0]).split("-")
                        end_date = datetime.datetime(int(r[0]),int(r[1]),int(r[2]))
                        difference = end_date - current_date
                        difference = str(difference).split(",")[0]
                    except Exception as e :
                        try:
                            r = str(response[1].split(" ")[0]).split("-")
                            end_date = datetime.datetime(int(r[0]),int(r[1]),int(r[2]))
                            difference = end_date - current_date
                            difference = str(difference).split(",")[0]
                        except:
                            os.system("cls")
                            auth()
                except:
                        os.system("cls")
                        auth()
                ctypes.windll.kernel32.SetConsoleTitleW(f"|GOAT-ALLL IN ONE|  |VERSION|:3.8   |MODULE|:(Main-Menu)  |SUBSCRIPTION|:({difference})")
                print(f"\n{wh}[{ree}1{wh}] Password Edits")
                print(f"{wh}[{ree}2{wh}] Email Edits")
                print(f"{wh}[{ree}3{wh}] Combo Edits")
                print(f"{wh}[{ree}4{wh}] Combo Dumping")
                print(f"{wh}[{ree}5{wh}] Parsers")
                print(f"{wh}[{ree}6{wh}] Credits")
                Choicee = input(f"\n{wh}[{ree}!{wh}] Goat Aio: ")
                if Choicee == "1":
                    os.system("cls")
                    PrintGradient("#00FFFF","#FF69B4",NAME)
                    ctypes.windll.kernel32.SetConsoleTitleW("|GOAT-ALLL IN ONE|  |VERSION|:3.8   |MODULE|:(Password-Edits)")
                    print(f"\n{wh}[{ree}1{wh}] password_limit")
                    print(f"{wh}[{ree}2{wh}] Password hex")
                    print(f"{wh}[{ree}3{wh}] Password extractor")
                    print(f"{wh}[{ree}4{wh}] lowercase password")
                    print(f"{wh}[{ree}5{wh}] uppercase password")
                    print(f"{wh}[{ree}6{wh}] add prefix to password")
                    print(f"{wh}[{ree}7{wh}] add suffix to password")
                    print(f"{wh}[{ree}99{wh}] Main Menu")
                    choice = input(f"\n{wh}[{ree}!{wh}] Goat Aio: ")
                    if choice == "1":
                        limit = input(f"\n{ye}limit EX[4,5,6,7]: ")
                        password_limit(limit)
                    elif choice == "2":
                        hex = input(f"\n{ye}HEX EX[#,$,*]: ")
                        password_hex(hex)
                    elif choice == "3":
                        password_extracor()
                    elif choice == "4":
                        lowercase_pass()
                    elif choice == "5":
                        upper_password()
                    elif choice == "6":
                        add_prefix_to_password()
                    elif choice == "7":
                        add_prefix_to_password()
                    elif choice == "99":
                        pass  
                
                elif Choicee == "2":
                    os.system("cls")
                    PrintGradient("#00FFFF","#FF69B4",NAME)
                    ctypes.windll.kernel32.SetConsoleTitleW("|GOAT-ALLL IN ONE|  |VERSION|:3.8   |MODULE|:(Email-Edits)")
                    print(f"\n{wh}[{ree}1{wh}] Domain changer")
                    print(f"{wh}[{ree}2{wh}] Email extractor")
                    print(f"{wh}[{ree}3{wh}] Filter combo by domain")
                    print(f"{wh}[{ree}4{wh}] Email:pass to user:pass")
                    print(f"{wh}[{ree}5{wh}] Domain sorter")
                    print(f"{wh}[{ree}6{wh}] Check domains")
                    #print("[7] remove numbers from emails")
                    print(f"[99] Main Menu")
                    choice = input(f"\n{wh}[{ree}!{wh}] Goat Aio: ")
                    if choice == "1":
                        dom = input("Domain Ex(@gmail.com): ")
                        domain_changer(dom)
                    elif choice == "2":
                        email_extracor()
                    elif choice == "3":
                        domain = input("Domain without(@): ")
                        filter_combo_by_domain(domain)
                    elif choice == "4":
                        EP_TO_UP()
                    elif choice == "5":
                        domain_sorter()
                    elif choice == "6":
                        check_domains()
                    elif choice == "99":
                        pass 
                elif Choicee == "3":
                    os.system("cls")
                    PrintGradient("#00FFFF","#FF69B4",NAME)
                    
                    ctypes.windll.kernel32.SetConsoleTitleW("|GOAT-ALLL IN ONE|  |VERSION|:3.8   |MODULE|:(Combo-Edits)")
                    print(f"\n{wh}[{ree}1{wh}] Combo cleaner")
                    print(f"{wh}[{ree}2{wh}] Reverser")
                    print(f"{wh}[{ree}3{wh}] Combo sorter")
                    print(f"{wh}[{ree}4{wh}] Shuffle")
                    print(f"{wh}[{ree}5{wh}] Redupe")
                    print(f"{wh}[{ree}6{wh}] LQ TO HQ")
                    print(f"{wh}[{ree}7{wh}] Line counter")
                    print(f"{wh}[{ree}99{wh}] Main Menu")
                    choice = input(f"\n{wh}[{ree}!{wh}] Goat Aio: ")
                    if choice == "1":
                        CLEANER()
                    elif choice == "2":
                        reverser()
                    elif choice == "3":
                        combo_sorter()
                    elif choice == "4":
                        shuffle()
                    elif choice == "5":
                        remove_dupes()
                    elif choice == "6":
                        LQTOHQ()
                    elif choice == "7":
                     ComboLineCounter()
                    elif choice == "99":
                        pass  
                    
                elif Choicee == "4":
                    os.system("cls")
                    PrintGradient("#00FFFF","#FF69B4",NAME)
                    ctypes.windll.kernel32.SetConsoleTitleW("|GOAT-ALLL IN ONE|  |VERSION|:3.8   |MODULE|:(Dorking)")
                    print(f"\n{wh}[{ree}1{wh}] Dork Maker")
                    print(f"{wh}[{ree}2{wh}] scrape Pagetypes")
                    print(f"{wh}[{ree}3{wh}] scrape Pageformats")
                    print(f"{wh}[{ree}4{wh}] Get Parameters from Url")
                    print(f"{wh}[{ree}5{wh}] Get keywords from Url")
                    print(f"{wh}[{ree}6{wh}] filter URls")
                    print(f"{wh}[{ree}7{wh}] SQl Scanner")
                    #print(f"{wh}[{ree}8{wh}] Automatic Combo Leecher")
                    print(f"{wh}[{ree}99{wh}] Main Menu")
                    Choice = input(f"\n{wh}[{ree}!{wh}] Goat Aio: ")
                    if Choice== "1":
                        dorkbeg()
                    elif Choice == "2":
                        get_pagetypes()
                    elif Choice == "3":
                        get_pageformats()
                    elif Choice == "4":
                        get_pagetypes_from_urls()
                    elif Choice == "5":
                        keywords_from_urls()
                    elif Choice == "6":
                        Filter_urls()
                    elif Choice == "7":
                        SQL_SCANNER()
                    #elif Choice == "8":
                      #  get_combos()
                    elif Choice == "99":
                        pass
                elif Choicee == "5":
                    os.system("cls")
                    PrintGradient("#00FFFF","#FF69B4",NAME)
                    print("\n{ISNT FINISHED YET WAIT TILL NEXT UPDATE}")
                    time.sleep(5)
                    os.system("cls")
                elif Choicee == "6":
                    print("IQTHEGOAT#0310\n! Y1ZOX7#9758\nKillinMachine#2570")
                    time.sleep(5)
                
        else:
            print("[!] Invalid Choice")
            print("[!] Please try again")
            time.sleep(0.5)
                    
while True:
    auth()  
