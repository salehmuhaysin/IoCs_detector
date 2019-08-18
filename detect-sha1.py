#!/bin/bash

import argparse
import re
import sys
import os.path
import requests

print """                           
                        *
                    _:*///:_                     
                _+*///////////+_                
    ____----*////////////////////**----____    
   *//////////////////////////////////********    
   */////////////////       ////**************    
   *////////////////          /***************    
   *///////////////   /////   ****************    
   *//////////////   /////**   ***************    
   *//////////////   ////***   ***************    
   *//////////////   ///****   ***************    
   *////////////                 *************    
   *////////////    Saleh Bin    *************    
   *////////////     Muhaysin    *************    
   *////////////                 *************    
    *////////********************************     
     */////  github.com/salehmuhaysin  *****      
      *///*********************************             
=========================================================="""



# ======================= Arguments =========================# 
a_parser = argparse.ArgumentParser('Python script tool to get all hashes (SHA1,md5,IP) from given file')


requiredargs = a_parser.add_argument_group('required arguments')
requiredargs.add_argument('-i', dest='in_file', help='Input text file to get hashes from', required=True)

a_parser.add_argument('-o' , dest='out_file' , help='List of hashes per line')
a_parser.add_argument('-rd' , dest='remove_dup' , help='Remove duplicate hashes (default False)', action='store_true')


args = a_parser.parse_args()

# if output file not provided
if args.out_file is None:
	foutput = args.in_file + ".hashes.csv"
else:
	foutput = args.out_file

file_name = args.in_file



# ======================= Patterns =========================# 
patterns = {
	'sha1' 	: "[0-9a-f]{40}",
	'md5' 	: "[a-f0-9]{32}",
	'ip'	: "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
}

# ======================= Input File =========================# 
fo = open(file_name , 'r')
text = fo.read().lower()
fo.close()

# ======================= Regex Find =========================# 
res = {
	'sha1' 	: re.findall( patterns['sha1'] , text ),
	'md5'	: re.findall( patterns['md5'] , text ),
	'ip'	: re.findall( patterns['ip'] , text )
}


# ======================= Prepare Output =========================# 
output_text = "Type,Value"
for r in res.keys():
	print "[+] "+r+": \t" + str(len(res[r])) ,
	if args.remove_dup is True:
		res[r] = list( set( res[r] ) )
		print "\t[+] -> after removing duplicates: " + str(len(res[r])),
	print 
	for i in res[r]:
		output_text += "\n" + r + "," + i
	
# ======================= Write Output =========================# 
fo = open(foutput , 'w')
fo.write( output_text )
fo.close()



