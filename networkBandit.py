from scapy.all import ARP, Ether, srp
import socket
from datetime import datetime
import time
from termcolor import colored
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# Set your Slack API token and channel name
slack_client = WebClient(token='xxxxx-xxxxxx-xxxxx-xxxxx')
channel_id = "xxxxxxxxxxxxx"
channel_name = 'xxxxxxxxxxx' 


# Define the whitelist of trusted MAC addresses
whitelist = [
    "xx:xx:xx:xx:xx:xx",    # pc01
    "xx:xx:xx:xx:xx:xx",    # pc01
    "xx:xx:xx:xx:xx:xx",    # pc01
    "xx:xx:xx:xx:xx:xx",    # pc01
]


def get_ip_and_hostnames():
    target_ip = "10.0.1.0/24"    # Adjust this to your network range

    # Create an ARP request packet
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send the packet and get the response
    result = srp(packet, timeout=3, verbose=0)[0]

    # Parse the result
    devices = []
    for sent, received in result:
        # Get the IP and MAC addresses
        ip = received.psrc
        mac = received.hwsrc
        # Get the hostname
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = None
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        devices.append({'ip': ip, 'mac': mac, 'hostname': hostname, 'timestamp': timestamp})
    
    return devices


# Function to check if MAC address is trusted and send Slack notification if untrusted
def check_mac_address(mac, whitelist):
    if mac in whitelist:
        return f"{GREEN}OK{END}"
    else:
        message = f"UNTRUSTED device detected! {device} <<< WARNING"
        try:
            slack_client.chat_postMessage(
                channel=channel_id,
                text=message
            )
        except SlackApiError as e:
            print(f"{RED}Slack Error: {e}{END}")
        return f"{RED}>>> UNTRUSTED <<<{END}"
    


# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
END = '\033[0m'
LIGHTGRAY = '\033[37m'
DARKGRAY = '\033[90m'
EXTRADARKGRAY = '\033[30m'
LIGHTGREEN = '\033[92m'
LIGHTRED = '\033[91m'

# Find the channel ID for the given channel name
try:
    response = slack_client.conversations_list()
    channels = response['channels']
    channel_id = None
    for channel in channels:
        if channel['name'] == channel_name:
            channel_id = channel['id']
            break
except SlackApiError as e:
    print(f"{RED}Slack Error: {e}{END}")


if __name__ == "__main__":
    try:
        while True:
            devices = get_ip_and_hostnames()
            for device in devices:
                trust_status = check_mac_address(device['mac'], whitelist)
                print(f"{device['timestamp']} IP Address: {device['ip']} MAC Address: {device['mac']} Hostname: {device['hostname']} Status: {trust_status}")
            time.sleep(60)  # Wait for 60 seconds before the next scan
            print("===")
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
