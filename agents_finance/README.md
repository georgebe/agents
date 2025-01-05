# Finance Agent with phidata

## Overview
This project implements a finance agent using phidata and YFinanceTools to interact with financial data. The agent is capable of retrieving and analyzing stock market information using the Yahoo Finance API.

## Features
- Stock price information retrieval
- Analyst recommendations
- Company information
- Company news updates
- Data displayed in formatted tables

## Prerequisites
- Python 3.x
- phidata library
- OpenAI API key
- dotenv package for environment variable management
- yfinance

## Installation
1. Clone the repository
2. Install required dependencies:
```bash
pip install phi-agent
pip install python-dotenv
```
3. Create a `.env` file in the project root and add your OpenAI API key:
```plaintext
OPENAI_API_KEY=your_api_key_here
```

## Capabilities
The agent can:
- Fetch real-time stock prices
- Get analyst recommendations
- Retrieve company information
- Access latest company news
- Display data in formatted tables

## Example Output
When requesting analyst recommendations for a stock (e.g., NVDA), the agent provides:
- Overall market sentiment
- Buy/Sell recommendations count
- Price targets
- Growth trajectory analysis
- Disclaimer about market recommendations

## Note
This implementation is based on the phidata documentation example and serves as a demonstration of using AI agents with financial tools. Always perform your own due diligence before making any investment decisions based on this information.

## Contributing
Feel free to fork this repository and submit pull requests for any improvements.

## License
Open Source
