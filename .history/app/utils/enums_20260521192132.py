from enum import Enum


class UserRole(str, Enum):

    OWNER = "OWNER"

    ADMIN = "ADMIN"

    ANALYST = "ANALYST"

    VIEWER = "VIEWER"


class WidgetType(str, Enum):

    LINE_CHART = "LINE_CHART"

    BAR_CHART = "BAR_CHART"

    PIE_CHART = "PIE_CHART"

    KPI_CARD = "KPI_CARD"

    TABLE = "TABLE"


class AlertStatus(str, Enum):

    ACTIVE = "ACTIVE"

    TRIGGERED = "TRIGGERED"

    RESOLVED = "RESOLVED"

    MUTED = "MUTED"


class ReportFrequency(str, Enum):

    DAILY = "DAILY"

    WEEKLY = "WEEKLY"

    MONTHLY = "MONTHLY"


class EventSource(str, Enum):

    API = "API"

    CSV = "CSV"

    WEBHOOK = "WEBHOOK"