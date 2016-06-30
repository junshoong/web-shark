from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import unittest

caps = DesiredCapabilities.FIREFOX

caps["marionette"] = True

caps["binary"] = "/usr/bin/firefox"



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(capabilities=caps)
        self.browser = implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_capure_packet_and_view_detail(self):
        # 브라우저를 실행한다.
        self.browser.get('http://localhost:8000')

        # title과 헤더를 확인한다.
        self.assertIn('Web Shark', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Web Shark!', header_text)

        # Capture 버튼을 찾아서 누르면 Stop으로 바뀌고
        # 아래 항목에 캡쳐된 패킷이 나타난다.
        # button = self.browser.find_element_by_id('id_capture_button')
