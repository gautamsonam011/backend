import csv

from io import StringIO


def parse_csv(
    file_content: bytes
):

    decoded = file_content.decode(
        "utf-8"
    )

    csv_file = StringIO(decoded)

    reader = csv.DictReader(csv_file)

    rows = []

    for row in reader:

        rows.append(row)

    return rows