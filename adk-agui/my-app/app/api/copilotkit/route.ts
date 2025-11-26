

import {
    CopilotRuntime,
    ExperimentalEmptyAdapter,
    copilotRuntimeNextJSAppRouterEndpoint,
} from "@copilotkit/runtime";
import { HttpAgent } from "@ag-ui/client";
import { NextRequest } from "next/server";
// 1. マルチエージェントサポートのために、任意のサービスアダプタを使用できます。
// エージェントは1つだけなので、空のアダプタを使用します。
const serviceAdapter = new ExperimentalEmptyAdapter();
// 2. CopilotRuntime インスタンスを作成し、ADK AG-UI 統合を利用して接続をセットアップします。
const runtime = new CopilotRuntime({
    agents: {
        // Our AG-UI endpoint URL
        "myAgent": new HttpAgent({ url: "http://localhost:8000/" }),
    }
});
// 3. Next.js APIを実装
export const POST = async (req: NextRequest) => {
    const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
        runtime,
        serviceAdapter,
        endpoint: "/api/copilotkit",
    });
    return handleRequest(req);
};
