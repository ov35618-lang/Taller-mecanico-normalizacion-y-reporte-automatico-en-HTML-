import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os
from numpy.ma.core import count

class taller_data:
	def __init__(self):
		self.ordenes_servicio = None
	def leer(self):
		load_dotenv()
		base_path = Path(os.getenv('base'))
		if base_path.exists():
			try:
				self.ordenes_servicio = pd.read_excel(base_path, sheet_name="ORDENES_SERVICIO",header=1)
				self.garantias_reclamadas = pd.read_excel(base_path, sheet_name="GARANTIAS_RECLAMADAS",header=1)
				print("Excel cargado correctamente en memoria.")
				return True

			except Exception as e:
				print(f"Error inesperado al procesar el Excel: {e}")
				return False
		else:
			print("Error de escritura en el archivo .env (base)")
			return False
	def datos(self):
		numero_ordenes = count(self.ordenes_servicio["ID_ORDEN"].drop_duplicates())
		columna_totales = pd.to_numeric(self.ordenes_servicio["TOTAL_COBRADO_MXN"],errors='coerce')
		ingresos_totales = columna_totales.sum()
		score_satisfaccion = self.ordenes_servicio["SATISFACCION_CLIENTE"].mean()
		self.union_garantias = pd.merge(self.ordenes_servicio,self.garantias_reclamadas,how='left', on='ID_ORDEN')
		conteo_reclamos = count(self.garantias_reclamadas["ID_GARANTIA"])
		tasa_garantia_global = (conteo_reclamos/numero_ordenes)*100
		#Metricas
		metrica = self.union_garantias.groupby(["TIPO_SERVICIO_OS"]).agg(total=(
			"ID_ORDEN", "count"),garantia=("ID_GARANTIA", "count"), satisfaccion=("SATISFACCION_CLIENTE",lambda x: round(x.mean(), 0)),
		ingreso_promedio=("TOTAL_COBRADO_MXN",lambda x: round(x.mean(), 2)))
		metrica['tasa_garantia'] = round((metrica['garantia'] / metrica['total']) *100,1)
		metrica = metrica.reset_index()
		metrica.rename(columns={'TIPO_SERVICIO_OS': 'nombre'}, inplace=True)
		reporte_servicios = metrica.to_dict(orient="records")

		#Barras
		df_vehiculos = self.ordenes_servicio.groupby(['TIPO_VEHICULO']).agg(
			total_ordenes=('ID_ORDEN', 'count')
		).reset_index()

		labels_vehiculos = df_vehiculos["TIPO_VEHICULO"].tolist()
		data_vehiculos = df_vehiculos['total_ordenes'].tolist()

		self.union_garantias['FECHA_INGRESO'] = pd.to_datetime(self.union_garantias['FECHA_INGRESO'])
		self.union_garantias['MES_DE_INGRESO'] = self.union_garantias['FECHA_INGRESO'].dt.strftime('%b')
		df_mensual = self.union_garantias.groupby(['MES_DE_INGRESO']).agg(
			total=('ID_ORDEN', 'count'),
			garantias=('ID_GARANTIA', 'count')
		).reset_index()
		df_mensual['tasa_mes'] = round((df_mensual['garantias'] / df_mensual['total']) * 100, 1)
		meses_historicos = df_mensual['MES_DE_INGRESO'].tolist()
		tasas_mensuales = df_mensual['tasa_mes'].tolist()

		meta_establecida = [4.0] * len(meses_historicos)
		datos_reporte = {
			# KPIs Globales (Tarjetas principales)
			"total_ordenes": numero_ordenes,
			"ingresos_totales": ingresos_totales,
			"score_satisfaccion": round(score_satisfaccion, 1),
			"tasa_garantia": round(tasa_garantia_global, 2),

			# Datos de la Tabla Principal (Lista de diccionarios)
			"reporte_servicios": reporte_servicios,

			# Datos para el Gráfico de Barras (Tipos de Vehículo)
			"labels_vehiculos": labels_vehiculos,
			"data_vehiculos": data_vehiculos,

			# Datos para el Gráfico de Líneas (Evolución Mensual)
			"meses_historicos": meses_historicos,
			"tasas_mensuales": tasas_mensuales,
			"meta_establecida": meta_establecida
		}

		return datos_reporte





def menu():
	prueba = taller_data()
	if prueba.leer():
		data_final = prueba.datos()
		print("\n¡Análisis completado exitosamente!")
		print(f"Total Órdenes Calculadas: {data_final['total_ordenes']}")
		print(
			f"Tasa de Garantía Global del Taller: {data_final['tasa_garantia'] if 'tasa_garantie' in data_final else data_final['tasa_garantia']}%")
		return data_final


if __name__ == "__main__":
	menu()
menu()








