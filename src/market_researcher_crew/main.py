#!/usr/bin/env python
import sys
import warnings
import json
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

from market_researcher_crew.crew import MarketResearcherCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def get_inputs():
    """Helper to supply variables required by tasks.yaml"""
    return {
        'product_or_company_name': 'AutoAgentX',
        'target_market_or_industry': 'Autonomous AI Agents',
        'your_company_or_product_name': 'AutoAgentX',
        'target_customer_segment_or_use_case': 'Enterprise Engineering Teams',
        'industry_or_market_context': 'B2B Developer Tools',
        'product_name_or_category': 'AI Agent Orchestration Platform',
        'company_name_or_business_objectives': 'Capture 15% of the enterprise AI orchestration market in San Francisco and globally within 3 years'
    }

def run():
    """Run the crew."""
    try:
        MarketResearcherCrew().crew().kickoff(inputs=get_inputs())
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """Train the crew for a given number of iterations."""
    try:
        MarketResearcherCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=get_inputs())
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """Replay the crew execution from a specific task."""
    try:
        MarketResearcherCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """Test the crew execution and returns the results."""
    try:
        MarketResearcherCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=get_inputs())
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """Run the crew with trigger payload."""
    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")
    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = get_inputs()
    inputs["crewai_trigger_payload"] = trigger_payload

    try:
        return MarketResearcherCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")

if __name__ == "__main__":
    run()