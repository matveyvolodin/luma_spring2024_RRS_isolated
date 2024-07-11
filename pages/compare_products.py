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


compare_products_block = s('#block-compare-heading')


def visit(url):
    browser.open(url)


def compare_products_block_should_be_presented_on_the_page():
    compare_products_block.should(be.present)