from pydantic import BaseModel, EmailStr
from typing import Optional, List


class UserBase(BaseModel):
    """
    User schema基础格式
    """

    username: str
    email: EmailStr
    is_active: Optional[bool] = True
    nick_name: str
    avatar: str = "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
    menus: List[str] = []

    class Config:
        schema_extra = {
            "example": {
                "username": "huangtao",
                "email": "huangtao123689@gmail.com",
                "is_active": True,
                "nick_name": "huangtao",
                "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
            }
        }


class NewUser(UserBase):
    """
    新建用户schema
    """

    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "huangtao",
                "email": "huangtao123689@gmail.com",
                "is_active": True,
                "nick_name": "huangtao",
                "password": "123456",
            }
        }


class AllUser(BaseModel):
    """
    所有用户schema
    """

    total: int
    users: List[UserBase] = []

    class Config:
        schema_extra = {
            "example": {
                "total": 50,
                "users": [
                    {
                        "username": "huangtao",
                        "email": "huangtao123689@gmail.com",
                        "is_active": True,
                        "nick_name": "mark",
                    },
                    {
                        "username": "huangtao1",
                        "email": "huangtao1@gmail.com",
                        "is_active": True,
                        "nick_name": "huangtao1",
                    },
                ],
            }
        }


class ModifyUser(BaseModel):
    """
    修改用户schema
    """

    username: Optional[str] = None
    password: Optional[str] = None
    email: EmailStr
    is_active: Optional[bool] = True
    nick_name: str


class Token(BaseModel):
    """
    token schema
    """

    access_token: str
    token_type: str


class GroupBase(BaseModel):
    """
    Group schema基础格式
    """

    group_num: str
    group_name: str

    class Config:
        schema_extra = {
            "example": {
                "group_num": "10000",
                "group_name": "概况",
            }
        }


class GroupList(BaseModel):
    """
    Group schema基础格式
    """

    group_list: List[GroupBase]

    class Config:
        schema_extra = {
            "example": {
                "group_list": [
                    {"group_num": "10000", "group_name": "概况"},
                    {"group_num": "20000", "group_name": "渠道管理"},
                    {"group_num": "21000", "group_name": "渠道列表"},
                    {"group_num": "22000", "group_name": "渠道详情"},
                    {"group_num": "30000", "group_name": "订单管理"},
                    {"group_num": "31000", "group_name": "订单列表"},
                    {"group_num": "40000", "group_name": "人工审核"},
                    {"group_num": "41000", "group_name": "订单列表"},
                    {"group_num": "42000", "group_name": "订单池"},
                    {"group_num": "43000", "group_name": "审核统计"},
                    {"group_num": "50000", "group_name": "财务管理"},
                    {"group_num": "51000", "group_name": "还款计划"},
                    {"group_num": "52000", "group_name": "台账数据"},
                    {"group_num": "60000", "group_name": "数据统计"},
                    {"group_num": "61000", "group_name": "用户统计"},
                    {"group_num": "62000", "group_name": "订单统计"},
                    {"group_num": "63000", "group_name": "风险收益分析"},
                    {"group_num": "70000", "group_name": "设置"},
                    {"group_num": "71000", "group_name": "账号设置"},
                    {"group_num": "72000", "group_name": "功能设置"},
                ]
            }
        }


class UserGroupBase(BaseModel):
    user_id: int
    group_num: str

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "group_num": "10000",
            }
        }


class UserGroupList(BaseModel):
    user_group_list: List[UserGroupBase]

    class Config:
        schema_extra = {
            "example": {
                "user_group_list": [
                    {"user_id": 1, "group_num": "10000"},
                    {"user_id": 1, "group_num": "20000"},
                    {"user_id": 1, "group_num": "21000"},
                    {"user_id": 1, "group_num": "22000"},
                    {"user_id": 1, "group_num": "30000"},
                    {"user_id": 1, "group_num": "31000"},
                    {"user_id": 1, "group_num": "40000"},
                    {"user_id": 1, "group_num": "41000"},
                    {"user_id": 1, "group_num": "42000"},
                    {"user_id": 1, "group_num": "43000"},
                    {"user_id": 1, "group_num": "50000"},
                    {"user_id": 1, "group_num": "51000"},
                    {"user_id": 1, "group_num": "52000"},
                    {"user_id": 1, "group_num": "60000"},
                    {"user_id": 1, "group_num": "61000"},
                    {"user_id": 1, "group_num": "62000"},
                    {"user_id": 1, "group_num": "63000"},
                    {"user_id": 1, "group_num": "70000"},
                    {"user_id": 1, "group_num": "71000"},
                    {"user_id": 1, "group_num": "72000"},
                ]
            }
        }
