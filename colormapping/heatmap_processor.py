from text_extraction import TextExtraction
from format_text import TextFormatter
from grid_processor import GridProcessor
import os


class HeatmapProcessor:

  def __init__(self, input_dir, image):
    self.input_dir = input_dir
    self.image = image

  def process(self):
    image_path = os.path.join(self.input_dir, self.image)
      
    try:
      values = TextExtraction(image_path, self.image)
      clean_values = TextFormatter(values)
      matrix_values = GridProcessor(clean_values, image_path, self.image)
      print(matrix_values.extract_legend_color())
      matrix_values = matrix_values.create_grid_matrix()

      #For clearly displaying the contents in the array only
      print('')
      for items in matrix_values:
          print(items)

      # Pre-processing the data for decoder
      # (Add your pre-processing code here)

    except Exception as e:
      print(f"Error processing image {self.image}: {e}")

