from pyfiglet import figlet_format
from termcolor import cprint



def start_banner():
    color = 'cyan'
    banner = figlet_format("\nDRONE HACKER", font = 'ANSI Shadow', width = 200)
    cprint(banner, color)

def hacked_banner():
    color = 'light_green'
    banner = figlet_format("\nDRONE HACKED!!", font= '3d', width = 200 )
    cprint(banner, color, attrs=['blink'])

def fly_keys():
    control = figlet_format("\nCONTROLS", font= '3d', width = 200)
    cprint(control, 'cyan', attrs=['bold'])
    cprint(f"""
     =========================================================   
    |                                                         |
    |     - T: Takeoff                                        |                     
    |     - L: Land                                           |
    |     - W and S: Up and down.                             |                           
    |     - A and D: Rotate left and right.                   |
    |     - Arrow keys: Forward, backward, left and right.    |
    |                                                         |     
     =========================================================
    """, 'yellow')

def alert_banner():
    color = 'red'
    banner = figlet_format("\nALERT!!", font= '3d')
    cprint(banner, color, attrs=['blink'])

def ending():
    color = 'cyan'
    banner = figlet_format("\nTHANK YOU FOR PLAYING", font= '3d', width = 200)
    cprint(banner, color, attrs=['bold', 'blink'])
    