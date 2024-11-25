# XML Validation Script

This Python script validates an XML file against an XML Schema (XSD).

## Requirements

- Python 3.x
- `lxml` library (library used for XML parsing and schema validation)


`lxml` can be installed with pip using the following command:

```bash
pip install lxml
```

## Instructions

1. cd into the script folder

```bash
cd challenge/script/
```

2. run  the following command to run the script:

```bash 
python main.py
```

## Reflections of Challenge- The extra mile

a - Schema validation failed due to two unexpected elements, one being the PartnershipsSoleTraders element on line 102 and the other being the LLPs element on line 123 of the "FSA029-Sample-Full.xml" file. The regulator included a valid file for testing purposes, this valid file can be used against the script to see if it can correctly validate a valid file.

b - I would fix the file to pass the schema validation by removing the two elements that do not follow the schema.

c - The regulator has included an invalid file for similar reasons as the valid file, however now it is to check if the script can correctly invalidate an invalid file, both files will produce different results (valid or invalid) so both files are necessary for testing and to make sure there is no confirmation bias with the code.
