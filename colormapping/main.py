from text_extraction import TextExtraction
from format_text import TextFormatter
from grid_processor import GridProcessor
from format_data import DataFormatter
import os
import numpy as np
import matplotlib.pyplot as plt


class HeatmapEncoder:

  def __init__(self, input_dir):
    self.input_dir = input_dir
  
  def run_main(self):

    # Sort images according to their file name in ascending order
    images = sorted(os.listdir(self.input_dir), key=lambda x: [ord(c) for c in x])
    
    for image in images:
      
      image_path = os.path.join(self.input_dir, image)
      values = TextExtraction(image_path, image)
      values.draw_bounding_box(values.detect_title_roi())

      clean_values = TextFormatter(values)

      # Pre-processing the data for decoder
      #converted_values = DataFormatter(clean_values)

      matrix = GridProcessor(clean_values, image_path, image)

      #print(image , matrix.grid_color_matrix())

if __name__ == "__main__":
  input_dir = "D:\\encoder-tool\\generated-heatmaps"
  HeatmapEncoder(input_dir).run_main()