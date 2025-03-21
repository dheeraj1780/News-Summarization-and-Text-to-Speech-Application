import streamlit as st
from utils import fetch_news
# Streamlit Web App
st.title("News Summarization & Sentiment Analysis")
st.subheader("Enter a company name to fetch recent news articles")

company_list = ["Tesla", "Apple", "Google", "Amazon", "Microsoft"]  # Predefined options
default_company = company_list[0]

company_name = st.text_input("Enter Company Name:", default_company)
if st.button("Fetch News"):
    with st.spinner("Fetching news..."):
        news_articles = fetch_news(company_name)
        
        if not news_articles:
            st.warning("No news articles found.")
        else:
            for i, article in enumerate(news_articles, 1):
                st.markdown(f"### {i}. {article['title']}")
                st.write(f"**Summary:** {article['summary']}")
                st.write(f"**Sentiment:** {article['sentiment']}")
                st.write(f"**Source:** {article['source']}")
                st.write(f"**Timestamp:** {article['timestamp']}")
                st.write(f"**Key Topics:** {', '.join(article['topics'])}")  # Displaying extracted topics
                st.markdown(f"[Read More]({article['link']})")
                st.write("---")

st.write("Developed with ❤️ using Streamlit")
