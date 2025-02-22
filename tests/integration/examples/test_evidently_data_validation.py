#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

import pytest

from tests.integration.examples.utils import run_example
from zenml.post_execution.pipeline import get_pipeline


def test_example(request: pytest.FixtureRequest) -> None:
    """Runs the evidently_data_validation example."""

    with run_example(
        request=request,
        name="evidently_data_validation",
        pipelines={"text_data_report_test_pipeline": (1, 5)},
    ) as (example, runs):

        pipeline = get_pipeline("text_data_report_test_pipeline")
        assert pipeline

        # Analyzer step should have output missing values
        text_analyzer_step = runs["text_data_report_test_pipeline"][
            0
        ].get_step(step="text_analyzer")
        output = text_analyzer_step.outputs["ref_missing_values"].read()
        assert isinstance(output, int)
