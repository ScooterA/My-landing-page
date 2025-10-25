# --- ESL Comment Generator Lite Version ---
# Simplified: No grade or teacher inputs. Clean layout and direct generation.

import random
import tkinter as tk
from tkinter import messagebox, filedialog

# ---------------------------
# Helpers
# ---------------------------
def clean_clause(text: str) -> str:
    if not text:
        return ""
    t = text.strip()
    while t and t[-1] in ".!?,":  # remove ending punctuation
        t = t[:-1].rstrip()
    if t:
        t = t[0].lower() + t[1:]
    return t

def sentence_with_subject(subject: str, clause: str) -> str:
    c = clean_clause(clause)
    return f"{subject} {c}."

def cap(s: str) -> str:
    return s[:1].upper() + s[1:] if s else s

# ---------------------------
# Skill comment banks
# ---------------------------

def get_phonics_comment(score):
    comments = {
        1: ["needs extra guidance to recognise phonics sounds",
            "is just beginning with phonics and needs support",
            "is learning basic sounds slowly but trying hard"],
        2: ["is improving and recognises some sounds",
            "is making progress with phonics and needs guidance",
            "shows effort in learning new sounds"],
        3: ["can identify a few sounds with guidance",
            "is steadily progressing in phonics and pronunciation",
            "recognises some letter sounds and applies them with help"],
        4: ["is improving at sounding out simple words",
            "reads simple words with some support",
            "demonstrates growing confidence in phonics"],
        5: ["shows growing confidence in recognising and pronouncing sounds",
            "can read many words correctly and applies phonics rules",
            "is developing strong phonics skills"],
        6: ["reads many words fluently with some help",
            "applies phonics rules correctly in most words",
            "can sound out words accurately and consistently"],
        7: ["uses phonics effectively to read new words",
            "reads confidently and applies sounds correctly",
            "can decode words independently and correctly"],
        8: ["reads fluently and applies phonics rules accurately",
            "demonstrates strong phonics and reads confidently",
            "can read complex words with accuracy"],
        9: ["demonstrates strong phonics skills and reads with confidence",
            "reads fluently and confidently applies sounds in all words",
            "shows excellent phonics skills in reading"],
        10:["has excellent phonics skills and reads with accuracy and fluency",
             "is an outstanding reader who applies all phonics rules",
             "reads effortlessly and recognises all sounds correctly"]
    }
    return random.choice(comments.get(score, ["is developing phonics skills"]))

def get_vocabulary_comment(score):
    comments = {
        1: ["is just beginning to learn new words",
            "recognises few words and needs support",
            "needs help to use vocabulary"],
        2: ["is starting to learn basic vocabulary",
            "uses a few words with guidance",
            "needs reminders to apply new words"],
        3: ["can use some words correctly with support",
            "is steadily improving vocabulary",
            "applies familiar words with help"],
        4: ["shows good effort in learning vocabulary",
            "is improving and uses simple words correctly",
            "recognises and applies some new words"],
        5: ["uses vocabulary with growing confidence",
            "demonstrates good understanding of words",
            "applies vocabulary appropriately"],
        6: ["applies vocabulary correctly in sentences",
            "uses most words appropriately",
            "demonstrates solid vocabulary skills"],
        7: ["expresses ideas clearly using vocabulary",
            "uses a wide range of words confidently",
            "applies vocabulary effectively in discussions"],
        8: ["demonstrates strong vocabulary and uses words carefully",
            "uses advanced vocabulary in writing and speaking",
            "shows impressive vocabulary knowledge"],
        9: ["has excellent vocabulary and expresses ideas confidently",
            "chooses words accurately and effectively",
            "demonstrates extensive vocabulary"],
        10:["has outstanding vocabulary and uses words precisely",
             "expresses ideas with clarity and excellent word choice",
             "is a confident user of a rich vocabulary"]
    }
    return random.choice(comments.get(score, ["is developing vocabulary skills"]))

def get_spelling_comment(score):
    comments = {
        1: ["struggles with spelling and needs support",
            "needs help to spell simple words",
            "is just beginning to write correctly"],
        2: ["is starting to spell basic words",
            "tries to spell words but makes mistakes",
            "needs guidance to improve"],
        3: ["can spell simple words with help",
            "is improving spelling steadily",
            "applies some rules correctly"],
        4: ["is improving spelling and remembers patterns",
            "can spell most common words with guidance",
            "shows good effort in spelling"],
        5: ["spells familiar words correctly and shows confidence",
            "demonstrates growing spelling skills",
            "applies spelling rules with some support"],
        6: ["spells most words accurately",
            "can write words correctly and applies patterns",
            "demonstrates solid spelling skills"],
        7: ["spells accurately and shows strong understanding",
            "writes correctly and applies patterns consistently",
            "demonstrates good spelling confidence"],
        8: ["shows excellent spelling and writes accurately",
            "applies rules in all familiar words",
            "writes confidently with few errors"],
        9: ["demonstrates outstanding spelling skills",
            "writes words correctly consistently",
            "applies rules fluently"],
        10:["is an excellent speller and writes flawlessly",
             "shows exceptional spelling and accuracy",
             "writes with precision and strong spelling skills"]
    }
    return random.choice(comments.get(score, ["is developing spelling skills"]))

def get_reading_comment(score):
    comments = {
        1: ["struggles with reading and needs extra support",
            "recognises very few words",
            "needs guidance to understand text"],
        2: ["is beginning to read simple words",
            "reads short words with help",
            "needs support to understand sentences"],
        3: ["reads simple texts with guidance",
            "can decode words with help",
            "is making progress"],
        4: ["reads simple passages with support",
            "is improving fluency steadily",
            "can understand familiar texts"],
        5: ["reads fluently and is gaining confidence",
            "understands most of the text",
            "applies strategies with help"],
        6: ["reads accurately and understands most texts",
            "demonstrates solid skills",
            "can answer questions correctly"],
        7: ["reads confidently and applies strategies",
            "demonstrates strong fluency and comprehension",
            "can discuss texts in detail"],
        8: ["reads fluently and comprehends well",
            "demonstrates excellent understanding",
            "reads confidently and expresses ideas"],
        9: ["reads complex texts and interprets meaning accurately",
            "demonstrates strong comprehension",
            "can analyse ideas confidently"],
        10:["is an outstanding reader who understands texts easily",
             "reads with fluency and excellent comprehension",
             "demonstrates mastery of reading"]
    }
    return random.choice(comments.get(score, ["is developing reading skills"]))

def get_comprehension_comment(score):
    comments = {
        1: ["struggles to understand stories",
            "needs guidance to answer questions",
            "has difficulty following lessons"],
        2: ["understands simple stories with help",
            "can answer basic questions",
            "shows some comprehension"],
        3: ["can answer simple questions independently",
            "demonstrates some understanding",
            "is improving"],
        4: ["understands most simple texts",
            "can discuss familiar stories",
            "shows steady improvement"],
        5: ["understands stories well",
            "demonstrates good comprehension skills",
            "can retell simple stories"],
        6: ["understands most texts confidently",
            "can analyse basic ideas",
            "demonstrates solid skills"],
        7: ["understands complex instructions and stories",
            "can discuss texts in detail",
            "demonstrates strong comprehension"],
        8: ["shows excellent comprehension",
            "can answer in-depth questions confidently",
            "demonstrates high-level understanding"],
        9: ["demonstrates outstanding comprehension",
            "interprets texts accurately",
            "can analyse ideas effectively"],
        10:["has exceptional comprehension skills",
             "understands complex texts easily",
             "demonstrates mastery of comprehension"]
    }
    return random.choice(comments.get(score, ["is developing comprehension skills"]))

def get_grammar_comment(score):
    comments = {
        1: ["struggles with grammar and needs support",
            "makes frequent mistakes",
            "needs guidance in sentence structure"],
        2: ["is learning basic grammar",
            "sometimes applies rules correctly",
            "needs reminders"],
        3: ["can use simple sentences correctly",
            "is improving in grammar",
            "applies basic rules with help"],
        4: ["shows steady improvement in grammar",
            "uses sentences correctly with support",
            "demonstrates effort"],
        5: ["uses grammar appropriately",
            "demonstrates good understanding of rules",
            "can write correct sentences with help"],
        6: ["uses grammar correctly most of the time",
            "applies rules consistently",
            "demonstrates solid grammar skills"],
        7: ["uses grammar confidently",
            "writes accurately",
            "shows strong understanding"],
        8: ["demonstrates excellent grammar",
            "applies rules carefully",
            "writes fluently and correctly"],
        9: ["uses grammar precisely and consistently",
            "writes complex sentences accurately",
            "shows outstanding grammar skills"],
        10:["has exceptional grammar skills",
             "writes flawlessly",
             "demonstrates mastery of grammar"]
    }
    return random.choice(comments.get(score, ["is developing grammar skills"]))

def get_speaking_comment(score):
    comments = {
        1: ["struggles to express ideas verbally",
            "needs extra support to speak",
            "is very hesitant in speaking"],
        2: ["is beginning to speak simple sentences",
            "sometimes lacks confidence",
            "needs encouragement to speak"],
        3: ["can communicate basic ideas",
            "is improving confidence",
            "expresses simple ideas with guidance"],
        4: ["speaks clearly with some help",
            "shows good effort in communication",
            "can explain familiar ideas"],
        5: ["speaks confidently and communicates well",
            "demonstrates good speaking skills",
            "expresses ideas clearly"],
        6: ["communicates effectively in most situations",
            "participates actively",
            "can explain thoughts with guidance"],
        7: ["speaks confidently and contributes to discussions",
            "uses language well",
            "expresses ideas accurately"],
        8: ["demonstrates strong speaking skills",
            "speaks fluently",
            "can present ideas confidently"],
        9: ["is an excellent speaker",
            "expresses complex ideas clearly",
            "demonstrates outstanding speaking skills"],
        10:["has exceptional speaking ability",
             "communicates fluently and confidently",
             "is a confident and articulate speaker"]
    }
    return random.choice(comments.get(score, ["is developing speaking skills"]))

def get_listening_comment(score):
    comments = {
        1: ["struggles to listen and follow instructions",
            "needs repeated guidance",
            "has difficulty concentrating"],
        2: ["is learning to listen carefully",
            "sometimes misses details",
            "needs reminders to focus"],
        3: ["can follow simple instructions with help",
            "is improving listening skills",
            "responds to cues with support"],
        4: ["listens carefully sometimes",
            "can follow directions with guidance",
            "shows effort to pay attention"],
        5: ["listens attentively most of the time",
            "understands instructions well",
            "responds appropriately in class"],
        6: ["listens carefully and follows instructions",
            "demonstrates solid listening skills",
            "responds accurately to directions"],
        7: ["demonstrates strong listening skills",
            "pays attention and follows discussions",
            "can understand complex instructions"],
        8: ["listens attentively and consistently follows instructions",
            "understands details well",
            "shows excellent listening skills"],
        9: ["demonstrates outstanding listening skills",
            "follows complex instructions accurately",
            "is attentive and responsive"],
        10:["has exceptional listening skills",
             "always follows instructions accurately",
             "is a highly attentive student"]
    }
    return random.choice(comments.get(score, ["is developing listening skills"]))

def get_participation_comment(score):
    comments = {
        1: ["rarely participates in class activities",
            "needs encouragement to join in",
            "shows very limited engagement"],
        2: ["participates sometimes but hesitantly",
            "needs reminders to engage fully",
            "is learning to contribute"],
        3: ["participates well with guidance",
            "joins in class activities appropriately",
            "shows growing confidence"],
        4: ["actively participates sometimes",
            "contributes to discussions with some help",
            "shows interest in activities"],
        5: ["participates actively in class activities",
            "joins discussions confidently",
            "demonstrates engagement and effort"],
        6: ["participates well and contributes ideas",
            "shows good engagement",
            "joins activities confidently"],
        7: ["actively participates and contributes regularly",
            "demonstrates strong engagement",
            "shares ideas confidently"],
        8: ["participates enthusiastically",
            "engages well in all activities",
            "demonstrates leadership in discussions"],
        9: ["is an outstanding participant",
            "always engages actively",
            "contributes valuable ideas"],
        10:["shows exceptional participation",
             "is highly engaged and enthusiastic",
             "leads and encourages classmates effectively"]
    }
    return random.choice(comments.get(score, ["is developing participation skills"]))

def get_writing_comment(score):
    comments = {
        1: ["struggles with writing and needs support",
            "needs help to express ideas in writing",
            "writes very simple sentences with guidance"],
        2: ["is developing writing skills",
            "writes basic sentences with help",
            "needs guidance to improve clarity"],
        3: ["can write simple sentences independently",
            "demonstrates some organization in writing",
            "applies basic rules with support"],
        4: ["writes clearly with some help",
            "shows steady progress in organizing ideas",
            "demonstrates effort in writing"],
        5: ["writes competently and communicates ideas",
            "shows good understanding of structure",
            "applies rules correctly most of the time"],
        6: ["writes clearly and effectively",
            "can organize ideas with minimal support",
            "demonstrates solid writing skills"],
        7: ["writes confidently and communicates ideas well",
            "shows strong structure and clarity",
            "applies rules accurately"],
        8: ["demonstrates excellent writing skills",
            "writes fluently and logically",
            "organizes ideas clearly and consistently"],
        9: ["is an outstanding writer",
            "expresses ideas with precision and clarity",
            "demonstrates mastery of writing skills"],
        10:["has exceptional writing skills",
             "writes fluently with strong structure and clarity",
             "produces high-quality work consistently"]
    }
    return random.choice(comments.get(score, ["is developing writing skills"]))

def get_behaviour_comment(score):
    comments = {
        1: ["shows poor behaviour and needs constant guidance",
            "struggles to follow rules",
            "needs support to behave appropriately"],
        2: ["sometimes struggles with behaviour",
            "needs reminders to follow rules",
            "is learning to manage behaviour"],
        3: ["demonstrates generally good behaviour",
            "follows instructions with guidance",
            "shows steady improvement"],
        4: ["consistently shows good behaviour sometimes",
            "respects others with reminders",
            "is developing positive habits"],
        5: ["demonstrates good behaviour consistently",
            "respects classmates and rules",
            "shows effort to behave appropriately"],
        6: ["shows strong behaviour and respect",
            "follows rules reliably",
            "demonstrates self-control"],
        7: ["behaves very well and is respectful",
            "shows leadership in behaviour",
            "is a positive role model occasionally"],
        8: ["consistently demonstrates excellent behaviour",
            "respects others and follows rules",
            "is a strong role model"],
        9: ["demonstrates outstanding behaviour",
            "respects all and leads by example",
            "is highly responsible and respectful"],
        10:["is an exemplary student",
             "demonstrates perfect behaviour consistently",
             "is a role model for others"]
    }
    return random.choice(comments.get(score, ["is developing behaviour skills"]))

# ---------------------------
# Function list
# ---------------------------
SKILL_FUNCS = [
    get_phonics_comment,
    get_vocabulary_comment,
    get_spelling_comment,
    get_reading_comment,
    get_comprehension_comment,
    get_grammar_comment,
    get_speaking_comment,
    get_listening_comment,
    get_participation_comment,
    get_writing_comment,
    get_behaviour_comment
]

# ---------------------------
# Unified comment builder
# ---------------------------
def build_comment(name, pronoun, clauses, scores):
    avg_score = sum(scores) / len(scores)
    if avg_score <= 3:
        opening = f"{name} is finding English challenging this term and needs extra support."
    elif avg_score <= 6:
        opening = f"{name} is making steady progress across English skills."
    else:
        opening = f"{name} demonstrates strong English ability and approaches work confidently."
    sentences = [sentence_with_subject(pronoun, clause) for clause in clauses]
    body = " ".join(sentences)
    return f"{opening} {body}"

# ---------------------------
# Generate comment
# ---------------------------
def generate_comment(name, scores, gender_choice="She"):
    subject_name = name.strip()
    pronoun_cap = "She" if gender_choice.lower().startswith("s") else "He"
    clauses = [func(score) for func, score in zip(SKILL_FUNCS, scores)]
    sentences = build_comment(subject_name, pronoun_cap, clauses, scores)
    closing_line = f"Keep working hard, {subject_name}, and continue to grow each week."
    conclusion = random.choice([
        "Excellent work!", "Nicely done!", "Fantastic job!",
        "Superb effort!", "Smooth execution!", "Outstanding result!"
    ])
    return f"{sentences}\n{conclusion}\n{closing_line}"

# ---------------------------
# GUI
# ---------------------------
def run_gui():
    def generate_action():
        try:
            name = name_entry.get().strip()
            if not name:
                messagebox.showerror("Input Error", "Please enter the student's name.")
                return
            scores = []
            for e in entries:
                v = e.get().strip()
                if not v.isdigit():
                    raise ValueError
                num = int(v)
                if not (1 <= num <= 10):
                    raise ValueError
                scores.append(num)

            gender_choice = gender_var.get()
            comment = generate_comment(name, scores, gender_choice)
            comment_box.delete("1.0", tk.END)
            comment_box.insert(tk.END, comment)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter integer scores from 1 to 10 for all skills.")

    def copy_action():
        text = comment_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Nothing to Copy", "No comment to copy yet.")
            return
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Comment copied to clipboard.")

    def save_action():
        text = comment_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Nothing to Save", "No comment to save yet.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            messagebox.showinfo("Saved", f"Comment saved to:\n{path}")

    def clear_action():
        name_entry.delete(0, tk.END)
        for e in entries:
            e.delete(0, tk.END)

    root = tk.Tk()
    root.title("ESL Comment Generator – Lite Edition")
    root.geometry("920x760")

    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    tk.Label(root, text="Student Name:").grid(row=0, column=0, sticky="e", padx=6, pady=6)
    name_entry = tk.Entry(root, width=28)
    name_entry.grid(row=0, column=1, sticky="w")

    tk.Label(root, text="Gender:").grid(row=0, column=2, sticky="e", padx=6)
    gender_var = tk.StringVar(value="She")
    tk.OptionMenu(root, gender_var, "She", "He").grid(row=0, column=3, sticky="w")

    labels = ["Phonics", "Vocabulary", "Spelling", "Reading", "Comprehension",
              "Grammar", "Speaking", "Listening", "Participation", "Writing", "Behaviour"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(root, text=f"{label} (1-10):").grid(row=i+1, column=0, sticky="e", padx=6)
        e = tk.Entry(root, width=8)
        e.grid(row=i+1, column=1, sticky="w", pady=2)
        entries.append(e)

    tk.Button(root, text="Generate Comment", command=generate_action, bg="lightgreen").grid(row=13, column=0, pady=12)
    tk.Button(root, text="Copy Comment", command=copy_action, bg="lightblue").grid(row=13, column=1, pady=12)
    tk.Button(root, text="Save Comment", command=save_action, bg="khaki").grid(row=13, column=2, pady=12)
    tk.Button(root, text="Clear Inputs", command=clear_action, bg="lightpink").grid(row=13, column=3, pady=12)

    comment_box = tk.Text(root, height=20, width=110, wrap="word")
    comment_box.grid(row=14, column=0, columnspan=8, padx=10, pady=10, sticky="w")

    root.mainloop()

if __name__ == "__main__":
    run_gui()
