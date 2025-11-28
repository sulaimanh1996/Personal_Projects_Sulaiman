import {Page, expect} from '@playwright/test';
export class cartPage {
    constructor(private page: Page) {}

    async navigateToSite() {
        await this.page.goto('https://saucedemo.com');
    }

}