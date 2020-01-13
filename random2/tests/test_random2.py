import pytest
import unittest
from application import app, routes

def test_random_number2():
    assert routes.makerandomnum2()=="1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10"
