#!/usr/bin/env python

import subprocess
import sys
import csv

SIM_IDENTIFIERS = [
    'Alpha',
    'Bravo',
    'Charlie',
    'Delta',
    'Echo',
    'Foxtrot',
    'Golf',
    'Hotel',
    'India',
    'Juliet',
    'Kilo',
    'Lima',
    'Mike',
    'November',
    'Oscar',
    'Papa',
    'Quebec',
    'Romeo',
    'Sierra',
    'Tango',
    'Uniform',
    'Victor',
    'Whisky',
    'X-ray',
    'Yankee',
    'Zulu',
]


def shell(cmd_str) -> str:
    proc = subprocess.Popen([cmd_str], shell=True, stdout=subprocess.PIPE)

    return (proc.stdout.read()).decode().split('\n')[0]


if __name__ == '__main__':
    args = sys.argv

    if args[1] == 'make':
        sims = []
        for FONETIC in SIM_IDENTIFIERS:
            id = shell('xcrun simctl create \'' + FONETIC + ' iPhone 13 (15.2)\' com.apple.CoreSimulator.SimDeviceType.iPhone-13 com.apple.CoreSimulator.SimRuntime.iOS-15-2')
            sims.append(id)
            print(id + ' is successfully created.')


        with open('created_sims.csv', 'w') as sims_file:
            writer = csv.writer(sims_file)
            writer.writerow(["ID", "Device", "OS Version"])
            for sim in sims:
                writer.writerow([sim, "iPhone 13", "iOS 15.2"])

    if args[1] == 'clean':
        with open('created_sims.csv') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                shell('xcrun simctl erase ' + row[0])
                shell('xcrun simctl delete ' + row[0])
                print('Erased ' + row[0] + ' and deleted.')

    if args[1] == 'launch':
        with open('created_sims.csv') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                shell('xcrun simctl boot ' + row[0])
                print('Booted ' + row[0] + ' .')
