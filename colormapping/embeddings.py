import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Example data matrix
data = [
        ['2020.2021', 'Argentina', (185,155,125), '1 to 20'],
        ['2022.2023', 'Argentina', (155,185,125), '20 to 40'],
        ['2021.2022', 'Brazil', (155,155,185), '10 to 30']
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Year', 'Country', 'Color', 'Range'])

# Convert 'Year' to a numerical value
df['Year'] = df['Year'].apply(lambda x: (int(x.split('.')[0]) + int(x.split('.')[1])) / 2)

# Convert 'Country' using one-hot encoding
encoder = OneHotEncoder()
country_encoded = encoder.fit_transform(df[['Country']]).toarray()

# Convert 'Range' to a numerical value
df['Range'] = df['Range'].apply(lambda x: (int(x.split(' to ')[0]) + int(x.split(' to ')[1])) / 2)

# Combine all features into a final matrix
final_matrix = np.hstack([
    df[['Year', 'Range']].values,  # Numeric values
    country_encoded,  # One-hot encoded countries
    np.array(df['Color'].tolist())  # RGB values
])

print(final_matrix)
