from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool

from market_researcher_crew.tools.custom_tool import MyCustomTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
selenium_tool = SeleniumScrapingTool()
custom_tool = MyCustomTool()


@CrewBase
class MarketResearcherCrew():
    """MarketResearcherCrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    agents: List[BaseAgent]
    tasks: List[Task]

    # ------------ Agents -------------------

    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['market_research_specialist'],  # type: ignore[index]
            tools=[search_tool, scrape_tool, selenium_tool],
            verbose=True
        )

    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['competitive_intelligence_analyst'],  # type: ignore[index]
            tools=[search_tool, scrape_tool, selenium_tool, custom_tool],
            verbose=True
        )

    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['customer_insights_researcher'],  # type: ignore[index]
            tools=[search_tool, scrape_tool, selenium_tool],
            verbose=True
        )

    @agent
    def product_strategy_adviser(self) -> Agent:
        return Agent(
            config=self.agents_config['product_strategy_adviser'],  # type: ignore[index]
            tools=[search_tool, scrape_tool],
            verbose=True
        )

    @agent
    def senior_business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_business_analyst'],  # type: ignore[index]
            tools=[search_tool, scrape_tool, custom_tool],
            verbose=True
        )

    # ------------ Tasks -------------------

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_research_task'],          # type: ignore[index]
            agent=self.market_research_specialist()                    # ✅ agent= required (not defined in YAML)
        )

    @task
    def competitive_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config['competitive_intelligence_task'], # type: ignore[index]
            agent=self.competitive_intelligence_analyst()
        )

    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['customer_insights_task'],        # type: ignore[index]
            agent=self.customer_insights_researcher()
        )

    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_strategy_task'],         # type: ignore[index]
            agent=self.product_strategy_adviser()
        )

    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_analyst_task'],         # type: ignore[index]
            agent=self.senior_business_analyst()
        )

    # ------------ Crew -------------------

    @crew
    def crew(self) -> Crew:
        """Creates the MarketResearcherCrew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )