# Data Analysis Interface

A user-friendly web application built with Streamlit that makes data visualization and analysis accessible without writing code.

## Features

### 📊 Data Upload & Preview
- Support for CSV and Excel files
- Instant data preview in a clean tabular format

### 📋 Data Understanding Tools
- **Summary Statistics**: Quick overview of numeric data
- **Data Types**: Understand column types at a glance
- **Column Names**: Complete list of available columns
- **Missing Values Analysis**: Percentage and distribution of null values with handling recommendations

### 📈 Data Visualization
- **Value Count Visualizations**: Analyze categorical data with bar, line, and pie charts
- **Group By Analysis**: Perform aggregations across selected dimensions
- **Multiple Chart Types**:
  - Line charts with markers
  - Bar charts with grouping options
  - Scatter plots with size and color dimensions
  - Pie charts for proportion analysis
  - Sunburst charts for hierarchical data visualization

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/data-analysis-interface.git
cd data-analysis-interface

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

## Requirements

```
streamlit>=1.24.0
pandas>=1.5.0
plotly>=5.13.0
openpyxl>=3.1.0  # For Excel file support
```

## Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Open the provided URL in your browser (typically http://localhost:8501)

3. Upload your CSV or Excel file using the file uploader

4. Explore the data through the various analysis tabs

5. Generate visualizations using the interactive controls

## Example Workflow

1. **Upload Data**: Use the file uploader to import your CSV or Excel dataset
2. **Understand Your Data**: Review the summary statistics and check for missing values
3. **Explore Value Counts**: Select a categorical column to visualize distributions
4. **Perform Group By Analysis**: Select grouping columns and aggregation methods
5. **Visualize Results**: Choose from various chart types to represent your findings


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the amazing framework
- [Plotly Express](https://plotly.com/python/plotly-express/) for the interactive visualizations
- [Pandas](https://pandas.pydata.org/) for powerful data manipulation
