from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session

from database.datatables import get_session
from modules.services.home_service import build_home_data, get_achievements, get_allies, get_directors, get_events, get_post_by_id, get_posts, get_projects

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()


@router.get("/home")
async def get_home(session: SessionDep):
    return build_home_data(session)

@router.get("/noticias")
async def get_noticias(session: SessionDep):
    return get_posts(session)

@router.get("/noticias/{post_id}")
async def get_noticia_by_id(session: SessionDep, post_id: int):
    return get_post_by_id(session, post_id)

@router.get("/directiva")
async def get_directiva(session: SessionDep):
    return get_directors(session)

@router.get("/proyectos")
async def get_proyectos(session: SessionDep):
    return get_projects(session)

@router.get("/partners")
async def get_partners(session: SessionDep):
    return get_allies(session)

@router.get("/reconocimientos")
async def get_reconocimientos(session: SessionDep):
    return get_achievements(session)

@router.get("/eventos")
async def get_eventos(session: SessionDep):
    return get_events(session)