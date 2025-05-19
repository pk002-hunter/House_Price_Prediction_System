
#  House Price Prediction Model


## Overview

This project aims to predict house prices based on various features such as location, proximity to key amenities (like colleges, schools and hospitals), and property-specific details (e.g., area, number of rooms, furnishing status). Using statistical and machine learning models, the system analyzes historical housing data to estimate current market prices. An interactive web interface allows users to input property details and receive real-time price predictions. This tool is especially useful for home buyers, real estate agents, and property investors looking to make data-driven decisions.


**Key Features:**

* **Data Exploration and Preprocessing:**  Includes exploratory data analysis (EDA) to understand the data and preprocessing steps to prepare it for modeling.
* **Model Training:**  Employs various regression models including Linear Regression, Decision Tree, Random Forest, and XGBoost.
* **Hyperparameter Tuning:**  Parameter tuning was performed for all models, with a focus on Grid Search for optimizing XGBoost.
* **Performance Evaluation:**  Comprehensive evaluation of each model using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R2).

## Dataset

The dataset used in this project is  focused on predicting house prices across various cities in Uttarakhand, India. It includes a rich set of features that influence housing prices, allowing for accurate and context-aware predictions.


**Key Features:**


1. State & City – Geographical location of the property

2. Property Type – E.g., Apartment, Villa, etc.

3. BHK – Number of bedrooms

4. Size_in_SqFt – Total built-up area of the property

5. Price_in_Lakhs – Target variable representing house price

6. Price_per_SqFt – Price efficiency per unit area

7. Year_Built & Age_of_Property – Construction year and derived age

8. Furnishing Status – Furnished, semi-furnished, or unfurnished

9. Floor Details – Floor number and total floors in the building

10. Nearby_Schools & Nearby_Hospitals – Count of nearby facilities

11. Public Transport Accessibility – Level of connectivity (Low/Medium/High)

12. Parking, Security, and Amenities – Qualitative property features

13. Facing – Direction the house faces

14. Owner Type – Broker, Builder, or Owner

15. Availability Status – Ready to move or under construction

This dataset was manually curated to reflect real-world conditions and common features in Uttarakhand's property market. It supports both descriptive analytics and predictive modeling for house pricing.


## Business Applications

This house price prediction model can be valuable for:

- 🏘️ **Real Estate Agents**: Quickly estimate property values based on location and features
- 💰 **Property Investors**: Make data-driven decisions for investment opportunities across Indian states
- 🏦 **Banks & Lenders**: Assist in property valuation for mortgage and loan assessments
- 🏗️ **Property Developers**: Analyze market trends and optimize pricing strategies for new developments
- 🏡 **Home Buyers**: Get fair price estimates before making purchase decisions
- 📊 **Market Analysts**: Study housing market trends and price patterns across different Indian regions

The model's high accuracy (99.9% R² score with XGBoost) makes it a reliable tool for stakeholders in the Indian real estate market to make informed decisions.

## Methodology

The following steps were undertaken in this project:

1. **Exploratory Data Analysis (EDA):**  Initial exploration of the dataset to understand its structure, identify patterns, and gain insights into the features.
2. **Data Preprocessing:**
    * **Dropping Unnecessary Columns:** Identification and removal of irrelevant or redundant columns.
    * **Ordinal Encoding:** Encoding of ordinal categorical features into numerical representations.
    * **Data Sampling:**  Selection of a subset of approximately 100,000 rows from the dataset due to limited computational resources.
    * **One-Hot Encoding:** Application of One-Hot Encoding using `DictVectorizer` to convert remaining categorical features into a numerical format suitable for machine learning models.
3. **Model Training and Evaluation:**
    * Training of the following regression models:
        * Linear Regression
        * Decision Tree
        * Random Forest
        * XGBoost
    * Parameter tuning for each model to optimize performance.
    * Grid Search was specifically used to fine-tune the hyperparameters of the XGBoost model.
4. **Performance Evaluation:**  Evaluation of each trained model using the following metrics:
    * **Mean Absolute Error (MAE):** Average absolute difference between the predicted and actual prices.
    * **Mean Squared Error (MSE):** Average of the squared differences between the predicted and actual prices.
    * **Root Mean Squared Error (RMSE):** Square root of the MSE, providing an error metric in the original unit of the target variable.
    * **R-squared (R2):**  A statistical measure representing the proportion of the variance in the dependent variable that is predictable from the independent variables.

## Results

The following performance metrics were achieved by the trained models:

| Model | MAE | MSE | RMSE | R² Score |
|-------|-----|-----|------|----------|
| Linear Regression | 81.75 | 10364.25 | 101.80 |  0.962|
| Decision Tree | 7.70 | 96.81 | 9.84 | 0.997 |
| Random Forest | 50.60 | 3910.55 | 62.53 | 0.995|
| XGBoost | 6.96 | 78.74 | 8.87 |  0.9997 |

### Bar Plot Comparison of Models

![Model's performance using bar plots](https://raw.githubusercontent.com/pk002-hunter/pbl/main/performance.png)

### Radar Chart Models Comparison
![Model's Result Using Radar chartr](https://raw.githubusercontent.com/pk002-hunter/pbl/main/radarchart.png)

## How to Use the Model

### Prerequisites

- **Pipenv:** For managing Python environments and dependencies.
- **Docker:** For containerized deployment of the model.
- **Flask:** For app/webservice.

### Running Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/izaanz/ML-Indian-House-Prediction
   navigate to the cloned directory
   ```

2. **Setup Environment:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Run the Model:**
   
   Note: You may have to run `python train.py` if the model_.bin doesn't validate on your end.
   
   ```bash
   python app.py
   ```
   This will start a local server where you can send requests to get predictions.

4. **Testing Predictions:**

   You can use predict_test.py to test the predictions.
   
   ```bash
   python train.py
   ```
   This will return a predicted house priced based on the stored data in the file.


### Interacting with the Model

When testing the model, you can use the following JSON structure for a student's data:


```json
{

 'City': 'Dehradun',
 'Property_Type': 0.0,
 'BHK': 1,
 'Size_in_SqFt': 2059,
 'Year_Built': 1995,
 'Furnished_Status': 2.0,
 'Floor_No': 0,
 'Total_Floors': 2,
 'Age_of_Property': 30,
 'Nearby_Schools': 7,
 'Nearby_Hospitals': 6,
 'Public_Transport_Accessibility': 0.0,
 'Parking_Space': 'no',
 'Security': 0.0,
 'Amenities': 'garden, pool, gym, playground, clubhouse',
 'Facing': 2.0,
 'Owner_Type': 'broker',
 'Availability_Status': 'under_construction'
}
```
Use train.py to send test queries to your model:

- Use `train.py` to send test queries to your model:
  ```bash
  python train.py
  ```

  Modify this script to format your input data as per the model's expectations.

## Deployed on Cloud

This is a machine learning-based web application for predicting house prices in India. The app is powered by a regression model that takes various house attributes (such as location, size, number of rooms, etc.) to predict the price of a house.


![Cloud Deployment](https://raw.githubusercontent.com/pk002-hunter/pbl/main/Flowchart.png)

You can input house details into the app, and it will generate a predicted price based on the trained model.

## Contributions

This project was developed as a collaborative effort by a team of four members, each contributing to different aspects such as data collection, feature engineering, model development, and web integration. By combining our individual strengths in data science, software development, and design, we successfully built a functional and user-friendly house price prediction system tailored for Uttarakhand. Teamwork, continuous feedback, and shared learning were key to the successful execution of this project.


## Acknowledgements

We would like to express our heartfelt gratitude to everyone who supported us throughout the development of this project. Special thanks to our mentor and faculty member, Ms. Akshita Arya, for her invaluable guidance, insightful feedback, and continuous encouragement.

We are also thankful for the availability of powerful resources and tools that made this work possible, including Python libraries such as Pandas, Scikit-learn, and Flask. Additionally, we appreciate the open-source learning platforms that greatly aided us in deepening our knowledge of machine learning and web development.

Finally, we sincerely thank each team member for their unwavering dedication, collaborative spirit, and consistent efforts in bringing this project to fruition.



