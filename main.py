import streamlit as st
from math import ceil, floor

st.set_page_config(page_title="Winrate ML Calculator", page_icon=":video_game:")
st.title("Winrate Mobile Legends Calculator")

#----INPUT DATA----
match1 = st.number_input("Berapa match Anda",0)
wr1 = st.number_input("Ketik winrate Anda",0.0)
wr2 = st.number_input("Ketik winrate yang Anda inginkan",0.0)
hitung = st.button("Hitung Winrate")

#----CALCULATION----
def calc_match():
    match2Win = ceil((match1 * (wr2 - wr1)) / (100 - wr2))
    match2Lose = abs(floor((match1 * (wr2 - wr1)) / wr2))
    return (match2Win,"winstreak") if wr2 > wr1 else (match2Lose,"losestreak")

def calc_wr():
    wr2_win = ((100 * match_ke) + (match1 * wr1)) / (match1 + match_ke)
    wr2_lose = (match_ke + (match1 * wr1)) / (match1 + match_ke)
    return wr2_win if calc_match()[1] == "winstreak" else wr2_lose

#----DISPLAY THE CALCULATION----
if hitung:
    try:
        st.markdown(f"Anda harus bermain **{calc_match()[1]}** sebanyak **{calc_match()[0]}** kali")
        details,match_ke = st.expander("Perkembangan Winrate"), 1
        while match_ke <= calc_match()[0]:
            if calc_match()[0] > 100 and match_ke == 51:
                details.markdown("...")
                match_ke = calc_match()[0]-49
            details.markdown(f"match ke-{match_ke} = {round(calc_wr(), 2)}%")
            match_ke += 1
    except: 
        st.error("Mohon isi kolom di atas.")
        
# ---- HIDE STREAMLIT STYLE ----
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)
