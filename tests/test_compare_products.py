import allure
from pages import compare_products
import pytest
from selene import be, have, browser


@allure.link('')
@allure.title('TC_013.001.005 | Compare products | > Text menu "-Compare products-" is presented on every page'
              ' in the catalog')
@pytest.mark.parametrize('catalog_page_url',
    [
        compare_products.whats_new_page,
        compare_products.women_page,
        compare_products.women_tops_page,
        compare_products.women_bottoms_page,
        compare_products.women_jackets_page,
        compare_products.women_hoodies_and_sweatshirts_page,
        compare_products.women_tees_page,
        compare_products.women_bras_and_tanks_page,
        compare_products.women_pants_page,
        compare_products.women_shorts_page,
        compare_products.men_page,
        compare_products.men_tops_page,
        compare_products.men_bottoms_page,
        compare_products.men_jackets_page,
        compare_products.men_hoodies_and_sweatshirts_page,
        compare_products.men_tees_page,
        compare_products.men_tanks_page,
        compare_products.men_pants_page,
        compare_products.men_shorts_page,
        compare_products.gear_page,
        compare_products.gear_bags_page,
        compare_products.gear_fitness_equipment_page,
        compare_products.gear_watches_page,
        compare_products.gear_sale_page,
    ]
)
def test_compare_products_block_is_presented_on_every_page_in_the_catalog(catalog_page_url):
    compare_products.visit(catalog_page_url)
    compare_products.compare_products_block_should_be_presented_on_the_page()


@allure.title('TC_013.001.006 | Compare products | > Added to comparison product is displayed in comparison block and'
              ' on top of the catalog page')
def test_added_to_compare_product_is_presented_in_the_compare_products_block():
    compare_products.add_product_to_compare()
    compare_products.visit(compare_products.whats_new_page)
    compare_products.product_name_in_the_compare_products_block.should(have.text("Push It Messenger Bag"))


@allure.title('TC_013.001.007 | Compare products | > Added to comparison product is displayed on top of the catalog'
              'page by link "Compare products"')
def test_added_to_compare_product_is_presented_on_the_compare_products_page():
    compare_products.add_product_to_compare()
    compare_products.visit(compare_products.compare_products_page)
    compare_products.product_name_on_the_compare_product_page.should(have.text("Push It Messenger Bag"))

