import {Page, expect} from '@playwright/test';
export class purchasePage {
    constructor(private page: Page) {}

    async navigateToSite() {
        await this.page.goto('https://saucedemo.com');
    }

}