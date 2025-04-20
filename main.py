import streamlit as st
import random
import  string

def generator_passward(length,use_dights,use_special):
        characters = string.ascii_letters

        if use_dights:
                characters +=string.use_dights

        if use_special:
               characters += string.punctuation

               return    ''.join(random.choice(characters) for _ in range(length))
        
        st.title("Passward Generator")

        length =st.slider("Select Passward lenght ", min_value=6,   max_value=32,  value=12)

        use_dights = st.checkbox ("Include Dights")
 
        use_special =st.checkbox("Incdude special character")

        if st._bottom("Generator Passward"):
                passwad = generator_passward(length,use_dights,use_special,)
                st.write(f"Generator Password:`{passwad}`")

                st.write("----")
