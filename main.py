from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv

load_dotenv()

# Define Agents
researcher = Agent(
    role="Tech Researcher",
    goal="Find recent developments in AI agents",
    backstory="An expert in exploring the web for up-to-date tech news",
    verbose=True
)

writer = Agent(
    role="Tech Blogger",
    goal="Write engaging blog posts on new AI trends",
    backstory="Skilled at writing clear and concise content for non-experts",
    verbose=True
)

# Define Tasks
task1 = Task(
    description="Find the latest trends in AI agent systems like CrewAI or AutoGPT.",
    expected_output="List of 3-5 recent developments in bullet points.",
    agent=researcher
)

task2 = Task(
    description="Write a short blog post summarizing the trends.",
    expected_output="A 2-paragraph blog post suitable for Medium.",
    agent=writer,
    context=[task1]
)

# Define Crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True
)

# Execute
output = crew.kickoff()
print("\nFinal Blog Post:\n", output)
