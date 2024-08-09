# networkBandit
**Python Network Device Scanner with Slack Alerts**

This Python script continuously scans a specified network range to detect connected devices, capturing their IP, MAC addresses, hostnames, and timestamps. It checks the detected MAC addresses against a predefined whitelist of trusted devices. If an untrusted device is found, the script sends a real-time alert to a specified Slack channel and logs the device information in the terminal with colored status indicators. The script runs in an infinite loop, performing scans every 60 seconds, and can be gracefully terminated with Ctrl+C.

## Results
### networkBandit.py
<img width="829" alt="image" src="https://github.com/user-attachments/assets/c2fc450c-2377-44d4-b2b8-07212e5a39ca">

### Slack App
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

