import os
from sqlmodel import Session, select
from database.datatables import Project
from dotenv import load_dotenv

def seed_projects(session: Session):
    # Check if there are any projects in the database
    existing = session.exec(select(Project)).first()
    if existing:
        return
    
    load_dotenv()
    imageurl = os.environ["PUBLIC_URL"] + "/project-pictures"

    projects = [
        Project(
            title="SEDITALKS 2.0",
            description="SEDITALKS es un evento que ofrece conferencias estilo TED, lideradas por profesionales con amplia experiencia en gestión organizacional. El evento busca brindar a los asistentes conocimientos aplicables, oportunidades de networking, acceso a material exclusivo y dinámicas que fomentan el crecimiento profesional.",
            release_date="2025-05-18",
            season="2025-I",
            image_url=imageurl + "/pj-seditalks2-0.png"
        ),
        Project(
            title="SediPatitas",
            description="Sedipatitas Felices es una iniciativa impulsada por la organización estudiantil SediproUNT, con el objetivo de brindar ayuda a animalitos en situación de abandono. Actualmente, un pequeño refugio cuida con amor a muchos perritos, y gatitos. Nuestro proyecto busca apoyarlos a través de la recolección de alimentos, medicinas y donaciones económicas. ",
            release_date="2025-05-18",
            season="2025-I",
            image_url=imageurl + "/pj-sedipatitas.jpeg"
        ),
        Project(
            title="Amigos de la Tecnología",
            description="Amigos de la Tecnologia consiste en una serie de sesiones formativas dirigidas a adultos, enfocadas en el uso de teléfonos inteligentes. Es conveniente utilizar un método de enseñanza práctico y adaptado al ritmo de aprendizaje de los participantes. Las sesiones se podrían realizar de manera presencial en un espacio accesible para todos los participantes. Se abordan temas específicos: realizar llamadas, escribir mensajes de texto y el uso de WhatsApp.",
            release_date="2025-05-18",
            season="2025-I",
            image_url=imageurl + "/pj-tecnoamigos.png"
        ),
        Project(
            title="NAVISEDIPRO 9.0",
            description="NAVISEDIPRO, proyecto emblema de SEDIPRO UNT, el cual tiene como objetivo llevar alegría y entusiasmo de la navidad a los niños y niñas mas necesitados, que carecen de recursos económicos y de actividades recreativas. Recordemos que siempre podemos hacer la diferencia en los corazones de los más pequeños.",
            release_date="2025-10-22",
            season="2025-II",
            image_url=imageurl + "/pj-navisedipro2025.jpeg"
        ),
        Project(
            title="Gestión de Proyectos 360",
            description="El proyecto “Gestión de Proyectos 360” busca capacitar a los estudiantes universitarios en herramientas, metodologías y habilidades clave para gestionar y liderar proyectos de manera integral.",
            release_date="2025-10-22",
            season="2025-II",
            image_url=imageurl + "/pj-gestion-proyecto360.png"
        ),
        Project(
            title="CHEQUEATE UNT",
            description="Chequéate UNT” es una iniciativa de bienestar integral para la comunidad universitaria de la Universidad Nacional de Trujillo. El proyecto se desarrollará mediante cuatro espacios temáticos instalados en el campus, donde se brindarán gratuitamente chequeos de salud, orientación preventiva y actividades de autocuidado, promoviendo hábitos saludables y una cultura de bienestar físico, mental y emocional.",
            release_date="2025-10-22",
            season="2025-II",
            image_url=imageurl + "/pj-chequeateUNT.jpeg"
        ),
        Project(
            title="Proyectando Vocaciones 3.0",
            description="Proyectando Vocaciones 3.0 es un proyecto de SEDIPRO UNT que orienta a estudiantes preuniversitarios de colegios y academias de La Libertad para que tomen una decisión informada sobre su futura carrera en la Universidad Nacional de Trujillo.",
            release_date="2026-02-28",
            season="2026-I",
            image_url=imageurl + "/pj-proyectandov.png"
        ),
    ]

    session.add_all(projects)
    session.commit()