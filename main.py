from fastapi import FastAPI, HTTPException, Body
from agents.analyzeHandler import runBatchFilesAnalysis, runFileAnalysis
from constants.baseModels import FileAnalysisRequest

app = FastAPI()


@app.get("/")
def root():
    return {"message": "The API is not supported"}

@app.post("/analyze")
async def analyze(requests: list[FileAnalysisRequest] = Body(...)):
    try:
        print(requests)
        response = await runBatchFilesAnalysis(requests)
        return response
    except Exception as e:
        print("Error during analysis:", str(e))
        raise HTTPException(status_code=500, detail="Analysis failed")


@app.post("/analyze/single")
async def analyze_single(request: FileAnalysisRequest = Body(...)):
    try:
        print(request)
        response = await runFileAnalysis(
            filePath=request.filePath,
            licenses=request.licenses,
            copyrights=request.copyrights
        )
        return response
    except Exception as e:
        print("Error during single file analysis:", str(e))
        raise HTTPException(status_code=500, detail="Single file analysis failed")
