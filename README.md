# Mindcase Legal Chatbot
-----------------------------

## 1. Dependencies and Installation

To set up the Mindcase legal chatbot on your system, please follow these steps:

1. Clone the repository to your local machine.
```
   git clone https://github.com/samridhikapoor/Mindcase.git
```

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
OPENAI_API_KEY=your_secret_api_key
```

## 2. Usage

To use the Mindcase Legal chatbot, follow these steps:

1. Ensure that you have installed the required dependencies (from requirements.txt) and added the OpenAI API key to the `.env` file.

2. Run the `app.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Load multiple PDF documents into the app by following the provided instructions by clicking on `Browse`.

5. Click on the `Process` button.

6. Type your questions in the input box and interact with the chatbot
