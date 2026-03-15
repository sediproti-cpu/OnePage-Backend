import os
from sqlmodel import Session,select
from database.datatables import Achievement
from dotenv import load_dotenv

def seed_achievements(session: Session):
# Check if there are any students in the database
       existing = session.exec(select(Achievement)).first()

       if existing:
              return
       
       load_dotenv()
       imageurl = os.environ["PUBLIC_URL"] + "/achievement-picture"

       achievements = [
                     ###2020
                     Achievement(
                            title="1ER PUESTO PERUVIAN PROJECT MANAGEMENT CHAMPIONSHIP",
                            description="El PMC Perú es la versión nacional del campeonato de gestión de proyectos organizado por IPMA y su comunidad juvenil Young Crew. Reúne a equipos de estudiantes universitarios que compiten primero en una ronda online y luego en una final nacional resolviendo un caso práctico. El equipo ganador obtiene el pase para representar al país en la final internacional del IPMC, fortaleciendo sus habilidades, experiencia y proyección en la dirección de proyectos.",
                            publish_date="2020-11-24",
                            image_url=imageurl + "/ach-1.png",
                     ), 
                     Achievement(
                            title="3ER PUESTO INTERNATIONAL PROJECT MANAGEMENT CHAMPIONSHIP",
                            description="El IPMC en su edición Latinoamericana (PMC LatNet) es una competencia regional organizada por IPMA Young Crew que reúne a equipos universitarios de diversos países para evaluar sus competencias en dirección de proyectos. El torneo combina una fase teórica y una fase práctica basada en un caso de estudio complejo, replicando escenarios reales de gestión.",
                            publish_date="2020-10-01",
                            image_url=imageurl + "/ach-2.png",
                     ),
                     #2021 
                     Achievement(
                            title="1ER PUESTO: PERUVIAN PROJECT MANAGEMENT CHAMPIONSHIP",
                            description="El PMC Perú es la instancia nacional del certamen de gestión de proyectos promovido por IPMA y Young Crew. Participan equipos de estudiantes que primero afrontan una evaluación en línea y posteriormente una final presencial centrada en la solución de un caso aplicado. El conjunto que logra el mejor desempeño obtiene el derecho de representar al país en la etapa internacional del IPMC, potenciando su desarrollo profesional y su experiencia práctica en dirección de proyectos.",
                            publish_date="2021-10-02",
                            image_url=imageurl + "/ach-3.png",
                     ), 
                     Achievement(
                            title="1ER PUESTO: INTERNATIONAL PROJECT MANAGEMENT CHAMPIONSHIP",
                            description="La edición latinoamericana del IPMC, conocida como PMC LatNet, es un encuentro regional impulsado por IPMA Young Crew que convoca a equipos universitarios de distintos países para medir sus capacidades en gestión de proyectos. La competencia integra una prueba teórica y una resolución de caso de alta complejidad, diseñada para simular situaciones reales del entorno profesional.",
                            publish_date="2021-11-02",
                            image_url=imageurl + "/ach-4.png",
                     ), 
                     #2022
                     Achievement(
                            title="2DO PUESTO PM CHAMPIONSHIP",
                            description="Competencia nacional que evalúa las habilidades de gestión de proyectos de estudiantes universitarios mediante la resolución de casos reales y la aplicación de estándares internacionales. Reúne a los mejores equipos del país para demostrar excelencia técnica y estratégica en project managemen.",
                            publish_date="2022-10-09",
                            image_url=imageurl + "/ach-5.png",
                     ), 
                     Achievement(
                            title="3ER PUESTO CHANGEMAKERS STUDENTS",
                            description="Programa que promueve el liderazgo, la innovación y el impacto social en estudiantes, brindándoles herramientas para diseñar soluciones a problemas reales y desarrollar proyectos con enfoque transformador dentro de sus comunidades.",
                            #no es fecha real 
                            publish_date="2022-09-10",
                            image_url=imageurl + "/ach-6.png",
                     ), 
                     #2023
                     Achievement(
                            title="1ER PUESTO CONCEPMI 2023",
                            description="El Congreso Nacional de Comunidades Estudiantiles del PMI es un evento organizado por el Project Management Institute – Chapter Lima Perú, dirigido a estudiantes y jóvenes profesionales interesados en la gestión de proyectos. Promueve las buenas prácticas del PMBOK a través de charlas, talleres, concursos y espacios de networking. Haber obtenido el primer lugar en esta competencia representa un logro destacado y un reconocimiento nacional al desempeño y preparación de nuestra organización.",
                            publish_date="28/03/2023",
                            image_url=imageurl + "/ach-7.png",
                     ),
                     #2024
                     Achievement(
                            title="RECONOCIMIENTO DE LA MUNICIPALIDAD PROVINCIAL DE TRUJILLO COMO MEJOR VOLUNTARIADO UNIVERSITARIO 2024  CON EL PROYECTO “MIS AMIGOS LOS LIBROS”",
                            description="El Premio Provincial al Voluntariado reconoce a las organizaciones y personas que han destacado por su compromiso con el desarrollo, fortalecimiento y promoción del servicio de voluntariado en la ciudad de Trujillo. SEDIPRO UNT se presentó al  concurso con el proyecto: MIS AMIGOS LOS LIBROS iniciativa que buscó fortalecer la lectura infantil en más de 90 niños de 3er grado del colegio Liceo Trujillo, a través de un concurso de cuentos, full day de talleres lúdicos vivenciales y donando más de 100 libros a dicha institución educativa.",
                            publish_date="2024-12-14",
                            image_url=imageurl + "/ach-8.png",
                     ),
                     Achievement(
                            title="PROYECTANDO VOCACIONES 2.0 supera el récord histórico de SEDIPRO UNT alcanzando mayor nivel de participantes en la historia de la organización.",
                            description="Con más de 500 asistentes y 27 alianzas con centros de estudiantes y centros federados de la Universidad Nacional de Trujillo, Proyectando Vocaciones 2.0 se consolidó como un espacio de orientación para los jóvenes de nuestra región. Este proyecto consistió en brindar orientación vocacional a estudiantes de distintos colegios y academias de La Libertad, a través de una visita guiada por la UNT. Durante esta experiencia, los participantes también tuvieron la oportunidad de acceder a tres charlas de las carreras de su interés, permitiéndoles conocer más sobre cada profesión y así tomar una decisión informada sobre su futuro profesional.",
                            publish_date="2025-02-22",
                            image_url=imageurl + "/ach-9.png",
                     ),
                     Achievement(
                            title="ORGANIZADORES INTERNATIONAL PROJECT MANAGEMENT PERU 2024",
                            description="Participación como organizadores del International Project Management Perú 2024, evento orientado a promover el intercambio de conocimientos y experiencias en gestión de proyectos entre estudiantes y profesionales. La organización implicó la coordinación de actividades académicas, logística del evento y articulación con especialistas del sector, contribuyendo al fortalecimiento de redes profesionales y al desarrollo de competencias en project management.",
                            publish_date="2024-09-08",
                            image_url=imageurl + "/ach-10.png",
                     ),
                     Achievement(
                            title="3ER PUESTO NIVEL NACIONAL IPMC 2024",
                            description="Obtención del 3er puesto a nivel nacional en el IPMC 2024, competencia organizada por el Project Management Institute (PMI), que evalúa conocimientos y habilidades en gestión de proyectos, planificación estratégica y trabajo en equipo entre estudiantes de distintas universidades del país. Este logro destaca el desempeño académico y la capacidad de aplicar herramientas y metodologías del project management en contextos competitivos.",
                            publish_date="2024-09-08",
                            image_url=imageurl + "/ach-11.png",
                     ),
                     Achievement(
                            title="ORGANIZADORES CONGRESO NACIONAL DE CONEXIONES ESTUDIANTILES DEL PROJECT MANAGEMENT INSTITUTE (PMI)",
                            description="Organización y coordinación del Congreso Nacional de Conexiones Estudiantiles del Project Management Institute (PMI) 2024, impulsado por SEDIPRO UNT, orientado a fortalecer las redes académicas y profesionales entre estudiantes de distintas universidades del país. El evento promovió el intercambio de conocimientos en gestión de proyectos, liderazgo y desarrollo profesional mediante conferencias, espacios de networking y participación de especialistas del sector.",
                            publish_date="2024-12-01",
                            image_url=imageurl + "/ach-12.png",
                     ),
                     #2025
                     Achievement(
                            title="1ER PUESTO CONCEPMI 2025",
                            description="El congreso es un evento nacional que se realiza cada año y reúne a los estudiantes universitarios más comprometidos con la gestión de proyectos. Ofrece conferencias, talleres, competencias académicas, mentorías y espacios de networking con destacados profesionales que lideran la gestión de proyectos en el país. SEDIPRO UNT (Sección Estudiantil de Dirección de Proyectos de la Universidad Nacional de Trujillo) participó representando a la Universidad Nacional de Trujillo en la 5ta edición de este congreso que se realizó el 15 y 16 de noviembre del 2025.",
                            publish_date="2025-11-15",
                            image_url=imageurl + "/ach-13.png",
                     ),
                     Achievement(
                            title="RECONOCIMIENTO DE LA MUNICIPALIDAD PROVINCIAL DE TRUJILLO COMO MEJOR VOLUNTARIADO UNIVERSITARIO 2025  CON EL PROYECTO “AMIGOS DE LA TECNOLOGÍA”",
                            description="El Premio Provincial al Voluntariado reconoce a las organizaciones y personas que han destacado por su compromiso con el desarrollo, fortalecimiento y promoción del servicio de voluntariado en la ciudad de Trujillo. Este galardón valora las buenas prácticas implementadas en nuestra metrópoli y premia a quienes ejecutan proyectos que cumplen de manera sobresaliente los siguientes criterios: resultados de impacto, eficiencia en gestión de voluntarios, innovación, sostenibilidad, oportunidad de réplica y escalabilidad. SEDIPRO UNT se presentó al concurso con el proyecto: AMIGOS DE LA TECNOLOGÍCA iniciativa que buscó reducir la brecha digital en más de 40 adultos mayores, brindándoles capacitaciones presenciales en el uso de herramientas tecnológicas básicas en teléfonos inteligentes, redes sociales y servicios digitales.",
                            publish_date="29/11/2025",
                            image_url=imageurl + "/ach-14.png",
                     ),
                     Achievement(
                            title="3er PUESTO EN EL INTERNATIONAL PROJECT MANAGEMENT CHAMPIONSHIP (IPMC)   PERU 2025",
                            description="El International Project Management Championship (IPMC) es un concurso organizado por el International Project Management Association (IPMA), primera asociación mundial de gestión de proyectos, la cual promueve la competencia en dirección de proyectos, programas y portafolios para que los estudiantes prueben sus conocimientos de resolución mediante la realización de entregables de proyectos en entornos restantes.",
                            publish_date="15/11/2025",
                            image_url=imageurl + "/ach-15.png",
                     ),
                     Achievement(
                            title="DIRECTIVA 2025-2026 CONSIGUE OFICINA PARA SEDIPRO UNT DESPUÉS DE 12 AÑOS",
                            description="Gestión de la Directiva 2025 - 2026 de SEDIPRO UNT que logró la obtención de una oficina institucional para la asociación después de 12 años, fortaleciendo el espacio de trabajo y desarrollo de actividades académicas y organizacionales. La oficina se encuentra ubicada en el ex comedor universitario, en Calle Independencia N.° 162, Trujillo, dentro de las instalaciones de la Universidad Nacional de Trujillo, consolidando un hito importante para el crecimiento y la institucionalización de SEDIPRO.",
                            publish_date="2025-12-18",
                            image_url=imageurl + "/ach-16.png",
                     ),
                     Achievement(
                            title="EQUIPO MARKETING 2025 - 2026 CREA LA MASCOTA OFICIAL DE SEDIPRO UNT",
                            description="El equipo de marketing 2025 - 2026 de SEDIPRO UNT logró desarrollar la mascota oficial de la organización, denominada “HITO”, representada por un búho que simboliza la sabiduría, la visión estratégica y la toma de decisiones informadas. Su nombre hace referencia a los hitos (milestones) utilizados en la gestión de proyectos, reforzando la identidad institucional y el enfoque en project management de SEDIPRO dentro de la comunidad de la Universidad Nacional de Trujillo.",
                            publish_date="2026-01-24",
                            image_url=imageurl + "/ach-17.png",
                     ),
              ]
       session.add_all(achievements)
       session.commit()
       print("✅ Seeder ejecutado correctamente")