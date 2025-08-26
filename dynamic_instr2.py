# Exercise 2: Airline Seat Preference Agent (Intermediate-Advanced)
# Requirement: Build a dynamic instructions system for an airline booking agent that customizes responses based on seat_preference and travel_experience.

# Window + First-time: Explain window benefits, mention scenic views, reassure about flight experience Middle + Frequent: Acknowledge the compromise, suggest strategies, offer alternatives Any + Premium: Highlight luxury options, upgrades, priority boarding

# Context Fields: seat_preference (window/aisle/middle/any), travel_experience (first_time/occasional/frequent/premium)


from agents import Agent, RunContextWrapper, Runner, trace
from pydantic import BaseModel
import asyncio
from connection import config

class Passenger(BaseModel):
    seat_preference: str 
    travel_experience: str

async def airline_dynamic_instructions(ctx: RunContextWrapper[Passenger], agent: Agent):
    seat = ctx.context.seat_preference
    exp = ctx.context.travel_experience

    if seat == "window" and exp == "first_time":
        return "Explain window benefits, scenic views, and reassure about first flight."
    
    elif seat == "middle" and exp == "frequent":
        return "Acknowledge middle seat issues, suggest strategies, and offer alternatives."
    
    elif seat == "any" and exp == "premium":
        return "Highlight luxury options, upgrades, and priority boarding."
    
    else:
        return "Give general helpful advice about seat selection."


airline_agent = Agent(
    name="AirlineAgent",
    instructions=airline_dynamic_instructions,
)

async def main():
    passenger = Passenger(seat_preference="window", travel_experience="first_time")

    with trace("Airline Seat Preference Agent"):
        result = await Runner.run(
            airline_agent,
            "Can you suggest a good seat for me?",
            context=passenger
        )
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
