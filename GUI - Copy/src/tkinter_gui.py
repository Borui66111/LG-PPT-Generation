import tkinter as tk
from tkinter import messagebox
from ppt import Presentation
import openai, os
from dotenv import find_dotenv, load_dotenv
import llm, ppt, test, subprocess

# Initialize OpenAI API key
load_dotenv(find_dotenv())
openai.api_key=os.environ['OPENAI_API_KEY']

class PPTGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.file_path='../output/test.pptx'
        self.title("AI-Powered PPT Generator")
        self.geometry("500x400")

        # Description input
        self.desc_label = tk.Label(self, text="Enter Description:")
        self.desc_label.pack(pady=10)
        self.desc_text = tk.Text(self, height=5, width=50)
        self.desc_text.pack(pady=10)

        # Settings
        self.settings_label = tk.Label(self, text="Settings:")
        self.settings_label.pack(pady=10)

        self.min_slides_label = tk.Label(self, text="Minimum Slides:")
        self.min_slides_label.pack()
        self.min_slides_entry = tk.Entry(self)
        self.min_slides_entry.pack()

        self.word_limit_label = tk.Label(self, text="Word Limit per Slide:")
        self.word_limit_label.pack()
        self.word_limit_entry = tk.Entry(self)
        self.word_limit_entry.pack()

        # Buttons
        self.generate_btn = tk.Button(self, text="Generate PPT", command=self.generate_ppt)
        self.generate_btn.pack(pady=20)

    def generate_ppt(self):
        # Get user inputs
        description = self.desc_text.get("1.0", tk.END).strip()
        min_slides = int(self.min_slides_entry.get())
        word_limit = int(self.word_limit_entry.get())

        if not description:
            messagebox.showwarning("Input Error", "Description cannot be empty")
            return

        # Call functions to process the description and generate the PPT
        test.run(description,min_slides,word_limit)
        messagebox.showinfo("Success", "PPT generated successfully!")
        subprocess.run(['start', self.file_path], shell=True, check=True)


#     def generate_outline(self, description, min_slides):
#         # Mockup function to generate an outline
#         chain = create_chain(
#             functions_config={'functions': 'Outline', 'function_call': {'name': 'Outline'}},
#             system_message=f"You are a helpful assistant to create a ppt. There should be at least {min_slides} body slides"
#         )
#         resp = chat(description, chain)
#         return resp['slides']

#     def generate_slides(self, outline, word_limit):
#         # Mockup function to generate slide content
#         resp1 = chat(
#             [f"topic:{outline};title:" + i for i in outline],
#             force_invoke=0,
#             chain=create_chain(
#                 model_name='gpt-4',
#                 functions_config={'functions': 'Slide', 'function_call': {'name': 'Slide'}},
#                 temperature=0,
#                 system_message=f"Fill in the content according to the guide. Use layman's terms and keep it under {word_limit} words per slide."
#             )
#         )
#         return [i['content'] for i in resp1]

#     def create_ppt(self, outline, slides_content):
#         # Use python-pptx to create a presentation
#         prs = Presentation()
#         slide_layout = prs.slide_layouts[1]

#         for title, content in zip(outline, slides_content):
#             slide = prs.slides.add_slide(slide_layout)
#             title_placeholder = slide.shapes.title
#             content_placeholder = slide.placeholders[1]
#             title_placeholder.text = title
#             content_placeholder.text = content

#         prs.save("generated_presentation.pptx")

# def create_chain(functions_config, system_message):
#     return {
#         "functions_config": functions_config,
#         "system_message": system_message
#     }

# def chat(content, chain, force_invoke=1):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": chain['system_message']},
#             {"role": "user", "content": content}
#         ]
#     )
#     return response.choices[0].message['content']

if __name__ == "__main__":
    app = PPTGeneratorApp()
    app.mainloop()
