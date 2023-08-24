import openai

openai.api_key = "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"


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


def get_description(prompt):
    response = get_completion(prompt)
    return response
