from appium import webdriver

class Instance:

    def __init__(self):
        caps = {
            'platformName': 'Android',
            'deviceName': 'Appium',
            'app': '\\Users\\erick.santos\\Documents\\POSBDRZQ\\AutomaçãoMobile\\apk\\com.leavjenn.hews_28_apps.evozi.com.apk',
            'ensureWebviewsHavePages': True
        }
        self.instance = instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

