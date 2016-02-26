#!/usr/bin/python
# -*- coding: utf-8 -*-

from twython import Twython

CUSTOMER_KEY = "zEJRjkoAtVcEw0iloNuo35exu"
CUSTOMER_SECRET= "KcDPquKp6TbDE8ywLl2cnfSJp1cs3dSGu7mE1uq1HDuymmhr2g"
ACCESS_TOKEN = "52524273-nLPFENqt0YObSBnwRJwC6lr7dUAjwTVIWA5uhF0qq"
ACCESS_TOKEN_SECRET = "7AecUJRNkUL70igO1Nhw9O1w1NQk5qPKfxfcjyjRmqK32"

twitter = Twython(CUSTOMER_KEY, 
                  CUSTOMER_SECRET, 
                  ACCESS_TOKEN, 
                  ACCESS_TOKEN_SECRET)

twitter.update_status(status="Bot en #Twitter gracias a  @PythonDiario")

