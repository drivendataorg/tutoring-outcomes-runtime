from pathlib import Path


class TutoringOutcomesModel:
    def __init__(self, model_val):
        self.model_val = model_val

    @classmethod
    def load(cls, model_path):
        with Path(model_path).open("r") as f:
            model_val = f.read().strip()
        return cls(model_val)

    def predict(self):
        # Placeholder for prediction logic
        return self.model_val
