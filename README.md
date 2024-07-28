# LLM_ice_breaker
Welcome to the **LLM_Ice_Breaker** repository! This project serves as a learning and experimentation platform for exploring the capabilities and integrations of Large Language Models (LLMs). Here, you will find an app that leverages various tools and techniques to demonstrate the potential of LLMs, including the use of LangChain, agents, third-party integrations, and LangSmith.

## Features
- **LangChain**:
  - **Agents**: Implement agents that can perform tasks autonomously by interacting with various **tools** and APIs.
  - **Third-Party Integrations**: Usage of Tivaly and ProxyCurl to extract LinkedIn information
- **LangSmith**: Explored the features and applications of LangSmith in enhancing LLM production usability.

## Setup
To get started with the **LLM_Ice_Breaker** app, follow these steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/HantsonAlec/LLM_ice_breaker.git
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create .env file**:
   ```
    OPENAI_API_KEY='XXXXX' (Optional, current implementation uses open-source models)
    PROXYCURL_API_KEY ='XXXXX'
    TAVILY_API_KEY ='XXXXX'
   ```

4. **Run the app**:
   ```bash
   python app.py
   ```
