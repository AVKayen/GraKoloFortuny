from fastapi import FastAPI
import asyncio
import random
from fastapi.middleware.cors import CORSMiddleware
import yaml

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

global returnObj
global pula

with open('main.yaml', 'r') as file:
    pula = yaml.safe_load(file)

returnObj: dict = {
    "isSpin": False,
    "points": [0,0,0,0],
    "question": "...",
    "answer": "...",
    "phrase": "***",
    "uncovered": "***"
}

@api.get("/")
async def root():
    return returnObj

@api.get("/spin")
async def spin():
    returnObj["isSpin"] = True
    if len(pula) > 0:
        returnObj["question"] = random.choice(list(pula))
        returnObj["answer"] = pula[returnObj["question"]]
        pula.pop(returnObj["question"])
    else:
        returnObj["question"] = "Koniec Pytań~~~~ To się nie mialo zdarzyć"
    await asyncio.sleep(1)
    returnObj["isSpin"] = False
    return "NAWW I'M TRYINGGGG"

@api.get("/addpoints/{team}/{number}")
async def addpoints(team, number):
    returnObj["points"][int(team)-1] += int(number)
    return "DONE"

@api.get("/setphrase/{phraseT}")
async def setPhrase(phraseT):
    returnObj["uncovered"] = phraseT
    returnObj["phrase"] = ""
    for c in phraseT:
        if c != " ":
            returnObj["phrase"] += "*"
        else:
            returnObj["phrase"] += " "
    return returnObj["uncovered"]

@api.get("/uncover/{num}")
async def uncover(num):
    x= list(returnObj["phrase"])
    x[int(num)] = returnObj["uncovered"][int(num)]
    returnObj["phrase"] = "".join(x)
    return num

@api.get("/uncover/")
async def uncover_all():
    returnObj["phrase"] = returnObj["uncovered"]
    return num
