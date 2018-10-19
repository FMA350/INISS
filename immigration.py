import time
import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Constants, do not touch!
cat_name  = "Category"
subcat_name = "SubCategory"
GNIB_name = "ConfirmGNIB"
declaration_name = "UsrDeclaration"
given_name_name = "GivenName"
surname_name = "SurName"
nationality_name = "Nationality"
email_name = ["Email", "EmailConfirm"]
fam_app_name = "FamAppYN"
doc_name = "PPNoYN"
doc_box_name = "PPNo"
app_select_name = "AppSelectChoice"


# values

cat_value = "" # example: "Other"
subcat_value = "" #example: "Join family member"
GNIB_value = ""
given_name_value = "" 
surname_value = ""
nationality_index =  # index number starting from 0
email_value = "" # your email
fam_app_index = # 1 for yes, 2 for no
doc_index     = # 1 for yes, 2 for no
doc_box_value = "" # your document number
app_select_value = "S" # S means closest to today, leave this as it is



# script logic
while(True):
    driver = webdriver.Firefox()
    driver.get("https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/AppSelect?OpenForm")
    assert "INIS Registration Appointment Booking System" in driver.title
    category = Select(driver.find_element_by_name(cat_name))
    category.select_by_value(cat_value)
    GNIB = Select(driver.find_element_by_name(GNIB_name))
    GNIB.select_by_value(GNIB_value)
    subcategory = Select(driver.find_element_by_name(subcat_name))
    subcategory.select_by_value(subcat_value)
    # click on condition box
    driver.find_element_by_name(declaration_name).click()

    name_box = driver.find_element_by_name(given_name_name)
    name_box.send_keys(given_name_value)
    surname_box = driver.find_element_by_name(surname_name)
    surname_box.send_keys(surname_value)

    #date picker hacking

    control = driver.find_elements_by_class_name("control-label")
    control[6].click()
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/table/thead/tr/th[1]").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/table/thead/tr/th[1]").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/table/tfoot/tr[1]").click()


    nationality = Select(driver.find_element_by_name(nationality_name))
    nationality.select_by_index(nationality_index)

    email = driver.find_element_by_name(email_name[0])
    email.send_keys(email_value)
    email = driver.find_element_by_name(email_name[1])
    email.send_keys(email_value)

    fam_app = Select(driver.find_element_by_name(fam_app_name))
    fam_app.select_by_index(fam_app_index)

    doc = Select(driver.find_element_by_name(doc_name))
    doc.select_by_index(doc_index)

    doc_box = driver.find_element_by_name(doc_box_name)
    doc_box.send_keys(doc_box_value)

    look_for_appointments = driver.find_element_by_xpath("//*[@id=\"btLook4App\"]").click()

    app_select = Select(driver.find_element_by_name(app_select_name))
    app_select.select_by_value(app_select_value)
    # time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id=\"btSrch4Apps\"]").click()
    time.sleep(0.5)
    appointment = driver.find_element_by_xpath("//*[@id=\"dvAppOptions\"]/table/tbody/tr/td[2]")
    if appointment.text != "No appointment(s) are currently available":
         duration = 1  # second
         freq = 1220  # Hz
         os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
         print(appointment.text)
         a = raw_input('Press enter to continue: ')
    else:
        driver.close()
        print("no appointments")
    time.sleep(10)
