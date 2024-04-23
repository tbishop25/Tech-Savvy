from openai import OpenAI


client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )



messages = [
    {"role": "system", "content": "You are a kind helpful assistant that assists with problems in Microsoft Word."},
    {"role": "system", "content": "You ONLY assist people with Word."},
    {"role": "system", "content": "If a user ask about any else, redirect them to word help."},
]
# create exit condition
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages
        )
    else:print("Exit")
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"TSBot: {reply}")
    

    