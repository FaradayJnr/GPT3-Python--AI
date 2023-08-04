#GPT-3 powered AGI Chat Application: RANSFORD OPPONG: Aug 4,2023
import os
import openai
openai.api_key = "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"
#command to tell the model how to arrange the inputs and outputs.
start_sequence = "\nAI:"
restart_sequence = "\Human: "
#initial input
prompt ="The following is a conversation with an AI Assistant. The Assistant is helpful, creative, clever and very friendly. \n\nHuman: Hello, who are you\nAI: I am an AI created by OpenAI. How may I assist you today?\nHuman: ",
def gpt_output(prompt):
    response = openai.Completion.create(
        model ="text-davinci-003",
        prompt = prompt,
        temperature = 0.9,
        max_tokens = 150,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.6,
        stop = ["Human: ","AI: "]
    )
    print("AI response: ",response.choice[0].text)
#a loop to take input from a user when the function is true
while True:
    query = input("Ask a QUestion to AI:\n")
    gpt_output(query)