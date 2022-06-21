import streamlit as st
from math import ceil, floor

st.title("Winrate Mobile Legends Calculator")

match1 = st.number_input("Berapa match Anda",0)
wr1 = st.number_input("Ketik winrate Anda",0.0)
wr2 = st.number_input("Ketik winrate yang Anda inginkan",0.0)
hitung = st.button("Hitung Winrate")

if hitung:
    if wr2 > wr1:
        match2 = (match1 * (wr2 - wr1)) / (100 - wr2)
        st.markdown(f"Anda harus bermain winstreak sebanyak **{ceil(match2)}** kali.")

    else:
        match2 = (match1 * (wr2 - wr1)) / wr2
        st.markdown(f"Anda harus bermain losestreak sebanyak **{abs(floor(match2))}** kali.")
