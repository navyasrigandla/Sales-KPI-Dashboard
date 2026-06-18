import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Sales KPI Dashboard", layout="wide")

st.title("📈 Sales KPI Dashboard")

# Upload Sales Dataset
uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file is not None:
    # Read Data
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Expected Columns:
    # Order_ID, Sales, Quantity, Profit, Customer_ID

    # KPI Calculations
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order_ID"].nunique()
    total_customers = df["Customer_ID"].nunique()
    total_quantity = df["Quantity"].sum()

    avg_order_value = total_sales / total_orders if total_orders else 0
    profit_margin = (total_profit / total_sales * 100) if total_sales else 0

    # KPI Cards
    st.header("📊 Key Performance Indicators")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="💰 Total Sales",
            value=f"${total_sales:,.2f}"
        )

    with col2:
        st.metric(
            label="📦 Total Orders",
            value=f"{total_orders:,}"
        )

    with col3:
        st.metric(
            label="👥 Customers",
            value=f"{total_customers:,}"
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            label="📈 Total Profit",
            value=f"${total_profit:,.2f}"
        )

    with col5:
        st.metric(
            label="🛒 Avg Order Value",
            value=f"${avg_order_value:,.2f}"
        )

    with col6:
        st.metric(
            label="📊 Profit Margin",
            value=f"{profit_margin:.2f}%"
        )

    # Additional Analysis
    st.subheader("Sales Summary")

    summary = pd.DataFrame({
        "Metric": [
            "Total Sales",
            "Total Profit",
            "Total Orders",
            "Total Quantity Sold",
            "Average Order Value",
            "Profit Margin (%)"
        ],
        "Value": [
            total_sales,
            total_profit,
            total_orders,
            total_quantity,
            avg_order_value,
            profit_margin
        ]
    })

    st.dataframe(summary, use_container_width=True)

else:
    st.info("Please upload a sales dataset CSV file.")