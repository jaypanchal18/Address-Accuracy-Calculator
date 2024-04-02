import streamlit as st
import pandas as pd
from openpyxl import load_workbook
from fuzzywuzzy import fuzz
from io import BytesIO

def calculate_accuracy(address1, address2):
    if address1 is None or address2 is None:
        return None  
    
    # Use fuzz ratio to calculate similarity between two strings
    accuracy = fuzz.ratio(address1.lower(), address2.lower())
    
    return accuracy

def main():
    st.title('Address Accuracy Calculator')

    uploaded_file = st.file_uploader("Upload Excel File", type="xlsx")

    if uploaded_file is not None:
        wb = load_workbook(uploaded_file)
        sheet = wb.active
        data = sheet.values
        columns = next(data)
        df = pd.DataFrame(data, columns=columns)

        df['Accuracy'] = df.apply(lambda row: calculate_accuracy(row['Address on doc'], row['Address on visit']), axis=1)

        st.write(df)

        if st.button('Download Result'):
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='openpyxl')
            df.to_excel(writer, index=False)
            writer.close()  # Close the Excel writer object
            output.seek(0)
            st.download_button(label="Download Result", data=output.getvalue(), file_name='customer_data_with_accuracy.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    main()
