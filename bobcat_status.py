import requests
import argparse
import time

# Parsing rules
parser = argparse.ArgumentParser(description='Setup information for script')
parser.add_argument('--ip',type=str,required=True,help="Enter IP address. Ex. 192.168.x.x")
parser.add_argument('--sleep',type=int,required=True,help="Enter time to sleep in seconds.")
args = parser.parse_args()

# Global URL variables
reboot_url = 'http://{}/admin/reboot'.format(args.ip)

while True:
    try:
		time.sleep(args.sleep)
        r = requests.post(reboot_url,auth=('bobcat','miner'))
    except:
        print('[ERROR] Check IP address or bobcat miner power.')
