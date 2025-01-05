# AI Vacation Planning Assistant

An intelligent vacation planning system powered by AI that helps manage and process employee vacation requests. This system uses OpenAI's language models to understand and process vacation-related queries naturally.

## Overview

The AI Vacation Planning Assistant is built using Python and leverages the phi.agent framework along with OpenAI's language models to provide an interactive interface for vacation management. The system can check available vacation days and process vacation requests through natural language interactions.

## Features

- Natural language processing for vacation requests
- Real-time vacation availability checking
- Automated vacation day reservation
- Interactive conversation-based interface
- Persistent conversation history
- Integrated with OpenAI's language models

## Prerequisites

- Python 3.x
- phi.agent package
- OpenAI API key
- dotenv package for environment variable management

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
## Project Structure

```plaintext
├── hrAgent.py           # Main agent script
├── VacationTools.py    # Vacation management tools
├── initialize.py       # Initialization script
└── .env               # Environment variables
```

## Example Queries
1. "How much vacation does employee_id 1 have available?"
2. "Please reserve one day of time off, June 1 2024"
3. "Show my remaining vacation days"
4. "Book vacation from October 1 to October 15"

## Error Handling
The system includes error handling for:

1. Invalid employee IDs
2. Insufficient vacation days
3. Date format validation
4. API connection issues
5. Authentication errors

## Configuration
The system uses environment variables for configuration:

OPENAI_API_KEY: Your OpenAI API key

Additional configuration can be set in the initialize.py file

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
Open Source

## Support
For support, please open an issue in the repository or contact the project maintainers.

## Acknowledgments
Built with phi.agent framework
Powered by OpenAI's language models
