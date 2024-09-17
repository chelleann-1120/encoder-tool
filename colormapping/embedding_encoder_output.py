import tensorflow as tf
import numpy as np

# Hashing layer and embedding for country names
hashing_layer = tf.keras.layers.Hashing(num_bins=1000)
country_embedding = tf.keras.layers.Embedding(input_dim=1000, output_dim=300)

def get_country_embedding(country_name):
    country_idx = hashing_layer(tf.convert_to_tensor([country_name]))
    return country_embedding(country_idx)

def preprocess_features(matrix_values):
    country_vectors = []
    year_vectors = []
    #rgb_vectors = [] 
    legend_range_vectors = []

    for country, year_range, legend_range in matrix_values:
        # Process country
        country_vector = get_country_embedding(country)
        country_vectors.append(tf.reshape(country_vector, [-1]))

        # Process year
        year_start, year_end = map(float, year_range.split('.'))
        year_vector = tf.convert_to_tensor([year_start, year_end], dtype=tf.float32)
        year_vectors.append(year_vector)

        # Process legend range
        try:
            legend_start, legend_end = map(float, legend_range.split(' to '))
            # Normalize legend range
            legend_range_vector = np.array([legend_start, legend_end]) / 100.0
        except ValueError:
            legend_range_vector = np.zeros(2)  # Handle NaN or invalid legend range
        legend_range_vectors.append(tf.convert_to_tensor(legend_range_vector, dtype=tf.float32))

    # Concatenate all features
    grouped_vectors = []
    for country_vector, year_vector, legend_range_vector in zip(country_vectors, year_vectors, legend_range_vectors):
        grouped_vectors.append([country_vector, year_vector, legend_range_vector])

    grouped_vectors = preprocess_features(matrix_values)
    print("Grouped Vectors:")
    for group in grouped_vectors:
        group_as_list = [tensor.numpy().tolist() for tensor in group]
        print(group_as_list)
    print(len(grouped_vectors))
    return grouped_vectors

matrix_values = [['Sierra Leone', '1999.2001', 'NaN'], 
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
['China', '2002.2003', 'NaN']]

preprocess_features(matrix_values)