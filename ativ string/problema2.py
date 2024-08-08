# -*- coding: utf-8 -*-

string = input("")

oficial = ''
i = 0
while i < len(string):
    if i + 1 < len(string):
        if string[i] == string[i+1]:
            oficial = oficial + string[i].upper()
            i+=2
        else:
            oficial = oficial + string[i]
            i= i + 1
    else:
        oficial =oficial+ string[i]
        break
print(oficial.lstrip())