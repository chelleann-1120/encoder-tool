from text_extraction import TextExtraction
from grid_processor import GridProcessor

class ColorMapping(TextExtraction, GridProcessor):
  
  def __init__(self, image_path):
    super.__init__(self, image_path)
    pass

  def map_legend_color(self):
    pass

  def map_legend_values(self):
    pass

  def map_gridcells_color(self):
    pass
