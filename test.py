# This Python file uses the following encoding: utf-8

import sys
from airtest.core.api import *
from airtest.aircv import imread

#print(sys.path)


def main():
  target=Template(sys.argv[1])
  screen=imread(sys.argv[2])
  match_r=target.match_in_smartauto(screen)
  if match_r is None:
    print('SMARTAUTONOTFOUND')
  else:
    print('SMARTAUTOFOUND')
    print(match_r)
  
if __name__== "__main__":
  main()