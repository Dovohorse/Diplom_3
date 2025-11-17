from selenium.webdriver.common.by import By

# Локаторы элементов главной страницы
class BuilderLocators:

    WORK_AREA = (By.CLASS_NAME, "App_componentContainer__2JC2W") # Рабочая область страницы
    POPUP = (By.CLASS_NAME, "Modal_modal__container__Wo2l_") # Высплывающее окно с деталями ингредииента
    POPUP_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'close')]") # Кнопка-крестик, закрывающий всплывающее окна с деталями ингредиента
    CONSTRUCTOR_BASKET = (By.XPATH, "//*[starts-with(@class,'BurgerConstructor_basket__29Cd7')]") # Корзина
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка Войти в аккаунт
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка Оформить заказ
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]") # Номер заказа в всплываюющем окне
    CLOSE_ORDER_MODAL_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']") # Кнопка закрывающая всплывающее окно c заказом
    MODAL_ORDER_WINDOW = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']") # Модальное окно с номером заказа
    
    # Локаторы разделов
    BUN_SECTION = (By.XPATH, "//span[text()='Булки']") # Булки
    SAUCE_SECTION = (By.XPATH, "//span[text()='Соусы']") # Соусы
    FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']") # Начинки

    # Локторы карточек ингредиентов
    @staticmethod
    def locator_ingredient_card_by_id(ingredient_id):
        return (By.XPATH, f'//a[contains(@href, "/ingredient/{ingredient_id}")]')
    
    # Локаторы всплывающих окон с карточками ингредиентов
    @staticmethod
    def locator_ingredient_popup_by_id(ingredient_id):
        return (By.XPATH, f'//a[contains(@href, "/ingredient/{ingredient_id}")]//p[contains(@class, "counter__num")]')
    
    # Локатор счетчика количества ингредиента
    @staticmethod
    def locator_ingredient_counter(ingredient_id):
        return (By.XPATH, f'//a[contains(@href, "/ingredient/{ingredient_id}")]//p[contains(@class, "counter_counter__num__")]')
