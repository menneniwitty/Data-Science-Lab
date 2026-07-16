# 🏠 House Price Prediction Using Linear Regression

## 📌 Project Overview
This project predicts house prices using the **Linear Regression** algorithm. The model estimates the price of a house based on features such as the number of rooms, square footage, and number of floors.

## 🎯 Objectives
- Predict house prices accurately.
- Understand the implementation of Linear Regression.
- Learn data preprocessing, model training, and evaluation.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## 📂 Project Structure

```
House-Price-Prediction/
│── house_price_prediction.py
│── house_price_dataset.csv
│── README.md
```

## 📊 Dataset

The dataset contains the following features:

| Feature | Description |
|----------|-------------|
| Rooms | Number of rooms |
| SqFt | Total area in square feet |
| Floors | Number of floors |
| Price | House price (Target Variable) |

### Sample Dataset

| Rooms | SqFt | Floors | Price |
|-------:|-----:|--------:|------:|
| 2 | 900 | 1 | 150000 |
| 3 | 1200 | 2 | 220000 |
| 4 | 1800 | 2 | 320000 |
| 5 | 2500 | 3 | 450000 |
| 6 | 3200 | 3 | 580000 |

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
```

Move into the project folder:

```bash
cd House-Price-Prediction
```

Install the required libraries:

```bash
pip install pandas numpy matplotlib scikit-learn
```

## ▶️ Run the Project

Execute the Python file:

```bash
python house_price_prediction.py
```

## 🔍 Machine Learning Model

The project uses **Linear Regression**.

The prediction equation is:

```
Price = b0 + b1(Rooms) + b2(SqFt) + b3(Floors)
```

Where:

- **b0** = Intercept
- **b1** = Coefficient for Rooms
- **b2** = Coefficient for Square Feet
- **b3** = Coefficient for Floors

## 📈 Model Evaluation

The model can be evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

## 🚀 Future Enhancements

- Add more house features such as location and age.
- Improve prediction accuracy using advanced machine learning models.
- Deploy the project as a web application using Flask or Streamlit.

## 👨‍💻 Author

**Menneni Witty**

GitHub: https://github.com/menneniwitty

## 📄 License

This project is created for educational purposes.
