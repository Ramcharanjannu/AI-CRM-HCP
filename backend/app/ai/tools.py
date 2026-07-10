from langchain_core.tools import tool
from .groq_client import llm


@tool
def log_interaction(interaction: str) ->str:
    """
    Convert doctor's conversation into structured CRM notes.
    """

    prompt = f"""
You are an AI CRM assistant.

Convert the following doctor's interaction into CRM format.

Conversation:
{interaction}

Return:

Summary:
Sentiment:
Key Outcomes:
Follow-up Recommendation:
"""

    response = llm.invoke(prompt)

    return response.content


@tool
def edit_interaction(text:str)->str:
    """
    Edit an existing CRM interaction.
    """

    prompt=f"""
You are editing an existing CRM interaction.

Correct grammar.
Improve readability.
Keep all medical facts unchanged.

Interaction:

{text}
"""

    response=llm.invoke(prompt)

    return response.content


@tool
def search_hcp(name:str)->str:
    """
    Search Healthcare Professional.
    """

    prompt=f"""
Pretend you are an AI CRM.

Generate a realistic CRM search result for:

{name}

Include:

Doctor Name
Specialization
Hospital
Last Interaction
Overall Engagement
"""
    response=llm.invoke(prompt)

    return response.content


@tool
def generate_summary(notes: str) -> str:
    """
    Generate interaction summary.
    """

    prompt = f"""
    Summarize the following doctor's interaction in 4-5 professional sentences.

     Conversation:

    {notes}
    """

    response = llm.invoke(prompt)

    return response.content


@tool
def recommend_followup(notes: str) -> str:
    """
    Recommend next follow-up action.
    """

    prompt = f"""
    You are an AI Sales Assistant.

     Based on the interaction below recommend:

    1. Next action
    2. Best time to follow up
    3. Sales suggestion

    Interaction:

    {notes}
    """

    response = llm.invoke(prompt)

    return response.content


TOOLS = [
    log_interaction,
    edit_interaction,
    search_hcp,
    generate_summary,
    recommend_followup,
]