#!/usr/bin/python

import sys, getopt
import read_sim

def main(argv):
   inputfile = ''
   logOpt = False
   try:
      opts, args = getopt.getopt(argv,"hi:l:",["ifile=","log="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -l <logOpt>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -l <logOpt>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-l", "--log"):
         logOpt = arg
   print 'Input file is ', inputfile
   print 'Log option is ', logOpt


   read_sim.read_and_show(inputfile, logOpt)

   raw_input("type anything to quit")

if __name__ == "__main__":
   main(sys.argv[1:])