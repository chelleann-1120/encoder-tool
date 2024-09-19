import tensorflow as tf
from tensorflow.keras.layers import Input, LSTM, Dense, Attention
from tensorflow.keras.models import Model

class Training:

  def __init__():
    pass


# Sample input shape (batch_size, sequence_length, feature_dim)
input_shape = (None, 100, 64)  # (batch_size, sequence_length, feature_dim)

# LSTM layer with return_sequences=True to get hidden states for each time step
inputs = Input(shape=input_shape[1:])  # Ignore batch size dimension
lstm_output = LSTM(128, return_sequences=True)(inputs)

# Attention mechanism
# You can use the built-in Attention layer in Keras
attention = Attention()([lstm_output, lstm_output])

# Feed the attention output into a Dense layer for classification or regression
dense_output = Dense(64, activation='relu')(attention)
final_output = Dense(1, activation='sigmoid')(dense_output)  # For binary classification

# Define the model
model = Model(inputs=inputs, outputs=final_output)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Print model summary
model.summary()

# Training
# X_train: input sequences (shape: batch_size, sequence_length, feature_dim)
# y_train: ground truth labels (shape: batch_size, 1)
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

# NOTE: Don't forget to tokenize the ground truth
# And, add some padding during the training process






import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

class LSTMModel:
    def __init__(self, input_shape, num_classes=1, lstm_units=50, optimizer='adam', loss='binary_crossentropy'):
        """
        Initializes the LSTM model.

        :param input_shape: Tuple of the form (sequence_length, num_features)
        :param num_classes: Number of output classes (default is 1 for binary classification)
        :param lstm_units: Number of units in LSTM layers
        :param optimizer: Optimizer for compiling the model
        :param loss: Loss function for compiling the model
        """
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.lstm_units = lstm_units
        self.optimizer = optimizer
        self.loss = loss
        
        self.model = self._build_model()
    
    def _build_model(self):
        """
        Builds the LSTM model.
        """
        model = Sequential()
        model.add(LSTM(self.lstm_units, return_sequences=True, input_shape=self.input_shape))
        model.add(LSTM(self.lstm_units))
        if self.num_classes > 1:
            model.add(Dense(self.num_classes, activation='softmax'))  # For multi-class classification
            self.loss = 'categorical_crossentropy'
        else:
            model.add(Dense(1, activation='sigmoid'))  # For binary classification
        model.compile(optimizer=self.optimizer, loss=self.loss, metrics=['accuracy'])
        return model
    
    def train(self, X_train, y_train, epochs=10, batch_size=32, validation_split=0.2):
        """
        Trains the LSTM model.

        :param X_train: Training data
        :param y_train: Training labels
        :param epochs: Number of epochs to train the model
        :param batch_size: Batch size for training
        :param validation_split: Fraction of data to use for validation
        """
        history = self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=validation_split)
        return history
    
    def evaluate(self, X_test, y_test):
        """
        Evaluates the LSTM model.

        :param X_test: Test data
        :param y_test: Test labels
        :return: Loss and accuracy
        """
        loss, accuracy = self.model.evaluate(X_test, y_test)
        return loss, accuracy

# Example usage
if __name__ == "__main__":
    # Example data (replace with your data)
    X_train = np.random.rand(100, 10, 20)  # 100 samples, 10 time steps, 20 features
    y_train = np.random.randint(0, 2, size=(100,))  # Binary classification

    # Initialize and train the model
    lstm_model = LSTMModel(input_shape=(X_train.shape[1], X_train.shape[2]))
    history = lstm_model.train(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

    # Evaluate the model (using training data for demonstration)
    loss, accuracy = lstm_model.evaluate(X_train, y_train)
    print(f'Loss: {loss}')
    print(f'Accuracy: {accuracy}')

