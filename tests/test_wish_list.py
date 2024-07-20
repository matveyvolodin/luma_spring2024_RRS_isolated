import allure
import pytest

from pages import wish_list

# failing after 10 runs because of sharing restrictions on account -> Automatize new account creation for every 10 runs
@pytest.mark.xfail
@allure.link('https://trello.com/c/bd7oN49R')
@allure.title('TC_014.001.003 | Wish list > Wish list sharing using the "Share Wish List" button')
def test_wishlist_sharing():
    wish_list.open_login_page()
    wish_list.login('test.irwin@gmail.com','Asdf4321@')
    wish_list.add_item_to_wish_list()
    wish_list.open_page()
    wish_list.share_wishlist_button.click()
    wish_list.fill_in_the_emails_textfield('goodguy@gmail.com, badguy@gmail.com')
    wish_list.fill_in_the_message_textfield('Look what i found 123')
    wish_list.share_wish_list_button_fin.click()
    wish_list.wishlist_shared_success_msg_should_contain()
    wish_list.clear_wish_list()

