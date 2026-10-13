key  ="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"

from openai import OpenAI
client = OpenAI(api_key=key)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
        {
            "role": "user",
            "content": "complete this chat: Jack: Hey; Jill: How are you?; Jack: now what?; Jill:  ",
        }
  ],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


for choice in response.choices:
    print(choice.message.content)
