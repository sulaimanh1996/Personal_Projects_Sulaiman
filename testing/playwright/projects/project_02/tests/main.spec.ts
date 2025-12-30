import { productsPage } from "../library/products";
import { loginPage } from "../library/login";
import { hamburgerMenu } from "../library/hamburger";
import { generalKeywords } from '../library/general'
import { cartPage } from "../library/cart";
import { purchasePage } from "../library/purchase";
import { test } from '@playwright/test'

const productNames: string[] = ['sauce-labs-backpack', 'sauce-labs-bike-light', 'sauce-labs-bolt-t-shirt', 'sauce-labs-fleece-jacket', 'sauce-labs-onesie', 'test.allthethings()-t-shirt-(red)'];

test('As the user i want to be able to login', async ({page})=>{
    const general = new generalKeywords(page)
    const login = new loginPage(page);

    await general.navigateToSite();
    await login.noInput();

    await login.noPassword();
    await login.noUsername();
    await login.wrongPassword();
    await login.wrongUsername();
    await login.correctLogin();
})

test('As the user i want to be able to use the hamburger menu', async ({page})=>{
    const general = new generalKeywords(page)
    const login = new loginPage(page);
    const hamburger = new hamburgerMenu(page);

    await general.navigateToSite();
    await login.correctLogin();

    await hamburger.hamburgerAbout();
    await hamburger.hamburgerLogout();
    await hamburger.hamburgerAllitems();
    await hamburger.hamburgerCloseMenu();
})

test('As the user i want to be able to use the products page', async ({page})=>{
    const general = new generalKeywords(page)
    const login = new loginPage(page);
    const products = new productsPage(page);

    await general.navigateToSite();
    await login.correctLogin();

    await products.changeProductsOrder();
    await products.productProcesBackpack();
    await products.productProcesBikelight();
    await products.productProcesFleecejacket();
    await products.productProcesOnesie();
    await products.productProcesRedTShirt();
    await products.productProcesTShirt();  
})

test('As the user i want to be able to use the cart', async ({page})=>{
    const general = new generalKeywords(page)
    const login = new loginPage(page);
    const cart = new cartPage(page);
    const products = new productsPage(page);

    await general.navigateToSite();
    await login.correctLogin();

    await products.addAllProducts();
    await cart.clickOnShoppingCart();
    await cart.removeProductsFromCart();
    await cart.goBackFromShoppingCart();
    await products.addAllProducts();
    await cart.clickOnShoppingCart();
    await cart.checkout();
})

test('As the user i want to be able to finalize my purchase process', async ({page})=>{
    const general = new generalKeywords(page)
    const login = new loginPage(page);
    const purchase = new purchasePage(page);
    const products = new productsPage(page);
    const cart = new cartPage(page);

    await general.navigateToSite();
    await login.correctLogin();

    await products.addAllProducts();
    await cart.clickOnShoppingCart();
    await cart.checkout();
    await purchase.noFirstName();
    await purchase.noLastName();
    await purchase.noPostalCode();
    await purchase.CorrectDetails();

    await purchase.finishingPurchase();
})
