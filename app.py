"""
FastAPI application for the Indian Festival Chatbot web interface.
"""

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from festival_chatbot import FestivalChatbot
import json
import uvicorn
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Indian Festival Chatbot")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Initialize chatbot
chatbot = FestivalChatbot()

@app.get("/", response_class=HTMLResponse)
async def get_chat_page(request: Request):
    """
    Serve the main chat interface.
    """
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "ws_url": os.environ.get("VERCEL_URL", "localhost:8000")
    })

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for handling chat messages.
    """
    await websocket.accept()
    logger.info("WebSocket connection established")
    
    try:
        while True:
            try:
                # Receive message from client
                message = await websocket.receive_text()
                logger.info(f"Received message: {message}")
                
                # Get response from chatbot
                response = chatbot.process_query(message)
                logger.info(f"Chatbot response: {response}")
                
                # Send response back to client
                await websocket.send_text(json.dumps({
                    "message": message,
                    "response": response
                }))
                
            except WebSocketDisconnect:
                logger.info("WebSocket disconnected")
                break
            except Exception as e:
                logger.error(f"Error processing message: {str(e)}")
                await websocket.send_text(json.dumps({
                    "error": "Sorry, I encountered an error processing your message. Please try again."
                }))
                
    except Exception as e:
        logger.error(f"WebSocket error: {str(e)}")
    finally:
        try:
            await websocket.close()
            logger.info("WebSocket connection closed")
        except:
            pass

# Only run the server if this file is run directly
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port) 