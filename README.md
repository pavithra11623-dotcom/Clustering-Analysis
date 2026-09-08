# Clustering-Analysis
K-means model groups countries based on similar development indicators
World Development Clustering

**📌 Project Title**

World Development Measurement – Country Clustering

**📖 Business Objective**

The objective of this project is to analyze global development indicators and group countries based on their similar development characteristics.

**🎯 Project Goal**

To classify countries into different clusters based on indicators such as:

- 💰 GDP
- 🏥 Health Expenditure
- 👶 Infant Mortality
- ❤️ Life Expectancy
- 👥 Population
- 🌐 Internet Usage
- 📱 Mobile Phone Usage
- 🌍 CO₂ Emissions
- ✈️ Tourism

**📊 Dataset**

The dataset contains country-level development and economic indicators. It is used to identify similarities and differences between countries.

**🔧 Technologies Used**

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- StandardScaler
- K-Means
- Hierarchical Clustering
- DBSCAN
- PCA
- Streamlit

**🚀 Project Workflow**

1. Data Collection

- Load the World Development dataset.

2. Data Cleaning

- Handle missing values.
- Remove duplicate records.
- Convert text-based numerical values into numeric format.

3. Exploratory Data Analysis (EDA)

- Analyze development indicators.
- Study distributions and correlations.
- Visualize important features.

4. Feature Scaling

- Apply StandardScaler to standardize numerical features.

5. Model Building

- Apply K-Means Clustering.
- Apply Hierarchical Clustering.
- Apply DBSCAN.

6. Model Evaluation

- Compare clustering models using:
  - Silhouette Score
  - Davies-Bouldin Score
  - Calinski-Harabasz Score

7. Visualization

- Use PCA to visualize the country clusters in 2D.

8. Model Saving

- Save the trained clustering model and scaler using Joblib.

9. Deployment

- Deploy the final clustering application using Streamlit.

**📁 Project Structure**

World-Development-Clustering/

│

├── data/

│   └── World_development_mesurement.csv

│

├── notebooks/

│   ├── 01_Data_Cleaning.ipynb

│   ├── 02_EDA.ipynb

│   └── 03_Clustering_Model.ipynb

│
├── kmeans_model.pkl

├── scaler.pkl

├── app.py

├── requirements.txt

└── README.md

💻 How to Run the Project

Install Required Libraries

pip install -r requirements.txt

Run the Streamlit Application

streamlit run app.py

**📈 Expected Outcome**

The application will group countries into clusters based on their development indicators and allow users to explore the characteristics of each cluster.

**🌐 Deployment**

The final clustering model can be deployed using:

- Streamlit
- Flask

**👩‍💻 Author**

Pavithra Natarajan

---
