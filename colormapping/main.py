from text_extraction import TextExtraction
from format_text import TextFormatter
from grid_processor import GridProcessor
import os
import numpy as np
import matplotlib.pyplot as plt
from heatmap_processor import HeatmapProcessor


class HeatmapEncoder:

  def __init__(self, input_dir):
    self.input_dir = input_dir
    self.images = self.sort_images()
  
  def run_main(self):
    
    for image in self.images[8:9]:
      processor = HeatmapProcessor(self.input_dir, image)
      processor.process()

  def sort_images(self):
    sorted_images = sorted(os.listdir(self.input_dir), key=lambda x: [ord(c) for c in x])
    return sorted_images
        

if __name__ == "__main__":
  input_dir = "D:\\encoder-tool\\generated-heatmaps"
  HeatmapEncoder(input_dir).run_main()