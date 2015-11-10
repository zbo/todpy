__author__ = 'bob.zhu'
from auto.models import Feature, Scenario, Step
import json

def assert_gen_file(instance, plain_text):
    instance.assertEqual(plain_text[1],'  not fun now')
    instance.assertEqual(plain_text[4],"    When I open page 'http://www.okcoin.com/'")
    instance.assertEqual(plain_text[7],"  Scenario: second new created scenario")
    pass