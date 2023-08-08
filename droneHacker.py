from my_modules import banner
from my_modules import fly
from my_modules import wifi
from rich.prompt import Confirm, Prompt
from rich.text import Text
from rich.console import Console
from rich import print
from time import sleep
import pyautogui
import os, subprocess, threading

def clearScreen():
    os.system("clear")
clearScreen()
#Main Banner
banner.start_banner()
 
def execute_script(path):
    os.system(f"python3 {path}")

def play_video(path):
    os.system(f"parole -i {path}")

letsfly = threading.Thread(target=execute_script, args=("my_modules/fly.py",))
alert = threading.Thread(target=play_video, args=("my_modules/drone_hunter.mp4",))
#wifi_pass = "droney1216"
#drone_ssid = "evilDrone1"
wifi_pass = "droness425"
drone_ssid  = "evilDrone2"

#Prompt for name
name = ''
console = Console()
text = Text()

def whoareyou():
    global name
    name = Prompt.ask("[cyan]Please Enter Name")
whoareyou()


def user_input():
    global name
    res = Prompt.ask("[cyan]\n{}[/cyan]".format(name))
    if res == "easy":
        print("[bold magenta]\nAnonymous: [/bold magenta]We are launching wifite for you and it should automatically find your interface. Look for [bold red]{}[/bold red]. \nOnce you see it press [bold green]ctrl-c[/bold green] and choose the number next to it.".format(name))
        sleep(2)
        print("[bold magenta]\nAnonymous: [/bold magenta]Wifite will automatically cature the handshake and crack the password.")
        sleep(3)
        os.system("sudo wifite --new-hs --wpa --dict files/wordlist.txt")
        print("[bold magenta]\nAnonymous: [/bold magenta]Once you have the password connect to the [bold red]evilDrone1[/bold red] wifi and enter the wifi password here.")
    elif res == "hard":
        #send CTRL-SHIFT-R to terminal
        print("[bold magenta]\nAnonymous: [/bold magenta]All the tools you need are preinstalled on the new tab in the terminal")
        print("[bold magenta]\nAnonymous: [/bold magenta]Good Luck!")
        sleep(2)
        pyautogui.hotkey('ctrl', 'shift', 't')
        print("[bold magenta]\nAnonymous: [/bold magenta]Once you have the password connect to the [bold red]{}}[/bold red] wifi and enter the wifi password here.".format(drone_ssid))
    elif res == wifi_pass:
        ssid = wifi.get_essid()
        if ssid == drone_ssid:
            banner.hacked_banner()
            print("[bold magenta]\nAnonymous: [/bold magenta]You did it! You hacked the drone! Now type in [bold green]fly[/bold green] to fly the drone to the rooftop of the evil corporation.")
            sleep(3)
        else:
            print("[prompt.ivalid]Not Connected to [bold red]{}[/bold red]. Connect to the drone and type in the password again.".format(drone_ssid))
            user_input()
    elif res == "fly":
        banner.fly_keys()
        print("[bold magenta]\nAnonymous: [/bold magenta]Make sure you click on the window that pops up to use the controls.")
        sleep(3)
        print("[bold magenta]\nAnonymous: [/bold magenta]Ready [bold cyan]3..2..1[/bold cyan].") 
        sleep(3)
        letsfly.start()
        sleep(30)
        alert.start()
        print("[bold magenta]\nAnonymous: [/bold magenta]Once you've landed the drone type in [bold green]landed[/bold green].")
        user_input()
        
    elif res == "landed":
        print("[bold magenta]\nAnonymous: [/bold magenta]You did it! You landed the drone on the rooftop. The drone will automatically connect to the evil corporation's wifi.")
        sleep(3)
        wifi.connect_to_wifi()
        print("[bold magenta]\nAnonymous: [/bold magenta]Now you need to find the secret file, and expose it to the world.")
        sleep(3)
        print("[bold magenta]\nAnonymous: [/bold magenta]Run an nmap scan to find their vulnerable server.[bold red]192.168.8.1 is out of scope[/bold red].")
        user_input()
    elif res == "Flag{DRONES_or_UFOS?!}":
        clearScreen()
        banner.ending()
        exit()
    else:
        print("[prompt.ivalid]Unknown command")
    user_input()

def first_mission():
    print("[bold magenta]\nAnonymous: [/bold magenta]The drone we need to hack is broadcasting WiFi. We set you up with a wireless intrface on monitor mode.")
    sleep(1)
    print("[bold magenta]\nAnonymous: [/bold magenta]Your target is [bold red]evilDrone1[/bold red]. Make sure you only attack that drone or we can get in serious trouble.")
    sleep(1)
    print("[bold magenta]\nAnonymous: [/bold magenta]You have less than 5 minutes to take over the drone. If you think you can do it by yourself type in [bold red]hard[/bold red]. If you want us to help you type in [bold cyan]easy[/bold cyan]. We got your back!")
    user_input()
 
def intro_prompt():
    print("[bold magenta]\nAnonymous: [/bold magenta]You've been chosen for a mission to hack a drone and fly it to the rooftop of an evil corporation.")
    sleep(1)
    print("[bold magenta]\nAnonymous: [/bold magenta]They've got some serious secrets that, once exposed, can save the world. \nYour hacking skills are crucial, and you won't be alone; a skilled team will have your back.")
    sleep(1)
    print("[bold magenta]\nAnonymous: [/bold magenta]It's a risky job, but your bravery can change everything.")
    sleep(3)

    accept = Confirm.ask("[bold magenta]\nAnonymous: [/bold magenta]So, will you accept this mission, hack the drone, and be the hero the world needs?", default=True)
    if accept == True:
            first_mission()
    else: 
        print("[bold magenta]\nAnonymous: [/bold magenta]", ":loudly_crying_face:", "Its okay, not everyone is cut out for saving the world")
intro_prompt()
