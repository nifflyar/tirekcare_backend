from enum import StrEnum
from typing import Annotated
import datetime
from sqlalchemy import text, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base



intpk = Annotated[int, mapped_column(primary_key=True)]




class TaskOrm(Base):
    __tablename__ = "tasks"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None]
    max_points: Mapped[int] = mapped_column(nullable=False)


