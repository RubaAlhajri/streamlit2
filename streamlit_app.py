import streamlit as st
import requests
import streamlit as st
import json

st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to right, #4b6cb7, #182848);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app
st.markdown("<span style='font-size: 28px;'>⚽Football Player Value Predictor⚽</span>", unsafe_allow_html=True)

st.markdown("<span style='font-size: 20px;'>📊 Player Attributes</span>", unsafe_allow_html=True)
# Define the API endpoint
#url = 'https://uc7-api-2.onrender.com/'


age=st.number_input(" player age ", value=None, placeholder="Enter the player age please")
appearance=st.number_input("Appearance ", value=None, placeholder="Enter the time of appearance please")
minutes_played=st.number_input("minutes_played ", value=None, placeholder="Enter minutes of play please")
highest_value=st.number_input("highest_value ", value=None, placeholder="Enter highest value please")





inputs = {
     "age": age,
          "appearance": appearance,
          "minutes_played": minutes_played,
          "highest_value": highest_value
 }

if st.button('Get Prediction'):
    if age and appearance and minutes_played and highest_value:
        try:
            res = requests.post(
                url="https://uc7-api-2.onrender.com/predict",
                headers={"Content-Type": "application/json"},
                data=json.dumps(inputs)
            )
            res.raise_for_status()  # Check for HTTP request errors
            prediction = res.json() # Extract the prediction value
            if prediction is not None:
                st.subheader(f"Prediction result = {prediction}")
            else:
                st.error("No prediction found in the response.")

        except requests.exceptions.RequestException as e:
            st.error(f"HTTP Request failed: {e}")
        except ValueError as e:
            st.error(f"Failed to parse JSON response: {e}")
    else:
        st.error("Please fill in all input fields.")
