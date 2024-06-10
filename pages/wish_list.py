from selene.support.shared.jquery_style import s, ss
from selene import have, browser, be


url = "https://magento.softwaretestingboard.com/wishlist/"

success_msg = "div[class='message-success success message']"
product_url = "https://magento.softwaretestingboard.com/aether-gym-pant.html?qty=1#143=&93="


# Login page
url_login = "https://magento.softwaretestingboard.com/customer/account/login"
user_email = s("div.login-container #email")
user_password = s("div.login-container #pass")
sign_in_button = s("div.login-container #send2")

# Wish list sharing
message_wish_list_is_empty = s('div.block.block-wishlist > div.block-content > div')
delete_bucket_button = '.btn-remove.action.delete'
add_to_wishlist_button = "a[class='action towishlist']"
share_wishlist_button = s('//button[@class="action share"]')
emails_textfield = s('//textarea[@name="emails"]')
message_textfield = s('//textarea[@name="message"]')
share_wish_list_button_fin = s('//button[@class="action submit primary"]')
wishlist_shared_success_msg = s('(//div[@class="messages"])[1]')


def open_page(url=url):
    browser.open(url)


def open_login_page():
    browser.open(url_login)


def login(user, password):
    user_email.type(user)
    user_password.type(password)
    sign_in_button.click()


def add_item_to_wish_list():
    open_page(product_url)
    s(add_to_wishlist_button).should(be.clickable).click()
    s(success_msg).should(be.visible)


def fill_in_the_emails_textfield(emails):
    emails_textfield.type(emails)


def fill_in_the_message_textfield(message):
    message_textfield.type(message)


def wishlist_shared_success_msg_should_contain():
    wishlist_shared_success_msg.should(have.text('Your wish list has been shared.'))


def wish_list_is_not_empty():
    message_wish_list_is_empty.should(have.no.text('You have no items in your wish list.'))


def clear_wish_list():
    if wish_list_is_not_empty():
        items_in_wish_list = ss(delete_bucket_button)
        for item in items_in_wish_list:
            item.should(be.clickable).click()

