*** Settings ***
Resource    ../settings/libraries_and_resources.resource


*** Keywords ***
Suite Setup
    [Documentation]    This keyword is executed once before all tests in the suite. Fill in the URL and browser type as needed.
    [Arguments]    ${URL}    ${BROWSER}=chrome    ${SELENIUM_SPEED}=0.5    ${MAXIMIZE}=True
    Open Browser    url=${URL}    browser=${BROWSER}
    Set Selenium Speed    ${SELENIUM_SPEED}
    IF    ${MAXIMIZE} == True
        Maximize Browser Window
    END

Suite Teardown
    [Documentation]    This keyword is executed once after all tests in the suite.
    Close All Browsers