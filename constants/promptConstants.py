from enum import Enum
from dataclasses import dataclass

class wordingTemplateEnum(str, Enum):
    NO_LICENSE = "No license information provided."
    NO_COPYRIGHT = "No copyright information provided."

@dataclass(frozen=True)
class Prompt:
    system: str
    user: str