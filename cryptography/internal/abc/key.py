from abc import ABCMeta

from pydantic import BaseModel


class ABCKey(BaseModel, metaclass=ABCMeta):
    bits: int


__all__ = ("ABCKey",)
