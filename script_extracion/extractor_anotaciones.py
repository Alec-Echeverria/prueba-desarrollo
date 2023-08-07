import json
import re

def retorno_data(nombre_json):
    try:
        # Abre el archivo JSON y carga los datos en una variable
        with open(nombre_json) as json_file:
            data = json.load(json_file)

        # Accede al valor del campo "textoAnotaciones"
        texto_anotaciones = data['textoAnotaciones']

        # Si texto_anotaciones es una lista, combinamos sus elementos en un solo texto
        if isinstance(texto_anotaciones, list):
            texto_anotaciones = ' '.join(texto_anotaciones)

        # Utilizamos una expresión regular para buscar el número después de "ESPECIFICACION:"
        numeros_especificacion = re.findall(r'ESPECIFICACION: (\d+)', texto_anotaciones)

        # Utilizamos una expresión regular para buscar el número después de "ANOTACION: Nro"
        numeros_anotacion = re.findall(r'ANOTACION: Nro\s*(\d+)', texto_anotaciones)

        # Creamos el diccionario con la estructura deseada
        output = {
            "fmi": f"{data['circulo']}-{data['numeroMatricula']}",
            "anotaciones": []
        }

        # Agregamos las anotaciones al diccionario "anotaciones"
        for idx, numero in enumerate(numeros_anotacion, start=1):
            codigo_especificacion = numeros_especificacion[idx - 1] if idx <= len(numeros_especificacion) else None
            anotacion = {
                "numero": int(numero),
                "codigo_especificacion": codigo_especificacion
            }
            output["anotaciones"].append(anotacion)

        # Devolvemos el diccionario con los datos procesados
        return output
    
    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_json}' no existe.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_json}' no es un JSON válido.")
        return None
    except KeyError as e:
        print(f"Error: El archivo '{nombre_json}' no contiene el campo '{e.args[0]}'.")
        return None

if __name__ == "__main__":
    # Define el nombre del archivo JSON que se va a procesar
    nombre_json = 'script_extracion/archivos_analizar/132-22359.json'
    
    # Llama a la función retorno_data para procesar el archivo JSON y obtener los datos procesados
    data_procesada = retorno_data(nombre_json)
    
    # Verifica si la función retorno_data ha devuelto datos procesados
    if data_procesada is not None:
        # Imprime los datos procesados en formato JSON con sangría para una mejor presentación
        print(json.dumps(data_procesada, indent=4))
