from ghost import Ghost
import time

class Tools:
	def showExists(self, session, selector):
		print selector + " is exists: " + str(session.exists(selector))

ghost = Ghost()
tools = Tools()

with ghost.start() as session:
	page, extra_resources = session.open("http://qzone.qq.com/")
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
	print session.evaluate("document.getElementById('u').value='490089331'")
	print session.evaluate("document.getElementById('p').value='490089331'")
	time.sleep(10)
	#print session.fire("#loginform","submit")
	#print session.click("#login_button")
	print session.evaluate("document.getElementById('login_button').click()")
	session.show() # help to debug
	input = raw_input('Enter to exit: ')
	if input != null:
		exit
		

	
