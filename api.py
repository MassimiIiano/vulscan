from flask import Flask, jsonify
import subprocess
import re
import json


app = Flask(__name__)


def get_devices():
    
    # Define the command
    command = "sudo ./nmap/bin/nmap -O 10.11.81.6/20"

    # Execute the command and capture the output
    try:
        print('start:', command)
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        # print("Output:")
        print(result)

        return extract_devices(result)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.output}")


def get_vulns():
    command = './nmap/bin/nmap -sV --script=vulscan/vulscan.nse 10.11.81.6/20'
    print(command)

        # Execute the command and capture the output
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        
        ret =  parse_vulnerabilities(result)
        print(ret)

        return ret

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.output}")



def extract_devices(text):
    ipRegexp = r'Nmap scan report for (\d+\.\d+\.\d+\.\d+)'
    macRegexp = r'MAC Address: ([0-9A-Z:]+)'
    deviceType = r'Device type: (.*)'

    result = dict()
    for machine in text.split('\n\n')[:-1]:
        item = {
            'ip': re.search(ipRegexp, machine).group(1) if re.search(ipRegexp, machine) else None,
            'mac': re.search(macRegexp, machine).group(1) if re.search(macRegexp, machine) else None,
            'device': re.search(deviceType, machine).group(1) if re.search(deviceType, machine) else None,
        }
        result[item['ip']] = item

    return result

def parse_vulnerabilities(text):
    result = dict()
    parts = text.split('Nmap scan report for')[1:]
    for part in parts:
        lines = part.split('\n')
        first_line = lines[0]
        ip = re.search(r'[0-9]+(?:\.[0-9]+){3}', first_line).group()
        lines_with_json = [line for line in lines if line.startswith('| {')][:5]
        jsons = [ json.loads(re.sub(r'\\x[0-9A-Fa-f]{2}', '', line[2:])) for line in lines_with_json ]
        result[ip] = {
            'ip': ip,
            'vulnerabilities': jsons
        }
    return result


def merge_devices(dict1: dict, dict2: dict):
    # print to file dict1 & dict2
    with open('onne.txt', 'w') as file:
        json.dump(dict1, file)

    with open('two.txt', 'w') as file:
        json.dump(dict2, file)

    for key, value in dict2.items():
        if key in dict1:
            dict1[key].update(value)

    for key, value in dict1.items():
        if key not in dict2:
            dict1[key]['vulnerabilities'] = []

    return dict1


# Route to render the table
@app.route('/devices', methods=['GET'])
def devices():
    # print("devices")
    # vulns = get_vulns()
    # devices = get_devices()

    # all = merge_devices(devices, vulns)
    # json =  jsonify(all)
    # print(json)
    # read file glory.json
    with open('glory.json', 'r') as file:
        res = json.load(file)
    return res

if __name__ == '__main__':
    app.run(debug=True)



