# IoCs_detector
Detect indicator of compromise (MD5,SHA1,IP addresses) from a text file


### Usage
```
usage: Python script tool to get all hashes (SHA1,md5,IP) from given file
       [-h] -i IN_FILE [-o OUT_FILE] [-rd]

optional arguments:
  -h, --help   show this help message and exit
  -o OUT_FILE  List of hashes per line
  -rd          Remove duplicate hashes (default False)

required arguments:
  -i IN_FILE   Input text file to get hashes from
```

### Output
The result is a csv file with two columns (Type: MD5,SHA1, or IP | Value: hash or IP address)

![alt text](https://github.com/salehmuhaysin/IoCs_detector/blob/master/Selection_023.png?raw=true)
