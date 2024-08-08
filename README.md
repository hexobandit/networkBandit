# networkBandit
Network Device Scanner with Slack Alerts in Python

This Python script continuously scans a specified network range to detect connected devices, capturing their IP, MAC addresses, hostnames, and timestamps. It checks the detected MAC addresses against a predefined whitelist of trusted devices. If an untrusted device is found, the script sends a real-time alert to a specified Slack channel and logs the device information in the terminal with colored status indicators. The script runs in an infinite loop, performing scans every 60 seconds, and can be gracefully terminated with Ctrl+C.
