import gradio as gr
import google.generativeai as genai
import os

# ✅ Securely fetch Gemini API key (set as secret)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini 1.5 Flash model (fast, free)
model = genai.GenerativeModel("gemini-1.5-flash")

# Aidbyte chatbot persona
AIDBYTE_PROMPT = """
You are an AI assistant for Aidbyte, a student-led initiative based in India that helps NGOs and social impact groups grow using creative, accessible, and low-cost technology.

Aidbyte provides digital tools, automation systems, AI-powered features, and awareness platforms to organizations that often lack full-time tech support. Most services are free or symbolic in cost. Aidbyte does not rely on donations — instead, it helps NGOs generate passive revenue through creative and sustainable online systems.

Aidbyte supports:

    NGOs and grassroots initiatives

    Volunteer groups and student clubs

    Educational institutions

    Socially conscious individuals

Aidbyte offers:

    Website and tool development: custom NGO microsites, campaign pages, dashboards

    Creative monetization systems: survey-based earnings, affiliate platforms, "click-to-impact" tools

    AI tools: caption/poster generators, impact report writers, outreach planners

    Volunteer & automation support: digital certificate creators, data tracking systems, Google Forms integrations

    Resource kits: Canva templates, awareness packs, onboarding slides

Core principles:

    No reliance on direct donations

    Built and maintained by students

    Focused on real-world digital solutions

    Modular, flexible, and mission-driven

When users ask:

    "Can you help us earn money without donations?" → Yes, through surveys, affiliate tools, and engagement-based models

    "Can you help us build a tool or automate tasks?" → Yes, Aidbyte creates and customizes digital tools for outreach and operations

    "What does Aidbyte offer NGOs?" → A mix of tech tools, automation, and digital support, almost always free

    "Is Aidbyte free?" → Most services are completely free; some may involve symbolic cost when necessary

Contact Information:
🌐 Website: https://aidbyte.pages.dev
📸 Instagram: @aidbyte
📱 Mobile: coming soon
📧 Email: coming soon

Always respond in a friendly, supportive, and solution-oriented tone. Help users understand how Aidbyte can support their mission through technology — without needing traditional fundraising or costly platforms.
"""

# Chat function
def respond(message, history):
    # Convert chat history into a readable format
    chat_context = ""
    if history:
        for user_msg, bot_msg in history:
            chat_context += f"User: {user_msg}\nAidbyte AI: {bot_msg}\n"

    # Build full prompt with context and new user message
    full_prompt = f"{AIDBYTE_PROMPT}\n\n{chat_context}User: {message}\nAidbyte AI:"

    try:
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini error: {str(e)}"
# 🌌 Enhanced Chatbot UI with logo-inspired gradients
gr.ChatInterface(
    fn=respond,
    title="🌙 Aidbyte AI",
    description="Ask Aidbyte AI how we empower changemakers with free digital tools — no donations needed.",
    theme=gr.themes.Base(
        primary_hue="cyan",
        secondary_hue="purple",
        neutral_hue="slate",
        font=[gr.themes.GoogleFont("Inter"), gr.themes.GoogleFont("JetBrains Mono")],
        radius_size=gr.themes.sizes.radius_xxl,
        text_size=gr.themes.sizes.text_md,
        spacing_size=gr.themes.sizes.spacing_lg
    ),
    css="""
    /* Root variables inspired by your logo colors */
    :root {
        --gradient-primary: linear-gradient(135deg, #00d4ff 0%, #0099ff 25%, #6366f1 50%, #a855f7 75%, #ec4899 100%);
        --gradient-secondary: linear-gradient(45deg, #06b6d4 0%, #3b82f6 25%, #8b5cf6 50%, #d946ef 75%, #f97316 100%);
        --gradient-accent: linear-gradient(90deg, #14b8a6 0%, #06b6d4 20%, #3b82f6 40%, #8b5cf6 60%, #d946ef 80%, #f97316 100%);
        --bg-primary: #0a0a0a;
        --bg-secondary: #1a1a1a;
        --bg-tertiary: #2a2a2a;
        --text-primary: #ffffff;
        --text-secondary: #e5e7eb;
        --border-radius: 16px;
        --border-width: 1px;
    }

    /* Global background and text styling */
    body, .gradio-container {
        background: var(--bg-primary) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* Header styling */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        font-size: 2.5em !important;
        text-align: center !important;
        margin-bottom: 0.5em !important;
        text-shadow: 
            0 0 20px rgba(0, 212, 255, 0.6),
            0 0 40px rgba(139, 92, 246, 0.4),
            0 0 60px rgba(236, 72, 153, 0.2) !important;
    }

    /* Description text */
    .gr-box p, .description {
        color: var(--text-secondary) !important;
        text-align: center !important;
        font-size: 1.1em !important;
        line-height: 1.6 !important;
    }

    /* Main chat container - Remove borders */
    .gr-chatbox, .chatbot {
        background: var(--bg-secondary) !important;
        border: none !important;
        border-radius: var(--border-radius) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
        position: relative !important;
        overflow: hidden !important;
    }

    /* Chat messages container - Proper sizing */
    .gr-chatbox .message-wrap, .chatbot .message-wrap {
        background: transparent !important;
        border: none !important;
        border-radius: 0 !important;
        margin: 2px 0 !important;
        padding: 0 !important;
        width: 100% !important;
        display: flex !important;
        flex-direction: column !important;
    }

    /* Remove all borders from message elements */
    .message, .message > *, .message-wrap, .message-wrap > * {
        border: none !important;
        border-top: none !important;
        border-bottom: none !important;
        border-left: none !important;
        border-right: none !important;
    }

    /* Bot messages - No borders, responsive sizing */
    .message.bot, .bot {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #1a1a2e 100%) !important;
        border: none !important;
        color: var(--text-primary) !important;
        border-radius: 12px !important;
        padding: 10px 14px !important;
        margin: 6px 12px !important;
        max-width: min(75%, 600px) !important;
        min-width: min(200px, 50%) !important;
        width: fit-content !important;
        position: relative !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
        display: block !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.4 !important;
    }

    /* User messages - No borders, responsive sizing */
    .message.user, .user {
        background: linear-gradient(135deg, #2a1a2e 0%, #3e1640 50%, #2a1a2e 100%) !important;
        border: none !important;
        color: var(--text-primary) !important;
        border-radius: 12px !important;
        padding: 10px 14px !important;
        margin: 6px 12px 6px auto !important;
        max-width: min(75%, 600px) !important;
        min-width: min(200px, 50%) !important;
        width: fit-content !important;
        position: relative !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
        display: block !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.4 !important;
        text-align: left !important;
    }

    /* Override any potential inherited borders */
    .message-row, .chat-message, .chat-bubble {
        border: none !important;
        border-top: none !important;
        border-bottom: none !important;
    }

    /* Specific targeting for Gradio's chat interface structure */
    div[data-testid="chatbot"] > div, 
    div[data-testid="chatbot"] > div > div,
    div[data-testid="chatbot"] > div > div > div {
        border: none !important;
        border-top: none !important;
        border-bottom: none !important;
    }

    /* Input field styling */
    textarea, input[type="text"] {
        background: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        border: 1px solid #06b6d4 !important;
        border-radius: 12px !important;
        padding: 10px 14px !important;
        font-size: 1em !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
    }

    textarea:focus, input[type="text"]:focus {
        outline: none !important;
        border-color: #00d4ff !important;
        box-shadow: 
            0 0 10px rgba(0, 212, 255, 0.2),
            0 2px 8px rgba(0, 0, 0, 0.2) !important;
        transform: translateY(-1px) !important;
    }

    /* Primary buttons */
    .gr-button-primary, button[data-variant="primary"] {
        background: var(--gradient-primary) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        font-size: 1em !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3) !important;
        position: relative !important;
        overflow: hidden !important;
    }

    .gr-button-primary:hover, button[data-variant="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.4) !important;
    }

    /* Secondary buttons */
    .gr-button-secondary, button[data-variant="secondary"] {
        background: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        border: 1px solid #a855f7 !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }

    .gr-button-secondary:hover, button[data-variant="secondary"]:hover {
        background: var(--bg-tertiary) !important;
        border-color: #d946ef !important;
    }

    /* Container styling */
    .gr-box, .gr-form, .gr-panel {
        background: var(--bg-secondary) !important;
        border: 1px solid #14b8a6 !important;
        border-radius: var(--border-radius) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
        margin: 8px !important;
        padding: 16px !important;
    }

    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px !important;
    }

    ::-webkit-scrollbar-track {
        background: var(--bg-primary) !important;
        border-radius: 4px !important;
    }

    ::-webkit-scrollbar-thumb {
        background: var(--gradient-primary) !important;
        border-radius: 4px !important;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--gradient-secondary) !important;
    }

    /* Loading animation */
    .loading {
        background: var(--gradient-primary) !important;
        animation: shimmer 2s infinite linear !important;
    }

    @keyframes shimmer {
        0% { background-position: -200px 0; }
        100% { background-position: 200px 0; }
    }

    /* Floating animation for main container */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    .gr-chatbox:hover {
        animation: float 3s ease-in-out infinite !important;
    }

    /* Responsive design */
    @media (max-width: 1200px) {
        .message.bot, .message.user, .bot, .user {
            max-width: min(80%, 500px) !important;
        }
    }

    @media (max-width: 768px) {
        .gr-chatbox, .chatbot {
            margin: 8px !important;
            border-radius: 15px !important;
        }
        
        .message.bot, .message.user, .bot, .user {
            padding: 10px 14px !important;
            margin: 6px 8px !important;
            border-radius: 12px !important;
            max-width: min(85%, 320px) !important;
            min-width: min(150px, 40%) !important;
        }
    }

    @media (max-width: 480px) {
        .message.bot, .message.user, .bot, .user {
            padding: 8px 12px !important;
            margin: 4px 6px !important;
            max-width: min(90%, 280px) !important;
            min-width: min(120px, 35%) !important;
            font-size: 0.95em !important;
        }
        
        .gr-chatbox, .chatbot {
            margin: 4px !important;
        }
    }

    @media (max-width: 360px) {
        .message.bot, .message.user, .bot, .user {
            padding: 8px 10px !important;
            margin: 4px !important;
            max-width: 95% !important;
            min-width: min(100px, 30%) !important;
            font-size: 0.9em !important;
        }
    }

    /* Additional polish */
    .gr-app {
        background: var(--bg-primary) !important;
    }

    .gr-interface {
        background: var(--bg-primary) !important;
    }

    /* Status indicators */
    .gr-button:disabled {
        opacity: 0.6 !important;
        cursor: not-allowed !important;
    }

    /* Error messages */
    .error {
        color: #ff6b6b !important;
        background: linear-gradient(135deg, #2a1a1a 0%, #3a1a1a 100%) !important;
        border: 2px solid #ff6b6b !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }
    """
).launch()