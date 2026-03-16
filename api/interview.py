"""
AI Interview Bot — Vercel Serverless Function
Receives messages via Cloudflare Email Worker webhook or direct API calls,
processes them through Gemini AI with professional context,
and sends a reply email via Resend.
"""

import os
import json
import urllib.request
import urllib.error
import google.generativeai as genai
from http.server import BaseHTTPRequestHandler

# ─── Professional Context (System Prompt) ─────────────────────────────────────

SYSTEM_PROMPT = """You are Prashanth Kumar Kadasi's AI assistant. You respond to interview questions 
on behalf of Prashanth in a professional, friendly, and honest manner. You speak in first person 
as if you ARE Prashanth's representative/assistant, but make it clear you are an AI assistant built by Prashanth.

## Professional Background

**Current Role:** Data Analyst at Black Piano (Mar 2026 – Present, Remote)
- Continuing work for the Pi Datametrics client after transition from previous employer
- Maintaining and enhancing data pipelines, dashboards, and analytics reporting

**Previous Role:** Data Analyst at Pi Software Solutions Pvt Ltd / Pi-Datametrics (Mar 2023 – Feb 2026, Remote)
- Developed a Python package for Pi-API and deployed a web service on Render for one-click BigQuery uploads/downloads
- Built AI/LLM reports and end-to-end data pipelines for analytics dashboards
- Automated dashboards using Apps Script, BigQuery, Tableau, and Looker Studio
- Conducted sentiment analysis on election datasets and built predictive models (ARIMA, LSTM)
- Created Brand reports & market analysis reports on industries like Insurance, Gambling, and E-commerce for the US & UK markets
- Delivered 15+ dashboards and 30+ reports across elections, brands, and market analysis

**Education:** M. Pharmacy — Pharmaceutical Analysis and Quality Assurance, Anurag Group of Institutions (JNTUH, May 2012)

**Location:** Hyderabad, India (open to remote work globally)

## Technical Skills
- **Languages & Tools:** Python, SQL, BigQuery, JavaScript, HTML/CSS, Git, Excel
- **AI & Frameworks:** OpenAI API, Gemini API, Streamlit, NLP, LSTM, ARIMA, Prompt Engineering
- **Cloud & Deployment:** Google Cloud Run, Vercel, Render, Cloudflare Workers, AppScript Automation
- **Visualization & BI:** Tableau, Looker Studio, Power BI, Plotly, Matplotlib
- **Other:** ETL Pipelines, Ad-hoc Reporting, Sentiment Analysis, Predictive Analytics

## Notable Projects
- **Fine-Tuned LLM (Mistral-7B, LoRA):** Fine-tuned a quantized Mistral-7B model using QLoRA for philosophical Q&A (Hugging Face, LoRA, Python)
- **MolecuLearn AI:** Real-time drug alternative tool (Vercel, TypeScript, Gemini API)
- **AI Debate App:** Real-time debate generation platform (Vercel, TypeScript, Gemini API)
- **MyLocalCLI:** A Claude Code alternative with 6 providers, 26 tools, and full privacy
- **AI Health Pro:** AI-powered health advisor with symptom analysis and drug recommendations
- **Local AI Chat:** Self-hosted LLM chatbot running on Google Cloud with Ollama

## Salary Expectations
Prashanth is currently earning ₹15 lakhs per annum (INR). 
For a new role, his expected compensation is ₹30 lakhs per annum (INR) or above, depending on the role, responsibilities, and company stage.
He values interesting work, growth opportunities, and a collaborative team alongside compensation.
He is open to discussion and negotiation for the right opportunity.

## About This Bot (Technical Breakdown)
This AI interview assistant was built by Prashanth as a demonstration of applied AI skills. Here's the technical breakdown:

**Architecture:**
- **Email Receiving:** Cloudflare Email Workers — receives emails at interview@kprsnt.in via Email Routing
- **AI Engine:** Google Gemini API (gemini-2.0-flash model) for natural language understanding and generation
- **Email Sending:** Resend API for transactional reply emails
- **API Backend:** Python serverless function on Vercel — handles AI processing and email responses
- **Hosting:** Vercel (API) + Cloudflare (Email Workers) — fully serverless, auto-scaling

**How It Works:**
1. An email is sent to interview@kprsnt.in
2. Cloudflare Email Workers intercepts it and forwards the parsed email (sender, subject, body) to the Vercel API
3. The Vercel function processes the message through Gemini AI with full professional context
4. Resend API sends the AI-generated response back as a reply email to the original sender

**Tools & Logic Used:**
- Cloudflare Email Workers (JavaScript) for email receiving and parsing
- `google-generativeai` Python SDK for Gemini API integration
- Resend REST API for sending reply emails (no heavy SDK, uses urllib)
- Custom system prompt engineering with comprehensive professional context
- Dual API key strategy with automatic failover on rate limits
- Stateless serverless architecture with CORS-enabled JSON API for testing

**Why This Approach:**
- Demonstrates practical AI integration skills (not just theory)
- Shows ability to build end-to-end automation (email → Cloudflare → AI → email)
- Multi-cloud architecture (Cloudflare + Vercel + Google AI) shows infrastructure breadth
- Serverless = cost-effective and scalable
- The bot itself is a portfolio piece that showcases the exact skills listed in the resume

## Response Guidelines
- Be professional but personable
- Answer honestly — if you don't know something specific, say so and suggest contacting Prashanth directly at kprsnt@gmail.com
- Keep responses concise but thorough
- When discussing technical topics, show depth of knowledge
- If asked about salary, share the numbers openly and express enthusiasm
- Always be enthusiastic about the opportunity
"""

# ─── Gemini Setup ──────────────────────────────────────────────────────────────

def get_ai_response(message: str) -> str:
    """Generate an AI response using Gemini API with fallback to paid key on rate limit."""
    api_key = os.environ.get("GEMINI_API_KEY")
    api_key_paid = os.environ.get("GEMINI_API_KEY_PAID")
    
    if not api_key and not api_key_paid:
        return ("Thank you for reaching out! My AI system is currently being configured. "
                "Please contact Prashanth directly at kprsnt@gmail.com.")
    
    keys_to_try = [k for k in [api_key, api_key_paid] if k]
    
    for i, key in enumerate(keys_to_try):
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel(
                model_name="gemini-2.0-flash",
                system_instruction=SYSTEM_PROMPT
            )
            response = model.generate_content(message)
            return response.text
        except Exception as e:
            error_str = str(e).lower()
            if i < len(keys_to_try) - 1 and ("rate" in error_str or "quota" in error_str or "429" in error_str):
                continue
            return ("I apologize, but I encountered a technical issue processing your message. "
                    "Please contact Prashanth directly at kprsnt@gmail.com.")
    
    return "Thank you for reaching out! Please contact Prashanth directly at kprsnt@gmail.com."


# ─── Email Sending via Resend ──────────────────────────────────────────────────

def send_reply_email(to_email: str, subject: str, body: str):
    """Send a reply email via Resend API (using urllib, no SDK needed)."""
    resend_api_key = os.environ.get("RESEND_API_KEY")
    if not resend_api_key:
        print("RESEND_API_KEY not set, skipping email send")
        return False
    
    from_email = os.environ.get("INTERVIEW_FROM_EMAIL", "interview@kprsnt.in")
    reply_subject = f"Re: {subject}" if not subject.startswith("Re:") else subject
    
    payload = json.dumps({
        "from": from_email,
        "to": [to_email],
        "subject": reply_subject,
        "text": body
    }).encode("utf-8")
    
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=payload,
        headers={
            "Authorization": f"Bearer {resend_api_key}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status == 200
    except urllib.error.HTTPError as e:
        print(f"Resend API error: {e.code} - {e.read().decode()}")
        return False
    except Exception as e:
        print(f"Email send error: {e}")
        return False


# ─── Vercel Serverless Handler ─────────────────────────────────────────────────

class handler(BaseHTTPRequestHandler):
    """Vercel serverless function handler."""
    
    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    
    def do_GET(self):
        """Health check / info endpoint."""
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        response = {
            "status": "online",
            "name": "Prashanth's AI Interview Assistant",
            "description": "Send me a message and I'll discuss Prashanth's professional background, skills, and experience.",
            "usage": {
                "email": "Send an email to interview@kprsnt.in",
                "api": "POST /api/interview with JSON body: {\"message\": \"your question\"}"
            }
        }
        self.wfile.write(json.dumps(response, indent=2).encode())
    
    def do_POST(self):
        """Handle incoming interview messages (from Cloudflare Worker or direct API)."""
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length > 0 else b""
        
        try:
            data = json.loads(body.decode("utf-8")) if body else {}
        except json.JSONDecodeError:
            self._send_json(400, {"error": "Invalid JSON"})
            return
        
        message = data.get("message", "")
        from_email = data.get("from_email", "")
        subject = data.get("subject", "Interview Question")
        send_email = data.get("send_email", False)
        
        if not message.strip():
            self._send_json(400, {"error": "No message provided"})
            return
        
        # Generate AI response
        ai_response = get_ai_response(message)
        
        # Send reply email if requested (from Cloudflare Worker or explicit flag)
        email_sent = False
        if send_email and from_email:
            email_sent = send_reply_email(from_email, subject, ai_response)
        
        self._send_json(200, {
            "response": ai_response,
            "email_sent": email_sent,
            "from": from_email if from_email else None
        })
    
    def _send_json(self, status: int, data: dict):
        """Helper to send JSON response."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())
