from text_extraction import TextExtraction

class TextFormatter:
    
  def __init__(self, text):
    self.text = text
    self.title = self.format_title()
    self.yaxis_labels = self.format_yaxis_label()
    self.xaxis_labels = self.format_xaxis_label()
    self.legend_values = self.format_legend_values()

  def format_title(self):
    title = self.text.extract_title()
    title = title.replace('\n', ' ')
    return title
  
  def clean_yaxis_label(self):
    
    yaxis_labels = self.text.extract_yaxis_labels()
    array_yaxis = yaxis_labels.splitlines()
    array_yaxis = [label for label in array_yaxis if label]
    
    return array_yaxis

  def clean_xaxis_label(self):

    xaxis_labels = self.text.extract_xaxis_labels()
    array_xaxis = xaxis_labels.splitlines()
    array_xaxis = [label for label in array_xaxis if label]
    
    return array_xaxis

  def clean_legend_values(self):

    legend_values = self.text.extract_legend_values()
    array_legend_values = legend_values.splitlines()
    array_legend_values = [value for value in array_legend_values if value]

    return array_legend_values


class CellLabelMapping:

  def __init__(self, text):
    super().__init__(text)

  def map_cell_labels(self):
    pass


class GridProcessor(TextFormatter, CellLabelMapping):

  def __init__(self, text):
    super().__init__(text)

  def create_cell_matrix(self):
    pass

  # Key value pair, title: Size,, #hexvalue: 2.1+e10 to 2.3+e11, etc.,
  def create_legend_matrix(self):
    pass
