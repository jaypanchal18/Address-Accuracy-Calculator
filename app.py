import streamlit as st
from fuzzywuzzy import fuzz

def calculate_accuracy(address1, address2):
    if address1 is None or address2 is None:
        return None  
    
    address1_str = str(address1).lower()
    address2_str = str(address2).lower()
    
    accuracy = fuzz.ratio(address1_str, address2_str)
    
    return accuracy

def main():
    st.title('Address Accuracy Calculator')

    address1 = st.text_input('Address on doc:')
    address2 = st.text_input('Address on visit:')

    if st.button('Calculate Accuracy'):
        if not address1 or not address2:
            st.error('Please provide both addresses.')
        else:
            accuracy = calculate_accuracy(address1, address2)
            if accuracy is None:
                st.error('Unable to calculate accuracy.')
            else:
                st.success(f'Accuracy: {accuracy}%')

if __name__ == "__main__":
    main()
