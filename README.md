```
# 🛒 Walmart Sales Analysis – Predictive Analytics & Store Segmentation

Análisis de ventas semanales de 45 tiendas Walmart (2010–2012) aplicando CRISP-DM. Proyecto final del Minor en Análisis y Gestión de Datos – Universidad Privada Boliviana.

---

## 📊 Descripción

Este proyecto analiza 6,435 registros semanales de 45 tiendas Walmart en Estados Unidos, explorando patrones de ventas, el impacto de feriados, la influencia de variables macroeconómicas y el desempeño por tienda. Se implementaron dos modelos principales: segmentación K-Means y pronóstico ARIMA.

---

## 📁 Dataset

- **Fuente:** [Kaggle – Walmart Store Sales](https://www.kaggle.com/datasets/yasserh/walmart-dataset)
- **Registros:** 6,435 semanas × 45 tiendas
- **Período:** Febrero 2010 – Octubre 2012
- **Variables:** Store, Date, Weekly_Sales, Holiday_Flag, Temperature, Fuel_Price, CPI, Unemployment

---

## 🔍 Análisis realizado

- Curación y validación del dataset (0 nulos, 0 duplicados)
- Evolución mensual de ventas con detección de estacionalidad
- Ranking de tiendas por ingresos acumulados
- Impacto de semanas feriadas (+7.84% en ventas promedio)
- Matriz de correlación entre ventas y variables macroeconómicas

---

## 🤖 Modelos implementados

### K-Means Clustering (K=4)

Segmentación de las 45 tiendas en 4 perfiles:

| Cluster | Tiendas | Venta Media Semanal | Perfil |
|---------|---------|---------------------|--------|
| 2 | 7 | $1,975K | Elite |
| 0 | 10 | $1,410K | Alto Desempeño |
| 3 | 14 | $915K | Desempeño Medio |
| 1 | 14 | $454K | Bajo Desempeño |

### ARIMA(1,1,1)

- Seleccionado sobre ARIMA(2,1,2) por menores valores AIC y BIC
- **MAPE:** 18.44% | **MAE:** $38,110,973 | **RMSE:** $52,863,512
- Pronóstico: ~$200M mensuales para Nov 2012 – Abr 2013

---

## 🛠️ Tecnologías utilizadas

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- statsmodels
- scipy

---

## 📂 Estructura del proyecto

walmart-sales-analysis/
│
├── Walmart.xlsx
├── analysis.py
├── figures/
│   ├── fig_a1_ventas_mensuales.png
│   ├── fig_a2_top_tiendas.png
│   ├── fig_a3_holiday.png
│   ├── fig_a4_correlacion.png
│   ├── fig_a5_codo.png
│   ├── fig_a6_clusters_scatter.png
│   ├── fig_a7_perfil_cluster.png
│   └── fig_a9_arima.png
└── README.md

---

## ▶️ Cómo ejecutar

1. Clonar el repositorio: git clone https://github.com/CarolinaFlores/walmart-sales-analysis.git
2. Instalar dependencias: pip install pandas numpy matplotlib seaborn scikit-learn statsmodels scipy
3. Ejecutar el análisis: python analysis.py

---

## 👩‍💻 Autora

Carolina Flores Fuentes
Minor en Análisis y Gestión de Datos
Universidad Privada Boliviana – Gestión I-2026
```
