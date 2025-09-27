*** Settings ***
Resource            ../keywords/sauce_labs_keywords.resource
Resource            ../../settings/startup_shutdown.resource
Resource            ./PO/product_page.resource
Resource            ./PO/front_page.resource

Suite Setup         Suite Setup
...                     URL=${URL}
...                     BROWSER=${BROWSER}
...                     SELENIUM_SPEED=${SELENIUM_SPEED}
...                     MAXIMIZE=${MAXAMIZE}
Suite Teardown      Suite Teardown


*** Test Cases ***
As The User I Should Be Able To View, Add, Note The Price And Remove The Product From The Cart
    [Documentation]    This testcase is for testing the entire proces of all the products
    Log In
    View, Add, Note Price And Remove From Cart Bike Light 0
    View, Add, Note Price And Remove From Cart T-Shirt 1
    View, Add, Note Price And Remove From Cart Onesie 2
    View, Add, Note Price And Remove From Cart Red Shirt 3
    View, Add, Note Price And Remove From Cart Backpack 4
    View, Add, Note Price And Remove From Cart Fleece Jacket 5
