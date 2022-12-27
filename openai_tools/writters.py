import os
import openai
from .key import API_KEY
openai.api_key = API_KEY


def joineer(list):
    return "".join(list)


def reader(list):
    [print(x) for x  in list]


def model_list():
    models = openai.Engine.list()
    rid =  [x['id'] for x in models["data"]]
    return rid


class Writter:
    def __init__(self,prompt, model_engine = "text-davinci-003", max_tokens=1256, temperature=0, top_p=1, frequency_penalty=0, presence_penalty=0):
        self.prompt = prompt
        self.model_engine = model_engine
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.response = self.get_response()
        self.openobject = self.get_openobject()
        self.openobject_string = self.get_openobject_string()

    def get_response(self):
        response = openai.Completion.create(
            model=self.model_engine,
            prompt=self.prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )
        return response

    def get_openobject(self):
        response = self.response
        openobject = response["choices"][0]["text"]
        openobjectd = []
        # take the openobject which is a split by '\n', creeate a tab for each '\t' and remove the '+' from the beginning of each line
        for line in openobject.split("\n"):
            if line.startswith(".") and len(line) == 1:
                line = ""
            if line.startswith("+"):
                line = line[1:]
            if "\t" in line:
                openobjectd.append(line.replace("\t", "    "))
            openobjectd.append(line)
        return openobjectd

    def get_openobject_string(self):
        openobjectd = self.openobject
        openobject_string = ""
        for line in openobjectd:
            openobject_string += line + "\n"
        return openobject_string
