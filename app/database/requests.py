from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select, update, delete, desc

#Запрос на добавление пользователя в БД, если его нет
async def set_user(tg_id:int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, nf_status = False))
            await session.commit()

#Запрос на отмену отправления уведомления в 10 утра
async def set_not(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user:
            user.nf_status = False
            await session.commit()

#Запрос на отправление уведомления в 10 утра
async def set_yes(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user:
            user.nf_status = True
            await session.commit()

#Запрос всех пользователей, которым нужно отправлять сообщение в 10 утра
async def get_tg_ids():
    async with async_session() as session:
        result = await session.execute(select(User.tg_id).filter(User.nf_status == 1))
        return [tg_id[0] for tg_id in result.fetchall()]