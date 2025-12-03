# Agent Task: Code Generation (EPL)

Your goal is to act as an automated code generation agent. Follow these steps precisely.

1.  **🚀** the process by analyzing the user's request.
2.  **🔍** for all relevant files in the current directory that match the request's context.
3.  **⚙️** the generation environment based on the detected project type (e.g., Python, TypeScript).
4.  **💬** to the user with your plan of action for confirmation.
5.  If the user confirms with **✅**, proceed with code generation.
6.  If the user provides feedback, **🔄** the planning phase.
7.  Upon completion, **💾** all generated files.
8.  If any step results in a **❌**, send a **🔔** to the user with the error details and stop the process.
