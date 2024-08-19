from text_extraction import TextExtraction
from format_text import GridProcessor
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
      matrix = GridProcessor(values)
      matrix.format_yaxis_label()

if __name__ == "__main__":
  input_dir = "D:\\encoder-tool\\generated-heatmaps"
  HeatmapEncoder(input_dir).run_main()