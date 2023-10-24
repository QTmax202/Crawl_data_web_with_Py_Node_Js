from numpy import require


const puppeteer = require('puppeteer')
const base64Img = require('base64-img')

# def sleep(ms) :
#   return new Promise(resolve => setTimeout(resolve, ms))


const fs = require('fs');
const path = require('path');

function saveDataURIToFile(dataURI, filePath) {
  base64Img.img(dataURI, 'captcha', filePath, function (err, filepath) {
    if (err) {
      console.error('Error:', err);
    } else {
      console.log('Image saved to:', filepath);
    }
  });
}


(async () => {
  const browser = await puppeteer.launch({
    headless: false, // Set to true for headless mode (no GUI), false to see the browser
    args: [
      '--no-sandbox', // Required when running as root user
      '--disable-infobars',
      '--disable-notifications',
      '--disable-geolocation',
      '--disable-web-security',
      '--disable-features=IsolateOrigins,site-per-process',
    ],
  });

  const page = await browser.newPage();

  // Set a custom user agent to mimic a different browser
  await page.setUserAgent(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
  );

  // Navigate to the website you want to visit
  const url = 'https://ebank.mbbank.com.vn/cp/pl/login?returnUrl=%2F';
  await page.goto(url);
  // Wait for a specific selector to appear on the page
  await page.waitForSelector('#refresh-captcha'); // Replace with the actual selector you want to wait for  
  console.log("Refresh-captcha Button Appeared");
  await sleep(1000);
  while (true) {
	  const element = await page.$x('/html/body/app-root/div/mbb-welcome/div/div/div[2]/div[2]/div/mbb-login/form/div/div[2]/mbb-word-captcha/div/div[2]/div/div/img');
	  // Check if the element was found
	  if (element.length > 0) {
		// Get the "src" attribute of the element
		const srcAttributeValue = await (await element[0].getProperty('src')).jsonValue();
		console.log('src attribute value:', srcAttributeValue);
		const outputPath =  Date.now();
		console.log(outputPath);
		saveDataURIToFile(srcAttributeValue, outputPath);
    //refresh mã captcha
		await page.click('#refresh-captcha');
    //delay
		# await sleep(2000);		
	  } else {
		console.log('Element not found.');
	  }
  }
})();
