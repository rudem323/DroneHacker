#!/bin/bash

# Check if the script is running with root privileges
if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root."
    exit 1
fi

# Create a user named "dronehacker" with a home directory
useradd -m -s /bin/zsh dronehacker

# Set the password for the new user (You will be prompted to set a password)
passwd dronehacker

# Add to sudo group 
usermod -aG sudo dronehacker

# Grant sudo privileges only for executing /usr/sbin/wifite
echo "dronehacker ALL=(ALL:ALL) /usr/sbin/wifite" >> /etc/sudoers.d/dronehacker
echo "dronehacker ALL=(ALL:ALL) /opt/DroneHacker/dronehacker.py" >> /etc/sudoers.d/dronehacker

#add alias
echo "alias dronehacker='python3 /opt/DroneHacker/droneHacker.py'" >> /home/dronehacker/.zshrc
echo "alias setup='pip install -r /opt/DroneHacker/requirements.txt'" >> /home/dronehacker/.zshrc
echo "alias fonts='cp /opt/DroneHacker/files/*.flf ~/.local/lib/python3.11/site-packages/pyfiglet/fonts'"
