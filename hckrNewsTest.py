import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppiumCurso(unittest.TestCase):

  #  wait = WebDriverWait
    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "Appium"
        caps["app"] = "\\Users\\erick.santos\\Documents\\POSBDRZQ\\AutomaçãoMobile\\apk\\com.leavjenn.hews_28_apps.evozi.com.apk"
        caps["ensureWebviewsHavePages"] = True

        self.instance = instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        time.sleep(5)


    def tearDown(self):
        self.instance.quit()

    def test_airplane_login(self):

        # var = self.instance.mobile.AIRPLANE_MODE
        # self.instance.mobile.set_network_connection(var)
        # print(var)
        self.instance.set_network_connection(1)

        wait = WebDriverWait(self.instance, 10)
        # wait.until(EC.presence_of_element_located((By., "Navigate up")))
        hmbger = WebDriverWait(self.instance, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.ImageButton[@content-desc=\'Navigate up\']")))

        hmbger.click()
        setinha = WebDriverWait(self.instance, 10).until(EC.presence_of_element_located((By.ID, "com.leavjenn.hews:id/iv_expander")))
        # setinha = self.instance.find_element_by_id("com.leavjenn.hews:id/iv_expander")
        setinha.click()

        btn_login = wait.until(EC.presence_of_element_located((By.ID, "com.leavjenn.hews:id/design_menu_item_text")))
        btn_login.click()

        user_name = wait.until(EC.presence_of_element_located((By.ID, "com.leavjenn.hews:id/et_user_name")))
        user_name.send_keys("username")

        password = self.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        password.send_keys("123asd")

        loggar = self.instance.find_element_by_id("android:id/button1")
        loggar.click()

        msg_internet = self.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt").text
        self.assertEqual("Where's the Internet? Can't get it", msg_internet)