import traceback
import jwt
from core.config import settings
from core.db import get_db
from fastapi import APIRouter, Depends, Header, HTTPException, Request
from models.user import User, Group, UserGroup
from schema.user import NewUser, GroupList, UserGroupList
from sqlalchemy.orm import Session
from utils.logger import logger

init_router = APIRouter()


@init_router.put(
    "/create_user", responses={406: {"description": "创建的用户已经存在"}}, name="创建新用户"
)
def create_user(user: NewUser, db: Session = Depends(get_db)):
    old_user = db.query(User).filter(User.username == user.username).first()
    old_email = db.query(User).filter(User.email == user.email).first()
    if old_user or old_email:
        raise HTTPException(status_code=406, detail="创建的用户已经存在")
    user_dict = {
        "username": user.username,
        "email": user.email,
        "nick_name": user.nick_name,
        "is_active": user.is_active,
    }

    try:
        new_user = User(**user_dict)
        new_user.convert_pass_to_hash(user.password)
        db.add(new_user)
        db.commit()
        return {"message": "用户创建成功"}
    except Exception:
        logger.error(f"init admin error: {traceback.format_exc()}")


@init_router.put(
    "/create_group", responses={406: {"description": "创建的组已经存在"}}, name="创建新组"
)
def create_group(group_list: GroupList, db: Session = Depends(get_db)):
    for group in group_list.group_list:
        if (
            old_user := db.query(Group)
            .filter(Group.group_num == group.group_num)
            .first()
        ):
            raise HTTPException(status_code=406, detail="创建的组已经存在")
        user_dict = Group(
            **{"group_num": group.group_num, "group_name": group.group_name}
        )
        logger.info(user_dict)
        try:
            db.add(user_dict)
            db.commit()
        except Exception:
            db.rollback()
            logger.error(f"init group error: {traceback.format_exc()}")
    return {"message": "组创建成功"}


@init_router.put(
    "/create_user_group", responses={406: {"description": "创建的组已经存在"}}, name="创建新组"
)
def create_user_group(user_group_list: UserGroupList, db: Session = Depends(get_db)):
    for group in user_group_list.user_group_list:
        user_dict = UserGroup(
            **{"user_id": group.user_id, "group_num": group.group_num}
        )
        try:
            db.add(user_dict)
            db.commit()
        except Exception:
            logger.error(f"init group error: {traceback.format_exc()}")
    return {"message": "组创建成功"}
