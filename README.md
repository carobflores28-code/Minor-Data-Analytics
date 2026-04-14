Aquí va el README listo para copiar y pegar directamente en GitHub:

---

# 🛒 Walmart Sales Analysis

> Análisis predictivo y segmentación de tiendas Walmart aplicando CRISP-DM | Minor en Análisis y Gestión de Datos – Universidad Privada Boliviana

---

## 📌 Descripción

Este proyecto analiza **6,435 registros semanales** de **45 tiendas Walmart** en Estados Unidos durante el período febrero 2010 – octubre 2012. Se exploraron patrones de ventas, el impacto de feriados y la influencia de variables macroeconómicas, implementando dos modelos de machine learning: segmentación K-Means y pronóstico ARIMA.

---

## 📁 Dataset

| Campo | Detalle |
|-------|---------|
| Fuente | [Kaggle – Walmart Store Sales](https://www.kaggle.com/datasets/yasserh/walmart-dataset) |
| Registros | 6,435 |
| Tiendas | 45 |
| Período | Feb 2010 – Oct 2012 |
| Variables | Store, Date, Weekly_Sales, Holiday_Flag, Temperature, Fuel_Price, CPI, Unemployment |

---

## 🔍 Hallazgos principales

- ✅ Dataset sin valores nulos ni duplicados — 6,435 registros conservados íntegramente
- 📈 Pico de ventas en **diciembre 2010** con **$288,760,533** en ventas agregadas
- 🎄 Las semanas feriadas generan un **+7.84%** en ventas respecto a semanas normales
- 📉 Correlaciones débiles entre ventas y variables macroeconómicas (r máx = -0.106)
- 🏪 Brecha de **8.1x** entre la tienda de mayor y menor desempeño

---

## 🤖 Modelos implementados

### 📦 K-Means Clustering — Segmentación de tiendas (K=4)

| Cluster | Tiendas | Venta Media Semanal | Volatilidad | Perfil |
|---------|---------|---------------------|-------------|--------|
| 2 | 7 | $1,975K | $272K | 🏆 Elite |
| 0 | 10 | $1,410K | $186K | ⭐ Alto Desempeño |
| 3 | 14 | $915K | $134K | 🔵 Desempeño Medio |
| 1 | 14 | $454K | $53K | 🔴 Bajo Desempeño |

### 📉 ARIMA(1,1,1) — Pronóstico de ventas mensuales

| Métrica | Valor |
|---------|-------|
| MAE | $38,110,973 |
| RMSE | $52,863,512 |
| MAPE | 18.44% |
| Pronóstico Nov 2012 – Abr 2013 | ~$200M/mes |

> ARIMA(1,1,1) seleccionado sobre ARIMA(2,1,2) por menores valores AIC y BIC.

---

## 🛠️ Tecnologías

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Statsmodels](https://img.shields.io/badge/Statsmodels-3776AB?style=for-the-badge)

---

## 📂 Estructura del proyecto

```
walmart-sales-analysis/
│
├── 📊 Walmart.xlsx                    # Dataset original
├── 🐍 analysis.py                     # Script principal
│
├── 📁 figures/
│   ├── fig_a1_ventas_mensuales.png    # Evolución mensual de ventas
│   ├── fig_a2_top_tiendas.png         # Top 10 tiendas por ingresos
│   ├── fig_a3_holiday.png             # Impacto de feriados
│   ├── fig_a4_correlacion.png         # Matriz de correlación
│   ├── fig_a5_codo.png                # Método del codo
│   ├── fig_a6_clusters_scatter.png    # Segmentación K-Means
│   ├── fig_a7_perfil_cluster.png      # Perfil por cluster
│   └── fig_a9_arima.png               # Forecasting ARIMA
│
└── 📄 README.md
```

---

## ▶️ Cómo ejecutar

```bash
# 1. Clonar el repositorio
git clone https://github.com/CarolinaFlores/walmart-sales-analysis.git
cd walmart-sales-analysis

# 2. Instalar dependencias
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels scipy

# 3. Ejecutar el análisis
python analysis.py
```

---

## 👩‍💻 Autora

**Carolina Flores Fuentes**
Minor en Análisis y Gestión de Datos
Universidad Privada Boliviana — Gestión I-2026

---

*Proyecto académico desarrollado con fines educativos.*
