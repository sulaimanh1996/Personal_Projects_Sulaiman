*** Settings ***
Library     SeleniumLibrary
Resource    ../../library/global_library.resource

*** Keywords ***
Special View Product
    [Documentation]    Keyword for opening the product page
    [Arguments]    ${locator}
    Click Link    id=${locator}

Special Note Price
    [Documentation]    Gets the price text from the product details page.
    [Arguments]    ${locator}=css:div.inventory_details_price
    ${price}=    Get Text    ${locator}
    Log    Product price is: ${price}
    RETURN    ${price}

Special Add To Cart
    [Documentation]    Adds the product to the cart
    Click Button    id=add-to-cart

Special Remove From Cart
    [Documentation]    Adds the product to the cart
    Click Button    id=remove
