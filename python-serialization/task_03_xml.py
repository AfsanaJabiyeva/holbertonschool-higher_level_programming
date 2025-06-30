#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        # Create a child element with tag=key and text=value (as string)
        child = ET.SubElement(root, key)
        child.text = str(value)  # convert value to string to be safe

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            # child.tag is the key, child.text is the value as string
            result[child.tag] = child.text

        return result

    except (ET.ParseError, FileNotFoundError) as e:
        print(f"Error reading/parsing XML file: {e}")
        return None
