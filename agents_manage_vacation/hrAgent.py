from phi.agent import Agent, AgentMemory
from phi.model.openai import OpenAIChat
from VacationTools import VacationTools
from dotenv import load_dotenv
from initialize import initialize

load_dotenv()

initialize()

hr_agent = Agent(
    role="You are a vacation planner",
    instructions=["You are a vacation planner that helps people plan their vacations"],
    tools=[VacationTools()],
    model=OpenAIChat(),
    add_history_to_messages=True,
    show_tool_calls=True
)

#hr_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)
hr_agent.print_response("How much vacation does employee_id 1 have available?", stream=True)
hr_agent.print_response("great. please reserve one day of time off, June 1 2024", stream=True)

hr_agent.
#hr_agent.print_response("now let me take the last 3 months of the year off as vacation, from Oct 1 2024 through Dec 31 2024", stream=True)