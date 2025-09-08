from keras.models import Sequential
from keras.layers import Dense

def build_model_2_layers(input_dim):
    model = Sequential([
        Dense(14, activation='relu', input_dim=input_dim),
        Dense(14, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def build_model_3_layers(input_dim):
    model = Sequential([
        Dense(14, activation='relu', input_dim=input_dim),
        Dense(14, activation='relu'),
        Dense(14, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def build_model_4_layers(input_dim):
    model = Sequential([
        Dense(32, activation='relu', input_dim=input_dim),
        Dense(16, activation='relu'),
        Dense(16, activation='relu'),
        Dense(8, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
