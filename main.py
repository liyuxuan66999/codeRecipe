from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel  
from agents.analyzeHandler import runFileAnalysis

app = FastAPI()

class ANALYZE_REQUEST(BaseModel):
    filePath: str
    licenses: list[str] = None
    copyrights: list[str] = None


@app.get("/")
def root():
    return {"message": "The API is not supported"}

@app.post("/analyze")
async def analyze(request: ANALYZE_REQUEST = Body(...)):
    filePath = request.filePath
    licenses = request.licenses 
    copyrights = request.copyrights

    print(f"Analyzing file: {filePath}")
    print(f"Analyzing licenses: {licenses}")
    print(f"Analyzing copyrights: {copyrights}")

    try:
        response = await runFileAnalysis(
            filePath=filePath,
            licenses=licenses,
            copyrights=copyrights
        )
        return response
    except Exception as e:
        print("Error during analysis:", str(e))
        raise HTTPException(status_code=500, detail="Analysis failed")

