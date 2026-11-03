# Coffee Shop AI Assistant

A terminal chatbot that answers questions about a coffee shop menu. I built it after
finishing the DeepLearning.AI course "Building Systems with the ChatGPT API". It's one of
my first AI projects, so it's small on purpose.

## How it works
1. The user input is checked with the OpenAI Moderation API.
2. A classifier prompt checks for prompt injection attempts (Y/N).
3. An extraction prompt turns the question into a JSON list of menu items or categories.
4. Plain Python looks those up in the menu.
5. The assistant answers using only the menu data it was given.
6. The answer is checked with the Moderation API before it is shown.

API errors are caught, so the bot keeps running if a call fails.

## Run it
1. Create a virtual environment and install the dependencies:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2. Create a `.env` file in the project folder with your key:

OPENAI_API_KEY=your-key

3. Start the chatbot (type `quit` to exit):

python main.py

The model name is set in one place (`MODEL` in `main.py`). If it gets deprecated,
change it there.

## Evaluation
`evaluate.py` runs the extraction step on a list of test questions and prints the
result next to the expected one, so I can check by eye whether a prompt change broke
anything. Run it with `python evaluate.py`. Automatic scoring is on my to-do list.

## Known limitations
- Questions without a name or category ("cheapest drink", "anything vegan") are not supported yet.
- Menu data stays in the chat history every turn, so long chats get bigger.
- The injection classifier only sees the latest message, so an attack spread over several messages could get through.
- Prompts are only a request to the model, so none of these checks are a guarantee.

## What I'd add next
- Filters for price and vegan options
- Automatic scoring in the evaluation script
- Taking orders