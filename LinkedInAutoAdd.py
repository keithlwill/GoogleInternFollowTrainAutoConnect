import csv
from selenium import webdriver

def constructList():
    accounts = []

    with open("GoogleInternFollowTrain.csv", "r") as followTrain:
        reader = csv.reader(followTrain, delimiter=",")
        for row in reader:
            if "linkedin.com" in row[1]:
                accounts.append(row[1])

    for i in range(len(accounts)): #cleaning up links so that the driver can go to them
        if accounts[i][0:4] != "http":
            accounts[i] = "https://" + accounts[i]
    

    return accounts

if __name__ == "__main__":
    lst = constructList()

    driver = webdriver.Chrome('chromedriver')

    
    driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin') #driver navigates to LinkedIn.com

    username = driver.find_element_by_id('username') #find username field
    username.send_keys('ENTER LINKEDIN USERNAME HERE') #enter username

    password = driver.find_element_by_id('password') #enter password field
    password.send_keys('ENTER LINKEDIN PASSWORD HERE') #enter password

    signInButton = driver.find_element_by_class_name('login__form_action_container') #find login button
    signInButton.click() #click login
    
    print(lst)

    for link in lst:
        driver.get(link) 
        
        connectButton = driver.find_elements_by_xpath("//button[contains(string(), 'Connect')]")[0] #for every link in the follow train list, click the connect button
        connectButton.click()
        sendButton = driver.find_elements_by_xpath("//button[contains(string(), 'Done')]")[0] #In order for the connection invitation to send, this button NEEDS to be clicked
        sendButton.click()
        