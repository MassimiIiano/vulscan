import socket
import subprocess
import re
# Get the local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
my_ip = s.getsockname()[0]
s.close()


# Define the command
command = "sudo ./nmap/bin/nmap -O 10.11.81.6/20 | grep 'MAC' | cut -d':' -f2-"

# Execute the command and capture the output
try:
    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    # print("Output:")
    # print(result)

    mac_corp_dicts = []
    
    # Regex pattern to match MAC address and corporation name
    pattern = r'([0-9A-Fa-f:]{17})\s+\(([^)]+)\)'

    # Find all matches in the result
    matches = re.findall(pattern, result)

    # Create a dictionary for each MAC address and its corresponding corporation
    for match in matches:
        mac, corp = match
        mac_corp_dicts.append({'mac': mac, 'corp': corp})

    # Print the dictionary
    print(mac_corp_dicts)

except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e.output}")
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e.output}")


