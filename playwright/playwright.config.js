import { chromium, defineConfig, devices } from "@playwright/test";

const config = ({                        // Package everything here as default settings

  testDir : './tests',                   // Directory for test cases
  timeout : 40000,                       // Max time a test can run (ms)
  expect  : { timeout: 50000 },          // Max time for Playwright assertions
  use     : { browserName: 'chromium' },   // Browser type
  reporter: 'html'                       // Test results reporter

});

module.exports = config;                 // Make config accessible
