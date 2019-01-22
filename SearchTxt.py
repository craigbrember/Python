# Usage: SearchTxt.py -s <search string> -o <output file> 
import os
import sys, getopt 

def main(argv):
   srchDir = '/home/cjb/Programming'
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hs:o:")
   except getopt.GetoptError:
      print('invalid argument. Use -h for help\n')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('Usage: ListFiles.py -s <search text> -o <outputfile>')
         sys.exit()
      elif opt == "-s":
         srchTxt = arg
      elif opt == "-o":
         outputfile = arg
   if outputfile == "":
      print('invalid output filename')
      sys.exit(3)  
   print('List of files containing the string "' + srchTxt + '"\n')
   with open(outputfile,"w") as fileOut:
      fileOut.write('Looking for text "' + srchTxt + '"\n')
      fileOut.write('File Name|Line Number|Code|\n')
      for dirpath, dirnames, filenames in os.walk(srchDir):
         for filename in filenames:
            if filename.endswith(".py"):
               absolute_path = os.path.join(dirpath, filename)
               with open(absolute_path,"r") as fileIn:
                  for lineCount, x in enumerate(fileIn,1):
                     if srchTxt in x:
                        fileOut.write('{0}|{1}|{2}'.format(absolute_path, lineCount, x))
   print('Results placed into ' + outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])