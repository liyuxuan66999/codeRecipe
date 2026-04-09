from pydantic import BaseModel


class FileAnalysisRequest(BaseModel):
    filePath: str
    licenses: list[str] = None
    copyrights: list[str] = None
