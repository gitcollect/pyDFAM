from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import sys

device = MonkeyRunner.waitForConnection()
stateFilePath = "./state/"

def main():
    usr_id = sys.argv[1]
    timestamp = sys.argv[2]
    screenshot = device.takeSnapshot()
    screenshot.writeToFile(stateFilePath + usr_id + "_"  + timestamp + '.png','png')

if __name__ == "__main__":
    main()
