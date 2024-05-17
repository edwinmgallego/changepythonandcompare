import json
import xml.etree.ElementTree as ET
from deepdiff import DeepDiff

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_xml(file_path):
    tree = ET.parse(file_path)
    return tree.getroot()

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    return {element.tag: {child.tag: xml_to_dict(child) for child in element}}

def compare_data(json_data, xml_data):
    differences = DeepDiff(json_data, xml_data, ignore_order=True)
    return differences

# Rutas de los archivos
json_file_path = 'C:/Users/cript/OneDrive/Documentos/changepythonandcompare/nuevo1json/nuevo1.json'
xml_file_path = 'C:/Users/cript/OneDrive/Documentos/changepythonandcompare/nuevo1xml/xmkOk.xml'

# Leer archivos
json_data = read_json(json_file_path)
xml_root = read_xml(xml_file_path)
xml_data = xml_to_dict(xml_root)

# Comparar datos
differences = compare_data(json_data, xml_data)
print("Diferencias encontradas:")
print(differences)
