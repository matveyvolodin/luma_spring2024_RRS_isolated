from selene import be, have, browser
from selene.support.shared.jquery_style import s

whats_new_page = 'https://magento.softwaretestingboard.com/what-is-new.html'
women_page = 'https://magento.softwaretestingboard.com/women.html'
women_tops_page = 'https://magento.softwaretestingboard.com/women/tops-women.html'
women_bottoms_page = 'https://magento.softwaretestingboard.com/women/bottoms-women.html'
women_jackets_page = 'https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html'
women_hoodies_and_sweatshirts_page = ('https://magento.softwaretestingboard.com/women/tops-women/'
                                      'hoodies-and-sweatshirts-women.html')
women_tees_page = 'https://magento.softwaretestingboard.com/women/tops-women/tees-women.html'
women_bras_and_tanks_page = 'https://magento.softwaretestingboard.com/women/tops-women/tanks-women.html'
women_pants_page = 'https://magento.softwaretestingboard.com/women/bottoms-women/pants-women.html'
women_shorts_page = 'https://magento.softwaretestingboard.com/women/bottoms-women/shorts-women.html'
men_page = 'https://magento.softwaretestingboard.com/men.html'
men_tops_page ='https://magento.softwaretestingboard.com/men/tops-men.html'
men_bottoms_page = 'https://magento.softwaretestingboard.com/men/bottoms-men.html'
men_jackets_page = 'https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html'
men_hoodies_and_sweatshirts_page = ('https://magento.softwaretestingboard.com/men/tops-men/'
                                    'hoodies-and-sweatshirts-men.html')
men_tees_page = 'https://magento.softwaretestingboard.com/men/tops-men/tees-men.html'
men_tanks_page = 'https://magento.softwaretestingboard.com/men/tops-men/tanks-men.html'
men_pants_page = 'https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html'
men_shorts_page = 'https://magento.softwaretestingboard.com/men/bottoms-men/shorts-men.html'
gear_page = 'https://magento.softwaretestingboard.com/gear.html'
gear_bags_page = 'https://magento.softwaretestingboard.com/gear/bags.html'
gear_fitness_equipment_page = 'https://magento.softwaretestingboard.com/gear/fitness-equipment.html'
gear_watches_page = 'https://magento.softwaretestingboard.com/gear/watches.html'
gear_sale_page = 'https://magento.softwaretestingboard.com/sale.html'
compare_products_page = 'https://magento.softwaretestingboard.com/catalog/product_compare/'

compare_products_block = s('#block-compare-heading')
product_name_in_the_compare_products_block = s('(//strong[@class="product-item-name"])[last()]')
product_name_on_the_compare_product_page = s('//strong[@class="product-item-name"]')

# Push it messanger bag page
product_url = 'https://magento.softwaretestingboard.com/push-it-messenger-bag.html'
add_to_compare_button = s('//a[@class="action tocompare"]')

compare_products_link = s('//a[@class="action compare"]')
compare_products_heading = s('//h1[@class="page-title"]/span')
added_to_compare_success_message = s('//div[@class="message-success success message"]/div')
compare_list_link = s('//div[@class="message-success success message"]/div/a')

compare_button = s('//a[@class="action compare primary"]')


def visit(url):
    browser.open(url)


def compare_products_block_should_be_presented_on_the_page():
    compare_products_block.should(be.visible)


def compare_button_should_be_presented_on_the_page():
    compare_button.should(be.visible)


def add_product_to_compare():
    visit(product_url)
    add_to_compare_button.should(be.clickable).click()


def page_heading_should_have_text(text):
    compare_products_heading.should(have.text(text))


def success_message_should_have_text(text):
    added_to_compare_success_message.should(have.text(text))
