#!/usr/bin/python3
def remove_char(str, n):
      part_one = str[:n] 
      part_two = str[n+1:]
      return part_one + part_two
