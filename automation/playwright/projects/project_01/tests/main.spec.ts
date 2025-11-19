import { ProductsPage } from "../library/products";
import { LoginPage } from "../library/login";
import { HamburgerMenu } from "../library/hamburger";
import { test } from '@playwright/test'

test('Log in paths', async ({page})=>{
    const loginPage = new LoginPage(page);
    await loginPage.NavigateToPage();
    await loginPage.LogInSadFlowNoInput('','');
    await loginPage.LogInSadFlowWrongInput('test','test');
    await loginPage.LogInSadFlowNoPassword('test');
    await loginPage.LogInSadFlowNoUsername('test');
    await loginPage.LogInHappyFlow('standard_user','secret_sauce');
})

test('Products', async ({page})=>{
    const productsPage = new ProductsPage(page);
    await productsPage.NavigateToPageAndLogin();
    await productsPage.ViewAddRemoveBackpack();
    await productsPage.ViewAddRemoveBikeLight();
    await productsPage.ViewAddRemoveBoltTShirt();
    await productsPage.ViewAddRemoveFleeceJacket();
    await productsPage.ViewAddRemoveOnesie();
    await productsPage.ViewAddRemoveTestAllTheThingsTShirt();
})

test.only('Hamburger Menu', async ({page})=>{
    const hamburgerMenu = new HamburgerMenu(page);
    const productsPage = new ProductsPage(page);
    await productsPage.NavigateToPageAndLogin();
    await hamburgerMenu.About();
    await hamburgerMenu.Logout();
    await hamburgerMenu.AllItems();
})

