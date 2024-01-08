def handlePrompt(prompt: str):
    print("prompt: ", prompt)
    defaultResponse = "default response"
    promptResponse = "the response to the prompt {} is {}".format(
        prompt, defaultResponse
    )

    return promptResponse
