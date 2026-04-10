import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
from keras.models import load_model
from PIL import Image
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("✍️ Handwritten Digit Recognition")
st.write("Upload an image OR draw a digit below")

# Canvas
canvas = st_canvas(
    fill_color='black',
    stroke_width=20,
    stroke_color='white',
    background_color='black',
    height=280,
    width=280,
    key='canvas'
)

# Upload file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if st.button('Predict'):
    from PIL import ImageOps

    # ----------- CASE 1: Uploaded Image -----------
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('L')
        st.image(image, caption="Uploaded Image", use_column_width=True)

        image = image.resize((28, 28))
        img_array = np.array(image)
        img_array = img_array / 255.0
        img_array = img_array.reshape( 1,28, 28, 1)

    # ----------- CASE 2: Canvas Drawing -----------
    else:
        # Convert RGBA → grayscale
        img = Image.fromarray(canvas.image_data.astype('uint8')).convert('L')


        # Resize with padding (maintain aspect ratio)
        # img = ImageOps.pad(img, (28, 28), method=Image.Resampling.LANCZOS)
        img=img.resize((28,28))
        # Convert to array
        img_array = np.array(img) / 255.0

        # Reshape
        img_array = img_array.reshape(1,28, 28, 1)

    # Prediction
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction[0])
    confidence = np.max(prediction)

    st.success(f"Predicted Digit: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}")
