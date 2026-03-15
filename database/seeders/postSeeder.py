import os
from sqlmodel import Session,select
from database.datatables import Post
from dotenv import load_dotenv
def seed_posts(session: Session):
    # Check if there are any students in the database
    existing = session.exec(select(Post)).first()

    if existing:
        return
    load_dotenv()
    image_url = os.environ["PUBLIC_URL"] + "/post-picture"
    posts = [
        Post(
            title="GESCOVIAL Y SEDIPRO UNT",
            publishDate="2026-03-09",
            shortDescription="La alianza entre GESCONVIAL y SEDIPRO UNT",
            longDescription="La alianza entre GESCONVIAL y SEDIPRO UNT se renueva con el objetivo de fortalecer la formación de estudiantes y profesionales de Ingeniería y Arquitectura, ofreciendo capacitaciones especializadas y certificaciones respaldadas por el Colegio de Ingenieros del Perú, impulsando así el desarrollo del talento profesional.",
            imageUrl=image_url + "/ps-n1.png",
        ),
        Post(
            title="GENIALMENTE Y SEDIPRO UNT",
            publishDate="2026-03-06",
            shortDescription="La alianza entre GENIALMENTE y SEDIPRO UNT",
            longDescription="La alianza entre GENIALMENTE y SEDIPRO UNT se renueva para impulsar la transformación de personas, equipos y culturas a través de coaching, mentoring y desarrollo de marca personal, generando oportunidades que conectan el talento universitario con empresas y fomentan el crecimiento profesional.",
            imageUrl=image_url + "/ps-n2.png",
        ),
        Post(
            title="¡𝗬𝗮 𝘀𝗼𝗺𝗼𝘀 𝗺á𝘀 de 1K!",
            publishDate="2026-03-06",
            shortDescription="La comunidad de SEDIPRO UNT superó los 1,000 seguidores",
            longDescription="La comunidad de SEDIPRO UNT superó los 1,000 seguidores, consolidándose como un espacio en crecimiento para estudiantes interesados en la Dirección de Proyectos. Este logro refleja el compromiso y la participación activa de su comunidad, que impulsa la creación de oportunidades de aprendizaje, liderazgo y desarrollo profesional dentro de la Universidad Nacional de Trujillo. La organización reafirma así su propósito de seguir fortaleciendo el talento universitario y promoviendo la gestión de proyectos.",
            imageUrl=image_url + "/ps-n3.png",
        ),
        Post(
            title="Aniversario de la fundación de Trujillo",
            publishDate="2026-03-05",
            shortDescription="La familia de SEDIPRO UNT se unió a la celebración del aniversario de fundación de Trujillo",
            longDescription="La familia de SEDIPRO UNT se unió a la celebración del aniversario de fundación de Trujillo, rindiendo homenaje a su historia, cultura y legado como “Ciudad de la Primavera”, y reafirmando su compromiso de seguir contribuyendo al desarrollo y futuro de la ciudad mediante la formación y el impulso del talento universitario.",
            imageUrl=image_url + "/ps-n4.png",
        ),
        Post(
            title="Muchas gracias Colaboradores",
            publishDate="2026-03-04",
            shortDescription="Aliados que hicieron posible Proyectando Vocaciones 3.0 Desde SEDIPRO UNT",
            longDescription="Aliados que hicieron posible Proyectando Vocaciones 3.0 Desde SEDIPRO UNT expresamos nuestro agradecimiento a los centros estudiantiles, grupos de estudio y profesionales que contribuyeron al éxito de Proyectando Vocaciones 3.0. Su compromiso, dedicación y entusiasmo permitieron generar un espacio de aprendizaje, colaboración y crecimiento para la comunidad universitaria, fortaleciendo el desarrollo del talento y las oportunidades profesionales.",
            imageUrl=image_url + "/ps-n5.png",
        ),
    ]
    session.add_all(posts)
    session.commit()
    print("✅ Seeder ejecutado correctamente")