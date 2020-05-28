# Google Intern Follow Train AutoConnect
There's a Google Intern Follow Train. A.K.A a Google Sheets document with interns and a bunch of links to their LinkedIn, Instagram, Twitter, etc

**Instead of manually clicking through hundreds of links, why not learn some basic web automation and automate the process with Selenium?**

My LinkedIn adder is almost finished. I'll add other social media later.

## How To Use The File
-Make sure Selenium is installed! If it isn't, go to your terminal and type "pip install -U selenium"

-You need to install a webdriver that Selenium can interact with. Personally, I use Chromium for my webdriver. You can download it here: https://sites.google.com/a/chromium.org/chromedriver/downloads

-Save the follow train as a **CSV** file and place it in the same directory where the Python file is. If you don't have a link to the follow train, shoot me an email at Keith.Will247@gmail.com

-Enter your LinkedIn username and password in the Python file where it says to. (the parameter of the x.send_keys methods)

-Run the file, and watch magic happen.

## Many, Many, Many Issues
There are a **lot** of issues that need to be resolved, including, but not limited to:

-A couple of links in the follow train aren't valid. When the webdriver navigates to the invalid link, the file stops running because it can't find a connect button. 

-LinkedIn doesn't like when people scrape the website. The confirmation button to finalize a connection invitation changes between "Done" and "Send Now". You might need to alter the file so that the right button can be found. (the "sendButton" variable)

-When you are already connected with someone, the file stops running (because a "connect" button can't be found). I'm not sure how to fix this but it shouldn't be too difficult

-**You can only send a limited number of LinkedIn invitations in a limited period of time.** I'm not sure of the number or time period, but if too many invitations are sent too quickly, LinkedIn prohibits you from sending messages for a while. In my personal experience, sending ~50 invitations per day kept me in the safe zone. I had to alter the column containing the LinkedIn links (copying and pasting and messing around with the follow train CSV)

-Sometimes, the webdriver just stops. Don't know why.

## TLDR:
### Install Selenium. Download a webdriver and place in same directory as Python file. Go to Python file and enter LinkedIn username and password where applicable. Run file. Watch webdriver inevitably fail due to one of potentially billions of issues I haven't figured out yet.
