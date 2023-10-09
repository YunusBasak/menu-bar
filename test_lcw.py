
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Constants import globalConstants , environmentConstants


'''
Kullanılan Locator'lar
XPATH
'''

class TestLcw():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.get(globalConstants.BASEURL)
    self.driver.maximize_window()
  
  def teardown_method(self):
    self.driver.quit()

  def WaitForElementVisible(self,locator,timeout=15):
      WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
  
  def test_lcw(self):
    # Pop-up'ı kapatma kodudur.
    self.WaitForElementVisible((By.XPATH,environmentConstants.POPUP))
    popup = self.driver.find_element(By.XPATH, environmentConstants.POPUP)
    actions = ActionChains(self.driver)
    actions.move_to_element(popup).click().perform()
    self.WaitForElementVisible((By.XPATH, environmentConstants.GENDER))
    gender = self.driver.find_element(By.XPATH,environmentConstants.GENDER)
    actions = ActionChains(self.driver)
    assert self.driver.find_element(By.XPATH,environmentConstants.GENDER).text == "BEBEK"
    actions.move_to_element(gender).perform()
    self.WaitForElementVisible((By.XPATH,environmentConstants.CATEGORYS))
    categorys = self.driver.find_element(By.XPATH,environmentConstants.CATEGORYS)
    actions = ActionChains(self.driver)
    assert self.driver.find_element(By.XPATH,environmentConstants.CATEGORYS).text == "(0-12 AY)"
    actions.move_to_element(categorys).perform()
    self.WaitForElementVisible((By.XPATH, environmentConstants.CATEGORY))
    category = self.driver.find_element(By.XPATH, environmentConstants.CATEGORY)
    actions = ActionChains(self.driver)
    # 'Şort' kategorisine gitmektedir ancak 'Mont ve Kaban' kategorisi olarak görmektedir.
    assert self.driver.find_element(By.XPATH,environmentConstants.CATEGORY).text == "Mont ve Kaban"
    actions.move_to_element(category).click().perform()
    # Sayfayı 200 px aşağı kaydırma kodudur. Selenium Locatorı görünmediği için yazılmıştır.
    self.driver.execute_script("window.scrollBy(0,200)","")
    self.WaitForElementVisible((By.XPATH, environmentConstants.PRODUCT))
    product = self.driver.find_element(By.XPATH, environmentConstants.PRODUCT)
    actions = ActionChains(self.driver)
    assert self.driver.find_element(By.XPATH, environmentConstants.PRODUCT).text == "Standart Kalıp Kız Bebek Şort Etek"
    actions.move_to_element(product).click().perform()
    self.WaitForElementVisible((By.XPATH, environmentConstants.ADDSIZE))
    addSize = self.driver.find_element(By.XPATH,environmentConstants.ADDSIZE)
    actions = ActionChains(self.driver)
    assert self.driver.find_element(By.XPATH, environmentConstants.ADDSIZE).text == "5-6 Yaş"
    actions.move_to_element(addSize).click().perform()
    self.WaitForElementVisible((By.XPATH, environmentConstants.ADD_TO_CART))
    addToCart = self.driver.find_element(By.XPATH, environmentConstants.ADD_TO_CART)
    actions = ActionChains(self.driver)
    assert self.driver.find_element(By.XPATH, environmentConstants.ADD_TO_CART).text == "SEPETE EKLE"
    actions.move_to_element(addToCart).click().perform()
    self.WaitForElementVisible((By.XPATH, environmentConstants.CART))
    cart = self.driver.find_element(By.XPATH, environmentConstants.CART)
    actions = ActionChains(self.driver)
    assert self.driver.find_element(By.XPATH, environmentConstants.CART).text == "Sepetim"
    actions.move_to_element(cart).click().perform()
    self.WaitForElementVisible((By.XPATH, environmentConstants.HOMEPAGE))
    homePage = self.driver.find_element(By.XPATH, environmentConstants.HOMEPAGE)
    actions = ActionChains(self.driver)
    assert self.driver.find_element(By.XPATH, environmentConstants.HOMEPAGE).tag_name == "svg"
    actions.move_to_element(homePage).click().perform()


  
