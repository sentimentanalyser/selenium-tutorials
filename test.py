from settings import browser
import time
import unittest


# ok now create create new test object

class SeleniumTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        # lets setup browser
        self.browser = browser

        #wait your browser for 60 sec
        self.browser.implicitly_wait(60)

        #get url 
        self.browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


    def testInputText(self):
        #find element by id
        bill=self.browser.find_element_by_id("user-message")

        # check with unit test condition
        self.assertEqual("Please enter your Message",bill.get_attribute("placeholder"))
        #self.assertIn('Selenium Easy', self.browser.title)
    def form_test(self):
        button= self.browser.find_element_by_class_name("btn btn-default")
        self.assertTrue(button.is_enabled())

    
    @classmethod
    def tearDown(self):
        self.browser.quit()
        
if __name__ == '__main__':
    unittest.main(verbosity=2)