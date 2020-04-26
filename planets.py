#!/usr/bin/env python
# -*- coding: utf-8 -*-

# first let's assign our variable
planets = [("Planet", "Distance from Sun"), ("Mercury", 0.4), ("Venus", 0.7), ("Earth", 1.0), ("Mars", 1.5), ("Jupiter", 5.2), ("Saturn", 9.5), ("Uranus", 19.6), ("Neptune", 30.0)] # the planets variable is a list of tuples made up of strings for the names of planets followed by their distance from the sun

# now let's loop through the planets list
for i in planets: # for each item in planets
	print("{0: ^20}|{1: ^20}{2}".format(i[0], i[1], "" if i[0]=="Planet" else " AU")) # print the item's data with fancy formatting
