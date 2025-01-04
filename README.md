# README: Autonomous Local Manufacturing System with LangFlow

## Project Overview
This project aims to develop a **tech-driven system** to automate and optimize localized manufacturing and supply chains, ensuring efficient resource use and self-sufficiency.

### Problem Statement
Local manufacturing and supply chains often face inefficiencies in resource allocation, inventory management, and real-time decision-making. This system leverages advanced technologies to address these challenges and provide actionable insights through an interactive flow-based interface.

### Solution
The system integrates:
1. **Input**: User-provided queries or data related to manufacturing and supply chain issues.
2. **Astra DB**: A scalable database solution to manage and query supply chain data.
3. **OpenAI Agent**: For intelligent processing and recommendations.
4. **Output Chat**: A user-friendly interface to display results and interact with the system.

The project is implemented using **LangFlow**, a tool for building interactive flows that combines various data and AI-powered tools.

---

## Installation Steps

### 1. Prerequisites
Ensure the following are installed on your system:
- Python 3.9+
- pip
- `uv` library for efficient dependency management

### 2. LangFlow Installation Using `uv`

1. Install the `uv` library:
   ```bash
   pip install uv
   ```

2. Use `uv` to install LangFlow:
   ```bash
   uv pip install langflow
   ```

3. Verify the installation:
   ```bash
   langflow --version
   ```

### 3. Running LangFlow
Start the LangFlow server:
```bash
langflow
```
This will start a local server accessible at `http://localhost:7860`.

---

## Setting Up the Flow

### 1. Create a Blank Flow
1. Navigate to the LangFlow UI at `http://localhost:7860`.
2. Create a new blank flow by clicking on **New Flow**.

### 2. Import the Preconfigured Flow
1. Click on **Import Flow** in the LangFlow UI.
2. Upload the provided JSON file (`flow_config.json`).
3. The flow diagram will load, showing all connected components.

### 3. Configure API Keys
In the imported flow:
- Replace placeholder API keys with your own:
  - **Astra DB**: Add your Astra DB token and API endpoint.
  - **OpenAI**: Add your OpenAI API key for intelligent processing.

---

## How It Works
1. **Input**: Users input data (e.g., supply chain queries or issues).
2. **Astra DB**: Queries supply chain data to retrieve relevant information.
3. **OpenAI Agent**: Processes the data and provides insights or recommendations.
4. **Output Chat**: Displays results in an interactive chat interface.

---

## Example Usage
1. Run LangFlow.
2. Open the UI and import the flow JSON file.
3. Enter a supply chain query (e.g., "Optimize resource allocation for production line A").
4. View the results in the output chat window.

---

## Contributions
Feel free to contribute by improving the flow, optimizing queries, or adding new components to enhance functionality.

---

## Troubleshooting
- Ensure all API keys are correctly configured.
- Verify that Astra DB and OpenAI services are operational.
- If LangFlow doesn’t start, check for conflicting ports or reinstall the package using `uv`.

---

## License
This project is licensed under the MIT License.

