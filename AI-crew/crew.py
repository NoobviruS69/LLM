from crewai import Crew,Process
from tasks import data_collection_task, data_analysis_task, financial_advisory_task, compliance_check_task, client_interaction_task
from agents import data_collector,analyst,advisory,compliance,client_interaction

## Forming the tech focused crew with some enhanced configuration
# Forming the financial advisory crew
financial_crew = Crew(
    agents=[data_collector, analyst, advisory, compliance, client_interaction],
    tasks=[data_collection_task, data_analysis_task, financial_advisory_task, compliance_check_task, client_interaction_task],
    process=Process.sequential  # Sequential task execution
)

# Kickoff the crew with client data
result = financial_crew.kickoff(inputs={'client_data': 'Client specific data here'})
print(result)

