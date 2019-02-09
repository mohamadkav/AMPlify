# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import codecs


save_location="/Users/mohammad/Desktop/"
web_page="http://www.google.com"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(web_page)
with codecs.open(save_location+web_page[web_page.find('//')+2:]+".html", 'w', 'utf-8') as f:
    f.write(driver.page_source)
driver.get("https://mercury.postlight.com/amp?url="+web_page)
with codecs.open(save_location+web_page[web_page.find('//')+2:]+"_AMP.html", 'w', 'utf-8') as f:
    f.write(driver.page_source)
driver.close()