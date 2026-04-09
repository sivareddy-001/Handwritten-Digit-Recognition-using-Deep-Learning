# ✍️ Handwritten Digit Recognition using Deep Learning

## 📌 Project Overview

This project implements a **Handwritten Digit Recognition system** using a **Convolutional Neural Network (CNN)** trained on the MNIST dataset.
It also includes a **Streamlit web application** where users can:

* Upload an image of a digit
* Draw a digit on a canvas
* Get real-time predictions

---

## 🚀 Features

* 🧠 Deep Learning model using CNN
* 🎨 Interactive drawing canvas
* 📤 Image upload support
* 📊 Real-time prediction with confidence score
* 🌐 User-friendly Streamlit interface

---

## 🧰 Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pandas
* Matplotlib
* Streamlit
* PIL (Python Imaging Library)

---

## 📂 Dataset

The model is trained on the **MNIST dataset**, which contains:

* 60,000 training images
* 10,000 testing images
* Images are grayscale (28×28 pixels)
* Labels: digits from 0 to 9

---

## ▶️ How to Run

### 1. Train the Model

Run the notebook:

```bash
jupyter notebook Cleaning.ipynb
```

### 2. Run Streamlit App

```bash
streamlit run app.py
```

---

## 🧠 Model Architecture

The CNN model consists of:

* Convolutional Layers (feature extraction)
* MaxPooling Layers (downsampling)
* Flatten Layer
* Fully Connected Dense Layers
* Dropout (to prevent overfitting)

---

## 📸 Application Workflow

1. User uploads or draws a digit
2. Image is preprocessed (resize, normalize, invert)
3. Model predicts the digit
4. Result displayed with confidence score

---

## ⚠️ Challenges Faced

* Difference between MNIST data and user-drawn digits
* Image preprocessing inconsistencies
* Stroke thickness and digit alignment

---

## ✅ Improvements

* Added better preprocessing (centering, padding)
* Increased model accuracy using CNN tuning
* Improved UI with canvas drawing

---

## 📊 Results

* Initial Accuracy: ~60–70%
* Improved Accuracy: **95%+** after optimization

---

## 🔮 Future Enhancements

* 📱 Mobile app integration
* 🔍 Real-time camera digit recognition
* 📊 Display top-3 predictions
* ☁️ Deployment on Streamlit Cloud

---

## 👨‍💻 Author

Peram Venkata Siva Reddy

---

## ⭐ Acknowledgements

* MNIST Dataset
* TensorFlow & Keras
* Streamlit

---
