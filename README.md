# Social Media Engagement Insights Using LangFlow and Astra DB

## Project Overview
This project focuses on creating a streamlined solution to analyze and visualize engagement data from social media platforms. By integrating Astra DB for data storage and OpenAI's capabilities for insights, the project leverages LangFlow as the central tool to orchestrate the data flow and interaction. Users can easily query and visualize metrics such as average likes, shares, and comments for different types of posts, enabling actionable insights for content optimization and audience engagement.
You can alse checkout the video of the project [here](https://www.youtube.com/watch?v=Z6Q6wQ5Q6

## Problem Statement
Social media platforms generate an overwhelming amount of engagement data, which can be challenging to analyze efficiently. This project addresses the need for a system that can:

1. **Store engagement data** in a scalable and accessible format. You can see the mock data from the file `social_media_data.csv`.
2. **Provide insights** such as average engagement metrics for various post types.
3. **Simplify workflows** by using a visual interface for data flow and interaction.
4. **Enable seamless integration** of external tools like OpenAI for advanced analytics.

Using LangFlow, Astra DB, and OpenAI, this project creates a user-friendly interface to solve the problem of extracting meaningful insights from raw social media engagement data.

---
### How It Works
1. **Input Prompt**: The user provides a query, such as asking for engagement metrics for a specific post type (e.g., "carousel").
2. **Data Retrieval (Astra DB Tool)**: LangFlow uses the Astra DB integration to fetch the relevant data (likes, shares, comments) for the specified post type.
3. **Data Processing (OpenAI Agent)**: The retrieved data is sent to the OpenAI agent via LangFlow's tool terminal for advanced analysis.
4. **Output**: The OpenAI agent generates insights, which are then displayed to the user in the chat interface.

This streamlined workflow eliminates the complexity of manual data querying and processing, enabling seamless data analysis and visualization.


---

## LangFlow Installation Using `uv` Library

Follow the steps below to set up LangFlow with the help of the `uv` library for enhanced package management:

1. **Install the `uv` library:**  
   ```bash
   pip install uv
   ```

2. **Install LangFlow using `uv`:**  
   ```bash
   uv pip install langflow
   ```

3. **Verify the installation:**  
   Ensure LangFlow is installed correctly by running:  
   ```bash
   langflow --version
   ```

---

## Running LangFlow

1. **Start the LangFlow server:**  
   ```bash
   langflow run
   ```

2. **Access the LangFlow UI:**  
   Open your browser and navigate to `http://localhost:7860`.

---

## Setting Up Your Flow

1. **Create a new flow:**
   - Open the LangFlow UI.
   - Click on "Create Blank Flow."

2. **Import the provided JSON file:**
   - Click on the "Import" button in the LangFlow UI.
   - Upload the provided `open_ai_langflow_social_media_insights.json` file.

3. **Configure API Keys:**
   - Replace placeholders in the flow with your Astra DB API endpoint and OpenAI API key.

4. **Save and Run the Flow:**
   - Save the flow and start interacting with it.

---

## Usage Instructions

- **Input:** Provide a post type (e.g., "carousel") to analyze.
- **Data Processing:** The system retrieves engagement data from Astra DB and sends it to OpenAI for analysis.
- **Output:** Receive insights such as average likes, shares, and comments.

---

## Troubleshooting

1. **LangFlow not starting:**
   - Ensure all dependencies are installed and your environment is active.

2. **Empty collections in Astra DB:**
   - Verify that your data has been inserted into the database.

3. **API errors:**
   - Ensure your Astra DB and OpenAI API keys are correctly configured.

---

## Conclusion
This project demonstrates the power of integrating LangFlow, Astra DB, and OpenAI to create a robust solution for social media engagement analysis. By following the steps outlined, users can replicate and adapt the system for their own use cases.


## License
This project is licensed under the APACHE 2.0 License.

