*** Settings ***
Library     SeleniumLibrary


*** Keywords ***
GLOBAL Username
    [Documentation]    Fills in a username. If RANDOM=True, picks one from a list randomly.
    [Arguments]    ${username}    ${locator}    ${RANDOM}=False
    IF    '${RANDOM}'=='True'
        ${username}=    Evaluate    random.choice(${username})    random
    END
    Input Text    locator=${locator}    text=${username}

GLOBAL Password
    [Documentation]    Fills in a password. If RANDOM=True, picks one from a list randomly.
    [Arguments]    ${password}    ${locator}    ${RANDOM}=False
    IF    '${RANDOM}'=='True'
        ${password}=    Evaluate    random.choice(${password})    random
    END
    Input Text    locator=${locator}    text=${password}

GLOBAL Button
    [Documentation]    This keyword is for finding and pressing buttons
    [Arguments]    ${locator}
    ${status}    ${msg}=    Run Keyword And Ignore Error    Click Button    ${locator}
    IF    $status == 'FAIL'    Click Link    ${locator}

