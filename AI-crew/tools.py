import requests
from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


from crewai_tools import SerperDevTool

# Initialize tools

# Tool for internet searching capabilities
search_tool = SerperDevTool()



# Custom tools for financial analysis and compliance checks can be added here
# Example: Alpha Vantage tool for stock data


class AlphaVantageTool:
    def __init__(self):
        self.api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        self.base_url = "https://www.alphavantage.co/query"

    def get_market_news_sentiment(self, keywords):
        function = "NEWS_SENTIMENT"
        url = f"{self.base_url}?function={function}&keywords={keywords}&apikey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch data. Status code: {response.status_code}"}

alpha_vantage_tool = AlphaVantageTool()

# Example: Custom compliance tool
class ComplianceTool:
    name: str = "Compliance Tool"
    description: str = "Ensures financial advice complies with regulations."

    def _run(self, advice):
        # Placeholder implementation for compliance check
        return "Compliance check passed"

compliance_tool = ComplianceTool()

# Example: Custom client interaction tool
class ClientInteractionTool:
    name: str = "Client Interaction Tool"
    description: str = "Facilitates interaction with clients."

    def _run(self, client_data):
        # Placeholder implementation for client interaction
        return "Client interaction successful"

client_interaction_tool = ClientInteractionTool()

# Export tools to be used by agents
tools = {
    'search_tool': search_tool,
    'alpha_vantage_tool': alpha_vantage_tool,
    'compliance_tool': compliance_tool,
    'client_interaction_tool': client_interaction_tool
}
