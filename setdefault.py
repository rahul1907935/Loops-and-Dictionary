# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 12:34:34 2021

@author: rahul
"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)