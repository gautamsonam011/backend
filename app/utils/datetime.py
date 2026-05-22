from datetime import datetime
from datetime import timezone
from datetime import timedelta


def utc_now():

    return datetime.now(
        timezone.utc
    )


def format_datetime(
    dt: datetime
):

    return dt.strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def get_last_hours(
    hours: int
):

    return utc_now() - timedelta(
        hours=hours
    )


def get_last_days(
    days: int
):

    return utc_now() - timedelta(
        days=days
    )


def datetime_to_timestamp(
    dt: datetime
):

    return int(dt.timestamp())