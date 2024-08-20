from text_extraction import TextExtraction

class TextFormatter:
    
  def __init__(self, text):
    self.text = text

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
    self.title = self.format_title()
    self.yaxis_labels = self.clean_yaxis_label()
    self.xaxis_labels = self.clean_xaxis_label()
    self.legend_values = self.clean_legend_values()
    self.yaxis_len = len(self.yaxis_labels)
    self.xaxis_len = len(self.xaxis_labels)
    self.colors = self.text.extract_legend_color()

  def create_cell_matrix(self):

    cell_matrix = [[self.xaxis_labels[i] for i in range(self.xaxis_len)] for _ in range(self.yaxis_len)]
    print(cell_matrix)
    return cell_matrix

  # Key value pair, title: Size,, #hexvalue: 2.1+e10 to 2.3+e11, etc.,
  def create_legend_matrix(self):
    
    title = self.legend_values[0]
    legend_dict = {"title": title}
    legend_dict.update({self.colors[i]: self.legend_values[i + 1] for i in range(len(self.colors))})
    
    print(legend_dict)
    return legend_dict
