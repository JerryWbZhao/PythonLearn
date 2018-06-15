#coing=utf-8
 
from selenium import  webdriver

import  os,time
 
if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']
 
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
dr = webdriver.Chrome(chromedriver)

file_path = 'file:///' + os.path.abspath('status.html')
dr.get(file_path)
 
text_field = dr.find_element_by_name('user')
print( text_field.is_enabled())
time.sleep(5)
 
print(dr.find_element_by_class_name('btn').is_enabled())
time.sleep(5)

myjs = 'document.all.user.style.display = "none";'
dr.execute_script(myjs)
 
print( text_field.is_displayed())
time.sleep(5)
 
radio = dr.find_element_by_name('radio')
radio.click()
print(radio.is_selected())
time.sleep(5)
 
try:
    dr.find_element_by_id('none')
except:
    print('element does not exist')
 
time.sleep(5) 
dr.quit()