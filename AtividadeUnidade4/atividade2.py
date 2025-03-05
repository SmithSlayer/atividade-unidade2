import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns

crypto_symbol = "BTC-USD"
data = yf.download(crypto_symbol, start="2023-01-01", end="2024-01-01")

data.to_csv("crypto_prices.csv")
print("Dados salvos em 'crypto_prices.csv'")

data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)

features = ['Open', 'High', 'Low', 'Close', 'Volume']
X = data[features].dropna()
y = data['Target'].dropna()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy:.2f}")

feature_importances = pd.Series(model.feature_importances_, index=features)

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances, y=feature_importances.index)
plt.xlabel("Importância")
plt.ylabel("Variáveis")
plt.title("Importância das variáveis no modelo")
plt.show()
