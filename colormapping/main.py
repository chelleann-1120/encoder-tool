import os
from heatmap_processor import HeatmapProcessor


class HeatmapEncoder:

  def __init__(self, input_dir):
    self.input_dir = input_dir
    self.images = self.sort_images()
    self.x_max_len = 0
    self.y_max_len = 0
    self.legend_max_len = 0


  def run_main(self):
    
    for image in self.images[8:]:
      processor = HeatmapProcessor(self.input_dir, image)
      self.x_max_len, self.y_max_len, self.legend_max_len = processor.find_max_length(self.x_max_len, self.y_max_len, self.legend_max_len)

    # Separate the for loop, only applicable in finding the max_length of x, y, and legend


  def sort_images(self):
    sorted_images = sorted(os.listdir(self.input_dir), key=lambda x: [ord(c) for c in x])
    return sorted_images
        

if __name__ == "__main__":
  input_dir = "D:\\encoder-tool\\generated-heatmaps"
  HeatmapEncoder(input_dir).run_main()