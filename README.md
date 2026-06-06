# 🚗 Sistema Automatizado de Analítica Operativa y Control de Calidad del Taller

¡Bienvenido! Este proyecto es un sistema inteligente desarrollado en **Python** diseñado para transformar archivos de Excel llenos de datos complejos y desordenados en un **reporte web interactivo, limpio y fácil de entender** con solo un clic. 

El ecosistema se complementa con un tablero de control avanzado en **Looker Studio** para la toma de decisiones estratégicas mediante filtros dinámicos.

---

## 🎯 ¿Con qué finalidad se hizo? (El Problema)
Antes de este programa, revisar la salud del taller mecánico requería abrir hojas de cálculo enormes, contar filas manualmente, calcular porcentajes y perder horas intentando descifrar el rumbo del negocio. 

Este software se creó para:
1. **Eliminar el trabajo manual:** Olvidarse de sumar filas y calcular métricas en calculadora.
2. **Monitorear la calidad:** Detectar inmediatamente cuántos clientes regresan por fallas en el servicio (Tasa de Garantía).
3. **Facilitar la toma de decisiones:** Saber al instante qué servicios generan más ingresos y cuáles necesitan atención.

---

## 🛠️ ¿Cómo funciona el programa? (Paso a Paso)
El sistema funciona como una procesadora: tú le entregas los datos brutos del taller y él te devuelve información valiosa a través de 4 fases:

1. **Lectura Inteligente (Ingestión):** El script localiza de forma segura el archivo maestro de Excel usando variables de entorno (`.env`) para proteger las rutas de tus archivos.
2. **Limpieza de Datos básico (Data Wrangling):** Revisa que no existan celdas vacías o formatos extraños en los precios y calificaciones de satisfacción de los clientes.
3. **Agrupación Científica (Pandas):** Junta las órdenes por categorías, calcula automáticamente los meses de ingreso basados en la fecha y obtiene promedios financieros y de calidad.
4. **Inyección Visual (Jinja2 + Chart.js):** Pasa los resultados limpios a una plantilla HTML y activa gráficos animados mediante JavaScript que se adaptan a cualquier pantalla.

---

## 🎉 ¿Qué se logró con el Reporte Automatizado? (Los Resultados)
Cada vez que ejecutas el programa (`main.py`), se genera un archivo llamado `reporte_calidad_taller.html` que puedes abrir en cualquier navegador web. Este reporte incluye:

* **Tarjetas de Control:** Visualización directa de las órdenes totales, ingresos facturados (hermosamente formateados con signos de pesos y comas), score de satisfacción del cliente y la tasa global de garantías (fijada en un ~6.7%).
* **Tabla de Desempeño:** Un desglose detallado de qué servicios (frenos, motor, suspensión, etc.) se solicitaron más y su rentabilidad promedio.
* **Gráfico de Barras Animado:** Muestra visualmente qué tipos de vehículos (sedanes, SUVs, motos) generan mayor carga de trabajo.
* **Gráfico de Líneas con Meta Dinámica:** Traza la evolución de la calidad mes a mes y la compara automáticamente contra una línea de meta establecida mediante arreglos nativos (`Array(5, 5)`), permitiendo ver de inmediato cuándo nos pasamos del límite de fallas admisible.

---

## 📊 Módulo de Business Intelligence (Looker Studio)
Para cerrar con broche de oro y ofrecer una experiencia analítica completa, de forma paralela al programa de Python se implementó un **Dashboard interactivo en Looker Studio**.

Este cuadro de mando permite a cualquier usuario filtrar la información de todo el taller de manera sencilla a través de los siguientes controles:
* **Filtros por Año:** Configurados mediante campos de control de tipo fecha que extraen automáticamente el año (`YEAR`), permitiendo segmentar la historia del negocio de manera limpia sin alterar el origen de datos.
* **Filtros por Tipo de Vehículo:** Mediante listas desplegables dinámicas para aislar el comportamiento de segmentos específicos.
* **Filtros Cruzados Activos (Interacciones):** Al dar clic directamente sobre cualquier barra de la gráfica (por ejemplo, "MOTO"), todo el tablero se actualiza al instante de forma nativa para mostrar únicamente las métricas y KPI asociados a esa selección.

---


1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
