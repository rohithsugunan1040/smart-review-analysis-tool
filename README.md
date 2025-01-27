# Smart Review Analysis Tool

## Overview
The Smart Review Analysis Tool is designed to help users analyze product reviews by scraping, processing, and performing sentiment analysis on the collected data. This tool aims to provide insights into customer sentiments, helping businesses and consumers make informed decisions.

## Directory Structure
```
smart-review-analysis-tool/
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── sentiment_analysis.py
│   ├── review_scraper.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_data_processing.py
│   ├── test_sentiment_analysis.py
│   ├── test_review_scraper.py
│   └── test_utils.py
├── requirements.txt
└── README.md
```

## Installation
To install the required libraries, run the following command:

```
pip install -r requirements.txt
```

## Usage
1. **Scraping Reviews**: Use the `fetch_reviews(product_link)` function from `review_scraper.py` to collect reviews from a specified product link.
2. **Processing Reviews**: Clean the collected reviews using the `clean_reviews(reviews)` function from `data_processing.py`.
3. **Sentiment Analysis**: Analyze the sentiment of the cleaned reviews with the `analyze_sentiment(reviews)` function from `sentiment_analysis.py`.

## Running Tests
To ensure the functionality of the tool, run the unit tests located in the `tests` directory. You can use a testing framework like `pytest`:

```
pytest tests/
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.