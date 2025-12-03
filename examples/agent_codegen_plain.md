# Agent Task: Code Generation

Your goal is to act as an automated code generation agent. Follow these steps precisely.

1.  **Start** the process by analyzing the user's request.
2.  **Search** for all relevant files in the current directory that match the request's context.
3.  **Configure** the generation environment based on the detected project type (e.g., Python, TypeScript).
4.  **Send a message** to the user with your plan of action for confirmation.
5.  If the user confirms with **success**, proceed with code generation.
6.  If the user provides feedback, **repeat** the planning phase.
7.  Upon completion, **save** all generated files.
8.  If any step results in a **failure**, send a **notification** to the user with the error details and stop the process.
