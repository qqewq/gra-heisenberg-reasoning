"""
Illustrative reasoning example showing degeneracy.
"""

class DummyLLM:
    def generate_hypotheses(self, prompt, context=None):
        return [
            "Hypothesis A",
            "Hypothesis B",
            "Hypothesis C",
        ]

    def evaluate(self, hypothesis):
        return len(hypothesis)


if __name__ == "__main__":
    llm = DummyLLM()
    hyps = llm.generate_hypotheses("Explain symmetry")

    scored = [(h, llm.evaluate(h)) for h in hyps]
    print("Degenerate hypotheses:", scored)
