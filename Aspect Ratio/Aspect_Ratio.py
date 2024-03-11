# Ejercico 6 Aspect Ratio

# Autor: Daniel Jaeger

# Fecha: 2024/03/11

'''
/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */

Nota: En este ejercicio debemos utilizar varias librerías
Para intalarlas utilizaremos un entonrno virtual con:

Para activar:
python3 -m venv myenv
source myenv/bin/activate

Para desactivar:
deactivate
'''
import requests
from PIL import Image
from io import BytesIO

def calcular_aspect_ratio(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción en caso de que haya un error en la solicitud
        image = Image.open(BytesIO(response.content))
        width, height = image.size
        aspect_ratio = width / height
        return aspect_ratio
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)
    except Exception as e:
        print("Error al calcular el aspect ratio:", e)
    return None

url = "https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png"
aspect_ratio = calcular_aspect_ratio(url)
if aspect_ratio:
    print("Aspect ratio de la imagen:", aspect_ratio)
