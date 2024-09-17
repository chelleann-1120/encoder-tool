from text_extraction import TextExtraction
from format_text import TextFormatter
from grid_processor import GridProcessor
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Concatenate, Dense


class HeatmapProcessor:

  def __init__(self, input_dir):
    self.input_dir = input_dir
    self.images = os.listdir(input_dir)
    self.max_len = 0
    self.image = ""

  def process(self):
    image_path = os.path.join(self.input_dir, self.image)

    try:
      values = TextExtraction(image_path, self.image)
      clean_values = TextFormatter(values)
      matrix_values = GridProcessor(clean_values, image_path, self.image).create_grid_matrix()

      # print(matrix_values)
      return len(matrix_values)

    except Exception as e:
      print(f"Error processing image {self.image}: {e}")

  def find_max_length(self):

    for image in self.images:

      self.image = image
      length = self.process()

      if length > self.max_len:
        self.max_len = length
        print(self.max_len)
    
    return self.max_len
  
  def encode_and_pad_texts(self):
    # Encode the categories, for loop again?
    x_encoder = LabelEncoder()
    y_encoder = LabelEncoder()
    legend_encoder = LabelEncoder()

    x_encoded = x_encoder.fit_transform(self.x_axis)
    y_encoded = y_encoder.fit_transform(self.y_axis)
    legend_encoded = legend_encoder.fit_transform(self.legend_values)

    # Pad sequences to the same length
    x_padded = pad_sequences([x_encoded], maxlen=self.max_x_length, padding='post')[0]
    y_padded = pad_sequences([y_encoded], maxlen=self.max_y_length, padding='post')[0]
    legend_padded = pad_sequences([legend_encoded], maxlen=self.max_legend_length, padding='post')[0]

    return x_padded, y_padded, legend_padded, x_encoder, y_encoder, legend_encoder

  def separate_categories(self):
    pass

