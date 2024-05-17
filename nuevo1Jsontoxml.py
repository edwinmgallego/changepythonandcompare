import json
import xml.etree.ElementTree as ET

def xml_to_dict(elem):
    """Convierte un elemento XML y sus hijos a un diccionario."""
    def _xml_to_dict_recurse(e):
        d = {e.tag: {} if e.attrib else None}
        children = list(e)
        if children:
            dd = {}
            for dc in map(_xml_to_dict_recurse, children):
                for k, v in dc.items():
                    if k in dd:
                        if isinstance(dd[k], list):
                            dd[k].append(v)
                        else:
                            dd[k] = [dd[k], v]
                    else:
                        dd[k] = v
            d = {e.tag: dd}
        if e.attrib:
            d[e.tag].update(('@' + k, v) for k, v in e.attrib.items())
        if e.text:
            text = e.text.strip()
            if children or e.attrib:
                if text:
                    d[e.tag]['#text'] = text
            else:
                d[e.tag] = text
        return d
    return _xml_to_dict_recurse(elem)

def dict_compare(d1, d2):
    """Compara dos diccionarios recursivamente."""
    if d1 == d2:
        return True
    if isinstance(d1, dict) and isinstance(d2, dict):
        if sorted(d1.keys()) != sorted(d2.keys()):
            return False
        return all(dict_compare(d1[k], d2[k]) for k in d1)
    return False

# Leer el archivo JSON y convertir a diccionario
with open('C:/Users/cript/OneDrive/Documentos/changepythonandcompare/nuevo1json/nuevo1.json', 'r') as json_file:
    json_data = json.load(json_file)
print(json_data)
# Leer el archivo XML y convertir a diccionario
tree = ET.parse('C:/Users/cript/OneDrive/Documentos/changepythonandcompare/nuevo1xml/xmkOk.xml')
root = tree.getroot()
xml_data = xml_to_dict(root)
print (xml_data)

# Comparar los dos diccionarios
if dict_compare(json_data, xml_data):
    print("La información en ambos archivos es la misma.")
else:
    print("La información en los archivos es diferente.")
