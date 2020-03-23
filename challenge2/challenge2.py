import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_Challenge2(self):
        self.driver.get("https://www.copart.com")
        searchInput = self.driver.find_element_by_id("input-search")
        searchInput.send_keys("exotics")
        searchInput.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        assert "Porsche" in self.driver.page_source


if __name__ == '__main__':
    unittest.main()