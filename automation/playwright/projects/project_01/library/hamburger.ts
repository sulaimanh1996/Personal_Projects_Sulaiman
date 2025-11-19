import {Page} from '@playwright/test'
import { LoginPage } from "../library/login";
export class HamburgerMenu {
    constructor(private page:Page) {}

    async About() {
        await this.page.click('#react-burger-menu-btn');
        await this.page.click('#about_sidebar_link');
        await this.page.goBack();    
    }

    async Logout() {
        const loginPage = new LoginPage(this.page);
        await this.page.click('#react-burger-menu-btn');
        await this.page.click('#logout_sidebar_link');
        await loginPage.LogInHappyFlow('standard_user','secret_sauce');
    }

    async AllItems() {
        await this.page.click('text=Sauce Labs Backpack');
        await this.page.click('#react-burger-menu-btn');
        await this.page.click('#inventory_sidebar_link');
    }
    
}