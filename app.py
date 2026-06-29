import streamlit as st
import pandas as pd

from src.collectors.greenhouse import get_jobs
from src.filters.management_filter import remove_management_jobs

st.set_page_config(
    page_title="Job Search Automation",
    layout="wide"
)

st.title("🚀 Job Search Automation")

# ATS Selection
ats = st.selectbox(
    "ATS Platform",
    [
        "Greenhouse"
    ]
)

# Role Selection
role = st.selectbox(
    "Role",
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
    [
        "24 Hours",
        "48 Hours",
        "7 Days"
    ]
)

# Keyword Search
search_text = st.text_input("Keyword Search")

# Search Button
if st.button("🔍 Search Jobs"):

    # Fetch live jobs
    jobs = get_jobs()

    df = pd.DataFrame(jobs)

    # Remove management roles
    df = remove_management_jobs(df)

    # Role Keywords
    role_keywords = {
        "DevOps Engineer": [
            "devops"
        ],
        "Site Reliability Engineer": [
            "site reliability",
            "sre"
        ],
        "Platform Engineer": [
            "platform"
        ],
        "Data Platform Engineer": [
            "data platform",
            "lakehouse"
        ],
        "Data Engineer": [
            "data engineer"
        ]
    }

    # Apply Role Filter
    if role != "All":

        keywords = role_keywords.get(role, [])

        df = df[
            df["title"].str.lower().apply(
                lambda title: any(
                    keyword in title
                    for keyword in keywords
                )
            )
        ]

    # Keyword Search
    if search_text:

        df = df[
            df["title"].str.contains(
                search_text,
                case=False,
                na=False
            )
        ]

    st.success(f"Found {len(df)} jobs")

    st.dataframe(
        df,
        width="stretch"
    )