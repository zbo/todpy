__author__ = 'bob.zhu'
from auto.models import Feature, Scenario, Step
import json

def assert_gen_file(instance, plain_text):
    instance.assertEqual(plain_text[0],'Feature: not fun now')
    instance.assertEqual(plain_text[3],"    When I open page '([^']*)'")
    instance.assertEqual(plain_text[6],"  Scenario: second new created scenario")
    pass