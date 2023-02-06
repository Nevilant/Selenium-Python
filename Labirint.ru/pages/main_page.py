from base.base_class import Base


class MainPage(Base):
    """Главная страница"""

    url = 'https://www.labirint.ru/'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators

    # Getters

    # Actions

    # Methods
    '''Инициализируем методы функции'''

    def go_to_site(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
