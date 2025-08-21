
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated

from src.db.database import Base



intpk = Annotated[int, mapped_column(primary_key=True)]



class VideoOrm(Base):
    __tablename__ = "videos"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)