from dotenv import load_dotenv
from typing import TypedDict
from typing import Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# .envファイルから環境変数を読み込む
load_dotenv()

# toolの定義
@tool
def multiply_function(x: int, y: int) -> int:
    """
    2つのint型の値を引数で受け取り、掛け算の結果をint型で返す

    Args:
        x (int): 1つ目のint型の引数
        y (int): 2つ目のint型の引数

    Returns:
        int: x * y
    """
    return x * y

# toolの定義
@tool
def add_function(x: int, y: int) -> int:
    """
    2つのint型の値を引数で受け取り、足し算の結果をint型で返す

    Args:
        x (int): 1つ目のint型の引数
        y (int): 2つ目のint型の引数

    Returns:
        int: x + y
    """
    return x + y

# ツールの辞書作成
tools_dict = {
    "multiply_function": multiply_function,
    "add_function": add_function
}

# モデル設定
llm = ChatOpenAI(model="gpt-4o-mini")
# toolsの作成
tools = [multiply_function, add_function]
# toolsの紐づけ
llm_with_tools = llm.bind_tools(tools)

# Stateの定義
class State(TypedDict):
    messages: Annotated[list, add_messages]

# chatbotのNodeを定義
def chatbot(state: State):
    # LLMが有効なtoolを選択して生成した回答でStateを更新
    result = llm_with_tools.invoke(state["messages"])
    return {"messages": [result]}

# toolのNodeを定義
def tool_node(state: State):
    # 最後のメッセージを取得
    last_message = state["messages"][-1]
    # 実行結果を保存するためのリスト
    messages = []
    for tool_call in last_message.tool_calls:
        # toolの実行
        tool_output = tools_dict[tool_call["name"]].invoke(tool_call["args"])
        # toolの結果を使用してToolMessageの作成
        tool_messages = ToolMessage(
            content=tool_output,
            name=tool_call["name"],
            tool_call_id=tool_call["id"],
        )
        # ToolMessageをmessagesリストに追加
        messages.append(tool_messages)
    # Stateを更新可能な辞書型を返す
    return {"messages": messages}

# 条件分岐を判断する関数を定義
def router(state: State):
    # 最後のメッセージを取得
    last_message = state["messages"][-1]
    # 最後のメッセージにtool_callsが存在するか判定
    if last_message.tool_calls:
        # tool_callsが存在する場合、"tool"を返す
        return "tool"
    else:
        # それ以外の場合、"end"を返す
        return "end"

# Graphの初期化
graph_builder = StateGraph(State)

# chatbot Nodeの追加
graph_builder.add_node("chatbot", chatbot)
# tool Nodeの追加
# Note: Renamed function to tool_node to avoid conflict with @tool decorator if imported or confusion
graph_builder.add_node("tool", tool_node)

# 条件付きEdgeの追加
graph_builder.add_conditional_edges(
    # 遷移元のNode名を設定
    "chatbot",
    # 条件分岐を判断する関数を設定
    router,
    # routerの戻り値によって遷移先のNodeを決める
    {
        # "tool"の場合、tool Nodeに遷移
        "tool": "tool",
        #"end"の場合、END Nodeに遷移
        "end": END
    }
)

# tool Nodeからchatbot NodeへのEdgeを追加
graph_builder.add_edge("tool", "chatbot")
# STARTからchatbot NodeへのEdgeを追加
graph_builder.add_edge(START, "chatbot")

# Graphのコンパイル
graph = graph_builder.compile()
