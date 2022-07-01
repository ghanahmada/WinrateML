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
    try:
        st.markdown(f"Anda harus bermain **{calc()[1]}** sebanyak **{abs(calc()[0])}** kali")
        details = st.expander("Perkembangan Winrate")
        try:
            if calc()[1] == "winstreak":
                for match_Ke in range(1, ceil(calc()[0]) + 1, 1):
                    wr2 = ((100 * match_Ke) + (match1 * wr1)) / (match1 + match_Ke)
                    if ceil(calc()[0]) > 100 and match_Ke == 51:
                        details.write("...")
                        for match_Ke in range(ceil(calc()[0])-49,ceil(calc()[0]) + 1, 1):
                            wr2 = ((100 * match_Ke) + (match1 * wr1)) / (match1 + match_Ke)
                            details.write(f"match ke-{str(match_Ke)} = {str(round(wr2, 2))}%")
                        break
                    details.write(f"match ke-{str(match_Ke)} = {str(round(wr2, 2))}%")
            else:
                for match_Ke in range(1, abs(floor(calc()[0])) + 1, 1):
                    wr2 = (match_Ke + (match1 * wr1)) / (match1 + match_Ke)
                    if abs(floor(calc()[0])) > 100 and match_Ke == 51:
                        details.write("...")
                        for match_Ke in range(abs(floor(calc()[0]))-49,abs(floor(calc()[0])) + 1, 1):
                            wr2 = (match_Ke + (match1 * wr1)) / (match1 + match_Ke)
                            details.write(f"match ke-{str(match_Ke)} = {str(round(wr2, 2))}%")
                        break
                    details.write(f"match ke-{str(match_Ke)} = {str(round(wr2, 2))}%")
        except:
            details.markdown("*None*")
    except: st.error("Mohon isi kolom di atas")
