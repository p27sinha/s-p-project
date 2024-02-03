# S&P index project

## Automated Stock Trading System using Reinforcement Learning - IT Sector
### Overview
This GitHub repository contains code and resources for building an automated stock trading system using Reinforcement Learning, specifically applied to the Information Technology (IT) sector of the S&P 500.

### Objective
The goal of this project is to implement a Q-learning model that learns optimal combinations of buying, selling, or holding IT sector stocks based on historical data. While the trained model may not be immediately suitable for real-world trading due to the need for more extensive data, the primary aim is to understand how different IT sector stocks fluctuate in relation to each other.

### Data
The historical stock data for the IT sector is obtained from Yahoo Finance, covering the period from December 2018 to December 2023. The data includes information on stock indices for various sectors, with a focus on the IT sector.

### Code Structure
The code is structured as follows:

#### Data Processing: Python code using Pandas to read and process IT sector stock data, standardize the stocks for comparability, and round normalized index values for finite state-space Q-learning.

#### Q-learning Implementation: Implementation of Q-learning using a policy table to determine optimal actions. The Q-learning model is trained on the IT sector data.

#### Visualization: Utilizes Matplotlib and Seaborn for visualizing rewards during training and generating a heat map of the learned Q-table to represent trading rules.

#### Descriptive Statistics: Extracts and analyzes descriptive statistics for positively and negatively reinforced actions, providing insights into the model's learning.

#### Bipartite Graph Visualization: Utilizes NetworkX to create a bipartite graph illustrating the relationships between IT sector index values and corresponding actions, highlighting actions that yield higher rewards.

### Usage
To run the code and reproduce the results, follow the provided Jupyter Notebook or Python scripts. Make sure to have the required dependencies installed.

### Results
The project evaluates the effectiveness of the Q-learning model in making informed trading decisions within the IT sector of the S&P index. Explore the rewards plot, heat map, and descriptive statistics to gain insights into the learned trading rules.

### Future Work
Potential future improvements and investigations include expanding the dataset, exploring why certain actions receive higher rewards, and adapting the model for real-world applications.
