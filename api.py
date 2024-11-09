from flask import Flask, jsonify
import subprocess
import re
app = Flask(__name__)


def get_devices():
    
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
        p
        return mac_corp_dicts

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.output}")


def get_vulns():
    command = './nmap/bin/nmap -sV --script=vulscan/vulscan.nse 10.11.81.6/20'

        # Execute the command and capture the output
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)


    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.output}")


# Route to render the table
@app.route('/devices', methods=['GET'])
def devices():
    vulns = get_vulns()
    json =  jsonify(vulns)
    print(json)
    return json

if __name__ == '__main__':
    app.run(debug=True)



