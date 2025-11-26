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
