#!/usr/bin/python

junk ="\x90"*5

fo = open("foo.exe", "wb")
fo.write(junk)
fo.close()

