#!/bin/bash

# Check if the script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root."
   exit 1
fi

# Install vsftpd
apt-get update
apt-get install -y vsftpd
#apt install iptables-persistent
# Set up iptables rules
# Flush existing rules
iptables -F

# Allow established connections
#iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow SSH
#iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow FTP
#iptables -A INPUT -p tcp --dport 20 -j ACCEPT
#iptables -A INPUT -p tcp --dport 21 -j ACCEPT
#iptables -A INPUT -p tcp --dport 40000:50000 -j ACCEPT

# Allow ICMP (ping)
#iptables -A INPUT -p icmp --icmp-type any -j ACCEPT

# Default deny rule for other incoming connections
#iptables -A INPUT -j DROP

# Save iptables rules (this might vary depending on your system)
#iptables-save > /etc/iptables/rules.v4

# Create a backup of the original config file
cp /etc/vsftpd.conf /etc/vsftpd.conf.bak

# Set up the configuration for anonymous access
echo "anonymous_enable=YES
local_enable=NO
listen=YES
write_enable=NO
anon_root=/var/ftp
anon_upload_enable=NO
anon_mkdir_write_enable=NO
dirmessage_enable=YES
xferlog_enable=YES
connect_from_port_20=YES
chown_uploads=NO
async_abor_enable=YES
ascii_upload_enable=YES
ascii_download_enable=YES
ftpd_banner=Welcome to the anonymous FTP server.
pasv_min_port=40000
pasv_max_port=50000" > /etc/vsftpd.conf

# Change ownership and permissions for the configuration file
chown root:root /etc/vsftpd.conf
chmod 644 /etc/vsftpd.conf

# Create the directory for anonymous access
mkdir -p /var/ftp
mkdir -p /var/ftp/docs

# Restart vsftpd to apply the changes
systemctl restart vsftpd

echo "FTP server is set up for anonymous read-only access."
