

import streamlit as st 
 


# Define the custom style to position the last entry at the bottom
st.markdown("""
    <style>
    .bottom-text {
        position: fixed;
        bottom: 1;
        width: 50%;
        text-align: center;
        padding: 10px;
    }
   
    """, unsafe_allow_html=True)

# Main content
st.write()

col1, col2, col3 = st.columns([1, 1, 1])
if col2.button("Kérem az eredményeket!*"):
    st.write("OK")

# Place the last entry at the bottom
st.markdown('<div class="bottom-text">*A gomb megnyomásával hozzájárul adatainak kezeléséhez</div>', unsafe_allow_html=True)
