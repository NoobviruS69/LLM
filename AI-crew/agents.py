from crewai import Agent
from tools import search_tool, alpha_vantage_tool, compliance_tool, client_interaction_tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode

data_collector = Agent(
    role='Data Collector',
    goal='Gather financial data from multiple sources',
    verbose=True,
    memory=True,
    backstory='Specialized in collecting up-to-date financial data for analysis.',
    tools=[search_tool , alpha_vantage_tool],  # Added alpha vantage tool for market news & sentiment
    llm=llm,
    allow_delegation=True
)

# Analyst Agent
analyst = Agent(
    role='Financial Analyst',
    goal='Analyze financial data to generate insights',
    verbose=True,
    memory=True,
    backstory='Experienced in financial data analysis and trend identification.',
    tools=[],  # Custom analytical tools can be added here
    llm=llm,
    allow_delegation=False
)

# Advisory Agent
advisory = Agent(
    role='Financial Advisor',
    goal='Provide tailored financial advice based on analysis',
    verbose=True,
    memory=True,
    backstory='Expert in creating personalized financial strategies.',
    tools=[],  # Custom advisory tools can be added here
    llm=llm,
    allow_delegation=False
)

# Compliance Agent
compliance = Agent(
    role='Compliance Officer',
    goal='Ensure compliance with financial regulations',
    verbose=True,
    memory=True,
    backstory='Ensures all financial activities are compliant with regulations.',
    tools=[compliance_tool],  # Custom compliance tools can be added here
    llm=llm,
    allow_delegation=False
)

# Client Interaction Agent
client_interaction = Agent(
    role='Client Interaction Specialist',
    goal='Interact with clients to gather requirements and provide reports',
    verbose=True,
    memory=True,
    backstory='Skilled in understanding client needs and delivering comprehensive reports.',
    tools=[client_interaction_tool],  # CRM and interaction tools can be added here
    llm=llm,
    allow_delegation=False
)

