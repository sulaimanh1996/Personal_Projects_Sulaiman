*** Settings ***
Resource    ../../settings/libraries_and_resources.resource
Suite Setup    Suite Setup    URL=https://www.saucedemo.com/    BROWSER=chrome    SELENIUM_SPEED=0.2    MAXIMIZE=False
Suite Teardown    Suite Teardown

*** Variables ***

*** Test Cases ***
As the user i should be able to log in to the webshop.
    SL_Username    username=standard_user
    SL_Password    password=secret_sauce
    Click Button    locator=login-button

