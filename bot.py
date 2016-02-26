#!/usr/bin/python
# -*- coding: utf-8 -*-

from twython import Twython

CUSTOMER_KEY = ""
CUSTOMER_SECRET= ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

twitter = Twython(CUSTOMER_KEY, 
                  CUSTOMER_SECRET, 
                  ACCESS_TOKEN, 
                  ACCESS_TOKEN_SECRET)

twitter.update_status(status="Bot en #Twitter gracias a  @PythonDiario")

