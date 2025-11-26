import "@copilotkit/react-ui/styles.css";
import { CopilotSidebar } from "@copilotkit/react-ui";

export default function Home() {
    return (
        <main>
            <h1>Your main content</h1>
            <CopilotSidebar
                labels={{
                    title: "Popup Assistant",
                    initial: "こんにちは",
                }}
            />
        </main>
    );
}
