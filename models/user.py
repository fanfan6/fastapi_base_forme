from models.base import Base
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from passlib.context import CryptContext
from datetime import datetime

# 密码加密算法
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    """
    用户表
    """

    __tablename__ = "auth_users"
    __table_args__ = {"comment": "用户表"}
    user_id = Column(
        Integer, primary_key=True, autoincrement=True, index=True, comment="用户id"
    )
    username = Column(
        String(20), nullable=False, unique=True, index=True, comment="登陆用户名"
    )
    nick_name = Column(String(20), comment="昵称")
    avatar = Column(String(200), comment="头像")
    email = Column(String(30), unique=True, nullable=False, comment="邮箱")
    hashed_password = Column(String(200), nullable=False, comment="加密后的密码")
    is_active = Column(Boolean(), default=True, comment="是否激活")
    is_delete = Column(Boolean(), default=True, comment="是否可用0不可用/1可用")
    last_sign_in = Column(DateTime(), default=datetime.now, comment="最后登录时间")
    creat_time = Column(DateTime(), default=datetime.now, comment="创建时间")
    update_time = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now, comment="最后一次更新时间"
    )

    def convert_pass_to_hash(self, password):
        self.hashed_password = pwd_context.hash(password)

    def check_password(self, password):
        return pwd_context.verify(password, self.hashed_password)

    def __repr__(self):
        return f"<User(username={self.username},email={self.email})>"


class Group(Base):
    """
    组
    """

    __tablename__ = "auth_groups"
    __table_args__ = {"comment": "组"}
    group_num = Column(
        String(20),
        primary_key=True,
        nullable=False,
        unique=True,
        index=True,
        comment="组编号",
    )
    group_name = Column(String(64), comment="组名称")
    creat_time = Column(DateTime(), default=datetime.now, comment="创建时间")


class UserGroup(Base):
    """
    用户组关联
    """

    __tablename__ = "auth_user_group"
    __table_args__ = {"comment": "用户、组关联表"}
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment="id")
    user_id = Column(Integer, index=True, comment="用户id")
    group_num = Column(String(20), comment="组编号")
    creat_time = Column(DateTime(), default=datetime.now, comment="创建时间")

