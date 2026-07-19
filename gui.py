import customtkinter as ctk
from PIL import Image
from first import search_recipes
from first import get_recipe_details
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
#---------------------------------------------------

BG_COLOR = "#0d3b66"          # Window Background
FRAME_COLOR = "#e4dbb6"       # Main Frame
CARD_COLOR = "#C2984A"        # Result Frame
BUTTON_COLOR = "#ee964b"      # Search Button
BUTTON_HOVER = "#e27f2a"      # Button Hover
ENTRY_COLOR = "#475569"       # Entry Background
TEXT_COLOR = "#F8FAFC"        # White Text
LABEL_COLOR = "#93C5FD"

app = ctk.CTk()
app.title("Recipe Finder")
app.geometry("1100x700")
app.configure(fg_color=BG_COLOR)
app.resizable(False,False)

#------------------------------------------------
recipe = []
def search():
    global temp
    name = meal_entry.get().strip()
    if not name:
        return
    temp = search_recipes(name)
    if temp== None:
        return
    if len(temp) == 0:
        return 
    
    for widget in recipe_list.winfo_children():
        if widget != l1:      
            widget.destroy()
    for r in temp:
        btn = ctk.CTkButton(
        recipe_list,
        text=r["title"],
        fg_color="#334155",
        hover_color="#ee964b",
        anchor="w",
        height=40,
        command=lambda rid=r["id"]: show_recipe(rid)
     )
        btn.pack(fill="x", pady=5, padx=5)
    


#-----------------------------------------------------------
def show_recipe(recipe_id):
    recipe = get_recipe_details(recipe_id)
    if recipe is None:
        return
    title_label.configure(text=recipe["title"])
    time_label.configure(
        text=f"Ready In: {recipe['readyInMinutes']} minutes"
    )

    servings_label.configure(
        text=f"Servings: {recipe['servings']}"
    )

    health_label.configure(
        text=f"Health Score: {recipe['healthscore']}"
    )

    dish_label.configure(
        text=f"Dish Type: {recipe['dishTypes']}"
    )

    cuisine_label.configure(
        text=f"Cuisine: {recipe['cuisines']}"
    )

    ingredients_label.configure(
        text="\n".join(recipe["ingredients"])
    )

    summary_label.configure(
        text=recipe["summary"]
    )

    instructions_label.configure(
        text=recipe["instructions"]
    )

    
#----------------------------------------------------------------------------------------------------------
main_frame = ctk.CTkFrame(app,corner_radius=15,fg_color=FRAME_COLOR)
main_frame.pack(fill="both",expand=True,padx=15 , pady=15)

title= ctk.CTkLabel(main_frame,text=" 🍴Recipe Finder",font=("Segoe UI", 28, "bold"),text_color="#C2984A")
title.pack(pady=15)

search_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
search_frame.pack(pady=10)

meal_entry = ctk.CTkEntry(
    search_frame,
    width=350,
    height=40,
    placeholder_text="Enter Recipe Name or Main Ingredient",
    font=("Segoe UI", 15),
    fg_color=ENTRY_COLOR,
    text_color=TEXT_COLOR,
    border_color=BUTTON_COLOR,
)
meal_entry.pack(side="left", padx=10)

search_btn = ctk.CTkButton(
    search_frame,
    text="Search 🍳",
    width=120,
    height=40,
    font=("Segoe UI", 15, "bold"),
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="white",
    command = search
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

l1=ctk.CTkLabel(recipe_list,text="🍜 Recipe List ",font=('Arial',20),text_color="#C2984A")
l1.pack(pady=10)
recipe_list.grid(row=0, column=0, sticky="nsew", padx=(10,5), pady=10)

details_frame = ctk.CTkScrollableFrame(
    result_frame,
    width=250,
    fg_color="#243447"
)
details_frame.grid(row=0, column=1, sticky="nsew", padx=(5,10), pady=10)
l2=ctk.CTkLabel(details_frame,text=" 📖 Recipe Details ",font=('Arial',20),text_color="#C2984A")
l2.pack(pady=10)

placeholder = ctk.CTkImage(light_image=Image.open("assets/placeholder.png"),
    dark_image=Image.open("assets/placeholder.png"),
    size=(300, 220))


image_label = ctk.CTkLabel(
    details_frame,
    image=placeholder,
    text=""
)

image_label.pack(pady=15)

title_label = ctk.CTkLabel(
    details_frame,
    text="Recipe Title",
    font=("Segoe UI", 22, "bold"),
    text_color="white"
)
title_label.pack(pady=(10,5))

time_label = ctk.CTkLabel(
    details_frame,
    text="Ready In: ",
    anchor="w"
)
time_label.pack(fill="x", padx=20)

servings_label = ctk.CTkLabel(
    details_frame,
    text="Servings: ",
    anchor="w"
)
servings_label.pack(fill="x", padx=20)

health_label = ctk.CTkLabel(
    details_frame,
    text="Health Score: ",
    anchor="w"
)
health_label.pack(fill="x", padx=20)

dish_label = ctk.CTkLabel(
    details_frame,
    text="Dish Type: ",
    anchor="w"
)
dish_label.pack(fill="x", padx=20)

cuisine_label = ctk.CTkLabel(
    details_frame,
    text="Cuisine: ",
    anchor="w"
)
cuisine_label.pack(fill="x", padx=20)

ingredients_heading = ctk.CTkLabel(
    details_frame,
    text="Ingredients",
    font=("Segoe UI",18,"bold")
)
ingredients_heading.pack(pady=(15,5))

ingredients_label = ctk.CTkLabel(
    details_frame,
    text="",
    justify="left",
    anchor="w",
    wraplength=500
)
ingredients_label.pack(fill="x", padx=20)

summary_heading = ctk.CTkLabel(
    details_frame,
    text="Summary",
    font=("Segoe UI",18,"bold")
)
summary_heading.pack(pady=(15,5))

summary_label = ctk.CTkLabel(
    details_frame,
    text="",
    justify="left",
    wraplength=500
)
summary_label.pack(fill="x", padx=20)

instructions_heading = ctk.CTkLabel(
    details_frame,
    text="Instructions",
    font=("Segoe UI",18,"bold")
)
instructions_heading.pack(pady=(15,5))

instructions_label = ctk.CTkLabel(
    details_frame,
    text="",
    justify="left",
    wraplength=500
)
instructions_label.pack(fill="x", padx=20)
app.mainloop()