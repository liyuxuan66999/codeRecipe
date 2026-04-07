from dataclasses import dataclass
from .promptTemplates import systemPromptDefaultTemplate, userPromptDefaultTemplate
from utils.formatter import toBullets
from constants.promptConstants import wordingTemplateEnum, Prompt

def getPrompts(
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