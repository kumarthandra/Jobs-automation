import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Job Search Automation",
    layout="wide"
)

st.title("🚀 Job Search Automation")

# Role Dropdown
role = st.selectbox(
    "Select Role",
    [
        "All",
        "DevOps Engineer",
        "Site Reliability Engineer",
        "Platform Engineer",
        "Data Platform Engineer",
        "Data Engineer"
    ]
)

# Posted Date
posted = st.radio(
    "Posted Within",
    ["24 Hours", "48 Hours", "7 Days"]
)

try:
    df = pd.read_csv("output/jobs.csv")

    st.success(f"Loaded {len(df)} jobs")

    # Search box
    search = st.text_input("Search Jobs")

    if search:
        df = df[
            df["Title"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    # Role filter
    if role != "All":
        role_word = role.split()[0]

        df = df[
            df["Title"].str.contains(
                role_word,
                case=False,
                na=False
            )
        ]

    st.subheader("Job Results")

    st.write(
        df.to_html(
            render_links=True,
            escape=False,
            index=False
        ),
        unsafe_allow_html=True
    )

except FileNotFoundError:
    st.error(
        "jobs.csv not found. Run main.py first."
    )