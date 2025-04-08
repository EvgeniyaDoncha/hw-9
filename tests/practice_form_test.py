import command
from selene.support.shared import browser
from selene import have

from hw_9.resources import resources_path


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )

        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self,value):
        browser.element('#firstName').type('value')


    def fill_day_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('month')
        browser.element('.react-datepicker__year-select').type('year')
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datapiker__day--outside-month)'
            ).click()

    def should_registered_user_with(self, first_name, last_name, param2, param3, param4, param5, param6, param7, param8,
                                    param9):
        browser.element('table').all('td').even.should(
            have.exact_texts(
                f'{first_name}{last_name}',
                'name@example.com',
                'Female',
                '1234567891',
                '11 May,1999',
                'Computer Science',
                'Reading',
                'foto.jpg',
                'Moscowskaya Street 18',
                'NCR Delhi'

            )
        )


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()


    # WHEN
    registration_page.fill_first_name('Olga')


    browser.element('#lastName').type('YA')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()

    browser.element('#userNumber').type('1234567891')
    browser.element('#userEmail').type('name@example.com')

    browser.element('[for="hobbies-checkbox-2"]').perform(command.js.scroll_into_view).click()

    browser.element('#currentAddress').type('Moscowskaya Street 18')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('HCR')
    ).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_texts('Noida')
    ).click()


    registration_page.fill_day_of_birth('1999', 'May', '11')



    browser.element('#subjectsInput').type('Commerce').press_enter()

    browser.element('#uploadPicture').set_value(resources_path('foto.jpg'))


    browser.element('#submit').press_enter()
    browser.element('#submit').perform(command.js.click)

    #THEN
    registration_page.should_registered_user_with(


            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science',
            'Reading',
            'foto.jpg',
            'Moscowskaya Street 18',
            'NCR Delhi'
        )
    browser.element('table').all('td').even.should(
        have.exact_texts(
            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science',
            'Reading',
            'foto.jpg',
            'Moscowskaya Street 18',
            'NCR Delhi'

        )
    )