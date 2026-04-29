chat_history=[]
def fake_llm(prompt:str):
    prompt=prompt.lower()
    
    if "hello" in prompt:
        return "hello how can i help you"
    elif "email" in prompt:
        return "do you want a proffesioanl or casual email"
    elif "proffesional" in prompt:
         return "Dear sir i request you to grant me leave for two days due to certain health issues"
    else:
         return "I dont understand"
def process_chat(prompt:str):
    chat_history.append({"user":prompt})
    response=fake_llm(prompt)
    chat_history.append({"ai":response})
    return response , chat_history
