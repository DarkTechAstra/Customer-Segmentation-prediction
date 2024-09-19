# Customer-Segmentation-prediction
Here's an updated version of the README file, including a section on the **Usage** and **Benefits** of the project:

---

# Customer Segmentation Project

## Overview

This project involves implementing a customer segmentation model to categorize customers into different segments based on their purchasing behavior. The primary goal is to help businesses understand their customer base and tailor marketing strategies effectively.


## Introduction

Customer segmentation is a vital technique in marketing analytics that groups customers with similar characteristics. This project uses machine learning techniques to segment customers into different categories based on features such as age, gender, annual income, and spending score.

## Dataset

The dataset used for this project includes information about customer demographics and their spending behavior. The features in the dataset help in identifying patterns and segmenting the customers into different groups.

- **Source**: (https://www.kaggle.com/datasets/zubairmustafa/shopping-mall-customer-segmentation-data)
- **Description**: The dataset contains various columns related to customer attributes and purchasing behavior.

## Features

The following features are used in this model:

- **Age**: Age of the customer
- **Gender**: Gender of the customer (encoded as 0 for Male and 1 for Female)
- **Annual Income**: Total annual income of the customer
- **Spending Score**: A score assigned to the customer based on their spending behavior

## Model

The model used for customer segmentation is a [specific model used, e.g., K-Means Clustering, Gaussian Mixture Model, etc.]. The model was trained on the dataset to predict customer segments based on the provided features.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/DarkTechAstra/Customer-Segmentation-prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Customer-Segmentation-prediction
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Streamlit App

To use the model for customer segmentation, follow these steps:

1. **Upload Dataset**: Use the provided Streamlit app to upload your dataset.
2. **Select Features**: Choose the relevant features for prediction from the dataset.
3. **Predict**: Run the prediction to categorize the customers into different segments.
4. **Form Input**: Use the form to input specific customer data for individual predictions.

Run the Streamlit app with:
```bash
streamlit run Cust_Seg_Project.py
```

## Benefits

This project provides several benefits for businesses:

1. **Targeted Marketing**: By segmenting customers into distinct groups, businesses can tailor their marketing strategies to address the specific needs and preferences of each segment.
2. **Improved Customer Insights**: Understanding different customer segments allows businesses to gain deeper insights into their customer base and identify opportunities for growth.
3. **Enhanced Customer Experience**: Personalized marketing and services based on customer segments lead to improved customer satisfaction and loyalty.
4. **Optimized Resource Allocation**: Businesses can allocate resources more efficiently by focusing efforts on high-value customer segments and reducing waste in marketing spend.
