*** Settings ***
Resource    ../../keywords/sauce_labs_keywords.resource


*** Keywords ***
View, Add, Note Price And Remove From Cart Bike Light 0
    [Documentation]    This testcase is for veryfing the functionality of the product page
    Special View Product    locator=item-0-title-link
    Special Note Price
    Special Add To Cart
    Special Remove From Cart

View, Add, Note Price And Remove From Cart T-Shirt 1
    [Documentation]    This testcase is for veryfing the functionality of the product page
    Special View Product    locator=item-1-title-link
    Special Note Price
    Special Add To Cart
    Special Remove From Cart

View, Add, Note Price And Remove From Cart Onesie 2
    [Documentation]    This testcase is for veryfing the functionality of the product page
    Special View Product    locator=item-2-title-link
    Special Note Price
    Special Add To Cart
    Special Remove From Cart

View, Add, Note Price And Remove From Cart Red Shirt 3
    [Documentation]    This testcase is for veryfing the functionality of the product page
    Special View Product    locator=item-3-title-link
    Special Note Price
    Special Add To Cart
    Special Remove From Cart

View, Add, Note Price And Remove From Cart Backpack 4
    [Documentation]    This testcase is for veryfing the functionality of the product page
    Special View Product    locator=item-4-title-link
    Special Note Price
    Special Add To Cart
    Special Remove From Cart

View, Add, Note Price And Remove From Cart Fleece Jacket
    [Documentation]    This testcase is for veryfing the functionality of the product page
    Special View Product    locator=item-5-title-link
    Special Note Price
    Special Add To Cart
    Special Remove From Cart





