import cv2
import numpy as np
from color_extraction import ColorExtractor


class GridProcessor(ColorExtractor):

  def __init__(self, text, image_path, image_name):
    super().__init__(image_path, image_name)
    self.title = text.format_title()
    self.yaxis_labels = text.clean_yaxis_label()
    self.xaxis_labels = text.clean_xaxis_label()
    self.legend_values = text.clean_legend_values()
    self.yaxis_len = len(self.yaxis_labels)
    self.xaxis_len = len(self.xaxis_labels)
    self.colors = self.extract_legend_color()

  def grid_color_matrix(self):

    cell_matrix = [[self.xaxis_labels[i] for i in range(self.xaxis_len)] for _ in range(self.yaxis_len)]

    return cell_matrix

  # Key value pair, title: Size,, #hexvalue: 2.1+e10 to 2.3+e11, etc.,
  def create_legend_matrix(self):
    
    title = self.legend_values[0]
    legend_dict = {"title": title}
    legend_dict.update({self.colors[i]: self.legend_values[i + 1] for i in range(len(self.colors))})
    
    return legend_dict