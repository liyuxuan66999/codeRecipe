from .components import (
    batchFileAnalysisIntroWording,
    batchFileAnalysisPayloadShape,
    batchFileAnalysisPayloadSample,
    batchFileAnalysisRulesWording,
    singleFileAnalysisIntroWording,
    singleFileAnalysisPayloadShape,
    singleFileAnalysisPayloadSample,
)

systemPromptDefaultTemplate = """
{singleFileAnalysisIntroWording}

Your response must follow these rules:
1. Return only valid JSON.
2. Do not wrap the JSON in markdown code fences.
3. Do not include any explanation outside the JSON.

The JSON payload must use this shape:
{singleFileAnalysisPayloadShape}

Example:
{singleFileAnalysisPayloadSample}

If you cannot determine the source, return an empty list for possibleSources.
""".format(
    singleFileAnalysisIntroWording=singleFileAnalysisIntroWording,
    singleFileAnalysisPayloadShape=singleFileAnalysisPayloadShape,
    singleFileAnalysisPayloadSample=singleFileAnalysisPayloadSample
).strip()

systemPromptBatchGetTemplate = """
{batchFileAnalysisIntroWording}

Your response must follow these rules:
{batchFileAnalysisRulesWording}

The JSON payload must use this shape:
{batchFileAnalysisPayloadShape}

Example:
{batchFileAnalysisPayloadSample}

If you cannot determine any source groups, return an empty groupedSources list and place all files in unmatchedFiles.
""".format(
    batchFileAnalysisIntroWording=batchFileAnalysisIntroWording,
    batchFileAnalysisRulesWording=batchFileAnalysisRulesWording,
    batchFileAnalysisPayloadShape=batchFileAnalysisPayloadShape,
    batchFileAnalysisPayloadSample=batchFileAnalysisPayloadSample
).strip()

userPromptDefaultTemplate = """
Analyze the file located at: {filePath}.
If licenses are provided, check for the following licenses: 
    {licenses}
If copyrights are provided, check for the following copyrights: 
    {copyrights}
Please use above information to determine the possible external source of the file. and return the result in JSON format as specified.
""".strip()

userPromptBatchGetTemplate = """
Analyze the following batch of files and group them by likely upstream source.

Input batch:
{filesPayload}

Return the result using the required JSON schema from the system instructions.
""".strip()
