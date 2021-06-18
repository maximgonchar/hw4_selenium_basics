from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators import MainPage, Login, Catalog, Product, Admin


class TestMainPage:
    def test_title(self, browser):
        try:
            WebDriverWait(browser, 2).until(EC.title_is('Your Store'))
        except TimeoutException:
            browser.save_screenshot("title_not_found.png")
            raise AssertionError("Title not correct")

    def test_find_cart(self, browser):
        try:
            cart = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.cart_total))
        except TimeoutException:
            browser.save_screenshot("element_not_found.png")
            raise AssertionError("Element #cart-total not found")
        assert cart.text == '0 item(s) - $0.00', "Cart not found. Error!!!"

    def test_find_input_search(self, browser):
        try:
            WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.search_string))
        except TimeoutException:
            browser.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_menu_navbar(self, browser):
        try:
            WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.menu_navbar))
        except TimeoutException:
            browser.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_my_account_dropdown(self, browser):
        try:
            WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.my_account_dropdown))
        except TimeoutException:
            browser.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_go_home(self, browser):
        try:
            WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.go_home))
        except TimeoutException:
            browser.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")


class TestCatalog:

    def test_find_home_page(self, catalog_page):
        try:
            WebDriverWait(catalog_page, 2).until(EC.visibility_of_element_located(Catalog.home))
        except TimeoutException:
            catalog_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_desktops_category(self, catalog_page):
        try:
            WebDriverWait(catalog_page, 2).until(EC.visibility_of_element_located(Catalog.desktops_category))
        except TimeoutException:
            catalog_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_notebooks_category(self, catalog_page):
        try:
            WebDriverWait(catalog_page, 2).until(EC.visibility_of_element_located(Catalog.notebooks_category))
        except TimeoutException:
            catalog_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_components_category(self, catalog_page):
        try:
            WebDriverWait(catalog_page, 2).until(EC.visibility_of_element_located(Catalog.components_category))
        except TimeoutException:
            catalog_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_phones_category(self, catalog_page):
        try:
            WebDriverWait(catalog_page, 2).until(EC.visibility_of_element_located(Catalog.phones_category))
        except TimeoutException:
            catalog_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_list_view(self, catalog_page):
        try:
            WebDriverWait(catalog_page, 2).until(EC.visibility_of_element_located(Catalog.list_view))
        except TimeoutException:
            catalog_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_grid_view(self, catalog_page):
        try:
            WebDriverWait(catalog_page, 2).until(EC.visibility_of_element_located(Catalog.grid_view))
        except TimeoutException:
            catalog_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")


class TestProductCard:
    def test_find_add_to_wl(self, macbook):
        try:
            WebDriverWait(macbook, 2).until(EC.visibility_of_element_located(Product.add_to_wish_list))
        except TimeoutException:
            macbook.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_add_to_cart(self, macbook):
        try:
            WebDriverWait(macbook, 2).until(EC.visibility_of_element_located(Product.add_to_cart))
        except TimeoutException:
            macbook.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_tab_descr(self, macbook):
        try:
            desc = WebDriverWait(macbook, 2).until(EC.visibility_of_element_located(Product.tab_description))
        except TimeoutException:
            macbook.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")
        assert desc.text == 'Description'

    def test_find_add_tab_review(self, macbook):
        try:
            review = WebDriverWait(macbook, 2).until(EC.visibility_of_element_located(Product.tab_reviews))
        except TimeoutException:
            macbook.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")
        assert review.text == 'Reviews (0)'

    def test_find_qty(self, macbook):
        try:
            WebDriverWait(macbook, 2).until(EC.visibility_of_element_located(Product.qty))
        except TimeoutException:
            macbook.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")


class TestLogin:
    def test_title(self, on_login_page):
        try:
            WebDriverWait(on_login_page, 2).until(EC.title_is('Account Login'))
        except TimeoutException:
            on_login_page.save_screenshot("title_not_found.png")
            raise AssertionError("Title not correct")

    def test_find_input_email(self, on_login_page):
        try:
            WebDriverWait(on_login_page, 2).until(EC.visibility_of_element_located(Login.email_field))
        except TimeoutException:
            on_login_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_input_password(self, on_login_page):
        try:
            WebDriverWait(on_login_page, 2).until(EC.visibility_of_element_located(Login.password_field))
        except TimeoutException:
            on_login_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_link_forgotten_password(self, on_login_page):
        try:
            WebDriverWait(on_login_page, 2).until(EC.visibility_of_element_located(Login.forgotten_pass_link))
        except TimeoutException:
            on_login_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_button_login(self, on_login_page):
        try:
            WebDriverWait(on_login_page, 2).until(EC.visibility_of_element_located(Login.login_button))
        except TimeoutException:
            on_login_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_button_register(self, on_login_page):
        try:
            reg = WebDriverWait(on_login_page, 2).until(EC.visibility_of_element_located(Login.register_button))
        except TimeoutException:
            on_login_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")
        assert reg.text == 'Continue'

    def test_find_column_menu(self, on_login_page):
        try:
            WebDriverWait(on_login_page, 2).until(EC.visibility_of_element_located(Login.column_menu))
        except TimeoutException:
            on_login_page.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")


class TestAdministration:
    def test_title(self, admin):
        try:
            WebDriverWait(admin, 2).until(EC.title_is('Administration'))
        except TimeoutException:
            admin.save_screenshot("title_not_found.png")
            raise AssertionError("Title not correct")

    def test_find_username_field(self, admin):
        try:
            WebDriverWait(admin, 2).until(EC.visibility_of_element_located(Admin.username))
        except TimeoutException:
            admin.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_password_field(self, admin):
        try:
            WebDriverWait(admin, 2).until(EC.visibility_of_element_located(Admin.password))
        except TimeoutException:
            admin.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_btn_login(self, admin):
        try:
            WebDriverWait(admin, 2).until(EC.visibility_of_element_located(Admin.button_login))
        except TimeoutException:
            admin.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")

    def test_find_forgotten_pass(self, admin):
        try:
            forgotten = WebDriverWait(admin, 2).until(EC.visibility_of_element_located(Admin.link_forgot_pass))
        except TimeoutException:
            admin.save_screenshot("element_not_found.png")
            raise AssertionError("Element not found")
        assert forgotten.text == "Forgotten Password"
