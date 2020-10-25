#Imports
import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#Main Class
class Scraper: 
    
    def __init__ (self, config):
        driver = webdriver.Chrome(executable_path=config['driverPath'])
        driver.wait = WebDriverWait(driver, 5)
        driver.get("https://hanime.tv/browse/images")
        time.sleep(5)
        self.driver = driver
        self.config = config
        self.imageLinks = []
        self.totalCounter = 0
        
        
        
    def run (self):
        self.checkDirectory()
        self.askPages()
        self.selectTags()
        time.sleep(1)
        self.pageLooper()
        self.downloadImages()
        
        time.sleep(5)
        print("\n\n------------------------\n\nTotal downloaded: {}\nOutput directory: {}\nTime: {}s\n\n------------------------\n".format(self.totalCounter, os.path.abspath(self.config['targetPath']), round(time.time() - self.startTime, 2)))
    
    
    
    def checkDirectory (self):
        if not os.path.exists(self.config['targetPath']):
           os.mkdir(self.config['targetPath'])
        os.chmod(self.config['targetPath'], 0o777) 



    def askPages (self):
        print("------------------------")
        self.pageStart = int(input("Start page: ")) 
        self.pageEnd = int(input("End page: ")) 
        
        
        
    def selectTags (self): 
        self.resetTags()
        print("------------------------\nTags selection:")
        for key, value in self.config['tags'].items():
            if (value['enabled'] == True):
                #click on the tag by using its div index
                self.driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[{}]/div""".format(value['divIndex'])).click()
                time.sleep(1)
                print("\t- " + key)
        print("------------------------")



    def resetTags (self):
        #unclick on the #media and the #nsfw tags that are turned on by default
        self.driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[1]/div""").click()
        self.driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[2]/div""").click()



    def pageLooper(self):
        self.startTime = time.time() #save the timestamp just before the scraping in order to calculate the total scrape time
        for i in range (self.pageEnd):
            if i+1 >= self.pageStart:
                self.scrape()
            #next page
            if i+1 < self.pageEnd:
                self.driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[4]/button[3]/div""").click()  
    
    
    
    def scrape (self):
        for i in range(1, 100): #100 to get the maximum amount as possible
            try:
                content = self.driver.find_element_by_xpath(
                    """//*[@id="app"]/div[4]/main/div/div/div/div[5]/a[{0}]""".format(i)
                ).get_attribute("href") #get the link
                self.imageLinks.append(content) 
                if self.config["showLinks"] == True:
                    print(content)
            except:
                break
        
        
        
    def downloadImages(self):
        for imageLink in self.imageLinks:
            imageName = imageLink.split("/")[-1]
            if not os.path.exists(self.config['targetPath'] + imageName):
                subprocess.Popen("curl -s -O " + imageLink, shell=True, cwd=self.config['targetPath'])
                self.totalCounter += 1


            

        
        
    
        
        
        
    
    