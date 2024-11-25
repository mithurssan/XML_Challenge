import os
from lxml import etree

# Taking in FSA029 schema folder and path of a FSA029 submission as input as instructed by challenge
def validate(schema_folder, xml_file):
# Creating the path to the main schema using the folder
    main_schema_path = os.path.join(schema_folder, "FSA029-Schema.xsd")

# Reading the schema
    xmlschema_doc = etree.parse(main_schema_path)

# Creating the schema object
    xmlschema = etree.XMLSchema(xmlschema_doc)

# Reading XML file
    xml_doc = etree.parse(xml_file)

# Validating the XML
    try:
        xmlschema.assertValid(xml_doc)
        print("This submission is Valid")
        return True
    except etree.DocumentInvalid as e:
        print("This submission is Invalid, reason:", e)
        return False

# Using the script
schema_folder = "../../CommonTypes/v14/"
xml_file = "../../FSA029-v4-Samples/FSA029-Sample-Full.xml"

validate(schema_folder, xml_file)
