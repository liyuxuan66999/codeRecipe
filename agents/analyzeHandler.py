from typing import Optional, List, Dict, Any
from .fileAnalyzeAgent import getAgent, analyzeFile
from .prompt.fileAnalyzePrompt import (
    getPromptsForSingleFile, 
    getPromptsForBatchFiles
)
from constants.baseModels import FileAnalysisRequest

async def runFileAnalysis(
    filePath: str,
    licenses: Optional[List[str]] = None,
    copyrights: Optional[List[str]] = None
) -> Dict[str, Any]:
    print("fetching agent")
    agent = await getAgent()
    print("Agent fetched:", agent.model)
    prompt = getPromptsForSingleFile(
        filePath=filePath,
        licenses=licenses,
        copyrights=copyrights
    )


    response = await analyzeFile(agent=agent, prompt=prompt)

    return {
        "model": agent.model,
        "response": response,
    }

async def runBatchFilesAnalysis(
    files: List[FileAnalysisRequest]
) -> Dict[str, Any]:
    print("fetching agent")
    agent = await getAgent()
    print("Agent fetched:", agent.model)

    prompt = getPromptsForBatchFiles(files)
    response = await analyzeFile(agent=agent, prompt=prompt)

    return {
        "model": agent.model,
        "response": response,
    }
