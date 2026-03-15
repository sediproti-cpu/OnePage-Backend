from sqlmodel import Session,select
from database.datatables import Event
def seed_events(session: Session):
    # Check if there are any students in the database
    existing = session.exec(select(Event)).first()

    if existing:
        return
    events = [
        Event(
            title="Elecciones 2026",
            event_date="2026-03-15",
            url_event=None,
        ),
        Event(
            title="Inducciones Ing Civil",
            event_date="2026-03-21",
            url_event="",
        ),
        Event(
            title="Inducciones Ing Ambiental",
            event_date="2026-03-22",
            url_event=None,
        ),
        Event(
            title="Inducciones Derecho",
            event_date="2026-03-23",
            url_event=None,
        ),
        Event(
            title="Inducciones Administración",
            event_date="2026-03-25",
            url_event=None,
        ),
        Event(
            title="Convocatoria 2026",
            event_date="2026-04-04",
            url_event=None,
        )
    ]
    session.add_all(events)
    session.commit()
    print("✅ Seeder ejecutado correctamente")