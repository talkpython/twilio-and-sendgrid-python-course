from pathlib import Path

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from db.base_class import SqlAlchemyBase

__factory = None


def global_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    # Make sure the working folder is there!
    path = Path(db_file).parent
    path.mkdir(parents=True, exist_ok=True)

    conn_str = 'sqlite:///' + db_file.strip()
    print("Connecting to DB with {}".format(conn_str))

    # Adding check_same_thread = False after the recording. This can be an issue about
    # creating / owner thread when cleaning up sessions, etc. This is a sqlite restriction
    # that we probably don't care about in this example.
    engine = sa.create_engine(conn_str,
                              echo=False,
                              connect_args={"check_same_thread": False})
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import db.__all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    # noinspection PyCallingNonCallable
    session: Session = __factory()
    session.expire_on_commit = False
    return session


class SessionContext:
    def __init__(self, commit_on_success=False):
        self.commit_on_success: bool = commit_on_success
        self.session: Session = create_session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_val and self.commit_on_success:
            self.session.commit()

        self.session.close()
