# Google Intern Follow Train AutoConnect
There's a Google Intern Follow Train. A.K.A a Google Sheets document with interns and a bunch of links to their LinkedIn, Instagram, Twitter, etc

**Instead of manually clicking through hundreds of links, why not learn some basic web automation and automate the process with Selenium?**

My LinkedIn adder is almost finished. I'll add other social media later.

## How To Use The File
-Make sure Selenium is installed, if it isn't, go to your terminal and type "pip install -U selenium"

-You need to install a webdriver that Selenium can interact with. Personally, I use Chromium for my webdriver. You can download it here: https://sites.google.com/a/chromium.org/chromedriver/downloads Make sure the webdriver matches up with the version of Chrome you have installed.

-Save the follow train as a **CSV** file and place it in the same directory where the Python file is. If you don't have a link to the follow train, shoot me an email at Keith.Will247@gmail.com

-Enter your LinkedIn username and password in the Python file where it says to. (the parameter of the x.send_keys methods)

-Run the file, and watch magic happen.

## Many, Many, Many Issues
There are a few issues that need to be resolved, including, but not limited to:

-When you are already connected with someone, a connection invitation can be sent to an unintended person (because an alternate "connect" is found). I'm not sure how to fix this.

-**You can only send a limited number of LinkedIn invitations in a limited period of time.** I'm not sure of the number or time period, but if too many invitations are sent too quickly, LinkedIn prohibits you from sending messages for a while. In my personal experience, sending ~50 invitations per day kept me in the safe zone. I had to alter the column containing the LinkedIn links (copying and pasting and messing around with the follow train CSV)

-Sometimes, the webdriver just stops. I don't know why.

## TLDR:
### Make sure Selenium is installed. Download a webdriver and place in same directory as Python file. Go to Python file and enter LinkedIn username and password where applicable. Run file. Watch webdriver inevitably fail due to one of potentially billions of issues I haven't figured out yet.
