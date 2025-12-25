import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Name
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Seshagiri Thommandru")

driver.find_element(By.ID, "email").send_keys("get2tsgiri@gmail.com")

driver.find_element(By.ID, "phone").send_keys("8879882307")

driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("2401, Robin Way, Jastin, TX")

# radio button
radio_Buttons = driver.find_elements(By.NAME, "gender")
print(len(radio_Buttons))
for radio in radio_Buttons:
    if radio.get_attribute("value") == "female":
        radio.click()
        break

# check box
days_checkboxes = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and @type='checkbox']")
print(len(days_checkboxes))
for day_checkbox in days_checkboxes:
    if day_checkbox.get_attribute("value") == "wednesday":
        day_checkbox.click()
        break

#static drop down
dropdown = Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
dropdown.select_by_visible_text("India")
time.sleep(2)

#numvber of options in the country drop down
country_cnt = len(dropdown.options)
print("Number of options in the country drop down:", country_cnt)
for options in dropdown.options:
    print("Options in the country drop down:", options.text)

# Drop down with multiple select
colors_dropdown = Select(driver.find_element(By.XPATH,"//select[@id='colors']"))
colors_dropdown.select_by_value("red")
colors_dropdown.select_by_value("yellow")

#numvber of options in the colors drop down
colours_cnt = len(colors_dropdown.options)
print("Number of options in the colors drop down:", colours_cnt)
for colour in colors_dropdown.options:
    print("Options in the colors drop down:", colour.text)

#Sorted List
animals_list = Select(driver.find_element(By.XPATH,"//select[@id='animals']"))
animals_list.select_by_visible_text("Lion")
animals_list.select_by_visible_text("Cat")

#numvber of options in the animals drop down
animals_cnt = len(animals_list.options)
print("Number of options in the animals drop down:", animals_cnt)
for animal in animals_list.options:
    print("Options in the animals drop down:", animal.text)

actual_animal_List = [animal.text for animal in animals_list.options]
sorted_animal_list = sorted(actual_animal_List)
print(actual_animal_List)
print(sorted_animal_list)

if actual_animal_List == sorted_animal_list:
    print("The animals list is sorted")
else:
    print("The animals list is not sorted")

#Append all the animals to a list and print the list
x = []
for animal1 in animals_list.options:
    animal1 = animal1.text
    x.append(animal1)
print(x)


# ----------- Datepicker , Select the date, Type-1  -----------------
staticDateValue = "11/21/2025"

driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys(staticDateValue)
time.sleep(2)

year = "2027"
month = "March"
date = "15"

driver.find_element(By.XPATH, "//input[@id='datepicker']").clear()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
time.sleep(2)

# select the month and year in calendar header.
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yer = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yer == year:
        break
    else:
        driver.find_element(By.XPATH, "//span[text()='Next']").click()

#select the date in table body
alldates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
print(len(alldates))
for dateElement in alldates:
    dateValue = dateElement.text
    if dateValue == date:
        dateElement.click()
        break
time.sleep(2)

# ----------- Datepicker , Select the date, Type-2  -----------------

month_Value = "Nov"
Year_Value = "2018"
date_Value = "26"

driver.find_element(By.XPATH, "//input[@id='txtDate']").click()    # Opens datePicket
time.sleep(2)

datepicker_month = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
datepicker_month.select_by_visible_text(month_Value)
datepicker_year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
datepicker_year.select_by_visible_text(Year_Value)

alldates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
for date in alldates:
    if date.text == date_Value:
        date.click()
        print("Successfully selected the date of birth")
        break

time.sleep(10)
driver.quit()