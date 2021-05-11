from selenium.webdriver.common.by import By
from webdriver.webdriver import Instance
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy

class HckrNews:
    def __init__(self, instance):
        self.instance = instance

    def OpenMenu(self):
        # self.hmbger_menu = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageButton[@content-desc=\'Navigate up\']')))
        self.hmbger_menu = WebDriverWait(self.instance.instance, 10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Navigate up')))
        self.hmbger_menu.click()

    def CollapseLogin(self):
        self.setinha = WebDriverWait(self.instance.instance, 10).until(EC.presence_of_element_located((By.ID, 'com.leavjenn.hews:id/iv_expander')))
        self.setinha.click()

    def ClickLogin(self):
        self.btn_login = WebDriverWait(self.instance.instance, 10).until(EC.presence_of_element_located((By.ID, 'com.leavjenn.hews:id/design_menu_item_text')))
        self.btn_login.click()

    def UserName(self, username):
        self.user_name = WebDriverWait(self.instance.instance, 10).until(EC.presence_of_element_located((By.ID, 'com.leavjenn.hews:id/et_user_name')))
        self.user_name.send_keys(username)

    def Password(self, psswrd):
        self.password = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        self.password.send_keys(psswrd)

    def BtnSignIn(self):
        self.loggar = self.instance.instance.find_element_by_id("android:id/button1")
        self.loggar.click()

    def GetMsgNotInternt(self):
        self.msg_internet = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        return self.msg_internet.text

    def AirplaneMode(self, airplane):
        self.instance.instance.set_network_connection(airplane)