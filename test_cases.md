Test-cases for automation based on US from user_stories.md. UserStories were developed by another RRS students.

## US_013.001 | Compare products | From any catalog's page

### TC_013.001.005 | Compare products | > Text menu "Compare products" is presented on every page in the catalog

**Steps:**

1. Visit [What's new page](https://magento.softwaretestingboard.com/what-is-new.html)
2. Verify that the "compare products" block is presented on the page
3. Visit [Women page](https://magento.softwaretestingboard.com/women.html)
4. Verify that the "compare products" block is presented on the page
5. Visit [Woman > Tops page](https://magento.softwaretestingboard.com/women/tops-women.html)
6. Verify that the "compare products" block is presented on the page
7. Visit [Woman > Bottoms page](https://magento.softwaretestingboard.com/women/bottoms-women.html)
8. Verify that the "compare products" block is presented on the page
9. Visit [Women > Tops > Jackets page](https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html)
10.  Verify that the "compare products" block is presented on the page
11. Visit [Women > Tops > Hoodies & Sweatshirts page](https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html)
12.  Verify that the "compare products" block is presented on the page
13. Visit [Women > Tops > Tees page](https://magento.softwaretestingboard.com/women/tops-women/tees-women.html)
14.  Verify that the "compare products" block is presented on the page
15. Visit [Women > Tops > Bras & Tanks page](https://magento.softwaretestingboard.com/women/tops-women/tanks-women.html)
16.  Verify that the "compare products" block is presented on the page
17. Visit [Women > Bottoms > Pants page](https://magento.softwaretestingboard.com/women/bottoms-women/pants-women.html)
18.  Verify that the "compare products" block is presented on the page
19. Visit [Women > Bottoms > Shorts page](https://magento.softwaretestingboard.com/women/bottoms-women/shorts-women.html)
20.  Verify that the "compare products" block is presented on the page
21. Visit [Men page](https://magento.softwaretestingboard.com/men.html)
22.  Verify that the "compare products" block is presented on the page
23. Visit [Men > Tops page](https://magento.softwaretestingboard.com/men/tops-men.html)
24.  Verify that the "compare products" block is presented on the page
25. Visit [Men > Bottoms page](https://magento.softwaretestingboard.com/men/bottoms-men.html)
26.  Verify that the "compare products" block is presented on the page
27. Visit [Men > Tops > Jackets page](https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html)
28.  Verify that the "compare products" block is presented on the page
29. Visit [Men > Tops > Hoodies & Sweatshirts page](https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html)
30.  Verify that the "compare products" block is presented on the page
31. Visit [Men > Tops > Tees page](https://magento.softwaretestingboard.com/men/tops-men/tees-men.html)
32.  Verify that the "compare products" block is presented on the page
33. Visit [Men > Tops > Bras & Tanks page](https://magento.softwaretestingboard.com/men/tops-men/tanks-men.html)
34.  Verify that the "compare products" block is presented on the page
35. Visit [Men > Bottoms > Pants page](https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html)
36.  Verify that the "compare products" block is presented on the page
37. Visit [Men > Bottoms > Shorts page](https://magento.softwaretestingboard.com/men/bottoms-men/shorts-men.html)
38.  Verify that the "compare products" block is presented on the page
39. Visit [Gear page](https://magento.softwaretestingboard.com/gear.html)
40. Verify that the "compare products" block is presented on the page
41. Visit [Gear > Bags page](https://magento.softwaretestingboard.com/gear/bags.html)
42. Verify that the "compare products" block is presented on the page
43. Visit [Gear > Fitness equipment page](https://magento.softwaretestingboard.com/gear/fitness-equipment.html)
44. Verify that the "compare products" block is presented on the page
45. Visit [Gear > Watches page](https://magento.softwaretestingboard.com/gear/watches.html)
46. Verify that the "compare products" block is presented on the page
47. Visit [Gear > Sale page](https://magento.softwaretestingboard.com/sale.html)
48. Verify that the "compare products" block is presented on the page


**Expected results**:

1. The "compare products" block is presented on every visited page

### TC_013.001.006 | Compare products | > Added to comparison product is displayed in comparison block on the left side

**Preconditions:**

1. One product is added to "Compare products"

**Steps**:

1. Visit ["What's new" page](https://magento.softwaretestingboard.com/what-is-new.html)


**Expected results**:


1. Added to comparison product is displayed under the text "Compare products" on the left side.

### TC_013.001.007 | Compare products | > Added to comparison product is displayed on top of the catalog page by link "Compare products"

**Preconditions:**

1. One product is added to "Compare products"

**Steps**:

1. Visit ["Compare Products" page](https://magento.softwaretestingboard.com/catalog/product_compare/)

**Expected results**:

1. Added to comparison product is displayed on the "Compare products" page

### TC_013.001.008 | Compare products | > Redirecting to the "Compare products" page  after clicking the "Compare Products" link

**Preconditions:**
1. Any random product is added to "Compare products"

**Steps:**
1. Visit ["What's new page"](https://magento.softwaretestingboard.com/what-is-new.html)
2. Click the "Compare Products" link
 
**Expected results:**
1. User is redirected to the ["Compare Products" page](https://magento.softwaretestingboard.com/catalog/product_compare/)

### TC_013.001.009 | Compare products | > Redirecting to the "Compare products" page after clicking the 'comparison list" link

**Steps**:

1. Visit [product page](https://magento.softwaretestingboard.com/aether-gym-pant.html?qty=1#143=&93=)
2. Click the "Add to compare" button
3. Verify success message "You added product -Product- to the comparison list" is displayed above text -Shopping Options-
4. Verify that the text message "You added product -Product- to the comparison list" includes "comparison list" link 
5. Click to the "comparison list" link

**Expected results**:

1. User is redirected to the ["Compare Products" page](https://magento.softwaretestingboard.com/catalog/product_compare/)

### TC_013.001.010 | Compare products | > "Compare" button is presented on every page in the catalog

**Preconditions:**


1. Any random product is added to "Compare products"

**Steps:**

1. Visit [What's new page](https://magento.softwaretestingboard.com/what-is-new.html)
2. Click the "Compare" button

3. Visit [Women page](https://magento.softwaretestingboard.com/women.html)
4. Click the "Compare" button

5. Visit [Woman > Tops page](https://magento.softwaretestingboard.com/women/tops-women.html)
6. Click the "Compare" button

7. Visit [Woman > Bottoms page](https://magento.softwaretestingboard.com/women/bottoms-women.html)
8. Click the "Compare" button

9. Visit [Women > Tops > Jackets page](https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html)
10. Click the "Compare" button

11. Visit [Women > Tops > Hoodies & Sweatshirts page](https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html)
12. Click the "Compare" button

13. Visit [Women > Tops > Tees page](https://magento.softwaretestingboard.com/women/tops-women/tees-women.html)
14. Click the "Compare" button

15. Visit [Women > Tops > Bras & Tanks page](https://magento.softwaretestingboard.com/women/tops-women/tanks-women.html)
16. Click the "Compare" button

17. Visit [Women > Bottoms > Pants page](https://magento.softwaretestingboard.com/women/bottoms-women/pants-women.html)
18. Click the "Compare" button

19. Visit [Women > Bottoms > Shorts page](https://magento.softwaretestingboard.com/women/bottoms-women/shorts-women.html)
20. Click the "Compare" button

21. Visit [Men page](https://magento.softwaretestingboard.com/men.html)
22. Click the "Compare" button

23. Visit [Men > Tops page](https://magento.softwaretestingboard.com/men/tops-men.html)
24. Click the "Compare" button

25. Visit [Men > Bottoms page](https://magento.softwaretestingboard.com/men/bottoms-men.html)
26. Click the "Compare" button

27. Visit [Men > Tops > Jackets page](https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html)
28. Click the "Compare" button

29. Visit [Men > Tops > Hoodies & Sweatshirts page](https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html)
30. Click the "Compare" button

31. Visit [Men > Tops > Tees page](https://magento.softwaretestingboard.com/men/tops-men/tees-men.html)
32. Click the "Compare" button

33. Visit [Men > Tops > Bras & Tanks page](https://magento.softwaretestingboard.com/men/tops-men/tanks-men.html)
34. Click the "Compare" button

35. Visit [Men > Bottoms > Pants page](https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html)
36. Click the "Compare" button

37. Visit [Men > Bottoms > Shorts page](https://magento.softwaretestingboard.com/men/bottoms-men/shorts-men.html)
38. Click the "Compare" button

39. Visit [Gear page](https://magento.softwaretestingboard.com/gear.html)
40. Click the "Compare" button

41. Visit [Gear > Bags page](https://magento.softwaretestingboard.com/gear/bags.html)
42. Click the "Compare" button

43. Visit [Gear > Fitness equipment page](https://magento.softwaretestingboard.com/gear/fitness-equipment.html)
44. Click the "Compare" button

45. Visit [Gear > Watches page](https://magento.softwaretestingboard.com/gear/watches.html)
46. Click the "Compare" button

47. Visit [Gear > Sale page](https://magento.softwaretestingboard.com/sale.html)
48. Click the "Compare" button

**Expected results:**

1. User is redirected to the ["Compare Products" page](https://magento.softwaretestingboard.com/catalog/product_compare/)
from the every visited page 

### TC_013.001.011 | Compare products | > "Clear All" blue link is presented on every page in the catalog

**Preconditions:**

1. Any random product is added to "Compare products"

**Steps**:

1. Visit [What's new page](https://magento.softwaretestingboard.com/what-is-new.html)
2. Verify that the "Clear" blue link is presented on the page

3. Visit [Women page](https://magento.softwaretestingboard.com/women.html)
4. Verify that the "Clear" blue link is presented on the page

5. Visit [Woman > Tops page](https://magento.softwaretestingboard.com/women/tops-women.html)
6. Verify that the "Clear" blue link is presented on the page

7. Visit [Woman > Bottoms page](https://magento.softwaretestingboard.com/women/bottoms-women.html)
8. Verify that the "Clear" blue link is presented on the page

9. Visit [Women > Tops > Jackets page](https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html)
10.  Verify that the "Clear" blue link is presented on the page

11. Visit [Women > Tops > Hoodies & Sweatshirts page](https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html)
12.  Verify that the "Clear" blue link is presented on the page

13. Visit [Women > Tops > Tees page](https://magento.softwaretestingboard.com/women/tops-women/tees-women.html)
14.  Verify that the "Clear" blue link is presented on the page

15. Visit [Women > Tops > Bras & Tanks page](https://magento.softwaretestingboard.com/women/tops-women/tanks-women.html)
16.  Verify that the "Clear" blue link is presented on the page

17. Visit [Women > Bottoms > Pants page](https://magento.softwaretestingboard.com/women/bottoms-women/pants-women.html)
18.  Verify that the "Clear" blue link is presented on the page

19. Visit [Women > Bottoms > Shorts page](https://magento.softwaretestingboard.com/women/bottoms-women/shorts-women.html)
20.  Verify that the "Clear" blue link is presented on the page

21. Visit [Men page](https://magento.softwaretestingboard.com/men.html)
22.  Verify that the "Clear" blue link is presented on the page

23. Visit [Men > Tops page](https://magento.softwaretestingboard.com/men/tops-men.html)
24.  Verify that the "Clear" blue link is presented on the page

25. Visit [Men > Bottoms page](https://magento.softwaretestingboard.com/men/bottoms-men.html)
26.  Verify that the "Clear" blue link is presented on the page

27. Visit [Men > Tops > Jackets page](https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html)
28.  Verify that the "Clear" blue link is presented on the page

29. Visit [Men > Tops > Hoodies & Sweatshirts page](https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html)
30.  Verify that the "Clear" blue link is presented on the page

31. Visit [Men > Tops > Tees page](https://magento.softwaretestingboard.com/men/tops-men/tees-men.html)
32.  Verify that the "Clear" blue link is presented on the page

33. Visit [Men > Tops > Bras & Tanks page](https://magento.softwaretestingboard.com/men/tops-men/tanks-men.html)
34.  Verify that the "Clear" blue link is presented on the page

35. Visit [Men > Bottoms > Pants page](https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html)
36.  Verify that the "Clear" blue link is presented on the page

37. Visit [Men > Bottoms > Shorts page](https://magento.softwaretestingboard.com/men/bottoms-men/shorts-men.html)
38.  Verify that the "Clear" blue link is presented on the page

39. Visit [Gear page](https://magento.softwaretestingboard.com/gear.html)
40. Verify that the "Clear" blue link is presented on the page

41. Visit [Gear > Bags page](https://magento.softwaretestingboard.com/gear/bags.html)
42. Verify that the "Clear" blue link is presented on the page

43. Visit [Gear > Fitness equipment page](https://magento.softwaretestingboard.com/gear/fitness-equipment.html)
44. Verify that the "Clear" blue link is presented on the page

45. Visit [Gear > Watches page](https://magento.softwaretestingboard.com/gear/watches.html)
46. Verify that the "Clear" blue link is presented on the page

47. Visit [Gear > Sale page](https://magento.softwaretestingboard.com/sale.html)
48. Verify that the "Clear" blue link button is presented on the page


**Expected results**:

1. The "Clear" blue link is presented on every visited page

### TC_013.001.012 | Compare products | > Clearing the "Compare Products" list after clicking "Clear All" link

**Preconditions:**

1. Any random product is added to "Compare products"

**Steps:**

1. Visit ["What's new page"](https://magento.softwaretestingboard.com/what-is-new.html)
2. Verify that added product is displayed in "Compare Products" block on the left side
3. Click the "Clear" link
4. Verify that the message "Are you sure you want to remove all items from your Compare Products list" is displayed
5. Click the "OK" button in the active modal window

**Expected results:**

1. All products added to the "Compare products" list were removed from the list


### TC_013.001.013 | Compare products | > Removing specific product from the "Compare Products" list after clicking product tittle in the list

**Preconditions:**
1. Any random product is added to "Compare products"

**Steps:**
1. Visit ["What's new page"](https://magento.softwaretestingboard.com/what-is-new.html)
2. Click the specific title of any added to comparison product on the left side
3. Verify that the message "Are you sure you want to remove this item from your Compare Products list" is displayed 
4. Click the "OK" button in the active modal window with message "Are you sure you want to remove this item from your Compare Products list"
 
**Expected results:**
1. Selected product is removed from the Compare Products list