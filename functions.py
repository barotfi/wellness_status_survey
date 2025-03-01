


def convert(valasz):
    if valasz == 'Kiváló':
        pont = 100
    elif valasz == 'Jó':
        pont = 70
    elif valasz == 'Elfogadható':
        pont = 40
    elif valasz == 'Rossz':
        pont = 10
    return pont

def convertbmi(input):
    if input == 1000:
        bmiszazelek = 1000
    if input <= 18:
        bmiszazelek = 90
    elif 1000 < input >= 30:
        bmiszazelek = 10
    elif 25<= input <30:
        bmiszazelek = 55
    elif 18< input <25:
        bmiszazelek = 100
    else:
        bmiszazelek=0
    return bmiszazelek

def testsulytrend(ts,ts2):
    testsulyvalt = ((ts-ts2)/ts2)*100
    if testsulyvalt > 5:
        testsulytrend = 10
    else:
        testsulytrend = 100
    return testsulytrend

def taplalkozaspont (t):
    if t == "Naponta":
        taplalkozaspont = 100
    elif t == "Hetente néhány alkalommal":
        taplalkozaspont = 55
    elif t == "Ritkán":
        taplalkozaspont = 10
    else:
        taplalkozaspont = 0
    return taplalkozaspont


# Function to handle the button click
def next_step():
    import streamlit as st
  
    if st.session_state['step'] < 15:
                   
        st.session_state['step'] += 1
        
    else:
        st.session_state['ended'] = True
        # st.rerun()
        

def sessionstateinit(variable):
    import streamlit as st
    if variable not in st.session_state:
        st.session_state[variable] = 1

def progressline ():
    import streamlit as st
    import time

    progress_text = "Kérem várjon!"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(99):
        time.sleep(0.03)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)   
    my_bar.empty()




def atlag (lista):
    l = len(lista)
    sum_num = 0
    for t in lista:
        sum_num = sum_num + t           
    avg = round ((sum_num / l),ndigits=1)
    return avg