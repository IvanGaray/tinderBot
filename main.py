from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from credenciales import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://tinder.com')
        sleep(2)

        #Storing the current window handle to get back to dashboard
        main_page = self.driver.current_window_handle

        fb_btn = self.driver.find_element(By.XPATH,'//main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        fb_btn.click()
        sleep(5)

        btn = self.driver.find_element(By.XPATH,'//div/div/div[3]/span/div[2]/button')
        btn.click()
        sleep(2)

        #Storing the new pop up window as login_page for switching later.
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
      
        #Login Page.
        self.driver.switch_to.window(login_page)
        sleep(3)
        emailInput = self.driver.find_element(By.XPATH,'//input[@id="email"]')
        emailInput.send_keys(username)
        passInput = self.driver.find_element(By.XPATH,'//input[@id="pass"]')
        passInput.send_keys(password)
        sleep(1)
        login_btn = self.driver.find_element(By.CSS_SELECTOR,'label#loginbutton')
        login_btn.click()

        #Tinder main page.
        self.driver.switch_to.window(main_page)
        sleep(10)
        allowButton = self.driver.find_element(By.XPATH,'//button[@data-testid="allow"]')
        allowButton.click()
        sleep(2)
        allowButton = self.driver.find_element(By.XPATH,'//button[@data-testid="decline"]')
        allowButton.click()
        sleep(5)

        while True:
            try:
                sleep(0.5)
                like_btn = self.driver.find_element(By.XPATH,'//div/div[4]/button')
                like_btn.click()
            except:
                try:
                    notInterestedBtn = self.driver.find_element(By.XPATH,'//main/div/div[2]/button[2]')
                    notInterestedBtn.click()
                except:
                    try:
                        upSuperLike = self.driver.find_element(By.XPATH,'//main/div/button[2]')
                        upSuperLike.click()
                    except:
                        try:
                            seeWLYMbtn = self.driver.find_element(By.XPATH,'//main/div/div/div[3]/button[2]')
                            seeWLYMbtn.click()
                        except Exception as e:
                            print(e)
                            self.driver.close()
    
TinderBot()