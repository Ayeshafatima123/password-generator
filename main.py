import streamlit as st
import random
import  string

def generator_password(length,use_dights,use_special):
        characters = string.ascii_letters

        if use_dights:
                characters +=string.use_dights

        if use_special:
               characters += string.punctuation

               return    ''.join(random.choice(characters) for _ in range(length))
        
        st.title("Password Generator")

        length =st.slider("Select Password lenght ", min_value=6,   max_value=32,  value=12)

        use_dights = st.checkbox ("Include Dights")
 
        use_special =st.checkbox("Incdude special character")

        if st._buttom("Generator Password"):
                passoard = generator_password(length,use_dights,use_special,)
                st.write(f"Generator Password:`{password}`")

                st.write("----")
