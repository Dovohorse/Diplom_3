from selenium.webdriver.common.by import By

# Локаторы элементов страницы с лентой заказов
class FeedBoardLocators:

    WORK_AREA = (By.CLASS_NAME, "OrderFeed_orderFeed__2RO_j") # Рабочая область страницы
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]") # Счетчиик заказы за все время
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]") # Счетчик выполнено за сегодня


    # Номер заказа в ленте заказов
    @staticmethod
    def order_number_in_order_history(order_number):
        return (By.XPATH, f"//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(text(), '{order_number}')]")
