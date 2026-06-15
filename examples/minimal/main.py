# This is a minimal example of how to load the data and generate predictions for the test set.
# This example simply saves out the submission format as predictions,
# but demonstrates how to load in model assets and source code included in a submission
# To test this submission, run:
# $ `just pack-example minimal`
# $ `just test-submission`
from pathlib import Path

from loguru import logger
import pandas as pd

from src.model import TutoringOutcomesModel

DATA_DIR = Path("data")
SUBMISSION_PATH = Path("submission.csv")
SRC_ROOT = Path(__file__).parent.resolve()


def main() -> None:
    # Load data
    submission_format = pd.read_csv(DATA_DIR / "submission_format.csv")
    logger.info(f"Loaded submission_format.csv of shape {submission_format.shape}")

    features = pd.read_csv(DATA_DIR / "test_features.csv")
    logger.info(f"Loaded test_features.csv of shape {features.shape}")

    # Check that one transcript file exists
    example_session_id = features.iloc[0].session_id
    example_transcript_path = DATA_DIR / f"test_transcripts/{example_session_id}.csv"
    example_transcript = pd.read_csv(example_transcript_path)
    logger.info(
        f"Loaded an example transcript of shape {example_transcript.shape} from {example_transcript_path}"
    )

    # Demonstrate loading in a model
    model_path = SRC_ROOT / "model" / "model.txt"
    logger.info(f"Loading model from: {model_path}")
    model = TutoringOutcomesModel.load(model_path)

    # Generate predictions - placeholder that just saves out the submission format
    predictions = submission_format.copy()
    predictions.to_csv(SUBMISSION_PATH, index=False)
    logger.success(
        f"Predictions for {len(predictions):,} responses were written to {SUBMISSION_PATH}"
    )


if __name__ == "__main__":
    main()
