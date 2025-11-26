参考: https://zenn.dev/soundtricker/articles/03f39dbcab4ab6

# install

```
npx create-next-app@latest
npm install @copilotkit/react-ui @copilotkit/react-core @copilotkit/runtime
```

# debug

- .env で渡せているはずなのに, errorになる

```
litellm.exceptions.AuthenticationError: litellm.AuthenticationError: AuthenticationError: OpenAIException - Incorrect API key provided: sk-proj-********************************************************************************************************************************************************WZcA. You can find your API key at https://platform.openai.com/account/api-keys.
```
- 以下を実行すると動く
```
export OPENAI_API_KEY="sk-proj-***"
```

- chatで2回目のやり取りをしようとすると止まる

<img width="1468" height="718" alt="スクリーンショット 2025-11-26 23 43 46" src="https://github.com/user-attachments/assets/57a42984-0ea5-465c-a535-98a4f88d704a" />
