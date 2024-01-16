from gpt4all import GPT4All

basePrompt = "You are a helpful assistant called Jarvis who was created by a group of student in a school project for the company Ingescape."


def buildPrompt(prompt: str):
    return f"{basePrompt} \n User: {prompt} \n Jarvis:"


def handlePrompt(prompt: str):
    fullPrompt = buildPrompt(prompt)

    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
    output = model.generate(fullPrompt, max_tokens=50)

    return output
