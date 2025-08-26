# Exercise 3: Travel Planning Assistant (Intermediate-Advanced)
# Requirement: Build a dynamic instructions system for a travel planning agent that customizes recommendations based on trip_type and traveler_profile.

# Adventure + Solo: Suggest exciting activities, focus on safety tips, recommend social hostels and group tours for meeting people. Cultural + Family: Focus on educational attractions, kid-friendly museums, interactive experiences, family accommodations. Business + Executive: Emphasize efficiency, airport proximity, business centers, reliable wifi, premium lounges. medical_student/doctor

from agents import Agent, RunContextWrapper, Runner, trace
from pydantic import BaseModel
import asyncio
from connection import config


class Traveler(BaseModel):
    trip_type: str          
    traveler_profile: str    


async def travel_dynamic_instructions(ctx: RunContextWrapper[Traveler], agent: Agent):
    trip = ctx.context.trip_type
    profile = ctx.context.traveler_profile

    if trip == "adventure" and profile == "solo":
        return "Suggest exciting activities, include safety tips, recommend hostels and group tours to meet people."

    elif trip == "cultural" and profile == "family":
        return "Focus on educational attractions, kid-friendly museums, interactive experiences, and family accommodations."

    elif trip == "business" and profile == "executive":
        return "Emphasize efficiency, airport proximity, business centers, reliable wifi, and premium lounges."

    elif profile in ["medical_student", "doctor"]:
        return "Provide health-related travel tips, nearby hospitals or clinics, and balanced travel-work suggestions."

    else:
        return "Give general travel advice suitable for the situation."


travel_agent = Agent(
    name="TravelAgent",
    instructions=travel_dynamic_instructions,
)


async def main():
    traveler = Traveler(trip_type="adventure", traveler_profile="solo")

    with trace("Travel Planning Assistant"):
        result = await Runner.run(
            travel_agent,
            "Can you plan my trip?",
            context=traveler
        )
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
