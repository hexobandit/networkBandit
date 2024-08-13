# networkBandit
**Python Network Device Scanner with Slack Alerts**

This Python script continuously scans a specified network range to detect connected devices, capturing their IP, MAC addresses, hostnames, and timestamps. It checks the detected MAC addresses against a predefined whitelist of trusted devices. If an untrusted device is found, the script sends a real-time alert to a specified Slack channel and logs the device information in the terminal with colored status indicators. The script runs in an infinite loop, performing scans every 60 seconds, and can be gracefully terminated with Ctrl+C.

Bellow you can see examples how the app is running and what output it generates to the terminal and to the corresponding Slack app:

#### networkBandit.py
<img width="829" alt="image" src="https://github.com/user-attachments/assets/6f268446-354f-475a-bbba-5c6d747dbb82">


#### Slack App
<img width="829" alt="image" src="https://github.com/user-attachments/assets/e01b41ea-61f7-49e8-a21d-e5aa88ec9f59">


## Things you need to modify
### Slack Information
Line 8-10: Set your Slack API token and channel name.

    slack_client = WebClient(token='xxxxx-xxxxxx-xxxxx-xxxxx')
    channel_id = "xxxxxxxxxxxxx"
    channel_name = 'xxxxxxxxxxx' 
    
This section is where you input your specific Slack API token, channel ID, and channel name. The script will use these details to send notifications to the appropriate Slack channel when an untrusted device is detected.

### Whitelist MAC Addresses
Line 14-18: Define the MAC addresses you trust.

    whitelist = [
        "xx:xx:xx:xx:xx:xx",    # pc01
        "xx:xx:xx:xx:xx:xx",    # pc01
        "xx:xx:xx:xx:xx:xx",    # pc01
        "xx:xx:xx:xx:xx:xx",    # pc01
    ]

Replace the placeholder MAC addresses with the actual MAC addresses of the devices you trust. These devices won’t trigger a Slack notification.

### IP Range to Scan
Line 22: Set the network IP range that you want to scan.

    target_ip = "10.0.0.0/24"    # Adjust this to your network range

Adjust the target_ip variable to the correct IP range of your network. The script will scan this range to detect connected devices.

### Summary of Adjustments:
1. Slack Info: Insert your Slack API token, channel ID, and channel name on lines 8-10.
1. Whitelist MACs: Enter your trusted MAC addresses on lines 14-18.
1. IP Range: Set your network’s IP range on line 22.

With these modifications, the script will scan the specified network, compare detected devices against your whitelist, and send a Slack notification if an untrusted device is found.

# IMPORTANT:
## Downside of the Script: 
#### Inability to Detect Disabled ARP Broadcast Response
The script provided uses ARP (Address Resolution Protocol) requests to discover devices within the network by sending broadcast packets and waiting for responses. However, it has a significant downside: it cannot detect malicious devices that have disabled ARP broadcast responses. Here’s why:

#### Lack of Active Scanning:
The script only passively waits for ARP replies. A malicious device that is deliberately hiding itself by not responding will remain undetected. The script does not attempt more aggressive scanning techniques, such as port scanning or probing specific IPs, which might help identify devices that don't respond to ARP.

#### Spoofing Risks:
A malicious device could respond to ARP requests with a spoofed MAC address that matches an address in the whitelist. The script would then incorrectly classify this device as trusted.

#### Network-Specific Blind Spots:
If a network uses multiple VLANs or segments where broadcast traffic doesn’t reach all devices, some devices might not be detected. This is particularly problematic if the script is run on a different segment or VLAN from the malicious device.

### Mitigating the Issue
To address these limitations, I'd need to consider the following:
- **Active Probing:** Use additional network scanning methods, such as ICMP ping sweeps or TCP/UDP port scans, which do not rely on ARP responses.
- **Network Anomaly Detection**: Implement network anomaly detection systems (NIDS) to identify unusual behavior, such as devices that are active but not responding to ARP requests.
