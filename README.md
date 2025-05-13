# Indian Festival Chatbot

A web-based chatbot that provides information about Indian festivals, traditional attire, and cultural practices. The chatbot uses a simple keyword-based matching system to provide relevant information about various Indian festivals and their associated traditions.

## Features

- Information about major Indian festivals
- Details about traditional attire
- Real-time chat interface
- Responsive web design
- WebSocket-based communication
- No external API dependencies

## Setup

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app:app --reload
   ```

4. Open your web browser and navigate to:
   ```
   http://localhost:8000
   ```

## Project Structure

- `app.py` - FastAPI application and WebSocket handling
- `festival_chatbot.py` - Core chatbot logic
- `festival_data.py` - Festival database and keywords
- `templates/chat.html` - Web interface
- `requirements.txt` - Python dependencies

## Usage

1. Type your question in the chat input box
2. Press Enter or click the Send button
3. The chatbot will respond with relevant information

Example queries:
- "Tell me about Diwali"
- "What is Holi?"
- "What should I wear for Diwali?"
- "Help"

## Development

The chatbot uses a simple keyword-based matching system. To add more festivals or modify existing ones, edit the `FESTIVAL_DATABASE` and `FESTIVAL_KEYWORDS` in `festival_data.py`.

## License

This project is open source and available under the MIT License.

## Deployment

You can deploy this FastAPI chatbot to platforms like Render, Railway, or Heroku.

### 1. Render
- Connect your GitHub repo to Render.
- Add a web service with the start command:
  ```
  uvicorn app:app --host 0.0.0.0 --port $PORT
  ```

### 2. Railway
- Connect your repo and set the start command as above.

### 3. Heroku
- Add a `Procfile` with:
  ```
  web: uvicorn app:app --host=0.0.0.0 --port=${PORT:-8000}
  ```
- Push to Heroku and it will auto-detect and install from `requirements.txt`.

### Notes
- Make sure your `static` and `templates` folders are committed to your repo.
- The app will be available at the root URL (`/`).
- WebSocket endpoint is `/ws/chat`.

---

For local development:
```
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```
Then open [http://localhost:8000](http://localhost:8000) in your browser. 