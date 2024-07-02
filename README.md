# Radar Diagram

This repository contains the code for creating radar diagrams to visualize the performance of various models based on multiple evaluation metrics. The radar charts are generated from a CSV file containing the models' metrics, and the resulting charts are saved as SVG files.

## Features

- Generates radar charts for multiple models from a CSV file.
- Saves the radar charts as SVG files in a specified folder.
- Customizable categories for the radar charts.

## Getting Started

### Prerequisites

Ensure you have the following Python packages installed:

- `matplotlib`
- `pandas`

You can install these packages using `pip`:

```bash
pip install matplotlib pandas
```

### Repository Structure

- `RadarChart.py`: Contains the `RadarChart` class and script to generate radar charts.
- `data.csv`: Sample CSV file with model names and their corresponding metrics.
- `Figures/radar_chart/`: Folder where the radar charts will be saved.

### Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/EbrahimAlwajih/Radar-Diagram.git
   cd Radar-Diagram
   ```

2. **Prepare your CSV file:**

   Ensure your CSV file (`data.csv`) has a structure where the first column contains the model names, and the subsequent columns contain the values for the specified categories.

   Example of the `data.csv` structure:

   ```csv
   model,MAE,MSE,RMSE,R2,MedAE,EV,MBD,Adj_R2
   Model1,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8
   Model2,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9
   ```

3. **Run the script:**

   Execute the script to generate the radar charts:

   ```bash
   python RadarChart.py
   ```

   The radar charts will be saved as SVG files in the `Figures/radar_chart/` directory with filenames corresponding to the model names from the CSV file.

### Customization

- **Categories:**
  You can customize the categories for the radar charts by modifying the `categories` list in the script.

  ```python
  categories = ['MAE', 'MSE', 'RMSE', 'R2', 'MedAE', 'EV', 'MBD', 'Adj_R2']
  ```

- **Folder Path:**
  You can specify a different folder path to save the radar charts by changing the `folder_path` variable.

  ```python
  folder_path = './Figures/radar_chart'
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions, feel free to reach out to the repository owner.
