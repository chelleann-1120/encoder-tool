from text_extraction import TextExtraction
from format_text import TextFormatter
from color_mapping import ColorMapping
from grid_processor import GridProcessor
import os
import numpy as np
import matplotlib.pyplot as plt


class HeatmapEncoder:

  def __init__(self, input_dir):
    self.input_dir = input_dir
  
  def run_main(self):

    # Sort images according to their file name in ascending order
    images = sorted(os.listdir(self.input_dir), key=lambda x: [ord(c) for c in x])
    
    for image in images[:5]:
      
      image_path = os.path.join(self.input_dir, image)
      values = TextExtraction(image_path, image)

      # values.draw_bounding_box(values.detect_legend_roi())

      clean_values = TextFormatter(values)
      matrix_values = GridProcessor(clean_values, image_path, image).create_grid_matrix()

      print(matrix_values)

      # For clearly displaying the contents in the array only
      print('')
      for items in matrix_values:
        print(items)

      # Pre-processing the data for decoder
      # converted_values = DataFormatter(matrix_values)
        

if __name__ == "__main__":
  input_dir = "D:\\encoder-tool\\generated-heatmaps"
  HeatmapEncoder(input_dir).run_main()