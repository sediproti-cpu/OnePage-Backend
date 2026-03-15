import os
from sqlmodel import Session, select
from database.datatables import Student, InfoFellow, FellowArea, FellowRank
from dotenv import load_dotenv

def seed_students(session: Session):
        # Check if there are any students in the database
        existing = session.exec(select(Student)).first()

        if existing:
            return
        load_dotenv()

        profile_url = os.environ["PUBLIC_URL"] + "/profile-picture"

        students = [
            Student(
                firstName="Lucia",
                lastName="Amaya Caceda",
                middleName="de Fatima",
                studentCode="L4F1C",
                career="Ingeniería Industrial",
                urlLinked="https://www.linkedin.com/in/luc%C3%ADa-de-f%C3%A1tima-amaya-c%C3%A1ceda-473816303/",
                urlProfile=profile_url + "/pro-amaya-caceda.jpg"
            ),
            Student(
                firstName="Silvana",
                lastName="Pereda Llave",
                middleName="Valeria",
                studentCode="S23P12",
                career="Administración",
                urlLinked="https://www.linkedin.com/in/silvana-valeria-pereda-llave-05575b30a/",
                urlProfile=profile_url + "/pro-pereda-llave.jpg"
            ),
            Student(
                firstName="Marina",
                lastName="Gonzales Torres",
                middleName="Lizeth",
                studentCode="M12G21",
                career="Derecho",
                urlLinked="https://www.linkedin.com/in/marina-lizeth-gonzales-torres-40340a24a/",
                urlProfile=profile_url + "/pro-gonzales-torres.jpg"
            ),
            Student(
                firstName="Diego",
                lastName="Rodriguez Sabana",
                middleName="Jesus",
                studentCode="D10R20",
                career="Administración ",
                urlLinked="https://www.linkedin.com/in/diegoj-rodriguez/",
                urlProfile=profile_url + "/pro-rodriguez-sabana.jpg"
            ),
            Student(
                firstName="Angel",
                lastName="Iparraguirre Aguilar",
                middleName="",
                studentCode="A9A",
                career="Ingeniería Civil",
                urlLinked="https://www.linkedin.com/in/angel-iparraguirre-aguilar-02514b3a2/",
                urlProfile=profile_url + "/pro-iparraguirre-aguilar.jpg"
            ),
            Student(
                firstName="María",
                lastName="Herrera Cerquín",
                middleName="Fernanda de la Caridad",
                studentCode="M6D12C8C",
                career="Ingeniería Industrial",
                urlLinked="https://www.linkedin.com/in/maria-herrera-cerquin/",
                urlProfile=profile_url + "/pro-herrera-cerquin.jpg"
            ),
            Student(
                firstName="Christian",
                lastName="Morales Esquivel",
                middleName="Anthony",
                studentCode="C1M5",
                career="Ingeniería Informática",
                urlLinked="https://www.linkedin.com/in/cristian-morales-esquivel/",
                urlProfile=profile_url + "/pro-morales-esquivel.jpeg"
            ),
            Student(
                firstName="Sebastian",
                lastName="Facundo Reyes",
                middleName="Emanuel",
                studentCode="S5F19",
                career="Ingeniería Agroindustrial",
                urlProfile=None
            ),
            Student(
                firstName="Zulema",
                lastName="Valverde Zavaleta",
                middleName="Adeli",
                studentCode="Z1V27",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Ivanna",
                lastName="Vela Ocampo",
                middleName="Sofia",
                studentCode="I20V16",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Anderson",
                lastName="Saavedra Nolasco",
                middleName="Alexander",
                studentCode="A1S14",
                career="Ingeniería Civil",
                urlProfile=None
            ),
            Student(
                firstName="Cristhian",
                lastName="Sánchez Obeso",
                middleName="Luis David",
                studentCode="C12D20O",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Eleanor",
                lastName="Roca Mendoza",
                middleName="Marycielo",
                studentCode="E13R13",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Emilly",
                lastName="Zavaleta Chigne",
                middleName="Nicoll",
                studentCode="F14Z3",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Joaquin",
                lastName="Bocanegra Peláez",
                middleName="Adriano",
                studentCode="J1B17",
                career="Ingeniería Ambiental",
                urlProfile=None
            ),
            Student(
                firstName="Luis",
                lastName="Montoya Aguirre",
                middleName="Enrique",
                studentCode="L5M1",
                career="Educación Sec. Filosofía, psicología y CC.SS.",
                urlProfile=None
            ),
            Student(
                firstName="Valeria",
                lastName="Valderrama Muñoz",
                middleName="Angelie",
                studentCode="V1V13",
                career="Derecho",
                urlProfile=None
            ),
            Student(
                firstName="Ana",
                lastName="Segura Aredo",
                middleName="Nicoll",
                studentCode="A14S1",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Andrweeu",
                lastName="Urtecho Avila",
                middleName="Daniel",
                studentCode="A4U1",
                career="Ingeniería Ambiental",
                urlProfile=None
            ),
            Student(
                firstName="Corina",
                lastName="Sanchez Delgado",
                middleName="Marilu",
                studentCode="C13S4",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="José",
                lastName="Avila Santillan",
                middleName="Daniel",
                studentCode="J4A20",
                career="Ingeniería Civil",
                urlProfile=profile_url + "/pro-avila-santillan.jpg"
            ),
            Student(
                firstName="Lisseth",
                lastName="Chávez Rosales",
                middleName="Adelaida",
                studentCode="L1C19",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Mariann",
                lastName="Fernández Leyva",
                middleName="Estefany",
                studentCode="M5F12",
                career="Administración ",
                urlProfile=None
            ),
            Student(
                firstName="Michael",
                lastName="García García",
                middleName="Junior",
                studentCode="M10G7",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Nashaly",
                lastName="Alama Terrones",
                middleName="Nicolle",
                studentCode="N14A21",
                career="Ingeniería Ambiental",
                urlProfile=None
            ),
            Student(
                firstName="Renzo",
                lastName="Carrasco Lalangui",
                middleName="Georkael",
                studentCode="R7C12",
                career="Ingeniería Civil",
                urlProfile=None
            ),
            Student(
                firstName="Alisson",
                lastName="Pretell Canchas",
                middleName="Milagros",
                studentCode="A13P3M",
                career="Derecho",
                urlProfile=None
            ),
            Student(
                firstName="Dulce",
                lastName="Chavez Padilla",
                middleName="Geraldine",
                studentCode="D7C17",
                career="Ingeniería Industrial ",
                urlProfile=None
            ),
            Student(
                firstName="Elber",
                lastName="Pichén Zavaleta",
                middleName="Isaí",
                studentCode="E9P2",
                career="Ingeniería Civil",
                urlProfile=None
            ),
            Student(
                firstName="Cristhian",
                lastName="Campos Castro",
                middleName="Imanol",
                studentCode="C9C3",
                career="Administración",
                urlProfile=None


            ),
            Student(
                firstName="Sadhu",
                lastName="Rojas García",
                middleName="",
                studentCode="S19G",
                career="Ingeniería Informática ",
                urlProfile=None,
            ),
            Student(
                firstName="Paúl",
                lastName="Lazaro Solano",
                middleName="Jamir",
                studentCode="P10L20",
                career="Ingeniería Informática ",
                urlProfile=None,
            ),
            Student(
                firstName="Mirella",
                lastName="Gamboa Valderrama",
                middleName="Esteffany",
                studentCode="M5G23",
                career="Ingeniería Informática ",
                urlProfile=None,
            ),
            Student(
                firstName="Marco",
                lastName="Toledo Campos",
                middleName="Camilo",
                studentCode="M3T3",
                career="Ingeniería Informática ",
                urlProfile=None,
            ),
            Student(
                firstName="Luis",
                lastName="Morales Lino",
                middleName="Angel",
                studentCode="L1M12",
                career="Ingeniería Informática ",
                urlProfile=None,
            ),
            Student(
                firstName="Renato",
                lastName="Martinez Aguilar",
                middleName="Alexander",
                studentCode="R1M1",
                career="Ingeniería Informática",
                urlProfile=None,
            ),
            Student(
                firstName="Pablo",
                lastName="Sánchez Cabrera",
                middleName="César",
                studentCode="P3S3",
                career="Ingeniería Industrial",
                urlProfile=None,
            ),
            Student(
                firstName="Jhoanny",
                lastName="Vargas Ramos",
                middleName="Jheimilyn Xiomara",
                studentCode="J10X23R",
                career="Ingeniería Informática",
                urlProfile=None,
            ),
            Student(
                firstName="Elder",
                lastName="De la Cruz Calderón",
                middleName="Eli",
                studentCode="E5D12C3",
                career="Ingeniería Informática",
                urlProfile=profile_url + "/pro-delacruz-calderon.jpg",
            ),
            Student(
                firstName="Maria",
                lastName="Huaman Martinez",
                middleName="Celine",
                studentCode="M3H13",
                career="Ingeniería Metalúrgica",
                urlProfile=None
            ),
            Student(
                firstName="Aaron",
                lastName="Arteaga Rodriguez",
                middleName="Kaleb",
                studentCode="A11A19",
                career="Ingeniería Informática",
                urlProfile=None,
            ),
            Student(
                firstName="Jeoselyn",
                lastName="Espejo Rodríguez",
                middleName="Maribel",
                studentCode="J13E19",
                career="Ingeniería Ambiental",
                urlProfile=None
            ),
            Student(
                firstName="Ruben",
                lastName="Alcantara Toribio",
                middleName="Dario",
                studentCode="R4A21",
                career="Ingeniería Industrial",
                urlProfile=None,
            ),
            Student(
                firstName="Diego",
                lastName="Gutierrez Vásquez",
                middleName="Alonso",
                studentCode="D1G23",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Diego",
                lastName="Mostacero Lecca",
                middleName="Alejandro",
                studentCode="D1M12",
                career="Administración",
                urlProfile=None,
            ),
            Student(
                firstName="Dalery",
                lastName="Alayo Sifuentes",
                middleName="Nicoll",
                studentCode="D14AS",
                career="Ingeniería Civil",
                urlProfile=None
            ),
            Student(
                firstName="Angela",
                lastName="Loayza Gutierrez",
                middleName="Xiomara",
                studentCode="A25L7",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Abel",
                lastName="Pereda Cabanillas",
                middleName="Maximiliano",
                studentCode="A13P3H",
                career="Ingeniería Ambiental",
                urlProfile=profile_url + "/pro-pereda-cabanillas.jpg",
            ),
            Student(
                firstName="Daniel",
                lastName="Sanchez Cabrera",
                middleName="Angel",
                studentCode="D1S3",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Sebastian",
                lastName="Vásquez Estrada",
                middleName="Javier",
                studentCode="S10V5",
                career="Derecho",
                urlProfile=None,
            ),
            Student(
                firstName="Rodrigo",
                lastName="Quispe Cortijo",
                middleName="Alexander",
                studentCode="R1Q3",
                career="Ingeniería Industrial",
                urlProfile=None,
            ),
            Student(
                firstName="Ariana",
                lastName="Morales Ipanaqué",
                middleName="",
                studentCode="A13I",
                career="Administración",
                urlProfile=None,
            ),
            Student(
                firstName="Ghenary",
                lastName="Esquivel Davila",
                middleName="Tais",
                studentCode="G21E4",
                career="Ciencias de la Comunicación",
                urlProfile=None,
            ),
            Student(
                firstName="Anderson",
                lastName="Otiniano Morales",
                middleName="Abat",
                studentCode="A1O13",
                career="Ingeniería Química",
                urlProfile=None,
            ),
            Student(
                firstName="Stefany",
                lastName="Gutierrez Vega",
                middleName="Isabel",
                studentCode="S9G23",
                career="Administración",
                urlProfile=None,
            ),
            Student(
                firstName="Maria",
                lastName="Cárdenas Hidalgo",
                middleName="Fernanda",
                studentCode="M6C8",
                career="Ingeniería Civil",
                urlProfile=None,
            ),
            Student(
                firstName="Yojhania",
                lastName="Gonzales Contreras",
                middleName="Taitt",
                studentCode="Y21G3",
                career="Administración",
                urlProfile=None,
            ),
            Student(
                firstName="Jordyna",
                lastName="Robles Solorzano",
                middleName="Del Carmen",
                studentCode="J4C19S",
                career="Arquitectura Y Urbanismo",
                urlProfile=None,
            ),
            Student(
                firstName="Jakori",
                lastName="Hoyos Terrones",
                middleName="Nayeli",
                studentCode="J14H21",
                career="Administración",
                urlProfile=None,
            ),
            Student(
                firstName="Emelyn",
                lastName="Aguirre Valverde",
                middleName="Yasmin",
                studentCode="E26A23",
                career="Administración",
                urlProfile=None,
            ),
            Student(
                firstName="Cielo",
                lastName="Abanto Rojas",
                middleName="Valentina",
                studentCode="C23A19",
                career="Administración",
                urlProfile=profile_url + "/pro-abanto-rojas.jpg",
            ),
            # 30 LAST ESTUDENTS
            Student(
                firstName="Dalia",
                middleName="Irina",
                lastName="Garcia De la Cruz",
                studentCode="D9G4L3",
                career="Ingeniería Química",
                urlProfile=None
            ),
            Student(
                firstName="Diego",
                middleName="Andree",
                lastName="Garro Taboada",
                studentCode="D1G21",
                career="Ciencia Política ",
                urlProfile=None
            ),
            Student(
                firstName="Fabiana",
                middleName="Belen",
                lastName="Sosa Parra",
                studentCode="F2S17",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Nory Ann",
                middleName="Marie",
                lastName="Touzet Meneses",
                studentCode="N1M21M",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Priscila",
                middleName="Crystal",
                lastName="Villegas Dominguez",
                studentCode="P3V4",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Yamelyn",
                middleName="Leslie",
                lastName="Rios Tandaypan",
                studentCode="Y12R21",
                career="Contabilidad y Finanzas",
                urlProfile=None
            ),
            Student(
                firstName="Christian",
                middleName="Rodrigo",
                lastName="Valverde Caspito",
                studentCode="C19V3",
                career="Ingeniería Industrial",
                urlProfile=profile_url + "/pro-valverde caspito .png"
            ),
            Student(
                firstName="Eddie",
                middleName="Alessandro",
                lastName="Jiménez Vilchez",
                studentCode="E1J23",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Fabián",
                middleName="Nicolas",
                lastName="Paredes Calderón",
                studentCode="F14P3",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Kiara",
                middleName="Marife",
                lastName="Rodriguez Sifuentes",
                studentCode="K13R20",
                career="Ingeniería Ambiental",
                urlProfile=None
            ),
            Student(
                firstName="Luis",
                middleName="Angel",
                lastName="Laureano Escobedo",
                studentCode="L1L5",
                career="Ingeniería Industrial ",
                urlProfile=None
            ),
            Student(
                firstName="Grecia",
                middleName="Alexandra",
                lastName="Paredes Cachique",
                studentCode="G1P3",
                career="Economía",
                urlProfile=None
            ),
            Student(
                firstName="Maria",
                middleName="Fernanda",
                lastName="Pretell Leon",
                studentCode="M6P12",
                career="Economía ",
                urlProfile=None
            ),
            Student(
                firstName="Mixie",
                middleName="Arleni",
                lastName="Gil Zapata",
                studentCode="M1G27",
                career="Economía",
                urlProfile=None
            ),
            Student(
                firstName="Nestor",
                middleName="Rafael",
                lastName="Plasencia De la Cruz",
                studentCode="N19P4L3",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Tatiana",
                middleName="Yuleisy",
                lastName="Aliaga Pretell",
                studentCode="T26A17",
                career="Física",
                urlProfile=None
            ),
            Student(
                firstName="Kevin",
                middleName="Gamaliel",
                lastName="Rodríguez Alfaro",
                studentCode="K7R1",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Fernanda ",
                middleName="Milagros",
                lastName="Rojas Rodriguez",
                studentCode="F13R19",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Adriana",
                middleName="Gabriela",
                lastName="Castillo Ochoa",
                studentCode="A7C16",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Angelo",
                middleName="Salvattore",
                lastName="Chavarry Bustamante",
                studentCode="A20C2",
                career="Ingeniería Informática",
                urlProfile=None
            ),
            Student(
                firstName="Cesar",
                middleName="Junior",
                lastName="Quito Cruz",
                studentCode="C10Q3",
                career="Ingeniería Mecatrónica",
                urlProfile=None
            ),
            Student(
                firstName="Juan",
                middleName="José",
                lastName="Chávez Tenorio",
                studentCode="J10C21",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Lorena",
                middleName="Midalís",
                lastName="Primo Bueno",
                studentCode="L13P2",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Malena",
                middleName="Shecid",
                lastName="Huamán Arana",
                studentCode="M20H1",
                career="Ingeniería Ambiental",
                urlProfile=None
            ),
            Student(
                firstName="Melissa",
                middleName="del Rosario",
                lastName="Muñoz Uriarte",
                studentCode="M4R13U",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Milene",
                middleName="Xiomara",
                lastName="Delgado Silva",
                studentCode="M25D20",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Belinda",
                middleName="Maricielo",
                lastName="Arroyo Esquivel",
                studentCode="B13A5",
                career="Ingeniería Ambiental",
                urlProfile=None
            ),
            Student(
                firstName="Diego",
                middleName="Jesús",
                lastName="Ullilén Chávez",
                studentCode="D10U3",
                career="Ingeniería Civil",
                urlProfile=None
            ),
            Student(
                firstName="Luis",
                middleName="Angel",
                lastName="Lecca Cortez",
                studentCode="L1L3",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Angie",
                middleName="Tatiana",
                lastName="Recuenco Tapia",
                studentCode="A21R21",
                career="Ingeniería Mecatrónica",
                urlProfile=None
            ),
            Student(
                firstName="Jhosmel",
                middleName="Anderson",
                lastName="Vigo Cepeda",
                studentCode="J1V3",
                career="Ingeniería Química",
                urlProfile=None
            ),
            Student(
                firstName="Romina",
                middleName="Alejandra",
                lastName="Seclen Cespedes",
                studentCode="R1S3",
                career="Trabajo Social",
                urlProfile=None
            ),
            Student(
                firstName="Zaleth",
                middleName="Valentina",
                lastName="Rivas Calderón",
                studentCode="Z23R3",
                career="Ingeniería de Sistemas",
                urlProfile=None
            ),
            Student(
                firstName="Maite",
                middleName="",
                lastName="Palacios Asto",
                studentCode="M17A",
                career="Ingeniería Ambiental",
                urlProfile=None
            ),
            Student(
                firstName="Carla",
                middleName="Cecilia",
                lastName="Villacorta Mendoza",
                studentCode="C3V13",
                career="Derecho",
                urlProfile=None
            ),
            Student(
                firstName="Johan",
                middleName="Alexander Salvador ",
                lastName="Azañero Chunga",
                studentCode="J1SA",
                career="Ciencias de la comunicación",
                urlProfile=None
            ),
            Student(
                firstName="José",
                middleName="Félix",
                lastName="Paria Guerrero",
                studentCode="J6P7",
                career="Ingeniería Ambiental",
                urlProfile=None
            ),
            Student(
                firstName="Zaira",
                middleName="Josselyn",
                lastName="Zevallos Gamboa",
                studentCode="Z1Z7",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Brenda",
                middleName="Nicole",
                lastName="Carranza Burgos",
                studentCode="B14C2",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Brian",
                middleName="Jahir",
                lastName="Li Martínez",
                studentCode="B19L9",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="José",
                middleName="Miguel",
                lastName="Coveñas García",
                studentCode="J6M13",
                career="Economía",
                urlProfile=None
            ),
            Student(
                firstName="Fredy",
                middleName="Luis",
                lastName="Robles Huaman",
                studentCode="F19R8",
                career="Ciencias de la comunicación",
                urlProfile=None
            ),
            Student(
                firstName="Greicy",
                middleName="Liset",
                lastName="Chacon Escobedo",
                studentCode="G19C5",
                career="Administración",
                urlProfile=None
            ),
            Student(
                firstName="Kasumy",
                middleName="del Pilar",
                lastName="Guzmán Paredes",
                studentCode="K1G17",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Eduardo",
                middleName="Fabio",
                lastName="Chávez Solórzano",
                studentCode="E4F6C",
                career="Ingeniería Industrial",
                urlProfile=None
            ),
            Student(
                firstName="Marthy",
                middleName="Valentino",
                lastName="Chacón Ludeña",
                studentCode="M19V3",
                career="Ingeniería Civil",
                urlProfile=None
            ),
            Student(
                firstName="Oliver",
                middleName="Frank",
                lastName="Tirado Alfaro",
                studentCode="O12F21",
                career="Ingeniería Metalúrgica",
                urlProfile=None
            ),
            Student(
                firstName="Alexandra",
                middleName="Fabiola",
                lastName="Hernandez Caballero",
                studentCode="A12F8",
                career="Ingeniería Mecánica",
                urlProfile=None
            ),
            Student(
                firstName="Eliaser",
                middleName="Isai",
                lastName="Avila Zamudio",
                studentCode="E12I1",
                career="Ingeniería Informática",
                urlProfile=None
            ),
            Student(
                firstName="Germain",
                middleName="Alexander",
                lastName="Cruz Vargas",
                studentCode="G19A3",
                career="Ingeniería de Sistemas",
                urlProfile=None
            ),
            Student(
                firstName="Jesus",
                middleName="Alberto",
                lastName="Agreda Cruz",
                studentCode="J10A1",
                career="Ingeniería Informática",
                urlProfile=None
            ),
            Student(
                firstName="Manuel",
                middleName="Rodrigo",
                lastName="Albitres Cieza",
                studentCode="M13R1",
                career="Ingeniería Informática",
                urlProfile=None
            ),
            Student(
                firstName="Omar",
                middleName="Eduardo",
                lastName="Cipiran Mercedes",
                studentCode="O13E3",
                career="Ingeniería Informática",
                urlProfile=None
            ),
            Student(
                firstName="Yanxmarcos",
                middleName="",
                lastName="Chan Vásquez",
                studentCode="Y14C23",
                career="Ingeniería Informática",
                urlProfile=None
            ),
    ]
        session.add_all(students)
        session.commit()
        print("✅ Seeder ejecutado correctamente")