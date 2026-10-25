"""Some text that could happen in training"""

from typing import Any


def describe_run(config: dict[str, Any], epochs: int) -> str:
    return "\n".join(
        [
            "DEMO Text",
            f"model={config['model']}",
            f"epochs={epochs}",
            f"batch_size={config['batch_size']}",
            f"dataset={config['dataset']}",
        ]
    )
