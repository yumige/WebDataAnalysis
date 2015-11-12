from ghost import Ghost
import time

class Tools:
	def showExists(self, session, selector):
		print selector + " is exists: " + str(session.exists(selector))

ghost = Ghost()
tools = Tools()

with ghost.start(user_agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0") as session:
	page, extra_resources = session.open("http://qzone.qq.com/",user_agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0")
	#print page.content
	
	print session.exists("#login")	
	print session.evaluate("document.getElementById('login_frame').src")
    	print session.wait_for_selector("#login_frame")
	print session.frame("login_frame") # Frame by name
	print session.exists("#login")
	#Switch to login_frame
	print "--------switch to the login_frame"
	session.click("#switcher_plogin") # not necessary?

	tools.showExists(session, "#loginform")	
	#Commit the login form

	#print session.evaluate("document.getElementById('u').outerHTML")
	session.click("#u")
	session.click("#p")
	#print session.fill("#loginform",{"u":"490089331","p":"490089331"})
	#print session.evaluate("document.getElementById('u').value='490089331'")
	print session.wait_for_selector("#u[name='u']", 2)
	print session.set_field_value("#u[name='u']","123123123", True)
	time.sleep(1)	
	print session.set_field_value("#p","123",True)
	time.sleep(1)
	#print session.evaluate("document.getElementById('p').value='490089331'")
	#time.sleep(5)
	#print session.fire("#loginform","submit")
	print session.click("#login_button")
	#print session.evaluate("document.getElementById('login_button').click()")
	session.show() # help to debug
	input = raw_input('Enter to exit: ')
	if input != null:
		exit
		

	
