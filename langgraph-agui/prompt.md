目的
- ag_ui (https://github.com/ag-ui-protocol/ag-ui) と langgraph を用いた chat アプリケーションを実装する
- agent の部分と uiの開発の部分を切り離した適切な設計を作成する

環境
- uv を利用しています
- 各モジュールのversionは pyproject.toml を参照してください

検証済みの事項
- uv run chatbot_tools.py によって lagngraph のcodeについては動くことを確認しました。

やること
- chatbot_tools.py は agent の定義と、agent の実行が1つになっているのでまずは分離して agent の1つのmodelとしてください。
- ag_ui によりシンプルなuiを実装し、その中で分離した chatbot_toolsの機能を使えるようにしてください。
- agentの実装と uiの開発の部分を切り離した設計で開発を行ってください。今後のagent実装の充実とui開発の充実を分離して進められるようにしたいためです
