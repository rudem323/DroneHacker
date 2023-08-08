import subprocess
import re

def get_essid():
    try:
        output = subprocess.check_output(['iwconfig', 'wlan0']).decode('utf-8')
        essid_match = re.search(r'ESSID:"(.*?)"', output)
        if essid_match:
            return essid_match.group(1)
        else:
            return None
    except subprocess.CalledProcessError:
        return None

def connect_to_wifi():
    subprocess.call(['nmcli', 'device', 'wifi', 'connect', 'evilCorp1', 'password', 'droney1216', 'hidden', 'yes'])

#essid = get_essid()
#if essid:
#    print(essid)
#else:
#    print("Unable to retrieve ESSID.")