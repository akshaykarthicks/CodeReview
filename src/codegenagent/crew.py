from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Codegenagent():
    """Codegenagent crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'



    @agent
    def  code_explainer(self) -> Agent:
        return Agent(
            config=self.agents_config['code_explainer'], # type: ignore[index]
            verbose=True
        )
       
    @task
    def explain_generated_code(self) -> Task:
        return Task(
            config=self.tasks_config['explain_generated_code'], # type: ignore[index]
            agent=self.code_explainer(),
            verbose=True,
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Codegenagent crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

