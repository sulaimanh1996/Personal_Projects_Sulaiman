import {Page} from '@playwright/test';
export class CartPage {
    constructor(private page: Page) {}


//? Selectors


//? Methods
async removeProductFromCart(productName: string){
    await this.page.locator('[data-test="remove-sauce-labs-backpack"]').click();
    await this.page.locator('[data-test="remove-sauce-labs-bike-light"]').click();
    await this.page.locator('[data-test="remove-sauce-labs-bolt-t-shirt"]').click();
    await this.page.locator('[data-test="remove-sauce-labs-fleece-jacket"]').click();
    await this.page.locator('[data-test="remove-test.allthethings()-t-shirt-(red)"]').click();
    await this.page.locator('[data-test="remove-sauce-labs-onesie"]').click();
}

async 
}


}