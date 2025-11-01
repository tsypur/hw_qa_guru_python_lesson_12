import allure

from data import users
from pages.registration_page import RegistrationPage


def test_demo_qa_form(browser_window):
    registration_page = RegistrationPage()
    student = users.student

    with allure.step("open registration page"):
        registration_page.open()
    with allure.step("add personal information"):
        registration_page.register(student)
    with allure.step("check registration form"):
        registration_page.should_have_registered_user(student)