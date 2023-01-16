import datetime


class Base:
    """Создаем общие функции: получение ссылок, сравнения, скриншоты и т.д."""

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ' + get_url)

    """Method assert words"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Right value word')

    """Method assert urls"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Get value url')

    """Method screenshots"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y, %m, %d, %H, %M, %S")
        name_screenshot = "screenshot" + now_date + '.png'
        self.driver.save_screenshot('/home/nevi/GitProjects/labirintProject/screens' + name_screenshot)
