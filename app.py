import streamlit as st
from crawler import get_links
import json
import csv


def save_as_json(links, filename):
    with open(filename, "w") as f:
        json.dump(links, f, indent=4)

def save_as_csv(links, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Link"])
        writer.writerows([[link] for link in links])

def main():
    st.title("YouTube Channel Scraper")

    
    search_term = st.text_input("Enter search term:")
    max_results = st.number_input("Enter maximum number of results:", min_value=1, value=10)

    if st.button("Scrape"):
        
        links = get_links(search_term, max_results)

        
        json_filename = f"{search_term}_results.json"
        save_as_json(links, json_filename)
        st.markdown(f"Download [JSON](/{json_filename})")

        
        csv_filename = f"{search_term}_results.csv"
        save_as_csv(links, csv_filename)
        st.markdown(f"Download [CSV](/{csv_filename})")

if __name__ == "__main__":
    main()
