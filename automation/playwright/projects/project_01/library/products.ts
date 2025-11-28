import {Page} from '@playwright/test';
export class productsPage {
    constructor(private page: Page) {}


//? Selectors
    addToCartButton = 'text=Add to cart';
    removeButton = 'text=Remove';


//? Methods
async viewAddRemoveProduct(productName: string) {
    await this.page.click(`text=${productName}`);
    await this.page.click(this.addToCartButton);
    await this.page.click(this.removeButton);
    await this.page.goBack();
}

async changeViewingOrder() {
    await this.page.locator('[data-test="product-sort-container"]').selectOption('za');
    await this.page.locator('[data-test="product-sort-container"]').selectOption('lohi');
    await this.page.locator('[data-test="product-sort-container"]').selectOption('hilo');
    await this.page.locator('[data-test="product-sort-container"]').selectOption('az');
}

async addProductsToCart(){
    await page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click();
    await page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click();
    await page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click();
    await page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click();
    await page.locator('[data-test="add-to-cart-sauce-labs-onesie"]').click();
    await page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click();
}

}
