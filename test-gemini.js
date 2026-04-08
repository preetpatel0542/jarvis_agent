const GEMINI_API_KEY = "AIzaSyCihhnYExvUyVa_AGbd7Ti_VfhWKxTv1Ns";
const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${GEMINI_API_KEY}`;

const systemPrompt = "You are J.A.R.V.I.S., a helpful AI assistant. Be concise and reply in 1-3 sentences maximum. If asked to speak in Hindi or Gujarati, use the English/Latin alphabet. User query: india pm name";

fetch(url, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    contents: [{ parts: [{ text: systemPrompt }] }]
  })
})
.then(res => res.json())
.then(data => {
  console.log(JSON.stringify(data, null, 2));
})
.catch(e => {
  console.error("error:", e);
});
