library(ComplexHeatmap)
library(circlize)
library(grid)

# Install colorspace package if not already installed
if (!require(colorspace)) {
  install.packages("colorspace")
}

# Load colorspace package
library(colorspace)

# Set the csv file directory
setwd("C:\\Users\\roche\\Desktop\\Thesis-related\\included-dataset-final")

print(getwd())

file_list <- list.files(pattern = "\\.csv$")

if (length(file_list) == 0) {
  stop("No CSV files found in the directory.")
}

for (current_file in file_list) {
  # Read the data into a data frame
  data <- read.csv(current_file, stringsAsFactors = FALSE)

  row.names(data) <- data[, 1]
  data <- data[, -1]
  colnames(data) <- sub("^X", "", colnames(data))

  data_matrix <- data.matrix(data)

  # Preprocess the data to replace empty values with NA
  data[data == ""] <- NA

  # Convert the data to numeric, keeping NA values
  data <- apply(data, 2, function(col) {
    as.numeric(col)
  })

  # Define column and row labels
  column_labels <- colnames(data_matrix)
  row_labels <- row.names(data_matrix)

  # Define the breaks for the discrete legend
  min_val <- min(data_matrix, na.rm = TRUE)
  max_val <- max(data_matrix, na.rm = TRUE)

  # Generate breaks and ensure they are unique
  breaks <- seq(min_val, max_val, length.out = 6)

  # Adjust the last break to ensure it includes the maximum value
  breaks[length(breaks)] <- max_val

  # Function to format values greater than 10,000 in scientific notation
  format_value <- function(value) {
    if (nchar(as.character(floor(value))) > 4) {
      return(format(value, scientific = TRUE, digits = 3))
    } else {
      return(floor(value))
    }
  }

  # Generate range labels for the legend
  labels <- sapply(1:(length(breaks) - 1), function(i) {
    paste0(format_value(breaks[i]), " to ", format_value(breaks[i + 1]))
  })

  # Ensure the last label includes the maximum value
  labels[length(labels)] <- paste0(format_value(breaks[length(breaks) - 1]),
                                    " to ", format_value(max_val))

  color_array_light <- c("#75ddff", "#8ddf00", "#ff9292",
                         "#ff8944", "#ff8b9f",
                         "#77c0ff", "#d376ff", "#ffc53e")

  color_array_dark <- c("#000060", "#006c10", "#7e0000",
                        "#604a00", "#630042",
                        "#002057", "#5b007c", "#7b4800")

  # Function to generate a gradient of colors
  generate_gradient <- function(light, dark, n) {
    # Create the color ramp palette
    color_palette <- colorRampPalette(c(light, dark))(n)
    return(color_palette)
  }

  # Randomize heatmap colors and generate a gradient
  random_color_light <- sample(color_array_light, 1)
  random_color_dark <- sample(color_array_dark, 1)

  gradient_colors <- generate_gradient(random_color_dark, random_color_light, length(breaks) - 1)

  # Create a discrete color function
  col_fun <- function(x) {
    if (is.matrix(x) && nrow(x) > 0 && ncol(x) > 0) {
      apply(x, 2, function(col) {
        ifelse(is.null(col) | is.na(col) | col == "", "#ffffff", as.character(cut(col, breaks = breaks, labels = gradient_colors, include.lowest = TRUE)))
      })
    } else {
      ifelse(is.null(x) | is.na(x) | x == "", "#ffffff", as.character(cut(x, breaks = breaks, labels = gradient_colors, include.lowest = TRUE)))
    }
  }

  # Extract the base name of the file without the extension
  base_name <- sub("\\.csv$", "", current_file)

  # Replace special characters only for the file name
  safe_base_name <- gsub("[^A-Za-z0-9]", "_", base_name)

  # Replace underscores with spaces for the title
  base_name <- gsub("_", " ", base_name)

  # Manually wrap the title if it is too long
  words <- unlist(strsplit(base_name, "\\s+"))
  wrapped_title <- ""
  line_length <- 0
  max_line_length <- 60  # Adjust this value as needed

  for (word in words) {
    if (line_length + nchar(word) + 1 > max_line_length || grepl("[(]", word)) {
      wrapped_title <- paste0(wrapped_title, "\n", word)
      line_length <- nchar(word)
    } else {
      wrapped_title <- paste0(wrapped_title, " ", word)
      line_length <- line_length + nchar(word) + 1
    }
  }

  # Add padding around the title
  padding <- "\n"
  wrapped_title <- paste0(padding, wrapped_title, padding)

  # Define a custom function to draw the border for each cell
  cell_border_fun <- function(j, i, x, y, width, height, fill) {
    grid.rect(x = x, y = y, width = width, height = height, 
              gp = gpar(col = "black", lwd = 0.05, fill = NA))
  }

  # Create the heatmap with the discrete color mapping function
  heatmap <- Heatmap(data_matrix, 
                     name = "Size",
                     column_title = wrapped_title,
                     column_title_gp = gpar(fontsize = 24,
                                            fontface = "bold", just = "center"),
                     cluster_rows = FALSE,
                     na_col = "white",
                     cluster_columns = FALSE,
                     row_labels = row_labels,  # Ensure row labels are set
                     row_names_side = "left",  # Move y-axis labels to the left
                     column_labels = column_labels,
                     row_names_gp = gpar(fontsize = 22),
                     column_names_gp = gpar(fontsize = 22),
                     col = col_fun,  # Use the custom color function
                     cell_fun = cell_border_fun,
                     show_heatmap_legend = FALSE,
                     border = TRUE,
                     width = unit(20, "cm"),  # Adjust the width of the cells
                     height = unit(28, "cm"), # Adjust the height of the cells
                     heatmap_legend_param = list(
                       at = breaks, # Define tick positions
                       labels = labels
                      ))

  # Define the output directory
  output_dir <- "C:\\Users\\roche\\Desktop\\Thesis-related\\generated-heatmaps"

  # Ensure the directory exists
  if (!dir.exists(output_dir)) {
    dir.create(output_dir, recursive = TRUE)
  }

  # Extract the base name of the file without the extension
  safe_base_name <- tools::file_path_sans_ext(basename(current_file))

  # Replace special characters in the file name
  safe_base_name <- gsub("[^A-Za-z0-9]", "_", safe_base_name)

  # Define the output file path
  output_file <- file.path(output_dir, paste0(safe_base_name, ".png"))

  # Read the data into a data frame
  data <- read.csv(current_file, stringsAsFactors = FALSE)

  # Check each column for empty data (NA values)
  has_empty_data <- any(sapply(data, function(column) any(is.na(column))))

  additional_legend_values <- breaks
  additional_legend_labels <- rev(labels)
  additional_legend_colors <- gradient_colors[seq_along(additional_legend_values)]

  # Check if any label is in scientific notation
  is_scientific <- any(grepl("e\\+", additional_legend_labels))

  # Set padding based on the presence of large values
  padding_value <- if (is_scientific) unit(c(25, 10, 2, 80), "mm")
  else unit(c(25, 10, 2, 10), "mm")

  if (has_empty_data) {
    empty_color <- "#ffffff"  # Set the white color for NaN
    additional_legend_values <- c(additional_legend_values, "NaN") 
    additional_legend_labels <- c(additional_legend_labels, "NaN") 
    additional_legend_colors <- c(additional_legend_colors, empty_color)
  }

  # Reverse the gradient colors to have the darkest color at the top
  gradient_colors <- rev(gradient_colors)

  # Create a function to draw the border for NaN color
  cell_border_fun <- function(index, ...) {
    if (additional_legend_labels[index] == "NaN") {
      grid::grid.rect(gp = grid::gpar(col = "black", lwd = 2))
    }
  }

  # Add padding below the image
  padding_below_image <- unit(5, "mm")  # Adjust the value as needed

  additional_legend <- Legend(at = additional_legend_values,
                              title = "Size",
                              labels = additional_legend_labels,
                              legend_gp = gpar(fill = additional_legend_colors),
                              title_gp = gpar(fontsize = 22, fontface = "bold"),
                              labels_gp = gpar(fontsize = 20),
                              border = TRUE,
                              grid_height = unit(0.9, "cm"), #color cell height
                              grid_width = unit(0.9, "cm")) #color cell width

  # Save the heatmap to the specified directoryS
  png(output_file, width = 1300, height = 1100)

  draw(heatmap, heatmap_legend_side = "right",
       annotation_legend_side = "right", padding = padding_value)
  draw(additional_legend, x = unit(1, "npc") - unit(22, "mm"),
       y = unit(0.6, "npc"), just = c("right", "center"))

  dev.off()
}