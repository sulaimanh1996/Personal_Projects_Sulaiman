//? Imports and Exports
import {Page, expect} from '@playwright/test';
export class loginPage {
    constructor(private page: Page) {}


//? Selectors
    private usernameInput = '#user-name';
    private passwordInput = '[name="password"]';
    private loginButton = '#login-button';
    private errorMessageNoInputOrUsername = 'Epic sadface: Username is required';
    private errorMessageWrongInput = 'Epic sadface: Username and password do not match any user in this service';
    private errorMessageNoPassword = 'Epic sadface: Password is required';
    private productsTitle = 'Products';
    private pagelink = 'https://www.saucedemo.com/';


//? Methods
    async navigateToSite() {
        await this.page.goto(this.pagelink);
    }

    async noInput(username: string, password: string) {
        await this.page.click(this.loginButton);
        await expect(this.page.getByText(this.errorMessageNoInputOrUsername)).toBeVisible();
    }

    async wrongInput(username: string, password: string) {
        await this.page.fill(this.usernameInput, username);
        await this.page.fill(this.passwordInput, password);
        await this.page.click(this.loginButton);
        await expect(this.page.getByText(this.errorMessageWrongInput)).toBeVisible();
    }

    async noUsername(password: string) {
        await this.page.fill(this.usernameInput, '');
        await this.page.fill(this.passwordInput, password)
        await this.page.click(this.loginButton);
        await expect(this.page.getByText(this.errorMessageNoInputOrUsername)).toBeVisible();
    }
    
    async noPassword(username: string) {
        await this.page.fill(this.usernameInput, username);
        await this.page.fill(this.passwordInput, '');
        await this.page.click(this.loginButton);
        await expect(this.page.getByText(this.errorMessageNoPassword)).toBeVisible();
    }

    async login(username: string, password: string) {
        await this.page.fill(this.usernameInput, username);
        await this.page.fill(this.passwordInput, password);
        await this.page.click(this.loginButton);
        await expect(this.page.getByText(this.productsTitle)).toBeVisible()
    }
}
