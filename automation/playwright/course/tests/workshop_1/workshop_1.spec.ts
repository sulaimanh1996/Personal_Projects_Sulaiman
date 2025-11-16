import {test, expect} from '@playwright/test';

test('Log In', async ({page})=>{

    //navigate to page
    await page.goto('https://www.saucedemo.com/');

    //sad-flow no input
    await page.click('#login-button');
    await expect(page.locator('text=Epic sadface: Username is required')).toBeVisible();

    //sad-flow wrong input
    await page.fill('#user-name', 'test');
    await page.fill('[name="password"]', 'test')
    await page.click('#login-button');
    await expect(page.locator('text=Epic sadface: Username and password do not match any user in this service')).toBeVisible();

    //sad-flow no username
    await page.fill('#user-name', '');
    await page.fill('[name="password"]', 'test')
    await page.click('#login-button');
    await expect(page.locator('text=Epic sadface: Username is required')).toBeVisible();

    //sad-flow no password
    await page.fill('#user-name', 'test');
    await page.fill('[name="password"]', '')
    await page.click('#login-button');
    await expect(page.locator('text=Epic sadface: Password is required')).toBeVisible();

    //happy-flow login
    await page.fill('#user-name', 'standard_user');
    await page.fill('[name="password"]', 'secret_sauce')
    await page.click('#login-button');
    await expect(page.locator('text=Products')).toBeVisible()

})

test('Product Page', async ({page})=>{

    //nivate to page and login
    await page.goto('https://www.saucedemo.com/');
    await page.fill('#user-name', 'standard_user');
    await page.fill('[name="password"]', 'secret_sauce')
    await page.click('#login-button');

    //view product Sauce Labs Backpack
    await page.click('text=Sauce Labs Backpack');
    await page.click('text=Add to cart');
    await page.click('text=Remove');
    await page.screenshot();
    await page.goBack();

    //view product Sauce Labs Bike Light
    await page.click('text=Sauce Labs Bike Light');
    await page.click('text=Add to cart');
    await page.click('text=Remove');
    await page.goBack(); 

    //view product Sauce Labs Bolt T-Shirt
    await page.click('text=Sauce Labs Bolt T-Shirt');
    await page.click('text=Add to cart');
    await page.click('text=Remove');
    await page.goBack(); 

    //view product Sauce Labs Fleece Jacket
    await page.click('text=Sauce Labs Fleece Jacket');
    await page.click('text=Add to cart');
    await page.click('text=Remove');
    await page.goBack(); 

    //view product Sauce Labs Onesie
    await page.click('text=Sauce Labs Onesie');
    await page.click('text=Add to cart');
    await page.click('text=Remove');
    await page.goBack(); 

    //view product Test.allTheThings() T-Shirt (Red)
    await page.click('text=Test.allTheThings() T-Shirt (Red)');
    await page.click('text=Add to cart');
    await page.click('text=Remove');
    await page.goBack(); 

})
