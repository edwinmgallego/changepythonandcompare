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

def compare_dicts(d1, d2, path=""):
    """Compara dos diccionarios y devuelve las diferencias."""
    differences = []
    for k in d1:
        if k not in d2:
            differences.append(f"{path}/{k} está en JSON pero no en XML")
        else:
            if isinstance(d1[k], dict) and isinstance(d2[k], dict):
                differences.extend(compare_dicts(d1[k], d2[k], f"{path}/{k}"))
            elif isinstance(d1[k], list) and isinstance(d2[k], list):
                if len(d1[k]) != len(d2[k]):
                    differences.append(f"{path}/{k} listas tienen diferente longitud")
                else:
                    for i, (item1, item2) in enumerate(zip(d1[k], d2[k])):
                        differences.extend(compare_dicts(item1, item2, f"{path}/{k}[{i}]"))
            elif d1[k] != d2[k]:
                differences.append(f"{path}/{k} valor diferente (JSON: {d1[k]} vs XML: {d2[k]})")
    for k in d2:
        if k not in d1:
            differences.append(f"{path}/{k} está en XML pero no en JSON")
    return differences

# Leer el archivo JSON y convertir a diccionario
with open('C:/Users/cript/OneDrive/Documentos/changepythonandcompare/nuevo1json/nuevo1.json', 'r') as json_file:
    json_data = json.load(json_file)

# Leer el archivo XML y convertir a diccionario
tree = ET.parse('C:/Users/cript/OneDrive/Documentos/changepythonandcompare/nuevo1xml/xmkOk.xml')
root = tree.getroot()
xml_data = xml_to_dict(root)

# Comparar los dos diccionarios y encontrar diferencias
differences = compare_dicts(json_data, xml_data)

if not differences:
    print("La información en ambos archivos es la misma.")
else:
    print("La información en los archivos es diferente. Diferencias encontradas:")
    for difference in differences:
        print(difference)
