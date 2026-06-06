from jinja2 import Environment, FileSystemLoader
from main import taller_data  # Tu clase de datos


def renderizar_html():
	# 1. Obtener los datos procesados por tu clase de Pandas
	procesador = taller_data()
	if not procesador.leer():
		print("No se pudo cargar el Excel.")
		return

	# Aquí se genera tu diccionario gigante 'datos_reporte'
	datos_para_el_html = procesador.datos()

	# 2. Configurar Jinja2 para buscar tus plantillas HTML
	# En este ejemplo, asumo que tu plantilla está en la misma carpeta
	origen_plantillas = FileSystemLoader(searchpath="./")
	entorno_jinja = Environment(loader=origen_plantillas)

	try:
		# 3. Cargar el archivo de tu plantilla base HTML
		# Cambia 'plantilla_taller.html' por el nombre real de tu archivo
		plantilla = entorno_jinja.get_template("index.html")

		# 4. Inyectar los datos en la plantilla para crear el HTML real
		html_final = plantilla.render(datos_para_el_html)

		# 5. Guardar el resultado en un nuevo archivo HTML listo para producción
		archivo_salida = "reporte_calidad_taller.html"
		with open(archivo_salida, "w", encoding="utf-8") as archivo:
			archivo.write(html_final)

		print(f"\n🚀 ¡Reporte generado con éxito!")
		print(f"Búscalo en tu carpeta como: '{archivo_salida}' e inténtalo abrir en tu navegador.")

	except Exception as e:
		print(f"Error al renderizar el archivo HTML: {e}")


if __name__ == "__main__":
	renderizar_html()