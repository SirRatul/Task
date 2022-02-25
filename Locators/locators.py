from selenium.webdriver.common.by import By

class CheckoutPagelocators(object):
    SUMMARY_PROCEED_BTN = (By.XPATH, "//*[@class='cart_navigation clearfix']/a")
    ADDRESS_PROCEED_BTN = (By.XPATH, "//*[@name='processAddress']")
    TOS_CHECKBOX_ID = (By.ID, "cgv")
    SHIPPING_PROCEED_BTN_NAME = (By.NAME, "processCarrier")
    PAYMENT_PAY_BE_CHECK_BTN = (By.XPATH, "//*[@title='Pay by check.']")
    CONFIRM_ORDER_BTN = (By.XPATH, "//*[@class='button btn btn-default button-medium']")

class MyAccountPageLocator(object):
    SIGN_OUT_BTN_NAME = (By.CLASS_NAME, "logout")
    DRESS_BTN = (By.CSS_SELECTOR, "#block_top_menu > ul > li:nth-child(2)")
    CASUAL_DRESS_BTN = (By.CSS_SELECTOR, "#block_top_menu > ul > li:nth-child(2) > ul > li:nth-child(1) > a")


class HomeLocators(object):
    SIGN_IN_BTN_NAME = (By.CLASS_NAME, "login")

class CreateAccountLocators(object):
    SIGN_IN_BUTTON = (By.ID, "SubmitLogin")
    ENTER_EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    REGISTER_EMAIL_BUTTON = (By.ID, "email_create")
    CREATE_ACCOUNT_BTN = (By.ID, "SubmitCreate")
