from selene import be, have, browser
from selene.support.shared.jquery_style import s
from selene.core import query

product_url = 'https://magento.softwaretestingboard.com/push-it-messenger-bag.html'
update_shopping_cart_button = s('.action.update')

cart_icon = s('a.showcart')
mini_cart = s('#ui-id-1')
counter_number = s('.counter-label')
qty = s('.input-text.qty')

product_price_cart = s('//td[@class="col price"]/span/span/span')
subtotal_price_cart = s('//td[@class="col subtotal"]/span/span/span')


def visit(url):
    browser.open(url)


def click_cart_icon():
    cart_icon.click()


def click_update_shopping_cart_button():
    update_shopping_cart_button.click()
    update_shopping_cart_button.wait_until(be.visible)


def counter_should_be_equal(quantity):
    counter_number.should(have.text(quantity))


def is_qty_present():
    qty.should(be.present)


def set_value_of_qty(value):
    is_qty_present()
    qty.clear()
    qty.send_keys(value)


def add_item_to_cart():
    visit(product_url)
    s("//button[@class='action primary tocart']").should(be.clickable).click()
    s("//div[@class='message-success success message']").should(be.visible)


def cart_subtotal_should_be_calculated_with_qty_equal(quantity):
    price = float(product_price_cart.get(query.text).strip('$'))
    cart_subtotal = float(subtotal_price_cart.get(query.text).strip('$'))
    assert cart_subtotal == price * int(quantity)


def click_view_and_edit_card_button():
    s('//a[@class="action viewcart"]').click()