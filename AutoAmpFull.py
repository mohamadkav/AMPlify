from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

br = webdriver.Chrome(ChromeDriverManager().install())
br.get('http://www.google.com/')

# save_me = ActionChains(br).key_down(Keys.CONTROL)\
#          .key_down('s').key_up(Keys.CONTROL).key_up('s')
save_me = ActionChains(br).key_down(Keys.COMMAND)\
           .key_down('s').key_up(Keys.COMMAND).key_up('s')
save_me.perform()