import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_data(path: str):
    df = pd.read_csv(path)
    return df

def preprocess_data(df, target_col="Quality", test_size=0.3, random_state=42):
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Label Encoding no alvo
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Split treino/teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    # Padronização (Z-score)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, le
