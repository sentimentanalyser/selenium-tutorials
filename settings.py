from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

# browser is nothing more then chrome driver manager
browser = webdriver.Chrome(ChromeDriverManager().install())