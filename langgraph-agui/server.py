from fastapi import FastAPI
from ag_ui_langgraph import AGUILangGraph
from agent import graph

app = FastAPI()

# Initialize AG-UI LangGraph integration
ag_ui = AGUILangGraph(graph=graph)

# Add AG-UI endpoints to the FastAPI app
app.include_router(ag_ui.router, prefix="/api/ag-ui")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
