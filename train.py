import argparse
from pathlib import Path

import yaml

from src.services.training import describe_run


def positive_integer(value: str) -> int:
    """Just some function"""
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("epochs must be an integer") from exc
    if number <= 0:
        raise argparse.ArgumentTypeError("epochs must be greater than zero")
    return number


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="configs/train.yaml")
    parser.add_argument("--epochs", type=positive_integer, default=None)
    args = parser.parse_args()

    try:
        with Path(args.config).open(encoding="utf-8") as stream:
            cfg = yaml.safe_load(stream)
    except (OSError, yaml.YAMLError) as exc:
        parser.error(f"cannot read configuration: {exc}")

    if not isinstance(cfg, dict):
        parser.error("configuration must contain key/value pairs")

    required = {"model", "epochs", "batch_size", "dataset"}
    missing = required - cfg.keys()
    if missing:
        parser.error(f"missing configuration keys: {', '.join(sorted(missing))}")

    # Explicit precedence: CLI value first, YAML default otherwise.
    epochs = args.epochs if args.epochs is not None else cfg["epochs"]
    if type(epochs) is not int or epochs <= 0:
        parser.error("effective epochs must be a positive integer")

    print(describe_run(cfg, epochs))


if __name__ == "__main__":
    main()
