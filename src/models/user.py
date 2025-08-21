from enum import StrEnum
from typing import Annotated
import datetime
from sqlalchemy import ForeignKey, text, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base



intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
                        server_default=text("TIMEZONE('utc', now())"),
                        onupdate=datetime.datetime.utcnow)]



class UserRoles(StrEnum):
    user = "user"
    admin = "admin"



class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    role: Mapped[StrEnum] = mapped_column(Enum(UserRoles), nullable=False, default=UserRoles.user)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]




class UserProgressOrm(Base):
    __tablename__ = "user_progress"

    id: Mapped[intpk]
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user_points: Mapped[int] = mapped_column(default=0)