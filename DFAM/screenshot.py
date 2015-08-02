from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

device = MonkeyRunner.waitForConnection()

def snap(usr_id, timestamp):
    screenshot = device.takeSnapshot()
    screenshot.writeToFile(usr_id + " "  + timestamp,'png')
