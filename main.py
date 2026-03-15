from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.datatables import create_db_and_tables, get_session
from database.seeders.studentSeeder import seed_students
from database.seeders.infofellowSeeder import seed_info_fellows
from database.seeders.projectSeeder import seed_projects
from database.seeders.memberSeeder import seed_member
from database.seeders.allySeeder import seed_ally
from database.seeders.achievementSeeder import seed_achievements
from database.seeders.eventSeeder import seed_events
from database.seeders.postSeeder import seed_posts
from modules.auth.auth_controller import router as auth_router
from modules.project_controller import router as project_router
from modules.controllers.home_controller import router as home_router

from sqlmodel import Session, select
from database.datatables import Student


session = next(get_session())


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ✅ Solo se ejecuta una vez al iniciar
    create_db_and_tables()
    with next(get_session()) as session:
        seed_students(session)
        seed_info_fellows(session)
        seed_projects(session)
        seed_member(session)
        seed_ally(session)
        seed_achievements(session)
        seed_events(session)
        seed_posts(session)

    yield  # La app corre aquí
    # Aquí puedes poner lógica de cierre si la necesitas


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(auth_router)
app.include_router(project_router)
app.include_router(home_router)