// Import Playwright test API
const { test } = require('@playwright/test');

/**
 * Playwright Test Basics
 * ----------------------
 * - Each `test()` defines a test case.
 * - Tests can run in parallel, so always use `async/await` for async actions.
 * - An anonymous function is written like: test('name', async () => { ... }).
 *
 * Fixtures (provided automatically by Playwright):
 * - browser → a browser instance (Chromium, Firefox, WebKit).
 * - context → an isolated browser profile/session.
 * - page → a single tab within the context where actions happen.
 *
 * Ways to use them:
 * - You can create your own context/page using browser.newContext().
 * - Or let Playwright manage it by using the { page } fixture directly.
 */

// Example 1: Manually creating context + page
test.only('Browser-level Playwright test', async ({browser}) => {
  const context = await browser.newContext();   // fresh browser context
  const page = await context.newPage();         // new page (tab) in that context
  await page.goto('https://rahulshettyacademy.com/loginpagePractice/');
});

// Example 2: Using the built-in { page } fixture (simpler)
test('Page-level Playwright test', async ({page}) => {
  await page.goto('https://google.com');
});
