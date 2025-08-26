# Exercise 1: Medical Consultation Assistant (Intermediate)
# Requirement: Create a dynamic instructions system for a medical consultation agent that adapts based on user_type.
# Patient: Use simple, non-technical language. Explain medical terms in everyday words. Be empathetic and reassuring. Medical Student: Use moderate medical terminology with explanations. Include learning opportunities. Doctor: Use full medical terminology, abbreviations, and clinical language. Be concise and professional.

from agents import Agent, RunContextWrapper, Runner, trace
from pydantic import BaseModel
from connection import config
import asyncio

class User(BaseModel):
    name: str
    user_type: str  
    
    
async def medical_instructions(ctx: RunContextWrapper[User], agent: Agent):
    if ctx.context.user_type == "patient":
        return "Use simple language, explain medical terms, be kind and reassuring."
    elif ctx.context.user_type == "medical_student":
        return "Use some medical terms, explain them, and add learning points."
    elif ctx.context.user_type == "doctor":
        return "Use clinical language, abbreviations, and be concise."


medical_agent = Agent(
    name="Medical Consultation Assistant",
    instructions=medical_instructions,
)


async def main():
    user = User(name="Ali", user_type="patient")

    with trace("Medical Assistant"):
        result = await Runner.run(
            medical_agent,
            "What is diabetes?",
            run_config=config,
            context=user
        )
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
