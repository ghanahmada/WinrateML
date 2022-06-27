import streamlit as st
from math import ceil, floor

st.title("Winrate Mobile Legends Calculator")

match1 = st.number_input("Berapa match Anda",0)
wr1 = st.number_input("Ketik winrate Anda",0.0)
wr2 = st.number_input("Ketik winrate yang Anda inginkan",0.0)
hitung = st.button("Hitung Winrate")

def calc(match1=match1, wr1=wr1, wr2=wr2):
    match2Win = ceil((match1 * (wr2 - wr1)) / (100 - wr2))
    match2Lose = floor((match1 * (wr2 - wr1)) / wr2)
    return (match2Win,"winstreak") if wr2 > wr1 else (match2Lose,"losestreak")

if hitung:
    st.markdown(f"Anda harus bermain {calc()[1]} sebanyak **{calc()[0]}** kali")
