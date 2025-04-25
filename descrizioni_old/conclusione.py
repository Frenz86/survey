import streamlit as st

def main():
###############################################

#    # Puoi usare le colonne di Streamlit per centrare contenuti
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
        st.title("Conclusione")
        text= """
<div style="text-align: justify;">





</div>
"""
        st.markdown(text, unsafe_allow_html=True)

###############################################

if __name__ == "__main__":
   main()