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

}