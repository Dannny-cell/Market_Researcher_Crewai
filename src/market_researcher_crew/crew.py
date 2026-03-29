from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MarketResearcherCrew():
    """MarketResearcherCrew crew"""

    # CrewAI automatically loads these when using @CrewBase
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ------------ Agents -------------------

    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['market_research_specialist'],
            verbose=True
        )

    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['competitive_intelligence_analyst'],
            verbose=True
        )

    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['customer_insights_researcher'],
            verbose=True
        )

    @agent
    def product_strategy_adviser(self) -> Agent:
        return Agent(
            config=self.agents_config['product_strategy_adviser'],
            verbose=True
        )

    @agent
    def senior_business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_business_analyst'],
            verbose=True
        )

    # ------------ Tasks -------------------

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_research_task']
        )

    @task
    def competitive_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config['competitive_intelligence_task']
        )

    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['customer_insights_task']
        )

    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_strategy_task']
        )

    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_analyst_task']
        )

    # ------------ Crew -------------------

    @crew
    def crew(self) -> Crew:
        """Creates the MarketResearcherCrew"""
        return Crew(
            agents=self.agents, # Automatically gathered by the @agent decorators
            tasks=self.tasks,   # Automatically gathered by the @task decorators
            process=Process.sequential, # You can change this to Process.hierarchical if needed
            verbose=True,
        )