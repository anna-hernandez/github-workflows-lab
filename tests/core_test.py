import os

EXPECTED_INPUT_BUCKET = "gs://lab-0"


def test_config():
    input_bucket = os.getenv("INPUT_GSC_SOURCE")
    assert input_bucket, "No input bucket specified"
    assert input_bucket == EXPECTED_INPUT_BUCKET
