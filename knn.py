from generateData import generateData
import pandas as pd # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

#pré-processamento
df = generateData(1000)
# Converter variáveis categóricas para numéricas usando get_dummies
df = pd.get_dummies(df, columns=['bebe', 'fuma', 'sexo', 'profissao', 'pratica_exercicios', 'checkup_anual'], drop_first=True)

# Definir variáveis independentes (X) e dependente (y)
X = df.drop(columns=['sinistro2Anos'])
y = df['sinistro2Anos'].apply(lambda x: 1 if x == 'sim' else 0)  # Converter para valores binários

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Criar e treinar o modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Fazer previsões
y_pred = knn.predict(X_test)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Calcular a matriz de confusão
cm = confusion_matrix(y_test, y_pred)

# Criar um heatmap da matriz de confusão
plt.figure(figsize=(8, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Não', 'Sim'], yticklabels=['Não', 'Sim'])
plt.xlabel('PREDIÇÃO')
plt.ylabel('REAL')
plt.title(f'Accuracy: {accuracy:.2f}\n\nClassification Report:\n{report}')
plt.tight_layout()
plt.show()
