# 🚀 Air Quality Prediction Web App

Predicting Air Quality Index (AQI) using city-level air pollution data with a playful cartoon-style web interface and interactive smoke effects.

---

## 📊 About the Dataset

- **Source:** `data/city_day.csv`
- Contains daily air quality measurements for multiple cities, including pollutants (PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, Benzene, Toluene, Xylene) and AQI values.
- Used for regression modeling to predict AQI.

---

## 🎯 Objectives

- Load and preprocess air quality data
- Perform exploratory data analysis (EDA)
- Handle missing values and outliers
- Engineer features (date extraction, encoding)
- Build and evaluate regression models to predict AQI
- Compare model performance with different scaling techniques
- Deploy a web app for interactive AQI prediction

---

## 📝 Steps Performed

1. **Data Loading & Initial Exploration**
   - Loaded dataset, checked for missing values and duplicates
2. **Feature Engineering**
   - Extracted day, month, year from date
   - Encoded categorical city names
   - Dropped unnecessary columns
3. **Missing Value & Outlier Handling**
   - Filled missing values with median
   - Detected and removed outliers using z-score and IQR
4. **Exploratory Data Analysis**
   - Visualized distributions and correlations
5. **Model Building & Evaluation**
   - Built linear regression models
   - Compared three approaches:
     - Outliers removed, non-scaled
     - MinMax scaled
     - Standard scaled
   - Evaluated using MSE, RMSE, R-squared
6. **Web App Development**
   - Created a Flask backend serving predictions via `/predict` API
   - Designed a cartoon-style frontend with pastel colors, comic fonts, and a cartoon street background
   - Added interactive smoke effects that follow the mouse pointer
   - Integrated AJAX for real-time AQI prediction and display in a speech bubble

---

## 🛠 Tech Stack

- **Languages:** Python, HTML, CSS, JavaScript
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn, scipy, joblib
- **Frameworks/Tools:** Jupyter Notebook, Flask

---

## 🌐 Web App Features

- Cartoon-style, playful UI with Google Fonts (Comic Neue)
- Input boxes and buttons styled with pastel colors and rounded edges
- Cartoon street background with buildings, clouds, and trees
- Interactive smoke effect (light green, cartoon fart style) that follows the mouse pointer
- AJAX-based prediction: inputs sent to Flask `/predict` endpoint, result shown in a cartoon speech bubble
- Responsive and immersive user experience

---

## 📈 Test Results

Three regression tests were performed:

1. **Outliers removed - Non Scaled Model**
   - Metrics: MSE, RMSE, R-squared
2. **MinMax Scaled Model**
   - Metrics: MSE, RMSE, R-squared
3. **Standard Scaled Model**
   - Metrics: MSE, RMSE, R-squared

*(Please refer to the notebook output for actual values)*

---

## 🏁 Conclusion

This project demonstrates a complete workflow for predicting AQI using regression techniques and deploying a fun, interactive web app. Feature engineering, outlier handling, and scaling methods were compared to assess their impact on model performance. The web app provides a playful and engaging way for users to interact with the model and visualize predictions.

---

## 📂 Project Structure

```
Air quality prediction/
│
├── data/
│   └── city_day.csv         # Raw air quality data
├── Air_quality_prediction.ipynb  # Main notebook
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Cartoon-style frontend
├── static/
│   └── style.css           # Cartoon CSS styles
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── LICENSE                 # License file
```

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Contact / Credits

**Author:** Devarsh S R

---

✨ *Feel free to star the repo and share your feedback!* ✨
