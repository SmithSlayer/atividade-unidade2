import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

data = {
    "Combustivel": ["Gasolina", "Diesel", "Etanol", "Gasolina", "Diesel", "Etanol", "Gasolina", "Diesel"],
    "Idade": [5, 3, 8, 2, 6, 7, 1, 4],
    "Quilometragem": [60000, 40000, 90000, 25000, 70000, 85000, 15000, 50000],
    "Preco": [30000, 45000, 20000, 50000, 28000, 22000, 55000, 40000]
}

df = pd.DataFrame(data)

label_encoder = LabelEncoder()
df["Combustivel"] = label_encoder.fit_transform(df["Combustivel"])

print("Tabela de dados com Pipeline:")
print(df)

X = df.drop(columns=["Preco"])
y = df["Preco"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

num_features = ["Idade", "Quilometragem", "Combustivel"]
num_transformer = StandardScaler()

preprocessor = ColumnTransformer(
    transformers=[
        ("num", num_transformer, num_features)
    ]
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Erro Quadrático Médio (MSE): {mse:.2f}")
