import openai
import tkinter as tk
from tkinter import messagebox, scrolledtext

# ✅ OpenRouter API Setup
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

def generate_feedback(portfolio_text):
    prompt = f"""You are a professional academic evaluator.

The following is a student's portfolio:
\"\"\"{portfolio_text}\"\"\"

Based on this, give a short structured evaluation in the exact format below:

Eligibility: [Write one of the following - Excellent, Good, Satisfactory, Needs Attention]

Lackments:
- [Mention 1–2 weaknesses or areas for improvement, or write 'None' if perfect]

Regards: [Write a suitable closing based on eligibility like 'Outstanding work', 'Needs improvement', 'Good effort', or 'Best of luck']

Do not write any extra sentences or paragraphs. Follow only the structure.
At last give a one line concise rewiew
"""

    try:
        response = openai.ChatCompletion.create(
            model="mistralai/devstral-small:free",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.6
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"


# ✅ GUI Function
def on_generate():
    input_text = input_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Empty Input", "Please paste the student portfolio content.")
        return

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "⏳ Generating feedback...\n")
    window.update_idletasks()

    feedback = generate_feedback(input_text)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, feedback)

# ✅ GUI Setup
window = tk.Tk()
window.title("Student Portfolio Feedback Generator")
window.geometry("500x700")
window.config(bg="#f2f2f2")

tk.Label(window, text="📄 Enter Student Portfolio Content:", font=("Segoe UI", 12, "bold"), bg="#f2f2f2").pack(pady=(10, 0))
input_box = scrolledtext.ScrolledText(window, font=("Segoe UI", 11), width=95, height=12, wrap=tk.WORD)
input_box.pack(padx=10, pady=10)

generate_btn = tk.Button(window, text="✨ Generate Feedback", font=("Segoe UI", 12), bg="#4CAF50", fg="white", command=on_generate)
generate_btn.pack(pady=10)

tk.Label(window, text="🧾 Generated Feedback:", font=("Segoe UI", 12, "bold"), bg="#f2f2f2").pack(pady=(15, 0))
output_box = scrolledtext.ScrolledText(window, font=("Segoe UI", 11), width=95, height=10, wrap=tk.WORD)
output_box.pack(padx=10, pady=10)

window.mainloop()
