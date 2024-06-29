import json
import xml.etree.ElementTree as ET 
from xml.dom import minidom


# conversion of json file to xml tree structure

# a=input("input json file")
# with open(a, 'r') as f:
#     data=json.load(f)

with open('D:/New_Securin/sampletry2/complete_assign_scratchToEnd/finalcode/finaljson.json', 'r') as f: 
    data=json.load(f)


def json_xml(tag,d):
    elem=ET.Element(tag)
    if isinstance(d,dict):
        if isinstance(d,dict): 
            if tag.lower() != "object":
                elem=ET.Element("object")
                elem.set("name",tag)
       
        for key, val in d.items(): 
            child = json_xml(key, val)
            elem.append(child)
    elif isinstance(d,list):
        if tag.lower()!="object":
            elem=ET.Element("array")
            elem.set("name",tag)
        for val in d:
            if isinstance(val,dict):
                child=ET.Element('object')
                child.text=str(val)
                child=json_xml("dict",val)
            elif isinstance(val, bool):
                child = ET.Element('boolean')
                child.text = 'true' if val else 'false'
            elif isinstance(val, int):
                child = ET.Element('number')
                child.text = str(val)
            elif isinstance(val, float):
                child = ET.Element('number')
                child.text = str(val)
            elif isinstance(val, str):
                child = ET.Element('string')
                child.text = val
            else:
                child = json_xml('array', val)
            elem.append(child)
    elif d is None:
        elem = ET.Element("null")
        elem.set("name", tag)
       
    elif isinstance(d,bool):
        if tag is None:
            child=ET.Element("boolean")
            child.text=str(d).lower()
            elem.append(child)
        else:
            elem=ET.Element("boolean")
            elem.text=str(d).lower()
            elem.set("name",tag)
        
    elif isinstance(d,(int,float)):
        elem=ET.Element("number")
        elem.text=str(d)
        elem.set("name",tag)
    elif isinstance(d,str):
        elem=ET.Element("string")
        elem.text=str(d)
        elem.set(tag,d)

    else:
        elem.text=str(d)
    return elem


root=json_xml('object',data)
tree=ET.ElementTree(root)
xml_str=ET.tostring(root)
#indent
dom = minidom.parseString(xml_str)
pretty_xml_str = dom.toprettyxml(indent="    ")

with open('finalxml.xml','w') as f:
    f.write(pretty_xml_str)
# with open('outputxml.xml','w') as f:
#     f.write(pretty_xml_str)
print(pretty_xml_str)
    
