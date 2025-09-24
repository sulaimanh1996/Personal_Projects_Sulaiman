*** Settings ***
Resource    ../settings/libraries_and_resources.resource

*** Variables ***


*** Keywords ***
SL_Username
    [Arguments]    ${username}    
    Input Text    locator=user-name    text=${username}

SL_Password
    [Arguments]    ${password}
    Input Text    locator=password    text=${password}

