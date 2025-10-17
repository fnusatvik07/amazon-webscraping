import streamlit as st
from src.oxylabs_client import scrape_product_details

def render_header():
    st.title("Amazon Competitor Analysis- AI ")
    st.subheader("An AI-powered tool to compare Amazon products.")
    st.caption("Enter your product details below to get started.")


def render_inputs():
    asin=st.text_input("Enter the ASIN of the product:",placeholder="e.g. B08N5WRWNW")
    geo= st.text_input("ZIP/Postal Code:",placeholder="e.g. 10001")
    domain=st.selectbox("Domain:", [
        "com",
        "co.uk",
        "de",
        "fr",
        "jp",
        "ca",
        "it",
        "in",
    ])

    return asin.strip(), geo.strip(), domain


def main():
    st.set_page_config(page_title="Amazon Competitor Analysis- AI", layout="wide")
    render_header()
    asin, geo, domain = render_inputs()

    if st.button("Scrape Product ") and asin:
        with st.spinner("Fetching product data..."):
            product = scrape_product_details(asin, geo, domain)
        st.success("Scraping completed Successfully!")
        st.write(product)


if __name__ == "__main__":
    main()

