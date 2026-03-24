import streamlit as st
import numpy as np
import joblib

# load model
model = joblib.load("mobile_price_model.pkl")

st.title("Mobile Price Classification")

st.write("Enter Mobile Specifications")

battery_power = st.number_input("Battery Power", 500, 2000)
blue = st.selectbox("Bluetooth", [0,1])
clock_speed = st.number_input("Clock Speed", 0.5, 3.0)
dual_sim = st.selectbox("Dual SIM", [0,1])
fc = st.number_input("Front Camera", 0, 20)
four_g = st.selectbox("4G", [0,1])
int_memory = st.number_input("Internal Memory", 2, 128)
m_dep = st.number_input("Mobile Depth", 0.1, 1.0)
mobile_wt = st.number_input("Mobile Weight", 80, 250)
n_cores = st.number_input("Cores", 1, 8)
pc = st.number_input("Primary Camera", 0, 20)
px_height = st.number_input("Pixel Height", 0, 2000)
px_width = st.number_input("Pixel Width", 0, 2000)
ram = st.number_input("RAM", 256, 8000)
sc_h = st.number_input("Screen Height", 5, 20)
sc_w = st.number_input("Screen Width", 0, 20)
talk_time = st.number_input("Talk Time", 2, 20)
three_g = st.selectbox("3G", [0,1])
touch_screen = st.selectbox("Touch Screen", [0,1])
wifi = st.selectbox("WiFi", [0,1])

if st.button("Predict Price"):

    features = np.array([[
        battery_power,
        blue,
        clock_speed,
        dual_sim,
        fc,
        four_g,
        int_memory,
        m_dep,
        mobile_wt,
        n_cores,
        pc,
        px_height,
        px_width,
        ram,
        sc_h,
        sc_w,
        talk_time,
        three_g,
        touch_screen,
        wifi
    ]])

    prediction = model.predict(features)

    price_map = {
        0: "Low Cost",
        1: "Medium Cost",
        2: "High Cost",
        3: "Very High Cost"
    }

    st.success(f"Predicted Price Range: {price_map[int(prediction[0])]}")