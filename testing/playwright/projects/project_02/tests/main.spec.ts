import { test } from '@playwright/test';
import { expect } from '@playwright/test';

test('as the user i want to control all the main tabs', async ({page})=> {
    await page.goto('https://demos.bellatrix.solutions');
    await page.click('a[href="https://demos.bellatrix.solutions/"]')
    await page.click('a[href="https://demos.bellatrix.solutions/blog/"]')
    await page.click('a[href="https://demos.bellatrix.solutions/cart/"]')
    await page.click('a[href="https://demos.bellatrix.solutions/checkout/"]')
    await page.click('a[href="https://demos.bellatrix.solutions/contact-form/"]')
    await page.click('a[href="https://demos.bellatrix.solutions/my-account/"]')
    await page.click('a[href="https://demos.bellatrix.solutions/welcome/"]')
    await page.close();
})

test('as the user i want to check out the shop', async ({page})=> {
    await page.goto('https://demos.bellatrix.solutions');
    await page.click('a[href="https://demos.bellatrix.solutions/product/falcon-9/"]')
    await page.fill('#quantity_695358465d8bf','4')
    await page.getByRole('button', { name: 'add-to-cart'}).click();
    await page.click('a[href="#tab-additional_information"]')
    await page.click('a[href="#tab-reviews"]')
    await page.click('a[href="#tab-description"]')
    await expect(page.locator('text=Falcon 9 is a family of two-stage-to-orbit medium lift launch vehicles, named for its use of nine Merlin first-stage engines, designed and manufactured by SpaceX. Variants include the initial v1.0 (expendable), v1.1 (partially-reusable), and current “Full Thrust” v1.2 (partially-reusable). Falcon 9 is powered by rocket engines utilizing liquid oxygen (LOX) and rocket-grade kerosene (RP-1) propellants.')).toBeVisible();

    await page.close();
})

