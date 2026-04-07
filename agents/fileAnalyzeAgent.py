import asyncio
import os
import json
from dotenv import load_dotenv
from openai import OpenAI,AsyncOpenAI
from dataclasses import dataclass
from typing import Dict, Optional
from constants.promptConstants import Prompt

DEFAULT_MODEL = "gpt-5-nano"

@dataclass(frozen=True)
class FileAnalyzeAgent:
    client: AsyncOpenAI
    model: str

_agent_instance: Optional[FileAnalyzeAgent] = None
_agent_lock = asyncio.Lock()

async def getAgent(model: str = DEFAULT_MODEL) -> FileAnalyzeAgent:
    global _agent_instance
    if _agent_instance is not None:
        return _agent_instance
    
    async with _agent_lock:
        if _agent_instance is None:
            print("loading API keys")
            load_dotenv(override=True)
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise RuntimeError("OPENAI_API_KEY is missing. Check your .env or environment variables.")
            print("invoking FileAnalyzeAgent")
            client = AsyncOpenAI(api_key=api_key)

            _agent_instance = FileAnalyzeAgent(
                client=client,
                model=model
            )
            print("created client")

    return _agent_instance

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
            messages=messages,
        )
        print("OpenAI API responded")
        assistant_message = response.choices[0].message.content
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