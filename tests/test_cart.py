import allure
from pages import cart


@allure.link('https://trello.com/c/YNtpKcN1')
@allure.title('TC_004.001.004 | Sign in & Registration, Account > Anonym User can change item quantity in the cart')
def test_item_quantity_updating_by_anonym_user():
    cart.add_item_to_cart()
    cart.click_cart_icon()
    cart.click_view_and_edit_card_button()
    cart.counter_should_be_equal('1')
    cart.set_value_of_qty('2')
    cart.click_update_shopping_cart_button()
    cart.counter_should_be_equal('2')
    cart.cart_subtotal_should_be_calculated_with_qty_equal(2)