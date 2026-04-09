singleFileAnalysisPayloadShape = """
{
    "filePath": "/absolute/path/to/file",
    "possibleSources": [
        {
            "source": "the URL of the possible source",
            "license": ["license names if available"],
            "score": 100,
            "suggestedGroupName": "<repo owner name>-<repo name> <repo version v#.# if version is identified v-u if unknown> <dominant license>"
        }
    ]
}
""".strip()

singleFileAnalysisPayloadSample = """
{
    "filePath": "/PalamidaScanDir/SWCSD-1234/source/amd_tee_sdk3.0/src/Tpm/include/HashTestData.h",
    "possibleSources": [
        {
            "source": "https://github.com/Microsoft/TSS.MSR/tree/main",
            "license": ["MIT"],
            "score": 100,
            "suggestedGroupName": "Microsoft-TSS.MSR v-u (MIT)"
        }
    ]
}
""".strip()

batchFileAnalysisPayloadShape = """
{
    "groupedSources": [
        {
            "source": "the URL of the most likely source repository or location",
            "license": ["license names if available"],
            "score": 100,
            "suggestedGroupName": "<repo owner name>-<repo name> <repo version v#.# if version is identified v-u if unknown> <dominant license>",
            "groupedFiles": [
                {
                    "filePath": "/absolute/path/to/file"
                }
            ]
        }
    ],
    "unmatchedFiles": [
        {
            "filePath": "/absolute/path/to/file"
        }
    ]
}
""".strip()

batchFileAnalysisPayloadSample = """
{
    "groupedSources": [
        {
            "source": "https://github.com/lua/lua/tree/master/manual",
            "license": ["MIT", "Apache-2.0"],
            "score": 100,
            "suggestedGroupName": "lua-lua v-u (MIT)",
            "groupedFiles": [
                {
                    "filePath": "/PalamidaScanDir/SWCSD-1234/source/lua/testes/manual.of"
                },
                {
                    "filePath": "/PalamidaScanDir/SWCSD-1234/source/lua/manual/2html"
                }
            ]
        }
    ],
    "unmatchedFiles": [
        {
            "filePath": "/PalamidaScanDir/SWCSD-1234/source/test.java"
        },
        {
            "filePath": "/PalamidaScanDir/SWCSD-1234/source/app.js"
        }
    ]
}
""".strip()
