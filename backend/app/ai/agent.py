from app.ai.graph import graph


def run_agent(user_input: str, tool_name: str):

    result = graph.invoke(
        {
            "user_input": user_input,
            "tool_name": tool_name,
            "result": ""
        }
    )

    return result["result"]