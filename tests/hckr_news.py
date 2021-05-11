import time
import unittest
from pages.base import HckrNews
from webdriver.webdriver import Instance

class HackerNewsTest(unittest.TestCase):
    def setUp(self):
        self.instance = Instance()
        self.instance.instance.set_network_connection(6)


    def tearDown(self):
        self.instance.instance.quit()



    def test_01_validacaoUsernameVazio(self):
        hckr_news = HckrNews(self.instance)
        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()
        time.sleep(2)
        # PREENCHER O CAMPO USERNAME COM VAZIO
        inputUsername = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        inputUsername.clear()
        inputUsername.send_keys("")
        time.sleep(2)

        # PREENCHER O CAMPO PASSWORD
        inputPassword = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        inputPassword.clear()
        inputPassword.send_keys("123456")
        time.sleep(2)

        # CLICAR NO BOTÃO LOGIN
        btnLogin = self.instance.instance.find_element_by_id("android:id/button1")
        btnLogin.click()
        time.sleep(2)
        # VERIFICAR VALIDAÇÃO USERNAME
        msgValidacaoUsername = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        assert msgValidacaoUsername.text == "Catch you, anonymous!"
        print("test_01_validacaoUsernameVazio")

    def test_02_validacaoPasswordVazio(self):
        hckr_news = HckrNews(self.instance)
        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()
        time.sleep(2)
        # PREENCHER O CAMPO USERNAME
        inputUsername = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        inputUsername.clear()
        inputUsername.send_keys("test@test.com")

        # PREENCHER O CAMPO PASSWORD COM VAZIO
        inputPassword = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        inputPassword.clear()
        inputPassword.send_keys("")

        # CLICAR NO BOTÃO LOGIN
        btnLogin = self.instance.instance.find_element_by_id("android:id/button1")
        btnLogin.click()

        # VERIFICAR VALIDAÇÃO PASSWORD
        msgValidacaoPassword = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        assert msgValidacaoPassword.text == "You got a short…password"
        print("test_02_validacaoPasswordVazio")

    def test_03_validacaoUsernameEPasswordVazio(self):
        hckr_news = HckrNews(self.instance)
        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()
        time.sleep(2)
        # PREENCHER O CAMPO USERNAME COM VAZIO
        inputUsername = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        inputUsername.clear()
        inputUsername.send_keys("")

        # PREENCHER O CAMPO PASSWORD COM VAZIO
        inputPassword = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        inputPassword.clear()
        inputPassword.send_keys("")

        # CLICAR NO BOTÃO LOGIN
        btnLogin = self.instance.instance.find_element_by_id("android:id/button1")
        btnLogin.click()

        # VERIFICAR VALIDAÇÃO PASSWORD
        msgValidacaoUsernameEPassword = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        assert msgValidacaoUsernameEPassword.text == "Catch you, anonymous!"
        print("test_03_validacaoUsernameEPasswordVazio")

    def test_04_validacaoDadosAposChamada(self):
        hckr_news = HckrNews(self.instance)
        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()
        time.sleep(2)

        username = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        username.clear()
        username.send_keys("Nome Usuario")

        password = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        password.clear()
        password.send_keys("Senha123")

        self.instance.instance.make_gsm_call('5551234567', "call")
        time.sleep(2)
        self.instance.instance.make_gsm_call('5551234567', "accept")
        time.sleep(2)
        self.instance.instance.make_gsm_call('5551234567', "hold")
        time.sleep(2)
        self.instance.instance.make_gsm_call('5551234567', "cancel")
        time.sleep(2)

        # username_text = self.instance.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        assert username.text == "Nome Usuario"
        assert password.text != None

    def test_05_validar_botao_cancel_e_voltar_tela_inicial(self):
        hckr_news = HckrNews(self.instance)
        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()
        time.sleep(2)
        # Validando algumas informações do modal de login
        login_title = self.instance.instance.find_element_by_id("android:id/alertTitle").text
        assert login_title == "Login", "Título login é diferente"
        # print(login_title)
        login_btn = self.instance.instance.find_element_by_id("android:id/button1").text
        assert login_btn == "LOGIN", "Nome do botão login é diferente"
        cancel_btn = self.instance.instance.find_element_by_id("android:id/button2").text
        assert cancel_btn == "CANCEL", "Nome do botão cancelar é diferente"

        # Clicando no botão Cancel
        cancel = self.instance.instance.find_element_by_id("android:id/button2")
        cancel.click()
        time.sleep(2)
        # Validando o título da página inicial
        hews_home_title = self.instance.instance.find_element_by_class_name("android.widget.TextView").text
        assert hews_home_title == "Hews", "O título da página home está errado"

    def test_06_login_without_connection(self):
        hckr_news = HckrNews(self.instance)

        hckr_news.ConnectionType(0)
        # self.instance.instance.set_network_connection(1)

        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()
        hckr_news.UserName("Erick")
        hckr_news.Password("123asd")
        hckr_news.BtnSignIn()

        message = hckr_news.GetMsgNotInternt()
        self.assertEqual("Where's the Internet? Can't get it", message)

