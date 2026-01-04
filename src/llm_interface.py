"""
llm_interface.py

Abstract LLM interface.
The architecture is intentionally API-agnostic.
"""

from abc import ABC, abstractmethod

class LLMInterface(ABC):

    @abstractmethod
    def generate_hypotheses(self, prompt, context=None):
        pass

    @abstractmethod
    def evaluate(self, hypothesis):
        pass
