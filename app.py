import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from agent_core import run_agent

if __name__ == "__main__":
    topic = input("Enter your topic: ")
    run_agent(topic)