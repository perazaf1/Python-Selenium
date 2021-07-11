from selenium import webdriver 

# get variable to get driver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://github.com/login")

# username field
user_bar = driver.find_element_by_id("login_field")
user_bar.send_keys("perazaf1")

# password field 
pswd_bar = driver.find_element_by_id("password")
pswd_bar.send_keys("paulemile_2701")

# click on "sign in" button
connect_btn = driver.find_element_by_class_name("btn-primary")
connect_btn.click()