from contextlib import contextmanager
from typing import ContextManager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app.core.settings import settings


Base = declarative_base()
engine = create_engine(settings.POSTGRES, echo=False)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


@contextmanager
def session_scope() -> ContextManager[Session]:
	session = DBSession()
	try:
		yield session
		session.commit()
	except Exception as e:
		session.rollback()
		raise e
	finally:
		session.close()
