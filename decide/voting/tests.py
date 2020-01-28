import random
import itertools
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from base import mods
from base.tests import BaseTestCase
from census.models import Census
from mixnet.mixcrypt import ElGamal
from mixnet.mixcrypt import MixCrypt
from mixnet.models import Auth
from voting.models import Voting, Question, QuestionOption
import unittest 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time 


class TestVotacionSiNo(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
        super().setUp()
        
    def test_signUpInorrect(self):
        self.driver.get("http://localhost:8000/admin/login/?next=/admin/")
        #self.driver.find_element_by_id('id_username').send_keys("1234")
        #self.driver.find_element_by_id('id_password').send_keys("1234")
        #self.driver.find_element_by_id('login-form').click()
        #self.assertTrue(len(self.driver.find_elements_by_id('user-tools'))!=1)

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
