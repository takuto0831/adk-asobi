from agent import graph

# Graphの実行
result = graph.invoke({"messages": ["100掛ける200の計算と1足す2の計算をそれぞれしてください"]})

# 結果表示
print(result)
