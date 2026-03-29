from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool

# Import your custom tool
from market_researcher_crew.tools.custom_tool import MyCustomTool

# Instantiate tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
selenium_tool = SeleniumScrapingTool()
custom_tool = MyCustomTool()

@CrewBase
class MarketResearcherCrew():
    """MarketResearcherCrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ------------ Agents -------------------

    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['market_research_specialist'],
            tools=[search_tool, scrape_tool, selenium_tool],
            verbose=True
        )

    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['competitive_intelligence_analyst'],
            tools=[search_tool, scrape_tool, selenium_tool, custom_tool],
            verbose=True
        )

    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['customer_insights_researcher'],
            tools=[search_tool, scrape_tool, selenium_tool],
            verbose=True
        )

    @agent
    def product_strategy_adviser(self) -> Agent:
        return Agent(
            config=self.agents_config['product_strategy_adviser'],
            tools=[search_tool, scrape_tool], 
            verbose=True
        )

    @agent
    def senior_business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_business_analyst'],
            tools=[search_tool, scrape_tool, custom_tool],
            verbose=True
        )

    # ------------ Tasks -------------------

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_research_task'],
            agent=self.market_research_specialist()
        )

    @task
    def competitive_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config['competitive_intelligence_task'],
            agent=self.competitive_intelligence_analyst()
        )

    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['customer_insights_task'],
            agent=self.customer_insights_researcher()
        )

    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_strategy_task'],
            agent=self.product_strategy_adviser()
        )

    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_analyst_task'],
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