import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

from constants.agentModels import DEFAULT_MODEL, GPT_5_NANO

DEFAULT_INTERNAL_BASE_URL = "https://llm-api.amd.com/OnPrem"


def getClient(model: str = DEFAULT_MODEL) -> AsyncOpenAI:
    load_dotenv(override=True)

    if model == GPT_5_NANO:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is missing. Check your .env or environment variables.")

        return AsyncOpenAI(api_key=api_key)

    if model == DEFAULT_MODEL:
        internal_api_key = os.getenv("INTERNAL_LLM_API_KEY")
        if not internal_api_key:
            raise RuntimeError("INTERNAL_LLM_API_KEY is missing. Check your .env or environment variables.")

        base_url = DEFAULT_INTERNAL_BASE_URL
        request_user = os.getlogin()

        return AsyncOpenAI(
            base_url=base_url,
            api_key="dummy",
            default_headers={
                "Ocp-Apim-Subscription-Key": internal_api_key,
                "user": request_user,
            },
        )

    raise ValueError(f"Unsupported model: {model}")
