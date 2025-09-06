# 🌍 AI Traveller – Your Smart Travel Companion 🧳

AI Traveller is a Streamlit-powered web app that helps users plan their journeys with intelligent recommendations. Powered by Google's Gemini model via LangChain, it offers personalized travel suggestions based on user preferences like budget, speed, comfort, and language.

---

## 🚀 Features

- **Multi-modal Travel Search**: Choose from Train, Bus, Flight, Cab, or Bike.
- **Preference-Based Filtering**: Prioritize Budget, Fastest, or Most Comfortable options.
- **Smart Sorting**: Sort results by Price, Duration, or Departure Time.
- **Multilingual Support**: Get responses in English, Hindi, Tamil, Telugu, Kannada, or Marathi.
- **AI-Powered Suggestions**: Uses Gemini 2.0 Flash via LangChain for dynamic travel planning.
- **Stylized UI**: Clean, gradient-themed layout with responsive sidebar controls.

---

## 🛠️ Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/ai-traveller.git
   cd ai-traveller
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your Gemini API Key**  
   Save your API key in a file named `gemini_key.txt` inside the `/Python_Challenges/` directory:
   ```
   /Python_Challenges/gemini_key.txt
   ```

4. **Run the App**  
   ```bash
   streamlit run app.py
   ```

---

## 📦 Dependencies

- `streamlit`
- `langchain-google-genai`
- `google-api-core`

You can install them manually or via `requirements.txt`.

---

## 📸 UI Preview

> The app features a gradient-themed header, sidebar input controls, and dynamic markdown output for travel suggestions.

---

## 💡 How It Works

- Users input travel details via the sidebar.
- A prompt is dynamically generated based on inputs.
- The Gemini model processes the prompt and returns travel suggestions.
- Results are displayed with estimated cost and duration in bullet format.

---

## 🧠 Powered By

- **LangChain** – Framework for building LLM-powered applications.
- **Google Gemini 2.0 Flash** – Fast, generative AI model for real-time responses.
- **Streamlit** – Rapid UI development for Python apps.

---

## 📌 Notes

- Ensure your API key is valid and has access to Gemini models.
- The app uses `GRPC_DNS_RESOLVER=native` for compatibility with gRPC.

---

## ✨ Future Enhancements

- Integration with real-time travel APIs (IRCTC, RedBus, etc.)
- Map-based visualization of routes.
- User authentication and saved itineraries.

---

Feel free to tweak the tone or structure to match your book’s aesthetic or portfolio style. Want a logo or visual diagram to go with it? I can help sketch that out too.
