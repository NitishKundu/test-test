from agency_swarm.agents import Agent
from typing import Union


class Copywriter_test(Agent):
    def __init__(self):
        super().__init__(
            name="Copywriter",
            description="The Copywriter Agent is responsible for creating clear and persuasive content based on the templaate given and research provided, specializing in health and wellness writing.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            # max_prompt_tokens=25000,
            model="gpt-4o-2024-11-20"
        )
        
    def response_validator(self, message):
        return message