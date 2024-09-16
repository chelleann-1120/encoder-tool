import os
from heatmap_processor import HeatmapProcessor


class HeatmapEncoder:

  def __init__(self, input_dir):
    self.input_dir = input_dir
    self.images = self.sort_images()
    self.max_len = 0


  def run_main(self):
    processor = HeatmapProcessor(self.input_dir).find_max_length()


  def sort_images(self):
    sorted_images = sorted(os.listdir(self.input_dir), key=lambda x: [ord(c) for c in x])
    return sorted_images
        

if __name__ == "__main__":
  input_dir = "D:\\encoder-tool\\generated-heatmaps"
  HeatmapEncoder(input_dir).run_main()