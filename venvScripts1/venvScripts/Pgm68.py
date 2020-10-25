from selenium.webdriver import Chrome
driver = Chrome("C:\Kiran Kumar SY\Python\Softwares\chromedriver.exe")

# How to maximize a Browser window
driver.maximize_window()

# How to get the Size of a Browser window
size = driver.get_window_size()
print(size)
print('Height =',size['height'])
print('Width =',size['width'])

# How to change the size of a Browser window
driver.set_window_size(width=400,height=400)

# How to get the position of Browser window
position = driver.get_window_position()
print(position)
print('x =',position['x'])
print('y =',position['y'])

# How to change the position of a Browser window
driver.set_window_position(x=500,y=500)

# How to load web page
driver.get("https://www.google.com/")

# How to get the title of current webpage
print(driver.title)

# How to get the Current or Existing URL from a browser
print(driver.current_url)

# How to refresh a page
driver.refresh()

# How to click on Back and Forward Btn on a Browser window
driver.back()
driver.forward()

# How to get cookies from a browser
print(driver.get_cookies())

# How to remove available cookies from browser
driver.delete_all_cookies()

# How to close a Browser window
driver.close()