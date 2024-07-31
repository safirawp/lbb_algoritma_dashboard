import streamlit as st
from streamlit_gsheets import GSheetsConnection

# ydata profiling
import pandas as pd
from ydata_profiling import ProfileReport

# report untuk streamlit
from streamlit_pandas_profiling import st_profile_report

# ------- Config
st.set_page_config(
	page_title="Data Employee Attrition",
	page_icon="",
	layout="wide",
	initial_sidebar_state="collapsed",
)

# ------- Judul Dashboard
# st.title("Data Profiler") -> Opsi lain rata kiri
st.markdown("<h1 style='text-align: center;'> Data Employee Attrition </h1>",
            unsafe_allow_html=True)
st.markdown("---")

# ------- Sidebar
with st.sidebar:
	st.subheader("Data")
	st.markdown("---")
	

# ------- Buat button
if st.sidebar.button("Start Generate Data"):

	## Read Data
    conn = st.connection("gsheet", type=GSheetsConnection)
    df = conn.read(
        spreadsheet = st.secrets.gsheet_attrition["spreadsheet"],
        worksheet = st.secrets.gsheet_attrition["worksheet"]
    )

	## Generate Report
	#---- progile report using ydata profiling
    pr = ProfileReport(df)

	# Display to streamlit
    st_profile_report(pr)
	
else:
	
    st.info("Click Button in The Left Sidebar to Generate Report")