from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os

# Você está vendo isso no DataBricks?
databricks = "DATABRICKS_RUNTIME_VERSION" in os.environ

if databricks:
    path_sales = "/Volumes/rocket_lab/default/rocket_lab/sales_data_sample.csv"
    path_continents = "/Volumes/rocket_lab/default/rocket_lab/continents.csv"
else:
    path_sales = "sales_data_sample.csv"
    path_continents = "continents.csv"

# Inicialização
spark = SparkSession.builder.appName("GlobalTech_Sales_Analysis").getOrCreate()

# Leitura dos dados
df_sales = spark.read.csv(path_sales, header=True, inferSchema=True)
df_continents = spark.read.csv(path_continents, header=True, inferSchema=True)

# Preparação da tabela
df_sales = df_sales.withColumn("TOTALVALUE", F.col("QUANTITYORDERED") * F.col("PRICEEACH")) # Coluna de valor total
df_joined = df_sales.join(df_continents, on="COUNTRY", how="left")                          # Join com continentes

# Agrupamento e cálculo de métricas
df_agrupado = df_joined.groupBy("COUNTRY", "CONTINENT").agg(
    F.sum("TOTALVALUE").alias("valor_total_vendas"),
    F.avg("TOTALVALUE").alias("media_vendas")
)

# Avaliação condicional
df_final = df_agrupado.withColumn(
    "avaliacao_performance",
    F.when(F.col("valor_total_vendas") >= 500000, "alta").otherwise("baixa")
)

# Resultado
if databricks:
    display(df_final)
else:
    df_final.show()