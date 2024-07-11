import allure
from pages import popular_search_terms


@allure.link('https://trello.com/c/Q7ZoeJxT')
@allure.title('TC_015.003.001 | Popular Search Terms > Search results check after clicking the'
                  '"Popular Search Terms" links')
def test_popular_search_terms_jacket_link_results():
    popular_search_terms.visit()
    popular_search_terms.jacket_link.click()
    popular_search_terms.card_titles_should_be_matching_to_link()
