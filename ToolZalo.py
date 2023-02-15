from ToolAutoFB import *
import random
import json
import os
import time


auto = Login_2fa(username = '100087021713631',
            password = 'NhoRID101azgW',
            fa='ADDBUL7ZPQMQI3VFC2L5UJ6I2B2STSLM')
driver = auto.open_profile()
try:
    auto.get_2facode()
except:
    pass

# driver.close()
