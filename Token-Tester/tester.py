import pyfiglet
import requests
from colorama import Fore,Back,Style,init
import time
FileToTest = input("File name >")
FileValid = input("File name for save valid token >")
init(autoreset=True)
with open(FileToTest) as f:
    for line in f:
        TokenToTest = line.strip("\n")
        headers = {'Content-Type': 'application/json', 'authorization': TokenToTest}
        UrlToTest = "https://discordapp.com/api/v6/users/@me/library"
        Req = requests.get(UrlToTest, headers=headers)
        if Req.status_code == 200:
            time.sleep(2)
            print(Fore.LIGHTGREEN_EX + "{} is valid token!".format(TokenToTest))
            with open(FileValid, 'w') as f:
                f.write(TokenToTest)
        else:
            print(Fore.LIGHTRED_EX + "{} is invalid token.".format(TokenToTest))
