#####################################################################
#
# This is a script for exporting mongodb collection to a legit
# csv file. Program accepts execution arguments which shall
# allow you to customize everything neccesary starting from
# csv seperator ending on mongo related options.
#
#####################################################################

# The MIT License (MIT)

# Copyright (c) <2014> <Oskar Jarczyk>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# The advante over mongoexport is one and vast, my program
# doesn't require from you providing all fields for the export
# and if the collection happens suddently to have more fields than the previous
# one, this situation is handled by expanding the column set and fixing
# columns in the result csv in the fly
# http://docs.mongodb.org/v2.2/reference/mongoexport/#cmdoption--csv

# update: 30.05.2014
# version 1.00 codename: ThetaSigma (ΘΣ)

from pymongo import MongoClient
import __builtin__


__author__ = 'doctor ko'


def usage():
    f = open('usage.txt', 'r')
    for line in f:
        print line

if __name__ == "__main__":
    __builtin__.verbose = False
    __builtin__.log_all = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hlu:v", ["help", "log_all", "utf8=", "verbose"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-v", "--verbose"):
            __builtin__.verbose = True
            scream.ssay('Enabling verbose mode.')
        elif o in ("-l", "--log_all"):
            __builtin__.log_all = True
            scream.ssay('Enabling logging to file.')
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-u", "--utf8"):
            use_utf8 = (a not in ['false', 'False'])
