import os
import openai
import pandas as pd
import time
openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
    )
    return response.choices[0].message["content"]



c=get_completion('good mrg')
print(c)