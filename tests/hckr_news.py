
import unittest
from pages.base import HckrNews
from webdriver.webdriver import Instance

class HackerNewsTest(unittest.TestCase):
    def setUp(self):
        self.instance = Instance()

    def tearDown(self):
        self.instance.instance.quit()

    def test_login_withou_connection(self):

        hckr_news = HckrNews(self.instance)

        hckr_news.AirplaneMode(0)
        # self.instance.instance.set_network_connection(1)

        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()
        hckr_news.UserName("Erick")
        hckr_news.Password("123asd")
        hckr_news.BtnSignIn()

        message = hckr_news.GetMsgNotInternt()
        self.assertEqual("Where's the Internet? Can't get it", message)
