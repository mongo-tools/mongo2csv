mongo2csv
=========

An handy tool for smart export of MongoDB collections to CSV files.

#### Description

The advante over mongoexport is one and vast, my program doesn't require from you providing all fields for the export and if the collection happens suddently to have more fields than the previous one, this situation is handled by expanding the column set and fixing columns in the result csv in the fly (http://docs.mongodb.org/v2.2/reference/mongoexport/#cmdoption--csv). There are small scripts which skip asking for fields, but yet, they don't work well when a document in a collection have different field list than the previous one (http://drzon.net/export-mongodb-collections-to-csv-without-specifying-fields/). And finally, mongoexport doesn't work well with null values and big integers &lt;sic!&gt;.

#### Parameters

(to be provided soon...)

#### Version

update: 30.05.2014
version 1.00 codename: ThetaSigma (ΘΣ)

#### Licence

The MIT License (MIT)

Copyright (c) 2014 Oskar Jarczyk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
