#!/usr/bin/env python
import os


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

if __name__ == '__main__':
    print("Hello World!")

    for FONETIC in SIM_IDENTIFIERS:
        os.system('xcrun simctl delete \'' + FONETIC + ' iPhone 13 (15.2)\' com.apple.CoreSimulator.SimDeviceType.iPhone-13 com.apple.CoreSimulator.SimRuntime.iOS-15-2')
