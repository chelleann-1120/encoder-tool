import tensorflow as tf
import numpy as np


class EmbeddingLayer:

    def __init__(self, matrix_values):
        # Hashing layer and embeddings for x axis and legend range
        self.matrix_values = matrix_values
        self.hashing_layer = tf.keras.layers.Hashing(num_bins=1000)

    def get_yaxis_embedding(self, yaxis_label):
        yaxis_idx = self.hashing_layer(tf.convert_to_tensor(yaxis_label, dtype=tf.string))
        return self.get_embedding_layer(yaxis_idx)

    def get_legend_embedding(self, legend_values):
        legend_idx = self.hashing_layer(tf.convert_to_tensor(legend_values, dtype=tf.string))
        return self.get_embedding_layer(legend_idx)
    
    def get_xaxis_embedding(self, xaxis_label):
        xaxis_idx = self.hashing_layer(tf.convert_to_tensor(xaxis_label, dtype=tf.string))
        return self.get_embedding_layer(xaxis_idx)
    
    def get_embedding_layer(self, input):
        embedding_layer = tf.keras.layers.Embedding(input_dim=1000, output_dim=5)
        return embedding_layer(input)

    def preprocess_features(self):
        #rgb_vectors = []
        legend_val_vector = 0
        grouped_vectors = []

        for x_value, y_value, legend_value in self.matrix_values:
            # Process country
            y_value_vector = self.get_yaxis_embedding(y_value)
            x_value_vector = self.get_xaxis_embedding(x_value)

            # Process legend range using hashing and embedding
            if legend_value != 'NaN':
                legend_vector = self.get_legend_embedding(legend_value)
                legend_val_vector = tf.reshape(legend_vector, [-1])
            else:
                # Handle NaN or invalid legend range
                legend_val_vector = tf.zeros(5)

            combined_vector = tf.stack([x_value_vector, y_value_vector, legend_val_vector], axis=1)
            grouped_vectors.append(combined_vector)

        grouped_vectors_3d = tf.convert_to_tensor(grouped_vectors)
        return grouped_vectors_3d
        

matrix_values = [
    ['Sierra Leone', '1999.2001', 'NaN'], 
    ['Sierra Leone', '2002.2003', 'NaN'], 
    ['Sierra Leone', '2004.2005', 'NaN'], 
    ['Sierra Leone', '2006.2007', 'NaN'], 
    ['Sierra Leone', '2008.2009', 'NaN'], 
    ['Sierra Leone', '2010.2011', 'NaN'], 
    ['Sierra Leone', '2012.2013', '87 to 98'], 
    ['Sierra Leone', '2014.2015', '87 to 98'], 
    ['Sierra Leone', '2016.2017', 'NaN'], 
    ['Georgia', '1999.2001', 'NaN'], 
    ['Georgia', '2002.2003', 'NaN'], 
    ['Georgia', '2004.2005', 'NaN'], 
    ['Georgia', '2006.2007', 'NaN'], 
    ['Georgia', '2008.2009', '87 to 98'], 
    ['Georgia', '2010.2011', '87 to 98'], 
    ['Georgia', '2012.2013', '87 to 98'], 
    ['Georgia', '2014.2015', '87 to 98'], 
    ['Georgia', '2016.2017', '87 to 98'], 
    ['China', '1999.2001', 'NaN'], 
    ['China', '2002.2003', 'NaN']
]

value = EmbeddingLayer(matrix_values=matrix_values).preprocess_features()
print(value)