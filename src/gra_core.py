"""
gra_core.py

Zeroed Generalized Resonance Algorithm (GRA) core
with orthogonal auxiliary constraints and a minimum
uncertainty (Heisenberg-style) bound.
"""

class GRACore:
    def __init__(
        self,
        primary_objective,
        constraints=None,
        lambdas=None,
        min_uncertainty=1e-3,
    ):
        self.primary_objective = primary_objective
        self.constraints = constraints or []
        self.lambdas = lambdas or []
        self.min_uncertainty = min_uncertainty

    def loss(self, state):
        base = self.primary_objective(state)
        aux = sum(
            lam * c(state)
            for lam, c in zip(self.lambdas, self.constraints)
        )
        return base + aux + self.min_uncertainty
