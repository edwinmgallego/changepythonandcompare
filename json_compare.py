import json

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_json(data1, data2, path=""):
    differences = []

    if isinstance(data1, dict) and isinstance(data2, dict):
        for key in set(data1.keys()).union(data2.keys()):
            new_path = f"{path}/{key}" if path else key
            if key not in data1:
                differences.append(f"Key {new_path} is missing in the nuevo1 JSON file")
            elif key not in data2:
                differences.append(f"Key {new_path} is missing in the output JSON file")
            else:
                differences.extend(compare_json(data1[key], data2[key], new_path))

    elif isinstance(data1, list) and isinstance(data2, list):
        for index, (item1, item2) in enumerate(zip(data1, data2)):
            new_path = f"{path}[{index}]"
            differences.extend(compare_json(item1, item2, new_path))
        if len(data1) > len(data2):
            for index in range(len(data2), len(data1)):
                differences.append(f"Index {path}[{index}] is missing in the output JSON file")
        elif len(data2) > len(data1):
            for index in range(len(data1), len(data2)):
                differences.append(f"Index {path}[{index}] is missing in the nuevo1 JSON file")

    else:
        if data1 != data2:
            differences.append(f"Difference at {path}: {data1} != {data2}")

    return 

def buscar_dato(nombre):
    try:
        # Cargar el archivo JSON
        with open('nuevo1json/nuevo1.json', 'r') as archivo:
           datos1 = json.load(archivo)
        
        # Buscar el nombre en la lista de personas
        for persona in datos1['results']:
            if persona['atributes']['cedula_de_ciudadania']['identification_number'].lower() == nombre.lower():
                return  persona
            
        # Si no se encuentra la persona
        return f"No se encontró a una persona con el nombre '{nombre}'"
    except FileNotFoundError:
        return "El archivo 'datos.json' no se encontró."
    except json.JSONDecodeError:
        return "Error al decodificar el archivo JSON."
    except Exception as e:
        return f"Ocurrió un error: {e}"    


def main():
    file1 = 'nuevo1json/nuevo1.json'
    file2 = 'nuevo1xml/output.json'

    data1 = load_json_file(file1)
    data2 = load_json_file(file2)
    
    
    
    

    if data1 == data2:
        print("The JSON files are identical.")
    else:
        print("The JSON files are different. Differences:")
        differences = compare_json(data1, data2)
        for difference in differences:
            print(difference)
            
id_a_buscar = input("Introduce el nombre de la persona a buscar: ")
resultado = buscar_dato(id_a_buscar)            
print (resultado)
if __name__ == "__main__":
    main()
