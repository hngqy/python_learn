from selenium import webdriver

executable_path=r"C:\DEV\tool\python2.7\Scripts\phantomjs-2.1.1-windows\bin\phantomjs.exe"
drive = webdriver.PhantomJS(executable_path=executable_path)

drive.get("www.baidu.com")
data=drive.page_source
drive.save_screenshot("1.png")
print data.title()
drive.quit()