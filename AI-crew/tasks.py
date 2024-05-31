from crewai import Task
from tools import tools
from agents import data_collector, analyst, advisory, compliance, client_interaction

# Data Collection Task
data_collection_task = Task(
    description='Gather financial data such as stock prices, company financials, and market trends.',
    expected_output='A dataset of collected financial data.',
    tools=[tools['search_tool'], tools['alpha_vantage_tool']],  # Added alpha vantage tool for market news & sentiment
    agent=data_collector
)

# Data Analysis Task
data_analysis_task = Task(
    description='Perform financial analysis including trend analysis, risk assessment, and portfolio analysis.',
    expected_output='An analysis report with insights and trends.',
    tools=[],  # Added CSV and PDF search tools for analysis
    agent=analyst
)

# Financial Advisory Task
financial_advisory_task = Task(
    description='Provide tailored financial advice and investment strategies based on the analysis.',
    expected_output='A detailed financial advice report.',
    tools=[],  # Advisory tools
    agent=advisory
)

# Compliance Check Task
compliance_check_task = Task(
    description='Ensure all financial advice complies with relevant regulations.',
    expected_output='A compliance report verifying regulatory adherence.',
    tools=[tools['compliance_tool']],  # Added compliance tool
    agent=compliance
)

# Client Interaction Task
client_interaction_task = Task(
    description='Interact with clients to gather requirements and provide the final report.',
    expected_output='A comprehensive client report.',
    tools=[tools['client_interaction_tool']],  # Added client interaction tool
    agent=client_interaction
)
