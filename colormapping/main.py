from text_extraction import TextExtraction
from format_text import TextFormatter
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
    
    for image in images[8:9]:
      image_path = os.path.join(self.input_dir, image)
      
      try:
        values = TextExtraction(image_path, image)
        clean_values = TextFormatter(values)
        matrix_values = GridProcessor(clean_values, image_path, image)
        print(matrix_values.extract_legend_color())
        matrix_values = matrix_values.create_grid_matrix()

        #For clearly displaying the contents in the array only
        print('')
        for items in matrix_values:
            print(items)

        # Pre-processing the data for decoder
        # (Add your pre-processing code here)

      except Exception as e:
        print(f"Error processing image {image}: {e}")
        

if __name__ == "__main__":
  input_dir = "D:\\encoder-tool\\generated-heatmaps"
  HeatmapEncoder(input_dir).run_main()