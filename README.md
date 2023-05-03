# Playstore Review Analyzer

This is a Streamlit app that scrapes Playstore reviews and analyzes them, with topic modeling Aspect-based sentiment analysis.

## Getting Started

## Usage

Once you've launched the app, you can enter the name of an app in the search box and click the "Search" button to scrape its reviews. The app will display the reviews along with their topic labels, which are generated using Bertopic.

You can also adjust the number of topics to generate using the slider on the sidebar. The app will re-cluster the reviews based on the new number of topics and update the display accordingly.

## Dependencies

- [Streamlit](https://www.streamlit.io/)
- [Bertopic](https://github.com/MaartenGr/BERTopic)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/en/master/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Acknowledgements

This app was created as part of a data science project by [Your Name], using Bertopic and other open-source packages.
