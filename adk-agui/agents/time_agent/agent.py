import datetime

from ag_ui.core import RunAgentInput
from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint
from fastapi import FastAPI
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

import dotenv

dotenv.load_dotenv()

async def now_tool():
    """
    Return the current date time.
    """
    return datetime.datetime.now(tz=datetime.timezone.utc).isoformat()

root_agent = Agent(
    model=LiteLlm(model="openai/gpt-4.1"),
    name='root_agent',
    description='The Clock Agent',
    instruction="""
    You are clock agent. Your task is return current time using `now_tool`.
    """,
    tools=[now_tool]
)

# ユーザーIDの取得
def extract_user(input: RunAgentInput) -> str:
    # Extract from context
    for ctx in input.context:
        if ctx.description == "user":
            return ctx.value
    return f"anonymous_{input.thread_id}"

adk_agent_sample = ADKAgent(
    adk_agent=root_agent,
    app_name="demo_app",
    user_id_extractor=extract_user,
    session_timeout_seconds=3600,
    use_in_memory_services=True
)

app = FastAPI(title="Time Agent App")
add_adk_fastapi_endpoint(app, adk_agent_sample, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
