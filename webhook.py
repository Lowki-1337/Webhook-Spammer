import requests
import ctypes
import time
import os

from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def webhook():
    clear()
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Webhook Spammer => LowkiDev on Github')
    except:
        pass

    
    def title():
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(f'sent => {successful} | failed => {failed} | rl\'s => {ratelimited}')
        except:
            pass

    try:
        webhook = input('[-] Webhook => ')
        message = input('[-] Message => ')
        if message == '':
            message = 'LowkiDev on github'

        username = input('[-] Username => ')
        if username == '':
            username = 'Lowki-1337, LowkiDev on github'

        delete = input('[-] Delete the Webhook? (Y/N) => ')

    except:
        pass

    ratelimited = 0
    successful = 0
    failed = 0

    try:
        while failed < 15:
            r = requests.post(
                webhook, {"content": message, "username": username})
            try:
                if r.json()["retry_after"]:
                    ratelimited += 1
                    title()
                    print(
                        f'[!] rl\'ed | waiting : {r.json()["retry_after"] / 1000}s | {ratelimited} rl\'s')
                    time.sleep(r.json()["retry_after"] / 1000)
            except:
                if r.status_code == 204:
                    successful += 1
                    title()
                    print(f'[=>] {message} | sent : {successful}')
                else:
                    failed += 1
                    title()
                    print(f'[<=] {message} | failed : {failed}')
        print(
            f'deleted | sent => {successful} : rl\'s => {ratelimited} : fails => {failed}')
    except KeyboardInterrupt:
        if delete == 'y':
            requests.delete(webhook)
            input(
                f'webhook deleted | sent => {successful} : rl\'s => {ratelimited} : fails => {failed}')
        elif delete == 'n':
            input(
                f'ended | sent => {successful} : rl\'s => {ratelimited} : fails => {failed}')


webhook()
