import streamlit as st
import pandas as pd
import os
import time
import atexit
from threading import Thread
from utils import read_domains
from spiders.products import ProductCrawler
from scrapy.crawler import CrawlerProcess

# Function to run the crawler
def run_crawler(domains):
    process = CrawlerProcess({
        'FEEDS': {
            'output.csv': {'format': 'csv', 'overwrite': True},
        },
        'LOG_LEVEL': 'INFO'
    })
    process.crawl(ProductCrawler, domains=domains)
    process.start()

# Function to start the crawler in a separate thread
def start_crawler(domains):
    thread = Thread(target=run_crawler, args=(domains,))
    thread.daemon = True
    thread.start()

# Initialize session state
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()
if 'crawling_started' not in st.session_state:
    st.session_state['crawling_started'] = False

# Streamlit App
st.title("Web Crawler App")

# File paths
input_file = 'domains.txt'
output_file = 'output.csv'

# Step 1: Input domains
st.header("Step 1: Input Domains")
domains = st.text_area("Enter a list of domains (one per line):")

if st.button("Start Crawling"):
    if domains.strip():
        # Write domains to a file for the crawler
        with open(input_file, 'w') as f:
            f.write(domains)
        st.success("Domains saved successfully!")

        # Start the crawler
        st.info("Starting crawler... This may take a while.")
        start_crawler(read_domains(input_file))
        st.session_state['crawling_started'] = True

        with st.spinner("Loading..."):
            time.sleep(15)  # Simulate a delay for the spinner
        st.success("Crawler started successfully! Refreshing table every 10 seconds.")
    else:
        st.warning("Please enter at least one domain.")

# Step 2: Display results
if st.session_state['crawling_started']:
    # Function to refresh the table
    def refresh_table():
        if os.path.exists(output_file):
            try:
                # Update session state with new data
                st.session_state['data'] = pd.read_csv(output_file)
            except pd.errors.EmptyDataError:
                st.warning("The output CSV is empty. Please wait for the crawler to finish.")
        else:
            st.warning("Output file not found. Please start the crawler.")

    # Display the table
    if not st.session_state['data'].empty:
        st.write(st.session_state['data'])
    else:
        st.warning("No data available yet.")

    # Set up auto-refresh every 10 seconds
    if st.button("Refresh Now"):
        refresh_table()
        st.rerun()

    if 'auto_refresh' not in st.session_state:
        st.session_state['auto_refresh'] = True

    if st.session_state['auto_refresh']:
        time.sleep(10)
        refresh_table()
        st.rerun()

# Cleanup: Delete output file when the app is closed
def delete_output_file():
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"{output_file} deleted successfully.")

# Register atexit function
atexit.register(delete_output_file)
