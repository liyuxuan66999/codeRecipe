from typing import Optional, List, Dict, Any
from .fileAnalyzeAgent import getAgent, analyzeFile
from .prompt.fileAnalyzePrompt import getPrompts

async def runFileAnalysis(
    filePath: str,
    licenses: Optional[List[str]] = None,
    copyrights: Optional[List[str]] = None
) -> Dict[str, Any]:
    print("fetching agent")
    agent = await getAgent()
    print("Agent fetched:", agent.model)
    prompt = getPrompts(
        filePath=filePath,
        licenses=licenses,
        copyrights=copyrights
    )


    response = await analyzeFile(agent=agent, prompt=prompt)

    return {
        "model": agent.model,
        "response": response,
    }
