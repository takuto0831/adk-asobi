目的
- agent development kit による file操作のagentと human-in-the-loop の実装を試す

仕様
- agent は、docs/ 以下にファイルを作成、編集、削除することができる
- agent は docs/ 以下のファイルを削除、編集するときに、既存のファイルがあるかを確認して、ファイルが存在する場合にはユーザにそのまま作業を進めていいか確認する。
- ユーザへの確認は以下の例にある、require_confirmationを使用し、confirmation_criteriaとしては指定したfileが存在するか? を検証する

- human in the loop の利用例
```
def confirmation_criteria(order_items: dict[str, int]) -> bool:
  return calculate_total(order_items) > 100

root_agent = Agent(
    model='gemini-2.5-flash',
    name='fast_food_agent',
    instruction="""You help customers place orders at a restaurant.""",
    tools=[
        FunctionTool(place_order, require_confirmation=confirmation_criteria),
    ],
)
```
参考サイト: https://medium.com/google-cloud/2-minute-adk-human-in-the-loop-made-easy-da9e74d9845a

環境構築
- uvを使用しています
- python を利用します
- "uv add google-adk"　によって, google-adkはinstall済みです。
- script の実行などにも uv run を利用する想定です
- 必要なmoduleについても uv add を利用してください
