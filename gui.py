import customtkinter as ctk
from PIL import Image
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


BG_COLOR = "#0F172A"          # Window Background
FRAME_COLOR = "#1E293B"       # Main Frame
CARD_COLOR = "#334155"        # Result Frame
BUTTON_COLOR = "#2563EB"      # Search Button
BUTTON_HOVER = "#1D4ED8"      # Button Hover
ENTRY_COLOR = "#475569"       # Entry Background
TEXT_COLOR = "#F8FAFC"        # White Text
LABEL_COLOR = "#93C5FD"       # Light Blue Labels

app = ctk.CTk()
app.title("Recipe Finder")
app.geometry("1100x700")
app.configure(fg_color=BG_COLOR)
app.resizable(False,False)

main_frame = ctk.CTkFrame(app,corner_radius=15,fg_color=FRAME_COLOR)
main_frame.pack(fill="both",expand=True,padx=15 , pady=15)

title= ctk.CTkLabel(main_frame,text=" 🍴Recipe Finder",font=("Segoe UI", 28, "bold"),text_color="#A9B088")
title.pack(pady=15)

search_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
search_frame.pack(pady=10)

city_entry = ctk.CTkEntry(
    search_frame,
    width=350,
    height=40,
    placeholder_text="Enter Recipe Name or Main Ingredient",
    font=("Segoe UI", 15),
    fg_color=ENTRY_COLOR,
    text_color=TEXT_COLOR,
    border_color=BUTTON_COLOR,
)
city_entry.pack(side="left", padx=10)

search_btn = ctk.CTkButton(
    search_frame,
    text="Search🍳",
    width=120,
    height=40,
    font=("Segoe UI", 15, "bold"),
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="white",
    
)
search_btn.pack(side="left")
result_frame = ctk.CTkFrame(main_frame, corner_radius=12,fg_color=CARD_COLOR,)
result_frame.pack(fill="both", expand=True, padx=20, pady=20)
result_frame.grid_columnconfigure(0, weight=1)
result_frame.grid_columnconfigure(1, weight=3)
result_frame.grid_rowconfigure(0, weight=1)

recipe_list = ctk.CTkScrollableFrame(
    result_frame,
    width=250,
    fg_color="#2A3B52"
)

l1=ctk.CTkLabel(recipe_list,text="🍜Recipe List ",font=('Arial',20),text_color="#8D9275")
l1.pack(pady=10)
recipe_list.grid(row=0, column=0, sticky="nsew", padx=(10,5), pady=10)

details_frame = ctk.CTkScrollableFrame(
    result_frame,
    width=250,
    fg_color="#243447"
)
details_frame.grid(row=0, column=1, sticky="nsew", padx=(5,10), pady=10)
l2=ctk.CTkLabel(details_frame,text=" 📖Recipe Details ",font=('Arial',20),text_color="#8D9275")
l2.pack(pady=10)
for i in range(15):
    btn = ctk.CTkButton(
        recipe_list,
        text=f"🍽 Recipe {i+1}",
     fg_color="#334155",
       hover_color="#2563EB",
       anchor="w",
       height=40
    )
    btn.pack(fill="x", pady=5, padx=5)

placeholder = ctk.CTkImage(light_image=Image.open("assets/placeholder.png"),
    dark_image=Image.open("assets/placeholder.png"),
    size=(300, 220))

image_label = ctk.CTkLabel(
    details_frame,
    image=placeholder,
    text=""
)
image_label.pack(pady=15)
app.mainloop()