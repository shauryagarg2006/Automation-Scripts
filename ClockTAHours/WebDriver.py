import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def jobClockIn(unity_id, password, student_id):
    driver = webdriver.PhantomJS();
    #driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get('https://portalsp.acs.ncsu.edu/shibboleth-ds/?entityID=https%3A%2F%2Fportalsp.acs.ncsu.edu%2Fsp%2Fshibboleth&return=https%3A%2F%2Fportalsp.acs.ncsu.edu%2FShibboleth.sso%2FLogin%3FSAMLDS%3D1%26target%3Dss%253Amem%253A81c86f4c32490f1cdb39ff3f2de504c2041a62cc02553eab6c140f97a9272652')

    driver.find_element_by_xpath(
        '//*[@id="idpSelectPreferredIdPTile"]/div[2]/a/div[1]/img').click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(unity_id)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="formSubmit"]').click()
    driver.find_element_by_xpath(
        '//*[@id="content"]/main/form/div[1]/p[2]/input[2]').click()
    driver.find_element_by_xpath('//*[@id="NC_TAB1"]').click()
    time.sleep(4)
    driver.find_element_by_xpath(
        '//a[@title="Employee Self-Service Punch Clock" and text()="Web Time Clock"]').click()
    time.sleep(4)
    handles = driver.window_handles
    driver.switch_to_window(handles[1])
    driver.switch_to_frame('ptifrmtgtframe')
    driver.find_element_by_xpath('//input[@value="Accept"]').click()
    driver.find_element_by_xpath(
        '//input[@id="password1"]').send_keys(student_id)
    driver.find_element_by_xpath('//input[@id="button1"]').click()
    driver.find_element_by_xpath('//input[@id="button1"]').click()
    driver.quit()


def jobClockOut(unity_id, password, student_id):
    driver = webdriver.PhantomJS();
    #driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get('https://portalsp.acs.ncsu.edu/shibboleth-ds/?entityID=https%3A%2F%2Fportalsp.acs.ncsu.edu%2Fsp%2Fshibboleth&return=https%3A%2F%2Fportalsp.acs.ncsu.edu%2FShibboleth.sso%2FLogin%3FSAMLDS%3D1%26target%3Dss%253Amem%253A81c86f4c32490f1cdb39ff3f2de504c2041a62cc02553eab6c140f97a9272652')

    driver.find_element_by_xpath(
        '//*[@id="idpSelectPreferredIdPTile"]/div[2]/a/div[1]/img').click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(unity_id)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="formSubmit"]').click()
    driver.find_element_by_xpath(
        '//*[@id="content"]/main/form/div[1]/p[2]/input[2]').click()
    driver.find_element_by_xpath('//*[@id="NC_TAB1"]').click()
    time.sleep(4)
    driver.find_element_by_xpath(
        '//a[@title="Employee Self-Service Punch Clock" and text()="Web Time Clock"]').click()
    time.sleep(4)
    handles = driver.window_handles
    driver.switch_to_window(handles[1])
    driver.switch_to_frame('ptifrmtgtframe')
    driver.find_element_by_xpath('//input[@value="Accept"]').click()
    driver.find_element_by_xpath(
        '//input[@id="password1"]').send_keys(student_id)
    driver.find_element_by_xpath('//input[@id="button1"]').click()
    driver.find_element_by_xpath('//input[@id="button1"]').click()
    time.sleep(4)
    driver.quit()


def main(argv):
    if len(argv) < 5:
        print "Usage : command <Unity_Id> <Password> <Student_ID> <Time_In_Minutes>"
        exit()
    jobClockIn(argv[1], argv[2], argv[3])
    print "Job Clock In Successfull"
    print "Starting Timer"
    for counter in range(0, int(argv[4])):
        print str(counter) + " Minutes Elapsed"
        time.sleep(60)
    print argv[4] + " Minutes Elapsed"
    print "Timer Ended"
    jobClockOut(argv[1], argv[2], argv[3])
    print "Job Clock Out Successfull"


if __name__ == "__main__":
    main(sys.argv)
