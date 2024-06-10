**Hey! Here I want to showcase some automated tests that I developed during the RedRover2024_Spring AQA course.
Also, after taking this course, I wrote some more automated tests base on existing User Stories and set up CI in a personal repository.** 

## Test coverage 

Test coverage are determined according to the User Stories stored in user_stories.md

Testcases for automation are based on User Stories stored in test_cases.md

## Project structure

1. When writing tests, we use the Page Objects pattern (also called Page Elements, POM, Page components and so on)
2. The /pages folder contains components that describe the interaction with components on the page.
3. In the tests we import the necessary module from pages.

## Implementation nuances
Rules for writing pages (Also called: components, widgets, pages or whatever)

1. Do not use classes
2. Do not inherit from the base class. If necessary, auxiliary entities can be moved to separate modules (helpers).
3. We store locators only in pages. If necessary, they can be moved to separate modules, but they can be used only in pages
4. Test data can be stored only in tests


```python
from selene import browser
from selene.support.shared.jquery_style import s

url = "https://magento.softwaretestingboard.com/customer/account/login"


def visit():
    browser.open(url)


def login(user, password):
    s("#email").type(user)
    s("#pass").type(password)
    s("#send2").click()
```

You can see an example implementation in the repository c code 8 classes:
<https://github.com/victoretc/selenium_automation_course/tree/main/lesson8>
