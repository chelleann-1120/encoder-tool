from encoder_tool import *
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
      test = ColorExtractor(image_path)
      test.extract_legend_color()

if __name__ == "__main__":
  input_dir = "D:\\encoder-tool\\generated-heatmaps"
  HeatmapEncoder(input_dir).run_main()