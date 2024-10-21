# Gerar o dataset novamente
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split # treina a ia
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df_idade_faixa = pd.read_csv('etaria.csv')

# Separar os dados entre features (idade) e target (faixa_etaria)
X = df_idade_faixa[['idade']]  # Features (idade)
y = df_idade_faixa['faixa_etaria']  # Target (faixa etária)

# Dividir os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)  # Usando 3 vizinhos como exemplo
knn.fit(X_train, y_train) #X_train é numpy

# Fazer previsões no conjunto de teste
y_pred = knn.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)

print(f"Acurácia do modelo KNN: {accuracy:.2f}")  # Imprimir a acuracia do modelo

#Exibir as previsões feitas pelo modelo:
print(f"Previsões: {y_pred[:10]}") # mostrando as primeiras 10 previsoes

joblib.dump(knn, 'modelo_knn.pkl') #esse é o modelo de inteligencia artificial

print("Modelo KNN salvo com sucesso")
