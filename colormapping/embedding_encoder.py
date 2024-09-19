import tensorflow as tf
import numpy as np


class EmbeddingLayer:

    def __init__(self, matrix_values):
        # Hashing layer and embeddings for x axis and legend range
        self.matrix_values = matrix_values
        self.hashing_layer = tf.keras.layers.Hashing(num_bins=1000)

    def get_yaxis_embedding(self, yaxis_label):
        yaxis_idx = self.hashing_layer(tf.convert_to_tensor([yaxis_label]))
        embedding = tf.keras.layers.Embedding(input_dim=1000, output_dim=300)(yaxis_idx)
        return embedding

    def get_legend_embedding(self, legend_values):
        # Convert the legend range to a string and hash it
        legend_idx = self.hashing_layer(tf.convert_to_tensor([legend_values]))
        embedding = tf.keras.layers.Embedding(input_dim=1000, output_dim=50)(legend_idx)
        return embedding
    
    def get_xaxis_embedding(self, xaxis_label):
        xaxis_idx = self.hashing_layer(tf.convert_to_tensor([xaxis_label]))
        embedding = tf.keras.layers.Embedding(input_dim=1000, output_dim=300)(xaxis_idx)
        return embedding

    def preprocess_features(self):
        country_vectors = []
        year_vectors = []
        #rgb_vectors = [] 
        legend_range_vectors = []

        for country, year_range, legend_range in self.matrix_values:
            # Process country
            country_vector = self.get_yaxis_embedding(country)
            country_vectors.append(tf.reshape(country_vector, [-1]))

            year_vector = self.get_xaxis_embedding(year_range)
            year_vectors.append(tf.reshape(year_vector, [-1]))

            # Process legend range using hashing and embedding
            if legend_range != 'NaN':
                legend_vector = self.get_legend_embedding(legend_range)
                legend_range_vectors.append(tf.reshape(legend_vector, [-1]))
            else:
                # Handle NaN or invalid legend range
                legend_range_vectors.append(tf.zeros(50)) 

        # Concatenate all features
        grouped_vectors = []

        for cell in zip(country_vectors, year_vectors, legend_range_vectors):
            grouped_vectors.append([cell])
            print(cell)
        
        return grouped_vectors

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

EmbeddingLayer(matrix_values=matrix_values).preprocess_features()