from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

profileUrl = 'http://ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_module?i_uin=\
2468718769&i_login_uin=1360509576&style=35&version=8&needDelOpr=true&hideExtend=false\
&showcount=10&MORE_FEEDS_CGI=http%3A%2F%2Fic2.qzone.qq.com%2Fcgi-bin%2Ffeeds%2Ffeeds_html_act_all&refer=5'

browser = webdriver.Chrome()
browser.get('http://qzone.qq.com')
browser.switch_to_frame('login_frame')
try:
	ploginTab = browser.find_element_by_id('switcher_plogin')
	ploginTab.click()
	uinput = browser.find_element_by_id('u')
	uinput.send_keys('1360509576')
	pinput = browser.find_element_by_id('p')
	pinput.send_keys('spider2015')
	loginBtn = browser.find_element_by_id('login_button')
	time.sleep(1)
	loginBtn.click()
	browser.switch_to_default_content()
	try:
		browser.switch_to_frame('vcode')
		code = raw_input('input code value')
		capInput = browser.find_element_by_id('cap_input')
		cap_input.send_keys(code)
		submitBtn = browser.find_elements_by_class_name('verify_submit_btn')[0]
		submitBtn.click()
		browser.switch_to_default_content()
	except Exception as e:
		print('vcode not needed')

	print('login success')

	time.sleep(2)
	browser.get('http://user.qzone.qq.com/2468718769')
	time.sleep(1)
	browser.get(profileUrl)
	time.sleep(1)
	browser.switch_to_default_content()
	# src = browser.page_source.encode('utf-8')
	# print(src)
	#browser.execute_script('scrollTo(0,5000)')
	phones = browser.find_elements_by_class_name('phone-style')
	print('find {0} phone-style'.format(len(phones)))
	for p in phones:
		print(p.text)
	# profileBtn = browser.find_elements_by_class_name('app-name')[8]
	# print profileBtn
	# profileBtn.click()
except NoSuchElementException as e:
	print(e)
browser.close()
browser.quit()
