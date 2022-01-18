# Scraping 20K Shopify Websites

This project is about scraping 20K shopify websites. The actuall task is to find some strings on the html and collecting social media account such as facebook and instagram including its likes/followers count.  

It takes more than one weeks to work on this project. The difficulty of this project is on look for "learnq.push" and collecting social media likes/followers count. The final result of this project is writed on a spreadsheet file.  

Most of the scraping are being use in this project are `Python Selenium`. Since the facebook and Instagram API are no longer support mass requests, that's why I decide to use Python Selenium instead. That's also why this project consume so much time. But not all the part of this project done are manually using `Python Selenium`, some of the scripts are also include `asyncio` and `aiohttp` libraries to do the asynchronous programming stuff.  

This scraping porject is made up of 5 steps:
1. [Rendering HTML](#step-1-render-html-using-python-selenium)
2. [Look for "klaviyo" strings and collecting social media accounts](#step-2-look-for-klaviyo-strings-and-collecting-the-websites-social-media-accounts)
3. [Look for "learnq.push" strings](#step-3-look-for-learnqpush-strings)
4. [Collecting Facebook page likes and followers](#step-4-collecting-facebook-page-likes--followers-count)
5. [Collecting Instagram followers](#step-5-collecting-instagram-followers-count)
6. [Gather everything and write it out as excel (.xlsx) file](#step-6-write-to-excel-using-pandas)

### Step 1: Render HTML using Python Selenium
I have tried to use `aiohttp` to render 20K websites at once, but it seems some websites with JavaScript can not rendered completely. That's why I rerender everything using python selenium instead. You can check everything on my code [here](html_renderer.py).

### Step 2: Look for "klaviyo" strings and collecting the websites social media accounts
After the html rendered successfully. The next step I do is to looks for "klaviyo" strings and look for social media accounts from each the html using regular expresssion (link to github repo with monster regex). * I'm not really sure what is the strings accociated with, I should read more about that

klaviyo strings:
> https://static.klaviyo.com/onsite/js/klaviyo.js

### Step 3: Look for "learnq.push" strings
This step I think are the most difficult task, before continue on this task, I should make sure Step 1 and Step 2 are done completely so I can label the unsuccess rendered html as a broken url or not available websites and do not need to looks something with no data init. The challange of this task is trying to find url with "/products" inside the website html, sometimes you need to look it by open the "/collections" url.  

The actuall string I looking for are:
> learnq.push(['track', 'Added to Cart', item])  

or

>  learnq.push(['track', 'Add To Cart', item])

### Step 4: Collecting Facebook Page Likes \& Followers Count
Since I'm not use any Facebook API (not really sure it will works well), I decide to do it directly on the browser using `Selenium` and `BeautifulSoup`. For more details, I only use python selenium to render and collect the facebook front page html, while on the backend `BeautiulSoup` would scrape the data I wanted.

### Step 5: Collecting Instagram Followers Count
In this step I use Instagram public API for collecting the instagram account followers count.

### Step 6: Write to Excel using Pandas
After all the data was collected, the last step are turn the data as a `Pandas` `DataFrame` and then write it out as an excel file with `.xslx` extension.