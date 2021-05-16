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

        # PREENCHER O CAMPO USERNAME COM VAZIO
        hckr_news.UserName("")

        # PREENCHER O CAMPO PASSWORD
        hckr_news.Password("123456")

        # CLICAR NO BOTÃO LOGIN
        BtnLogin = hckr_news.BtnSignIn()
        BtnLogin.click()

        # VERIFICAR VALIDAÇÃO USERNAME
        msgValidacaoUsername = hckr_news.GetMsgNotInternt()
        assert msgValidacaoUsername == "Catch you, anonymous!"

    def test_02_validacaoPasswordVazio(self):
        hckr_news = HckrNews(self.instance)

        # ACESSA FORM LOGIN
        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()

        # PREENCHER O CAMPO USERNAME
        hckr_news.UserName("test@test.com")

        # PREENCHER O CAMPO PASSWORD COM VAZIO
        hckr_news.Password("")

        # CLICAR NO BOTÃO LOGIN
        BtnLogin = hckr_news.BtnSignIn()
        BtnLogin.click()

        # VERIFICAR VALIDAÇÃO PASSWORD
        msgValidacaoUsernameEPassword = hckr_news.GetMsgNotInternt()
        assert msgValidacaoUsernameEPassword == "You got a short…password"

    def test_03_validacaoUsernameEPasswordVazio(self):
        hckr_news = HckrNews(self.instance)

        # ACESSA FORM LOGIN
        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()

        # PREENCHER O CAMPO USERNAME COM VAZIO
        hckr_news.UserName("")

        # PREENCHER O CAMPO PASSWORD COM VAZIO
        hckr_news.Password("")

        # CLICAR NO BOTÃO LOGIN
        BtnLogin = hckr_news.BtnSignIn()
        BtnLogin.click()

        # VERIFICAR VALIDAÇÃO PASSWORD
        msgValidacaoUsernameEPassword = hckr_news.GetMsgNotInternt()
        assert msgValidacaoUsernameEPassword == "Catch you, anonymous!"

    def test_04_validacaoDadosAposChamada(self):
        hckr_news = HckrNews(self.instance)

        # ACESSA FORM LOGIN
        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()

        # PREENCHER O CAMPO USERNAME
        hckr_news.UserName("Nome Usuario")

        # PREENCHER O CAMPO PASSWORD
        hckr_news.Password("Senha123")

        # REALIZANDO CHAMADA, ACEITANDO, ESPERANDO E CANCELANDO
        hckr_news.Chamadas('5551234567', "call")
        time.sleep(2)
        hckr_news.Chamadas('5551234567', "accept")
        time.sleep(2)
        hckr_news.Chamadas('5551234567', "hold")
        time.sleep(2)
        hckr_news.Chamadas('5551234567', "cancel")
        time.sleep(2)

        # VALIDAÇÃO DO NOME E SENHA
        assert hckr_news.user_name.text == "Nome Usuario"
        assert hckr_news.password.text != None

    def test_05_ValidarBotaoCancelVoltarTelaInicial(self):
        hckr_news = HckrNews(self.instance)

        # ACESSA FORM LOGIN
        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()

        hckr_news.BtnSignIn()
        hckr_news.BtnCancel()

        # VALIDANDO ALGUMAS INFORMAÇÕES DO MODAL DE LOGIN
        assert hckr_news.LogginTitle() == "Login", "Título login é diferente"
        assert hckr_news.loggar.text == "LOGIN", "Nome do botão login é diferente"
        assert hckr_news.btn_cancel.text == "CANCEL", "Nome do botão cancelar é diferente"

        # CLICAR NO BOTÃO CANCEL
        hckr_news.btn_cancel.click()

        # VALIDANDO TÍTULO DA PÁGINA INICIAL
        hews_home_title = hckr_news.Home()
        assert hews_home_title.text == "Hews", "O título da página home está errado"

    def test_06_LoginWithoutConnection(self):
        hckr_news = HckrNews(self.instance)

        # DESLIGA ACESSO A INTERNET
        hckr_news.ConnectionType(0)
        # self.instance.instance.set_network_connection(1)

        # ACESSA FORM LOGIN
        hckr_news.OpenMenu()
        hckr_news.CollapseLogin()
        hckr_news.ClickLogin()

        # PREENCHER O CAMPO USERNAME
        hckr_news.UserName("Nome Usuario")

        # PREENCHER O CAMPO PASSWORD
        hckr_news.Password("Senha123")

        # CLICAR NO BOTÃO LOGIN
        BtnLogin = hckr_news.BtnSignIn()
        BtnLogin.click()

        # VALIDAÇÃO DA MENSAGEM
        message = hckr_news.GetMsgNotInternt()
        self.assertEqual("Where's the Internet? Can't get it", message)

