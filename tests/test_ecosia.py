from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s


def test_search():
    browser.open('https://www.ecosia.org/')

    s('[name=q]').type('yashaka selene').press_enter()
    ss('.result').first.element('.result-title').click()

    ss('[href="/yashaka/selene"]').should(have.size(3))
