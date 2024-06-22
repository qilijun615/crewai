"""
Goal: Create a 7-day travel itinerary with detailed per-day plans, including budget, packing suggestions, and safety tips

Captain/Manager/Boss: Expert travel agent

Employees/Experts to hire: city selection expert, local tour guide
"""
import os

from dotenv import load_dotenv
from crewai import Agent
from textwrap import dedent
# from langchain.llms import OpenAI, Ollama
# from langchain_openai import ChatOpenAI
from langchain_community.llms import HuggingFaceHub


from triptools.calculator_tool import CalculationTool
from triptools.search_tools import SearchTools

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TripAgents:
    def __init__(self):
        # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # self.Ollama = Ollama(model="openhermes")
        self.HF=HuggingFaceHub(repo_id="HuggingFaceH4/zephyr-7b-beta",
                               huggingfacehub_api_token= os.environ["HUGGINGFACEHUB_API_TOKEN"],
                               task="text-generation")

    def expert_travel_agent(self):
        return Agent(
            role="Define agent 1 role here",
            backstory=dedent(f"""Expert in travel planning and logistics. 
                             I have decades of experience making travel itineraries"""),
            goal=dedent(f"""Create a 7-day travel itinerary with detailed per-day plans,
                        including budget, packing suggestions, and safety tips."""),
            tools=[SearchTools.search_internet, 
                   CalculationTool.calculate_budget],
            allow_delegation=False,
            verbose=True,
            llm=self.HF,
        )

    def city_selection_expert(self):
        return Agent(
            role="Citi Selecttion Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best cities based on weather, season, prices, and traveler interests"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.HF,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local TOur Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information"""),
            goal=dedent(f"""Privde the best insights about the selected city"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.HF,
        )
