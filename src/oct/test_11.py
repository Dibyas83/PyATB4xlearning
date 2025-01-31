import pandas as pd
# PASSWORD - i store the password in the framework?

# Env File - .(dot.env)
# How do you store your password or credentials in the framework.
# pip install python-dotenv

from dotenv import load_dotenv
import os
import csv
import pandas as pd

class Test_crud(object):


    def test_object1(self):
        assert True == True

    def test_object2(self):
        assert True == True

    def test_object3(self):
        df = pd.read_csv("src/testdata.csv")
        print(df)

    def test_update(self):
        with open('src/testdata.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0], row[1])

