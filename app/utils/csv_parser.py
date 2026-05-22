import csv
import json

from io import StringIO


def parse_csv_events(content: str):

    reader = csv.DictReader(
        StringIO(content)
    )

    events = []

    for row in reader:

        row["properties"] = json.loads(
            row["properties"]
        )

        events.append(row)

    return events