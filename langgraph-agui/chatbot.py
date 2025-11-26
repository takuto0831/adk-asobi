from dotenv import load_dotenv
from typing import TypedDict
from typing import Annotated
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# .envファイルから環境変数を読み込む
load_dotenv()

# モデル設定
llm = ChatOpenAI(model="gpt-4.1")

# Stateの定義
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Nodeの定義
def chatbot(state: State):
    # LLMが生成した回答でStateを更新
    return {"messages": [llm.invoke(state["messages"])]}

# Graphの初期化
graph_builder = StateGraph(State)

# Nodeの追加
graph_builder.add_node("chatbot", chatbot)

# Node間を接続するEdgeの追加
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Graphのコンパイル
graph = graph_builder.compile()

# Graphの実行
result = graph.invoke({"messages": ["こんにちは"]})

# 結果表示
print(result)
