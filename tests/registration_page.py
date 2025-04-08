import os


from selene.support.shared import browser

from selene import be, have, command

from .locators import Locators



class RegistrationPage():
    def page_open(self):
        browser.open('/automation-practice-form')
        self._set_up_page()

    def _set_up_page(self):
        browser.execute_script(f'document.querySelector("{Locators.page_set_up_footer}").remove()')
        browser.execute_script(f'document.querySelector("{Locators.page_set_up_fixedban}").remove()')
        browser.execute_script(f'document.querySelector("{Locators.page_set_up_right_side_advertisment}").remove()')












