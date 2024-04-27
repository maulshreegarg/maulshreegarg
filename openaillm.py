import openai
import time
ke="sk-proj-IMPBA6aEznIlhj44DVSDT3BlbkFJRX5SlwrecueccmvAS7tU"
openai.api_key=ke;
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                messages=[{"role": "user", "content": "Listen to your"}],max_tokens=1,n=5,temperature=0)
#https://www.youtube.com/watch?v=czvVibB2lRA&t=861s

print(chat_completion.to_dict())
