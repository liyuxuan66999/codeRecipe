import json
from typing import List

from .promptTemplates import (
    systemPromptBatchGetTemplate,
    systemPromptDefaultTemplate,
    userPromptBatchGetTemplate,
    userPromptDefaultTemplate,
)
from utils.formatter import toBullets
from constants.promptConstants import wordingTemplateEnum, Prompt
from constants.baseModels import FileAnalysisRequest

def getPromptsForSingleFile(
        filePath: str,
        licenses: list[str] = None,
        copyrights: list[str] = None
) -> Prompt:
    print("creating prompt")
    licenseBullets = toBullets(licenses) if licenses else wordingTemplateEnum.NO_LICENSE.value
    copyrightBullets = toBullets(copyrights) if copyrights else wordingTemplateEnum.NO_COPYRIGHT.value

    system_prompt = systemPromptDefaultTemplate
    user_prompt = userPromptDefaultTemplate.format(
        filePath=filePath,
        licenses=licenseBullets,
        copyrights=copyrightBullets
    )
    prompt = Prompt(system=system_prompt, user=user_prompt)
    print("created prompt")
    return prompt


def getPromptsForBatchFiles(
    files: List[FileAnalysisRequest]
) -> Prompt:
    print("creating batch prompt")

    files_payload = json.dumps(
        [file.model_dump() for file in files],
        indent=2
    )

    system_prompt = systemPromptBatchGetTemplate
    user_prompt = userPromptBatchGetTemplate.format(
        filesPayload=files_payload
    )

    prompt = Prompt(system=system_prompt, user=user_prompt)
    print("created batch prompt")
    return prompt
