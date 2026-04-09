import asyncio
import json
from openai import AsyncOpenAI
from dataclasses import dataclass
from typing import Dict, Optional
from constants.promptConstants import Prompt
from constants.agentModels import (
    DEFAULT_MODEL, 
    GPT_5_NANO, 
    DEFAULT_MAX_TOKENS,
)
from agents.utils.getClient import getClient

@dataclass(frozen=True)
class FileAnalyzeAgent:
    client: AsyncOpenAI
    model: str

_agent_instances: Dict[str, FileAnalyzeAgent] = {}
_agent_lock = asyncio.Lock()

async def getAgent(model: str = GPT_5_NANO) -> FileAnalyzeAgent:
    if model in _agent_instances:
        return _agent_instances[model]
    
    async with _agent_lock:
        if model not in _agent_instances:
            print("invoking FileAnalyzeAgent")
            client = getClient(model=model)

            _agent_instances[model] = FileAnalyzeAgent(
                client=client,
                model=model
            )
            print("created client")

    return _agent_instances[model]

async def analyzeFile(
    agent: FileAnalyzeAgent,
    prompt: Prompt
) -> Dict[str,any]:
    messages = [
        {"role": "system", "content": prompt.system},
        {"role": "user", "content": prompt.user},
    ]
    try:
        print("Sending messages to OpenAI API")
        response = await agent.client.chat.completions.create(
            model=agent.model,
            max_completion_tokens=DEFAULT_MAX_TOKENS,
            messages=messages,
        )
        print("OpenAI API responded")
        assistant_message = response.choices[0].message.content
        print(assistant_message)
        assistant_message_json = json.loads(assistant_message)
        return {
            "status": "success",
            **assistant_message_json
        }
    except Exception as e:
        print("Error during API call:", str(e))
        return {
            "status": "error",
            "model": agent.model,
            "error": str(e),
        }
