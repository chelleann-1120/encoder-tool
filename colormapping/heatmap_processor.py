from text_extraction import TextExtraction
from format_text import TextFormatter
from grid_processor import GridProcessor
import os


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
  
  def insert_padding(self):
    pass

  def separate_categories(self):
    pass

