from datetime import datetime
from zoneinfo import ZoneInfo

from pydantic import BaseSettings, Field

class ClockSettings(BaseSettings):
    time_zone: ZoneInfo = Field(default=ZoneInfo("UTC"))


settings = ClockSettings()


class Clock:
    @staticmethod
    def now():
        return datetime.now(tz=settings.time_zone)
