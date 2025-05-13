"""
Indian Festival Chatbot
A simple chatbot that provides information about Indian festivals across different states and regions,
including traditional attire and how to wear them.
"""

from festival_data import FESTIVAL_DATABASE, FESTIVAL_KEYWORDS, TRADITIONAL_ATTIRE_DB, ATTIRE_KEYWORDS
import re
from typing import Optional, List, Dict, Any
import textwrap

class FestivalChatbot:
    def __init__(self):
        self.festival_db = FESTIVAL_DATABASE
        self.keywords = FESTIVAL_KEYWORDS
        self.attire_db = TRADITIONAL_ATTIRE_DB
        self.attire_keywords = ATTIRE_KEYWORDS
        self.exit_commands = {'quit', 'exit', 'bye', 'goodbye', 'stop'}
        self.help_commands = {'help', 'commands', 'what can you do', 'how to use'}
        self.dress_keywords = {'dress', 'clothes', 'attire', 'wear', 'wearing', 'outfit', 'traditional dress', 
                             'traditional clothes', 'how to wear', 'how to dress', 'what to wear'}
        
    def wrap_text(self, text: str, width: int = 70) -> str:
        """
        Wrap text to a specific width for better formatting.
        """
        return '\n'.join(textwrap.wrap(text, width=width))

    def find_attire_match(self, query: str) -> Optional[str]:
        """
        Find the best matching traditional attire based on the user's query.
        Returns the attire key if found, None otherwise.
        """
        query = query.lower().strip()
        
        # Direct match with attire names
        for attire_key, attire_data in self.attire_db.items():
            if attire_data['name'].lower() in query:
                return attire_key
        
        # Match with keywords
        for attire_key, keywords in self.attire_keywords.items():
            if any(keyword in query for keyword in keywords):
                return attire_key
        
        return None

    def format_attire_info(self, attire_key: str) -> str:
        """
        Format the traditional attire information into a readable string.
        """
        attire = self.attire_db[attire_key]
        types = '\n'.join(f"   • {t}" for t in attire['types'])
        
        return f"""
👗 {attire['name']} 👗

📝 Description:
{self.wrap_text(attire['description'])}

📋 How to Wear:
{self.wrap_text(attire['how_to_wear'])}

🎨 Types:
{types}

🎯 Suitable Occasions:
{self.wrap_text(attire['occasions'])}

💡 Tip: This attire is commonly worn during various Indian festivals and ceremonies.
"""

    def find_festival_match(self, query: str) -> Optional[str]:
        """
        Find the best matching festival based on the user's query.
        Returns the festival key if found, None otherwise.
        """
        query = query.lower().strip()
        
        # Direct match with festival names
        for festival_key, festival_data in self.festival_db.items():
            if festival_data['name'].lower() in query:
                return festival_key
        
        # Match with keywords
        for festival_key, keywords in self.keywords.items():
            if any(keyword in query for keyword in keywords):
                return festival_key
        
        return None

    def format_festival_info(self, festival_key: str, is_dress_query: bool = False) -> str:
        """
        Format the festival information into a readable string.
        If is_dress_query is True, focus on dress information.
        """
        festival = self.festival_db[festival_key]
        states = ', '.join(festival['states'])
        
        if is_dress_query:
            return f"""
🎉 {festival['name']} - Traditional Attire 🎉

👗 For Women:
📌 Traditional Dress: {festival['traditional_dress']['women']['name']}
📝 How to Wear: {self.wrap_text(festival['traditional_dress']['women']['description'])}
🎨 Popular Colors: {festival['traditional_dress']['women']['colors']}

👔 For Men:
📌 Traditional Dress: {festival['traditional_dress']['men']['name']}
📝 How to Wear: {self.wrap_text(festival['traditional_dress']['men']['description'])}
🎨 Popular Colors: {festival['traditional_dress']['men']['colors']}

💡 Tip: These are traditional styles, but modern variations are also popular.
"""
        else:
            return f"""
🎉 {festival['name']} 🎉

📍 Popular in: {states}
📅 Celebrated in: {festival['month']}
📝 About: {self.wrap_text(festival['description'])}

💃 Want to know about traditional attire? Ask "What to wear for {festival['name']}?" or "Tell me about {festival['name']} dress"
"""

    def get_help_message(self) -> str:
        """
        Return a help message explaining how to use the chatbot.
        """
        return """
🤖 Welcome to the Indian Festival Chatbot! 🤖

I can tell you about various Indian festivals and traditional attire across different states and regions.

Here's how you can interact with me:

1. Ask about festivals:
   • "Tell me about Diwali"


2. Ask about traditional attire:
   • "What to wear for Holi?"
   • "Tell me about Onam dress"
   • "What is a saree?"
   • "How to wear a kurta?"

3. General commands:
   • Type 'help' to see this message again
   • Type 'quit' or 'exit' to end the conversation

Some example festivals I know about:
• Diwali
• Holi
• Pongal
• Onam
• Durga Puja
• Ganesh Chaturthi
• Eid
• Christmas
And many more!

What would you like to know about?
"""

    def get_festivals_by_month(self, month: str) -> List[str]:
        """
        Find festivals that occur in a specific month.
        """
        month = month.lower()
        matching_festivals = []
        
        for festival_key, festival_data in self.festival_db.items():
            festival_month = festival_data['month'].lower()
            if month in festival_month:
                matching_festivals.append(festival_key)
        
        return matching_festivals

    def get_festivals_by_state(self, state: str) -> List[str]:
        """
        Find festivals that are popular in a specific state.
        """
        state = state.lower()
        matching_festivals = []
        
        for festival_key, festival_data in self.festival_db.items():
            states = [s.lower() for s in festival_data['states']]
            if state in states or 'all india' in states:
                matching_festivals.append(festival_key)
        
        return matching_festivals

    def is_dress_query(self, query: str) -> bool:
        """
        Check if the query is about traditional dress.
        """
        query = query.lower()
        return any(keyword in query for keyword in self.dress_keywords)

    def process_query(self, query: str) -> str:
        """
        Process the user's query and return an appropriate response.
        """
        query = query.lower().strip()
        
        # Check for exit commands
        if query in self.exit_commands:
            return "Thank you for chatting! Have a great day! 👋"
        
        # Check for help commands
        if query in self.help_commands:
            return self.get_help_message()
        
        # Check for traditional attire queries
        attire_key = self.find_attire_match(query)
        if attire_key:
            return self.format_attire_info(attire_key)
        
        # Check for month-based queries
        month_pattern = r"(?:festivals?|celebrations?) (?:in|during|of) (\w+)"
        month_match = re.search(month_pattern, query)
        if month_match:
            month = month_match.group(1)
            festivals = self.get_festivals_by_month(month)
            if festivals:
                response = f"Here are the festivals celebrated in {month.title()}:\n"
                for festival in festivals:
                    response += f"\n• {self.festival_db[festival]['name']}"
                return response
            return f"I don't have information about festivals in {month.title()}."

        # Check for state-based queries
        state_pattern = r"(?:festivals?|celebrations?) (?:in|of|from) (\w+(?:\s+\w+)*)"
        state_match = re.search(state_pattern, query)
        if state_match:
            state = state_match.group(1)
            festivals = self.get_festivals_by_state(state)
            if festivals:
                response = f"Here are the festivals celebrated in {state.title()}:\n"
                for festival in festivals:
                    response += f"\n• {self.festival_db[festival]['name']}"
                return response
            return f"I don't have information about festivals in {state.title()}."

        # Check for specific festival queries
        festival_key = self.find_festival_match(query)
        if festival_key:
            is_dress_query = self.is_dress_query(query)
            return self.format_festival_info(festival_key, is_dress_query)
        
        # Fallback response for unknown queries
        return """
I'm not sure I understand. You can:

1. Ask about festivals:
   • "Tell me about Diwali"


2. Ask about traditional attire:
   • "What is a saree?"
   • "How to wear a kurta?"
   • "Tell me about lehenga"

3. Type 'help' for more information
"""