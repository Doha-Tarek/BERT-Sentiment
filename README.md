# BERT Sentiment Analysis

![BERT](https://img.shields.io/badge/BERT-NLP-blue.svg) ![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Sentiment Analysis](https://img.shields.io/badge/Sentiment-Analysis-yellow.svg)

## Overview

Welcome to the BERT Sentiment Analysis project! This repository contains a real-world implementation of sentiment analysis using the BERT (Bidirectional Encoder Representations from Transformers) model. This project was developed to solve a specific problem, applying BERT for sentiment classification to derive actionable insights from textual data. Leveraging state-of-the-art Natural Language Processing (NLP) techniques, this solution provides accurate and reliable sentiment analysis.


## Project Structure

The project is organized into the following folders, reflecting the logical steps in the workflow:

- **Analysis/**: Contains Jupyter notebooks for the analysis and exploration of data.
  - `Analsis.ipynb`: Main analysis notebook, including data exploration, feature engineering, and model training.
  - `ZEST_ANALYSIS.ipynb`: Specific analysis focused on sentiment extraction using BERT.
  
- **Data Labeling/**: Focuses on the preparation and labeling of the dataset.
  - `Labeled_Data.xlsx`: The labeled dataset ready for analysis.
  - `Data Labeling for Sentiment Analysis.ipynb`: Jupyter notebook detailing the data labeling process.

- **Scraping/**: Contains the code and data for web scraping.
  - `selenium_scrapper.py`: Python script for web scraping.
  - `scraped_data.xlsx`: The raw data collected from the web scraping process.

- **Sentiment-Analysis/**: Stores sentiment analysis models and related files.
  - `BERT_Training.ipynb`: Jupyter notebook for training and fine-tuning the BERT model on the labeled data.
  
## Installation

To get started with this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Doha-Tarek/BERT-Sentiment.git
cd BERT-Sentiment

# Create a virtual environment (optional but recommended)
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

