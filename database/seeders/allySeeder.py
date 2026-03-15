import os
from sqlmodel import Session,select
from database.datatables import Ally
from dotenv import load_dotenv

def seed_ally(session:Session):
    existing = session.exec(select(Ally)).first()
    if existing:
        return
    load_dotenv()
    imageurl = os.environ["PUBLIC_URL"] + "/ally-picture"

    ally=[
        Ally(
            name="DATUX PERÚ",
            url="https://www.datuxonline.com/",
            image_url=imageurl + "/al-datuxpe.png",
            is_active=True,
        ),
        Ally(
            name="Fundación WE",
            url="https://we-educacion.com/fundacion-we",
            image_url=imageurl + "/al-fundacion-we.png",
            is_active=True,
        ),
        Ally(
            name="ITNOVA PLUS",
            url="https://itnovaplus.com/",
            image_url=imageurl + "/al-itnova.png",
            is_active=True,
        ),
        Ally(
            name="PROJECT NOW",
            url="https://www.facebook.com/academiaprojectnow/",
            image_url=imageurl + "/al-project-now.png",
            is_active=True,
        ),
        Ally(
            name="Genialmente",
            url="https://www.facebook.com/p/GenialMente-61555492632966/",
            image_url=imageurl + "/al-genialmente.png",
            is_active=True,
        ),
        Ally(
            name="GESCONVIAL",
            url="https://gesconvial.com.pe/",
            image_url=imageurl + "/al-gesconvial.png",
            is_active=True,
        ),
        Ally(
            name="LABORAL AI.",
            url="https://www.laboral.ai/",
            image_url=imageurl + "/al-laboral-ai.png",
            is_active=True,
        ),
        Ally(
            name="Good Finances",
            url="https://goodfinanceacademy.com/",
            image_url=imageurl + "/al-goodfinance.jpeg",
            is_active=True,
        ),
        Ally(
            name="UBBICUO",
            url="https://ubbicuo.com/",
            image_url=None,
            is_active=False,
        ),
    ]
    session.add_all(ally)
    session.commit()
    print("✅ Seeder ejecutado correctamente")