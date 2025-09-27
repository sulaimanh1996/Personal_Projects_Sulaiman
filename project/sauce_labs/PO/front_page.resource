*** Settings ***
Resource    ../../keywords/sauce_labs_keywords.resource

*** Variables ***
@{USERNAME LIST}            standard_user
${PASSWORD}                 secret_sauce
${LOCATOR USERNAME}         user-name
${LOCATOR PASSWORD}         password
${LOCATOR LOGINBUTTON}      login-button
${URL}                      https://www.saucedemo.com/
${BROWSER}                  chrome
${SELENIUM_SPEED}           0.2
${MAXAMIZE}                 True


*** Keywords ***
Log In
    [Documentation]    This testcase is for verifying that the user can log in the webpage
    GLOBAL Username    username=${username list}    locator=${locator username}    RANDOM=True
    GLOBAL Password    password=${password}    locator=${locator password}
    GLOBAL Button    locator=${locator loginbutton}
