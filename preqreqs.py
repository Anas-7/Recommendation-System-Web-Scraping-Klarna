import sys
import subprocess
import pkg_resources
# Install selenium and webdriver-manager
required_libraries = ['selenium', 'webdriver-manager']
installed_packages = pkg_resources.working_set
installed_packages_list = [i.key for i in installed_packages]

for library in required_libraries:
    if(library not in installed_packages_list):
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import time
from webdriver_manager.chrome import ChromeDriverManager