#!/usr/bin/env python
import os

if __name__ == '__main__':
    print("Hello World!")
    os.system('xcrun simctl create \'iPhone 13 (15.2) Node-A\' com.apple.CoreSimulator.SimDeviceType.iPhone-13 com.apple.CoreSimulator.SimRuntime.iOS-15-2')