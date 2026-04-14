import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Carga del dataset ---
df = pd.read_excel("Walmart.xlsx")

print("-------CURACION Y PREPARACION DE DATOS-------")
# --- Diagnóstico inicial ---
print("=== DIAGNÓSTICO DEL DATASET ===")
print(df.head())
print(df.describe())

# Valores nulos por variable
print("\nValores nulos por variable:")
print(df.isna().sum())

# Duplicados
print(f"\nDuplicados exactos: {df.duplicated().sum()}")

# Ventas negativas
print(f"Ventas negativas: {(df['Weekly_Sales'] < 0).sum()}")

# --- Transformación de fecha ---
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# --- Variables derivadas ---
df["Year"]      = df["Date"].dt.year
df["Month"]     = df["Date"].dt.month
df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)

print("Tipos de dato después de transformación:")
print(df.dtypes)
print("\nPrimeras filas con variables nuevas:")
print(df[["Store", "Date", "Year", "Month", "YearMonth", "Weekly_Sales"]].head())

# --- Métricas por tienda para clustering ---
store_metrics = df.groupby("Store").agg(
    Total_Sales  = ("Weekly_Sales", "sum"),
    Mean_Sales   = ("Weekly_Sales", "mean"),
    Std_Sales    = ("Weekly_Sales", "std")
).reset_index()

store_metrics["Std_Sales"] = store_metrics["Std_Sales"].fillna(0)

print("=== MÉTRICAS POR TIENDA ===")

print(store_metrics.describe())

# --- Resumen final del dataset limpio ---
print("=== RESUMEN FINAL ===")
print(f"Registros totales:         {len(df)}")
print(f"Registros eliminados:      0")
print(f"Periodo:                   {df['Date'].min().date()} – {df['Date'].max().date()}")
print(f"Tiendas:                   {df['Store'].nunique()}")
print(f"Semanas feriadas:          {df['Holiday_Flag'].sum()} ({round(df['Holiday_Flag'].mean()*100, 1)}%)")
print(f"Ventas totales acumuladas: ${df['Weekly_Sales'].sum():,.2f}")
print(f"Venta semanal promedio:    ${df['Weekly_Sales'].mean():,.2f}")
print(f"Venta semanal mínima:      ${df['Weekly_Sales'].min():,.2f}")
print(f"Venta semanal máxima:      ${df['Weekly_Sales'].max():,.2f}")
print(f"Desviación estándar:       ${df['Weekly_Sales'].std():,.2f}")

print("------ANALISIS EXPLORATORIO Y VISUALIZACION-------")
# Agregar ventas por mes
vm = df.groupby("YearMonth")["Weekly_Sales"].sum().reset_index()
vm["YearMonth_dt"] = pd.to_datetime(vm["YearMonth"])
vm = vm.sort_values("YearMonth_dt")

print("=== EVOLUCIÓN MENSUAL DE VENTAS ===")
print(f"Mes con más ventas:   {vm.loc[vm['Weekly_Sales'].idxmax(), 'YearMonth']} "
      f"(${vm['Weekly_Sales'].max():,.0f})")
print(f"Mes con menos ventas: {vm.loc[vm['Weekly_Sales'].idxmin(), 'YearMonth']} "
      f"(${vm['Weekly_Sales'].min():,.0f})")
print(f"Promedio mensual:     ${vm['Weekly_Sales'].mean():,.0f}")

# Gráfico de evolución mensual
fig, axes = plt.subplots(figsize=(11, 5))
sns.lineplot(x="YearMonth_dt", y="Weekly_Sales", data=vm, color="#2563EB", linewidth=2)
plt.fill_between(vm["YearMonth_dt"], vm["Weekly_Sales"], alpha=0.15, color="#2563EB")
plt.title("Ventas Mensuales Walmart (Feb 2010 – Oct 2012)", fontsize=13, fontweight="bold")
plt.xlabel("Mes")
plt.ylabel("Ingresos Totales (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("fig_a1_ventas_mensuales.png")
plt.show()

# Ventas totales por tienda
ventas_tienda = df.groupby("Store")["Weekly_Sales"].sum().reset_index()
ventas_tienda = ventas_tienda.sort_values("Weekly_Sales", ascending=False)
top10 = ventas_tienda.head(10)

print("=== TOP 10 TIENDAS POR INGRESOS ===")
print(top10.to_string(index=False))
print(f"\nTienda líder:  Store {ventas_tienda.iloc[0]['Store']} con ${ventas_tienda.iloc[0]['Weekly_Sales']:,.0f}")
print(f"Tienda menor:  Store {ventas_tienda.iloc[-1]['Store']} con ${ventas_tienda.iloc[-1]['Weekly_Sales']:,.0f}")
print(f"Ratio líder/menor: {ventas_tienda.iloc[0]['Weekly_Sales'] / ventas_tienda.iloc[-1]['Weekly_Sales']:.1f}x")

# Gráfico de barras top 10
fig, axes = plt.subplots(figsize=(10, 5))
sns.barplot(x="Store", y="Weekly_Sales", data=top10, palette="Blues_d")
plt.title("Top 10 Tiendas por Ingresos Totales", fontsize=13, fontweight="bold")
plt.xlabel("Tienda (Store ID)")
plt.ylabel("Ingresos Totales (USD)")
plt.tight_layout()
plt.savefig("fig_a2_top_tiendas.png")
plt.show()

# Promedio de ventas por tipo de semana
hv = df.groupby("Holiday_Flag")["Weekly_Sales"].mean().reset_index()
hv["Tipo"] = ["Sin Feriado", "Semana Feriada"]

print("=== IMPACTO DE SEMANAS FERIADAS ===")
print(f"Ventas promedio semana normal:   ${hv.loc[hv['Holiday_Flag']==0, 'Weekly_Sales'].values[0]:,.2f}")
print(f"Ventas promedio semana feriada:  ${hv.loc[hv['Holiday_Flag']==1, 'Weekly_Sales'].values[0]:,.2f}")

normal   = hv.loc[hv["Holiday_Flag"]==0, "Weekly_Sales"].values[0]
feriado  = hv.loc[hv["Holiday_Flag"]==1, "Weekly_Sales"].values[0]
lift     = (feriado / normal - 1) * 100
print(f"Incremento porcentual:           +{lift:.2f}%")
print(f"Ingreso adicional red completa:  ${(feriado - normal) * 45:,.0f} por semana feriada")

# Gráfico comparativo
fig, axes = plt.subplots(figsize=(7, 5))
sns.barplot(x="Tipo", y="Weekly_Sales", data=hv, palette=["#60A5FA", "#EF4444"])
plt.title("Ventas Promedio: Feriadas vs. Normales", fontsize=13, fontweight="bold")
plt.xlabel("")
plt.ylabel("Ventas Promedio (USD)")
plt.tight_layout()
plt.savefig("fig_a3_holiday.png")
plt.show()

# Selección de variables para correlación
corr_cols = ["Weekly_Sales", "Temperature", "Fuel_Price", "CPI", "Unemployment"]
corr = df[corr_cols].corr()

print("=== CORRELACIONES CON WEEKLY_SALES ===")
print(corr["Weekly_Sales"].drop("Weekly_Sales").sort_values().round(4))

# Heatmap de correlación
fig, axes = plt.subplots(figsize=(7, 6))
sns.heatmap(corr, annot=True, cmap="RdBu_r", vmin=-1, vmax=1, fmt=".2f")
plt.title("Matriz de Correlación – Variables Walmart", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("fig_a4_correlacion.png")
plt.show()

print("-----MODELADO Y ANALISIS AVANZADO-----")
from sklearn.preprocessing import StandardScaler

X = store_metrics[["Total_Sales", "Mean_Sales", "Std_Sales"]].copy()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Variables antes de estandarizar:")
print(X.describe().round(2))
print("\nPrimeras filas estandarizadas (media≈0, std≈1):")
print(pd.DataFrame(X_scaled,
      columns=["Total_Sales", "Mean_Sales", "Std_Sales"]).head().round(3))

from sklearn.cluster import KMeans
# Calcular inercia para K entre 2 y 8
inertias = []
valores_k = range(2, 9)

for k in valores_k:
    km = KMeans(n_clusters=k, n_init=20, random_state=42)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
    print(f"K={k}  Inercia={km.inertia_:.2f}")

# Gráfico del codo
fig, axes = plt.subplots(figsize=(7, 4))
sns.lineplot(x=list(valores_k), y=inertias, marker="o", color="#2563EB")
plt.title("Método del Codo – Clustering de Tiendas", fontsize=13, fontweight="bold")
plt.xlabel("Número de Clusters (K)")
plt.ylabel("Inercia (SSE)")
plt.tight_layout()
plt.savefig("fig_a5_codo.png")
plt.show()

# Entrenar modelo con K=4
kmeans = KMeans(n_clusters=4, n_init=20, random_state=42)
store_metrics["Cluster"] = kmeans.fit_predict(X_scaled)

# Resumen por cluster
resumen = store_metrics.groupby("Cluster").agg(
    Tiendas      = ("Store", "count"),
    Ventas_Media = ("Mean_Sales", "mean"),
    Volatilidad  = ("Std_Sales", "mean"),
    Total_M      = ("Total_Sales", "sum")
).reset_index()

resumen["Ventas_Media"] = resumen["Ventas_Media"].round(0)
resumen["Volatilidad"]  = resumen["Volatilidad"].round(0)
resumen["Total_M"]      = (resumen["Total_M"] / 1e6).round(1)

print("=== RESUMEN DE CLUSTERS ===")
print(resumen.to_string(index=False))

# Tiendas por cluster
for c in range(4):
    tiendas = store_metrics[store_metrics["Cluster"] == c]["Store"].tolist()
    print(f"\nCluster {c}: tiendas {sorted(tiendas)}")

print("----primer grafico de clusters----")
fig, axes = plt.subplots(figsize=(9, 6))
sns.scatterplot(x="Mean_Sales", y="Std_Sales", hue="Cluster",
                data=store_metrics,
                palette=["#3B82F6","#EF4444","#10B981","#F59E0B"],
                s=100)
plt.title("Segmentación de Tiendas – K-Means (K=4)",
          fontsize=13, fontweight="bold")
plt.xlabel("Ventas Medias Semanales (USD)")
plt.ylabel("Volatilidad de Ventas (Std USD)")
plt.tight_layout()
plt.savefig("fig_a6_clusters_scatter.png")
plt.show()

print("----segundo grafico de clusters----")
perfil = store_metrics.groupby("Cluster")[
    ["Total_Sales","Mean_Sales","Std_Sales"]].mean().reset_index()
perfil_melted = pd.melt(perfil, id_vars="Cluster",
                        value_vars=["Total_Sales","Mean_Sales","Std_Sales"],
                        var_name="Variable", value_name="Valor")

fig, axes = plt.subplots(figsize=(9, 5))
sns.barplot(x="Variable", y="Valor", hue="Cluster", data=perfil_melted,
            palette=["#3B82F6","#EF4444","#10B981","#F59E0B"])
plt.title("Perfil Promedio por Cluster",
          fontsize=13, fontweight="bold")
plt.ylabel("Valor Promedio (USD)")
plt.tight_layout()
plt.savefig("fig_a7_perfil_cluster.png")
plt.show()
print("--------------------------")
#Preparacion e implementación de ARIMA
vm = df.groupby("YearMonth")["Weekly_Sales"].sum().reset_index()
vm["YearMonth_dt"] = pd.to_datetime(vm["YearMonth"])
vm = vm.sort_values("YearMonth_dt").reset_index(drop=True)

print("*-*--")
from statsmodels.tsa.arima.model import ARIMA

modelo = ARIMA(vm["Weekly_Sales"], order=(1, 1, 1))
model_fit = modelo.fit()
print(f"φ (autorregresivo): {model_fit.params['ar.L1']:.4f}")
print(f"θ (media móvil):    {model_fit.params['ma.L1']:.4f}")
#print(model_fit.summary())

print("-*-*-------------------------------------")
#Evaluacion del modelo con métricas de error
import numpy as np

pred = model_fit.fittedvalues
y = vm["Weekly_Sales"].values

mae  = np.mean(np.abs(y - pred))
rmse = np.sqrt(np.mean((y - pred)**2))
mape = np.mean(np.abs((y - pred) / y)) * 100

print("=== EVALUACIÓN DEL MODELO ARIMA(1,1,1) ===")
print(f"MAE  (Error Absoluto Medio):        ${mae:,.2f}")
print(f"RMSE (Raíz Error Cuadrático Medio): ${rmse:,.2f}")
print(f"MAPE (Error Porcentual Medio Abs.):  {mape:.2f}%")
print(f"\nVentas mensuales promedio: ${np.mean(y):,.0f}")
print(f"MAE como % de la media:    {mae/np.mean(y)*100:.1f}%")

#Forecast y visualizacion final
print("####-------------------------------------")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

forecast = model_fit.forecast(steps=6)

fc_dates = pd.date_range(
    vm["YearMonth_dt"].iloc[-1] + pd.offsets.MonthBegin(1),
    periods=6, freq="MS")

fc_df = pd.DataFrame({
    "Mes":        fc_dates.strftime("%Y-%m"),
    "Pronostico": [f"${v/1e6:.2f}M" for v in forecast]
})
print("=== PRONÓSTICO NOV 2012 – ABR 2013 ===")
print(fc_df.to_string(index=False))

fig, axes = plt.subplots(figsize=(11, 5))
sns.lineplot(x=vm["YearMonth_dt"], y=vm["Weekly_Sales"]/1e6,
             color="#2563EB", linewidth=2, label="Ventas reales")
sns.lineplot(x=vm["YearMonth_dt"], y=pred/1e6,
             color="#F59E0B", linewidth=1.5,
             linestyle="--", label="Predicción in-sample")
sns.lineplot(x=fc_dates, y=np.array(forecast)/1e6,
             color="#EF4444", linewidth=2,
             marker="X", label="Forecast 6 meses")
plt.axvline(vm["YearMonth_dt"].iloc[-1], color="gray",
            linestyle=":", alpha=0.7)
plt.title("Forecasting Ventas Mensuales – ARIMA(1,1,1)",
          fontsize=13, fontweight="bold")
plt.xlabel("Mes")
plt.ylabel("Ingresos (millones USD)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("fig_a8_arima.png")
plt.show()
print("------------------------------------ñññ")
# Modelo 1
modelo1 = ARIMA(vm["Weekly_Sales"], order=(1, 1, 1))
fit1 = modelo1.fit()

# Modelo 2
modelo2 = ARIMA(vm["Weekly_Sales"], order=(2, 1, 2))
fit2 = modelo2.fit()

print("ARIMA(1,1,1):")
print(f"  AIC: {fit1.aic:.2f}")
print(f"  BIC: {fit1.bic:.2f}")

print("\nARIMA(2,1,2):")
print(f"  AIC: {fit2.aic:.2f}")
print(f"  BIC: {fit2.bic:.2f}")