import json
import xml.etree.ElementTree as ET
def buscar_dato(nombre):
    try:
        # Cargar el archivo JSON
        with open('nuevo1json/nuevo1.json', 'r') as archivo:
            datos = json.load(archivo)
        
        # Buscar el nombre en la lista de personas
        for persona in datos['results']:
            if persona['attributes']['cedula_de_ciudadania']['identification_number'].lower() == nombre.lower():
                return persona
        
        # Si no se encuentra la persona
        return f"No se encontró a una persona con el nombre '{nombre}'"
    except FileNotFoundError:
        return "El archivo 'datos.json' no se encontró."
    except json.JSONDecodeError:
        return "Error al decodificar el archivo JSON."
    except Exception as e:
        return f"Ocurrió un error: {e}"
    
def buscar_dato_xml_to_Json(Json_data, nombre_id):
#print(Json_data)
 
 #   print (nombre)
    try:
        # Cargar el archivo JSON
       
        for key, value in Json_data.items():
            if isinstance(value, dict):
                #result = buscar_dato_xml_to_Json(value, nombre)
       
                result = Json_data ['TCRMService'] ['TxResponse'] ['ResponseObject']['XAssociationListBObj']['XPartyAssociationBObj']['TCRMPersonBObj'] ['TCRMPartyIdentificationBObj']['IdentificationNumber']
                result_nombre = Json_data ['TCRMService'] ['TxResponse'] ['ResponseObject']['XAssociationListBObj']['XPartyAssociationBObj']['TCRMPersonBObj'] ['DisplayName']
                print(f"encontrado en output.json xml to JSON IBM result ID :  {result}")
            if result == nombre_id:
                print(f"xml to JSON IBM result nombre :  {result_nombre}")
                return result_nombre
            elif key == "IdentificationNumber" and value == nombre_id:
                return value
        return None

        
        
        # Si no se encuentra la persona
        return f"No se encontró a una persona con el nombre '{nombre}'"
    except FileNotFoundError:
        return "El archivo 'datos.json' no se encontró."
    except json.JSONDecodeError:
        return "Error al decodificar el archivo JSON."
    except Exception as e:
        return f"Ocurrió un error: {e}"
     
   
    
def buscar_dato_xml(nombre):
 # Cargar el archivo XML
        arbol = ET.parse('nuevo1xml/xmkOk.xml')
              
        raiz = arbol.getroot()
        
        # Buscar el nombre en la lista de personas
        for TCRMPartyIdentificationBObj in raiz.findall('TCRMPartyIdentificationBObj'):
            IdentificationNumber = TCRMPartyIdentificationBObj.find('IdentificationNumber').text
            print(f"raiz :{IdentificationNumber}")
            
            if  IdentificationNumber == nombre:
                
                return  TCRMPartyIdentificationBObj.find('IdentificationNumber').text     
          
            
        return None    
       
        # Si no se encuentra la persona
     
    


#leer archivoxml convertido a Json


# Pedir al usuario el nombre a buscar

with open('nuevo1xml/output.json', 'r') as file:
         datos = json.load(file) 
nombre_a_buscar = input("Introduce la identificacion de la persona a buscar: ")
resultado = buscar_dato(nombre_a_buscar)
resultado_xml = buscar_dato_xml(nombre_a_buscar)


resul2 =  buscar_dato_xml_to_Json(datos,nombre_a_buscar)

# Mostrar el resultado de la búsqueda
print(f"JSON:  {resultado}")

print(f"xml to JSON:  {resul2}")

print(resultado_xml)

#print(f"IdentificationNumber:{id_nombre_persona }")

