from text_extraction import TextExtraction

class TextFormatter:
    
  def __init__(self, text):
    self.text = text

  def format_title(self):
    title = self.text.extract_title()
    print(title)
  
  def format_yaxis_label(self):
    yaxis_labels = self.text.extract_yaxis_labels()
    print(yaxis_labels)

  def format_xaxis_label(self):
    xaxis_labels = self.text.extract_xaxis_labels()
    print(xaxis_labels)

  def format_legend_values(self):
    legend_values = self.text.extract_legend_values()
    print(legend_values)

class GridProcessor(TextFormatter):

  def __init__(self, text):
    super().__init__(text)
    pass