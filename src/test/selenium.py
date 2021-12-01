import time
import selenium
from selenium import webdriver

class IntegrationTest():

    def __init__(self):

        options = webdriver.ChromeOptions()

        options.add_argument('--headless')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome(executable_path="C:\\Users\\Jackelyn\\chromedriver_win32\\chromedriver.exe",
        #                                options=options)
        # self.driver = webdriver.ChromeOptions()
        self.driver.get('https://un1br0.sitict.net:4000/login')
    def test(self):
        print("[Integration Tests] - Starting tests")
        self.__labtest()
        self.tearDown()
        print("[Integration Tests] - All Integration Tests Passed")


    def __labtest(self):
        print("[Integration Tests] - Lab demo test")
        username = "test"
        pwd = "test"
        username_input = self.driver.find_element_by_xpath('//*[@id="username"]')
        username_input.send_keys(username)

        emp_pw_input = self.driver.find_element_by_xpath('//*[@id="password"]')
        emp_pw_input.clear()
        emp_pw_input.send_keys(pwd)

        self.driver.find_element_by_id('submit').click()
        time.sleep(1)
        assert self.driver.title == "DONE"
        print("[Integration Tests] - Labdemo passed")

    
        print("[Integration Tests] - Admin Delete Product Test Passed")


    def tearDown(self):
        self.driver.quit()


RunTest = IntegrationTest()
RunTest.test()
