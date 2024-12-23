import streamlit as st # type: ignore
from pdf_main import pdf_main
from excel_main import excel_main
from json_main import json_main
from reconcile_main import reconcile_main

def main():
    st.sidebar.title("Select an App")
    # Create a radio button in the sidebar for app selection
    app_selection = st.sidebar.radio("Choose App", ("PDF App", "Excel App", "JSON App", "Reconcile App"))

    # Render the selected app
    if app_selection == "PDF App":
        pdf_main()  # Call the pdf_main function from the first app
    elif app_selection == "Excel App":
        excel_main()  # Call the excel_main function from the second app
    elif app_selection == "JSON App":
        json_main()
    elif app_selection == "Reconcile App":
        reconcile_main

if __name__ == "__main__":
    main()
