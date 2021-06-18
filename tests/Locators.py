from selenium.webdriver.common.by import By


class MainPage:
    search_string = (By.CSS_SELECTOR, 'input[class="form-control input-lg"]')
    searching_button = (By.CSS_SELECTOR, '.input-group-btn .btn-lg')
    cart_total = (By.CSS_SELECTOR, '#cart-total')
    my_account_link = (By.CSS_SELECTOR, '#top-links .dropdown .fa-user')
    menu_navbar = (By.CSS_SELECTOR, '#menu.navbar')
    my_account_dropdown = (By.CSS_SELECTOR, '.dropdown .caret')
    go_home = (By.CSS_SELECTOR, 'a[href$="home"]')


class Catalog:
    home = (By.CSS_SELECTOR, '.fa.fa-home')
    desktops_category = (
        By.CSS_SELECTOR, 'a[href="https://demo.opencart.com/index.php?route=product/category&path=20"]')
    notebooks_category = (
        By.CSS_SELECTOR, 'a[href="https://demo.opencart.com/index.php?route=product/category&path=18"]')
    components_category = (
        By.CSS_SELECTOR, 'a[href="https://demo.opencart.com/index.php?route=product/category&path=25"]')
    phones_category = (By.CSS_SELECTOR, 'a[href="https://demo.opencart.com/index.php?route=product/category&path=24"]')
    list_view = (By.CSS_SELECTOR, '#list-view')
    grid_view = (By.CSS_SELECTOR, '#grid-view')


class Login:
    login_link = (By.CSS_SELECTOR, 'a[href="https://demo.opencart.com/index.php?route=account/login"]')
    forgotten_pass_link = (By.CSS_SELECTOR, 'a[href="https://demo.opencart.com/index.php?route=account/forgotten"]')
    email_field = (By.CSS_SELECTOR, '#input-email')
    password_field = (By.CSS_SELECTOR, '#input-password')
    login_button = (By.CSS_SELECTOR, 'input[type="submit"]')
    register_button = (
        By.CSS_SELECTOR, '.btn.btn-primary[href="https://demo.opencart.com/index.php?route=account/register"]')
    column_menu = (By.CSS_SELECTOR, '#column-right')


class Product:
    add_to_wish_list = (By.CSS_SELECTOR, 'button[data-original-title="Add to Wish List"]')
    add_to_cart = (By.CSS_SELECTOR, '#button-cart')
    tab_description = (By.CSS_SELECTOR, 'a[href="#tab-description"]')
    tab_reviews = (By.CSS_SELECTOR, 'a[href="#tab-review"]')
    qty = (By.CSS_SELECTOR, '#input-quantity')


class Admin:
    username = (By.CSS_SELECTOR, '#input-username')
    password = (By.CSS_SELECTOR, '#input-password')
    button_login = (By.CSS_SELECTOR, 'button[type="submit"]')
    link_forgot_pass = (By.CSS_SELECTOR, 'a[href="https://demo.opencart.com/admin/index.php?route=common/forgotten"]')


class Register:
    register_link = (By.CSS_SELECTOR, 'a[href="https://demo.opencart.com/index.php?route=account/register"]')
    first_name = (By.CSS_SELECTOR, '#input-firstname')
    last_name = (By.CSS_SELECTOR, '#input-lastname')
    email = (By.CSS_SELECTOR, '#input-email')
    telephone = (By.CSS_SELECTOR, '#input-telephone')
    password = (By.CSS_SELECTOR, '#input-password')
    password_confirm = (By.CSS_SELECTOR, '#input-confirm')
    register_button = (By.CSS_SELECTOR, 'input[type="submit"]')
