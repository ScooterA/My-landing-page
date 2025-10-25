# --- ESL Comment Generator – Teacher Edition (Unified Builder, Draft 2) ---
# Builds comments from skill banks
# Dynamic closing based on performance average

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
        1: ["needs extra guidance to recognise basic phonics sounds and letter patterns",
            "is still developing early phonics awareness and benefits from one-to-one support",
            "finds it challenging to match letters and sounds but tries to follow along in class",
            "is beginning to notice sound patterns in words and will improve with continued practice"],

        2: ["is improving and recognises some common sounds during reading practice",
            "shows effort in learning new sounds and tries to apply them in class activities",
            "can identify a few beginning sounds and is starting to blend simple words",
            "is developing confidence in phonics and benefits from continued review"],
        
        3: ["can identify a few sounds with guidance and is gaining confidence in phonics",
            "is steadily progressing in phonics and can recognise several familiar sounds",
            "tries to sound out short words with some support and is improving each week",
            "shows growing awareness of letter–sound relationships and applies them with help"],
        
        4: ["is improving at sounding out simple words and can read familiar ones with help",
            "reads simple words with support and is beginning to recognise common spelling patterns",
            "applies phonics skills to short words and is developing greater fluency",
            "shows consistent effort when sounding out words and benefits from gentle guidance"],
        
        5: ["shows growing confidence in recognising sounds and applying them in reading tasks",
            "reads many familiar words correctly and is building stronger decoding skills",
            "is developing smoother reading fluency and applies phonics knowledge independently in most cases",
            "recognises sound patterns more easily and continues to strengthen reading accuracy"],
        
        6: ["reads words fluently with some help and shows confidence in applying phonics rules",
            "applies phonics patterns correctly in most words and continues to build accuracy",
            "demonstrates good understanding of letter–sound combinations and reads more independently",
            "shows solid progress in decoding words and is becoming a more fluent reader"],
        
        7: ["uses phonics effectively to read new words and shows confidence when tackling unfamiliar text",
            "reads confidently and applies sound–letter patterns accurately across different words",
            "shows strong phonics understanding and reads new material with growing independence",
            "demonstrates clear fluency in decoding and rarely needs help with new words"],
        
        8: ["reads fluently and applies phonics rules accurately across a wide range of words",
            "demonstrates strong phonics understanding and reads new material with confidence",
            "uses phonics knowledge naturally to decode challenging words and maintain fluency",
            "shows excellent reading flow and rarely makes decoding errors during class activities"],
        
        9: ["shows excellent phonics skills and reads confidently across all types of text",
            "applies advanced phonics knowledge with ease and demonstrates strong reading fluency",
            "reads challenging words accurately and maintains a smooth, confident pace",
            "demonstrates near-mastery of phonics and consistently reads with expression and accuracy"],
        
       10: ["reads effortlessly and recognises all sounds with complete accuracy",
            "demonstrates exceptional mastery of phonics and reads with natural fluency",
            "shows full command of sound–letter patterns and reads with confidence and ease",
            "reads independently with flawless accuracy and excellent expression"],
    }
    return random.choice(comments.get(score, ["is developing phonics skills"]))

def get_vocabulary_comment(score):
    comments = {
        1: ["is just beginning to learn new words and often needs support to remember them",
            "struggles to recall and use familiar words but continues to try",
            "needs encouragement to review and practice new vocabulary regularly",
            "is developing early word awareness and benefits from extra repetition"],
        
        2: ["is starting to learn basic vocabulary and can recall a few familiar words",
            "shows growing interest in learning new words with guidance",
            "needs reminders to use recently learned vocabulary in class activities",
            "is beginning to connect new words to pictures or meanings with help"],
    
        3: ["can use some simple words correctly with support from the teacher",
            "is showing progress in remembering and applying familiar vocabulary",
            "recognises more words each week and is gaining confidence in using them",
            "is beginning to speak and write using a few known words independently"],
        
        4: ["shows good effort in learning vocabulary and is expanding basic word knowledge",
            "is improving and can use simple words in sentences with some support",
            "recognises many familiar words and applies them with growing accuracy",
            "demonstrates progress and motivation in vocabulary learning"],
        
        5: ["uses familiar vocabulary with increasing confidence in class discussions",
            "shows good understanding of word meanings and can apply them correctly",
            "is able to choose suitable words when writing or speaking about known topics",
            "demonstrates solid vocabulary skills and continues to expand word range"],
        
        6: ["applies vocabulary correctly in sentences and explains meanings with some detail",
            "uses new words naturally during reading and speaking activities",
            "shows confidence using most classroom vocabulary appropriately",
            "is building a broad and functional vocabulary across lessons"],
        
        7: ["expresses ideas clearly using a wide range of vocabulary",
            "uses topic-related words accurately in both oral and written tasks",
            "shows confidence when using new and more complex words",
            "demonstrates strong vocabulary control and understanding"],
        
        8: ["uses advanced vocabulary effectively in writing and discussion",
            "selects precise words to express ideas and opinions clearly",
            "demonstrates an excellent grasp of word meanings and usage",
            "applies sophisticated vocabulary naturally in class work"],
        
        9: ["has excellent vocabulary and uses words confidently and accurately",
            "shows strong awareness of word choice and style when expressing ideas",
            "integrates a wide range of vocabulary into fluent, natural sentences",
            "displays an impressive command of words and their meanings"],
        
        10: ["has outstanding vocabulary and uses words precisely and effectively",
            "expresses complex ideas with accuracy, confidence, and variety",
            "demonstrates mastery of vocabulary through clear, fluent communication",
            "uses rich and sophisticated language naturally in all areas of English"]
    }
    return random.choice(comments.get(score, ["is developing vocabulary skills"]))


def get_spelling_comment(score):
    comments = {
        1: ["struggles with spelling and often needs one-to-one support to complete written tasks",
            "has difficulty remembering basic spelling patterns and needs close guidance",
            "finds spelling challenging but continues to make small efforts",
            "needs regular reminders and help when writing unfamiliar words"],
        
        2: ["is beginning to spell short and familiar words but still needs support",
            "tries to apply simple spelling rules, though accuracy is inconsistent",
            "is developing awareness of sound–letter patterns with teacher guidance",
            "makes frequent attempts to spell on their own and benefits from encouragement"],
        
        3: ["can spell simple CVC or sight words correctly with help",
            "shows improving control of basic spelling patterns",
            "is starting to self-correct when spelling familiar words",
            "demonstrates growing confidence when spelling short words"],
        
        4: ["is improving spelling and beginning to remember common patterns",
            "spells most short words correctly and applies new rules with help",
            "uses phonics strategies to check spelling accuracy",
            "shows good effort to apply spelling lessons in writing"],
        
        5: ["spells familiar words correctly and shows confidence in writing",
            "demonstrates good progress and applies common spelling rules independently",
            "uses learned patterns effectively when writing short sentences",
            "is developing a consistent approach to spelling new vocabulary"],
        
        6: ["spells most words accurately and checks work carefully",
            "applies taught spelling rules with minimal support",
            "shows strong awareness of spelling patterns and exceptions",
            "writes neatly and pays attention to correct letter order"],
        
        7: ["spells accurately and uses a range of familiar and new words correctly",
            "applies spelling rules confidently across different writing tasks",
            "demonstrates solid control of patterns, prefixes, and suffixes",
            "self-corrects and edits work independently for spelling accuracy"],
        
        8: ["shows excellent spelling and consistently writes accurately",
            "applies complex spelling rules confidently in all written work",
            "demonstrates strong awareness of word structure and patterns",
            "uses new vocabulary accurately in writing with few or no errors"],
        
        9: ["demonstrates outstanding spelling skills and careful proofreading habits",
            "writes with precision and accuracy, using a wide range of words correctly",
            "shows mastery of advanced patterns and irregular spellings",
            "maintains high spelling accuracy even in extended writing tasks"],
        
        10: ["writes flawlessly with excellent spelling and clear attention to detail",
            "shows exceptional mastery of spelling and uses challenging words accurately",
            "consistently applies spelling rules across all forms of written expression",
            "produces written work that is precise, fluent, and virtually error-free"]
    }
    return random.choice(comments.get(score, ["is developing spelling skills"]))


def get_reading_comment(score):
    comments = {
        1: ["struggles with reading and often needs individual support to decode words",
            "finds it difficult to recognise common words and requires frequent guidance",
            "is still developing basic reading confidence and needs close assistance",
            "needs encouragement to stay focused while reading simple sentences"],
        
        2: ["is beginning to read short, familiar words with help from the teacher",
            "tries to sound out simple words and is slowly gaining confidence",
            "shows early understanding of phonics when reading basic texts",
            "is learning to recognise high-frequency words through repetition"],
        
        3: ["reads short and simple sentences with guidance and support",
            "is beginning to read familiar stories and can recall some details",
            "demonstrates growing confidence with short passages and sight words",
            "is developing fluency and can follow along with teacher support"],
        
        4: ["reads short passages with increasing fluency and understanding",
            "is improving reading flow and beginning to recognise patterns in text",
            "can understand simple stories and answer basic questions with support",
            "shows greater focus when reading short texts aloud"],
        
        5: ["reads familiar texts fluently and with growing confidence",
            "demonstrates good effort and comprehension during guided reading",
            "shows understanding of simple stories and can discuss key details",
            "is becoming an independent reader who enjoys short passages"],
        
        6: ["reads accurately and understands most short texts independently",
            "shows solid reading comprehension and good attention to meaning",
            "can identify key ideas in stories and respond thoughtfully",
            "reads aloud with smooth pacing and developing expression"],
        
        7: ["reads confidently and applies comprehension strategies effectively",
            "demonstrates clear understanding of both literal and implied meanings",
            "uses context to understand new vocabulary while reading",
            "reads a variety of texts with fluency and insight"],
        
        8: ["reads fluently and understands a wide range of stories and topics",
            "demonstrates excellent comprehension and makes thoughtful predictions",
            "connects ideas across paragraphs and understands character motivation",
            "reads with strong expression and confidence in all classroom tasks"],
        
        9: ["reads complex texts with strong understanding and clear interpretation",
            "demonstrates the ability to infer meaning and analyse deeper ideas",
            "reads confidently and explains main themes and details accurately",
            "shows maturity in reading comprehension and critical thinking"],
        
        10: ["is an outstanding reader who reads fluently and interprets meaning effortlessly",
            "demonstrates mastery of reading comprehension with insight and depth",
            "reads with perfect fluency and understands advanced vocabulary naturally",
            "shows exceptional analytical ability when reading complex passages"]
    }
    return random.choice(comments.get(score, ["is developing reading skills"]))


def get_comprehension_comment(score):
    comments = {
        1: ["struggles to understand stories and often needs questions repeated",
            "finds it difficult to recall story details or sequence events correctly",
            "needs help linking ideas together when listening or reading",
            "requires close teacher support to grasp the main idea of a text"],
        
        2: ["understands simple stories with help from the teacher",
            "can answer very basic questions when given clear examples",
            "shows partial understanding of key words and main events",
            "is beginning to identify who and what a story is about with guidance"],
        
        3: ["can answer simple questions independently after reading short passages",
            "demonstrates growing understanding of story structure and meaning",
            "is improving at recalling key details and basic cause-and-effect ideas",
            "shows developing comprehension when reading familiar topics"],
        
        4: ["understands most short texts and can retell key events with support",
            "can explain simple ideas from a passage with growing confidence",
            "shows steady improvement in recognising the main idea of a story",
            "is beginning to connect details to understand overall meaning"],
        
        5: ["understands stories well and can explain what happened clearly",
            "demonstrates good comprehension and can summarise short texts",
            "answers comprehension questions thoughtfully and accurately",
            "shows awareness of why characters act or feel a certain way"],
        
        6: ["understands most texts confidently and gives relevant answers",
            "shows solid comprehension and interprets meaning accurately",
            "can discuss main ideas and details without much guidance",
            "demonstrates consistent understanding of both fiction and nonfiction texts"],
        
        7: ["understands complex stories and explains ideas clearly in discussion",
            "interprets character feelings and motivations with good reasoning",
            "demonstrates strong comprehension and connects ideas effectively",
            "can identify the theme and key message of a passage confidently"],
        
        8: ["shows excellent comprehension and understands deeper meanings in text",
            "can analyse story elements and make logical inferences",
            "discusses character motives and text themes with maturity",
            "demonstrates clear insight when reading or discussing longer texts"],
        
        9: ["interprets texts accurately and can discuss ideas at an advanced level",
            "analyses details and explains complex messages effectively",
            "shows strong critical thinking while reading longer passages",
            "draws thoughtful conclusions supported by textual evidence"],
        
        10: ["has exceptional comprehension skills and analyses texts with insight and depth",
            "demonstrates mastery in understanding, inference, and interpretation",
            "discusses advanced ideas confidently and supports them with clear reasoning",
            "reads critically and understands subtle messages within complex texts"]
    }
    return random.choice(comments.get(score, ["is developing comprehension skills"]))


def get_grammar_comment(score):
    comments = {
        1: ["struggles with grammar and often needs help forming complete sentences",
            "finds it difficult to apply grammar rules and needs close guidance",
            "needs reminders to use correct word order and punctuation",
            "requires extra practice with sentence structure and verb forms"],
        
        2: ["is learning basic grammar and starting to recognise simple rules",
            "can form short sentences with teacher support",
            "sometimes applies rules correctly but needs consistent reminders",
            "is gaining awareness of basic tenses and sentence patterns"],
        
        3: ["can use simple sentences correctly with guidance",
            "is improving steadily in using proper grammar structures",
            "applies basic rules such as subject–verb agreement more accurately",
            "shows progress in forming complete sentences with correct punctuation"],
        
        4: ["shows steady improvement and uses grammar more consistently",
            "is beginning to self-correct small grammar mistakes in writing",
            "uses simple tenses correctly in most sentences",
            "demonstrates a growing understanding of sentence patterns"],
        
        5: ["uses grammar appropriately in short writing and speaking tasks",
            "demonstrates a good grasp of sentence structure and word order",
            "applies basic rules correctly and shows confidence in grammar use",
            "writes clear, simple sentences with few errors"],
        
        6: ["uses grammar correctly most of the time and self-corrects when needed",
            "shows solid understanding of different sentence forms and tenses",
            "applies grammar rules effectively in both writing and speaking",
            "constructs accurate and meaningful sentences consistently"],
        
        7: ["uses grammar confidently in all classroom activities",
            "writes and speaks with strong grammatical accuracy",
            "demonstrates good control of complex sentences and correct tense usage",
            "uses articles, prepositions, and connectors correctly in most cases"],
        
        8: ["demonstrates excellent grammar and consistent accuracy across tasks",
            "uses a wide range of sentence structures naturally and effectively",
            "shows strong command of tense consistency and word order",
            "applies grammar rules correctly and with confidence"],
        
        9: ["uses grammar precisely and consistently in all written and spoken work",
            "writes complex sentences with fluency and accuracy",
            "shows clear mastery of advanced grammar forms and sentence variety",
            "applies all grammar rules naturally and with minimal errors"],
        
        10: ["has exceptional grammar skills and uses language with great precision",
            "writes and speaks flawlessly, demonstrating full command of grammar",
            "shows mastery of complex sentence structures with natural flow",
            "applies advanced grammar intuitively and accurately in all contexts"]
    }
    return random.choice(comments.get(score, ["is developing grammar skills"]))


def get_speaking_comment(score):
    comments = {
        1: ["struggles to express ideas verbally and often stays very quiet in class",
            "needs encouragement to speak and relies heavily on teacher prompts",
            "finds it difficult to form complete sentences when speaking",
            "is shy during discussions and needs consistent support to participate"],
        
        2: ["is beginning to speak in simple sentences with help from the teacher",
            "shows effort in trying to communicate basic ideas verbally",
            "sometimes answers short questions but still lacks confidence",
            "is slowly becoming more comfortable speaking in front of others"],
        
        3: ["can communicate basic ideas and short answers with growing confidence",
            "shows progress in using simple words and phrases when speaking",
            "is beginning to use full sentences when responding to questions",
            "demonstrates improvement in pronunciation and clarity with support"],
        
        4: ["speaks clearly with some help and is improving in expressing ideas",
            "uses short sentences to share thoughts during class activities",
            "participates in class discussions when encouraged",
            "shows more confidence when practising dialogues or presentations"],
        
        
        5: ["speaks confidently in familiar situations and communicates ideas clearly",
            "shows a good understanding of how to express opinions and answers",
            "uses clear pronunciation and appropriate vocabulary when speaking",
            "is growing more fluent and willing to share ideas during discussions"],
        
        6: ["communicates effectively in most classroom situations",
            "can express thoughts and opinions clearly with few pauses",
            "uses correct grammar and vocabulary when speaking with support",
            "demonstrates solid fluency and confidence in short presentations"],
        
        7: ["speaks confidently and contributes actively to group discussions",
            "expresses ideas clearly and with good sentence flow",
            "uses a wide range of vocabulary and correct structures in speech",
            "shows strong understanding of tone, pronunciation, and intonation"],
        
        8: ["demonstrates strong speaking skills and engages well in conversations",
            "speaks fluently and naturally with accurate pronunciation",
            "shares complex ideas clearly and responds thoughtfully to others",
            "shows confidence and enthusiasm when speaking in front of the class"],
        
        9: ["is an excellent speaker who expresses ideas clearly and persuasively",
            "uses natural pacing and tone when delivering spoken tasks",
            "demonstrates excellent fluency and strong command of vocabulary",
            "shows leadership during group discussions through clear communication"],
        
        10: ["has exceptional speaking ability and communicates with ease and precision",
            "speaks fluently and confidently in both prepared and spontaneous situations",
            "demonstrates mastery of pronunciation, tone, and natural expression",
            "is a highly articulate and confident speaker in all classroom contexts"]
    }
    return random.choice(comments.get(score, ["is developing speaking skills"]))


def get_listening_comment(score):
    comments = {
        1: ["struggles to listen and follow instructions",
            "is easily distracted during lessons and often misses key details",
            "needs frequent reminders to stay focused and listen to English carefully",
            "speaks in their native language often and needs encouragement to listen and respond in English"],
        
        2: ["is learning to listen carefully but still becomes distracted during lessons",
            "needs encouragement to focus on English instructions instead of speaking in their native language",
            "can follow short directions with help but often needs repetition",
            "is beginning to understand English explanations but still relies on translation or peers for support"],
        
        3: ["can follow simple instructions with help when paying attention",
            "shows progress in listening but sometimes speaks in their native language instead of focusing on English",
            "needs reminders to listen actively and avoid distractions during listening tasks",
            "is improving in understanding short classroom dialogues when focused"],
        
        4: ["listens carefully sometimes and can follow simple instructions in English",
            "is improving at staying focused during listening tasks",
            "shows growing confidence in understanding spoken English with teacher support",
            "can respond correctly to short, familiar questions when attentive"],
        
        5: ["listens attentively most of the time and understands familiar instructions",
            "can follow English directions with little help",
            "is developing confidence in understanding short spoken passages",
            "shows good focus during listening activities"],
        
        6: ["listens carefully and follows most English instructions accurately",
            "can understand longer sentences and explanations in English",
            "shows solid concentration and responds well to spoken questions",
            "demonstrates steady improvement in listening comprehension"],
        
        7: ["pays attention and follows discussions with little difficulty",
            "understands spoken English clearly and responds appropriately",
            "shows good focus and effort during listening activities",
            "can follow classroom discussions and teacher explanations with confidence"],
        
        8: ["listens attentively and consistently follows English instructions",
            "understands details and main ideas in spoken English easily",
            "shows excellent focus and concentration during lessons",
            "demonstrates clear understanding of teacher directions and class discussions"],
        
        9: ["demonstrates outstanding listening skills and comprehension",
            "follows spoken English naturally and rarely needs repetition",
            "understands complex instructions and responds quickly and accurately",
            "shows excellent attention and understanding during all listening tasks"],
        
        10: ["has exceptional listening skills and understands spoken English effortlessly",
            "follows complex explanations and class discussions with complete accuracy",
            "pays full attention throughout lessons and rarely needs repetition",
            "demonstrates a high level of understanding and focus in all listening activities"]
    }
    return random.choice(comments.get(score, ["is developing listening skills"]))



def get_participation_comment(score):
    comments = {
        1: ["rarely participates in class activities and needs encouragement to share ideas",
            "is often hesitant to speak in English because of low confidence",
            "needs reassurance and support to feel comfortable joining class discussions",
            "is shy and sometimes avoids answering questions for fear of making mistakes"],
        
        2: ["participates occasionally but still feels nervous about making mistakes",
            "needs encouragement to raise their hand and share ideas more confidently",
            "is beginning to contribute in class with teacher support",
            "sometimes avoids speaking in English out of fear of saying something wrong"],
        
        3: ["joins class activities with growing confidence but still needs reminders to participate consistently",
            "is learning that it’s okay to make mistakes and improving in class participation",
            "shows willingness to contribute but benefits from extra encouragement",
            "participates in small groups with support and is slowly building confidence"],
        
        4: ["actively participates sometimes and shows interest in classroom activities",
            "is becoming more confident sharing ideas with peers",
            "joins discussions with some encouragement from the teacher",
            "demonstrates a positive attitude toward participation"],
        
        5: ["participates actively in class activities and shows good effort",
            "answers questions willingly and demonstrates engagement",
            "is becoming a confident and consistent contributor",
            "takes part in discussions and group work with enthusiasm"],
        
        6: ["participates regularly and contributes thoughtful ideas",
            "engages well with classmates during discussions and projects",
            "shows growing independence and initiative in class activities",
            "demonstrates enthusiasm and focus during lessons"],
        
        7: ["actively participates and contributes regularly in lessons",
            "shows strong engagement and often volunteers to answer questions",
            "shares ideas confidently and helps maintain a positive classroom atmosphere",
            "demonstrates initiative and leadership during group work"],
        
        8: ["participates enthusiastically and consistently in all classroom activities",
            "engages fully in discussions and helps motivate peers to join in",
            "shows excellent teamwork and positive classroom energy",
            "demonstrates confidence and leadership when sharing ideas"],
        
        9: ["is an outstanding participant who engages deeply in discussions",
            "always takes part in activities and encourages others to join",
            "shares thoughtful insights and models strong participation skills",
            "demonstrates genuine enthusiasm for class learning"],
        
        10: ["shows exceptional participation and enthusiasm in every lesson",
            "leads by example and helps create an inclusive classroom atmosphere",
            "is highly engaged, confident, and motivates others to contribute",
            "demonstrates mature communication and collaboration skills in all group settings"]
    }
    return random.choice(comments.get(score, ["is developing participation skills"]))


def get_writing_comment(score):
    comments = {
        1: ["struggles with writing and needs close support",
            "often forgets to write on the lines and leaves large spaces between words",
            "needs reminders to add punctuation and capital letters correctly",
            "is beginning to form clear letters but needs guidance to organize writing on the page"],
        
        2: ["is developing writing skills but sometimes forgets to use spaces or punctuation",
            "needs support to start sentences with capital letters and end with full stops",
            "writes basic sentences but requires reminders to stay on the line and write neatly",
            "shows effort in writing but often mixes words together without spacing"],
        
        3: ["can write simple sentences independently with some punctuation errors",
            "shows progress in spacing and neatness but still needs reminders",
            "is learning to use capital letters and punctuation consistently",
            "writes with support but sometimes forgets to separate words clearly"],
        
        4: ["writes short sentences clearly with some help",
            "shows steady progress in organizing ideas on the page",
            "is beginning to use punctuation and spacing more accurately",
            "demonstrates good effort in improving writing presentation"],
        
        5: ["writes competently and communicates ideas with basic structure",
            "uses punctuation and spacing correctly most of the time",
            "shows good understanding of sentence construction",
            "demonstrates clear progress in writing clarity and organization"],
        
        6: ["writes clearly and effectively using correct punctuation and spacing",
            "organizes ideas logically within simple paragraphs",
            "demonstrates solid grammar and spelling in most writing tasks",
            "shows confidence in structuring sentences and expressing ideas"],
        
        7: ["writes confidently and communicates ideas with good structure",
            "uses paragraphs appropriately and applies punctuation accurately",
            "shows strong spelling and grammar control",
            "writes neatly and demonstrates thoughtful expression"],
        
        8: ["demonstrates excellent writing skills with clarity and accuracy",
            "organizes ideas logically with good paragraphing and flow",
            "writes creatively using a variety of sentence types",
            "shows consistent attention to spelling, punctuation, and presentation"],
        
        9: ["is an outstanding writer who expresses ideas with precision and creativity",
            "uses advanced vocabulary and complex sentences effectively",
            "shows excellent control of grammar and organization",
            "writes with fluency and confidence across different topics"],
        
        10: ["has exceptional writing skills and produces high-quality work consistently",
            "writes fluently with strong structure, coherence, and creativity",
            "demonstrates mastery of spelling, grammar, and punctuation",
            "is a confident writer who communicates ideas with sophistication and style"]
    }
    return random.choice(comments.get(score, ["is developing writing skills"]))


def get_behaviour_comment(score):
    comments = {
        1: ["often disrupts lessons and needs reminders to focus on learning tasks",
            "has difficulty following instructions and staying on task",
            "frequently speaks in their native language and distracts classmates",
            "rarely completes homework and needs strong encouragement to take responsibility"],
        2: ["sometimes struggles to listen carefully during lessons",
            "needs reminders not to call out or speak while others are talking",
            "occasionally speaks in their native language instead of English during class",
            "forgets to raise their hand or wait their turn to speak"],
        3: ["shows improving behaviour but still needs reminders to stay focused",
            "sometimes loses concentration or talks during lessons",
            "is learning to follow rules and participate respectfully",
            "needs encouragement to complete homework and use English more consistently in class"],
        4: ["shows good behaviour with occasional reminders to stay focused",
            "respects classmates and usually follows class rules",
            "demonstrates better self-control and a positive attitude",
            "is beginning to take more responsibility for behaviour and effort"],
        5: ["demonstrates good behaviour consistently and follows classroom rules",
            "shows respect to classmates and teachers",
            "is becoming more responsible for their learning and actions",
            "participates appropriately and helps create a positive classroom atmosphere"],
        6: ["shows strong behaviour and treats others with respect",
            "follows rules reliably and shows growing maturity",
            "sets a positive example for others through good manners",
            "consistently listens well and focuses on tasks"],
        7: ["behaves very well and shows kindness and respect to others",
            "demonstrates leadership in behaviour and attitude",
            "follows instructions immediately and works cooperatively",
            "is a positive influence on classmates through good conduct"],
        8: ["demonstrates excellent behaviour and shows genuine respect for others",
            "acts responsibly and contributes to a calm, positive classroom environment",
            "shows strong self-discipline and cooperation with peers",
            "consistently displays positive attitude and maturity"],
        9: ["shows outstanding behaviour and sets a strong example for others",
            "respects all classmates and teachers and leads by example",
            "is highly dependable and consistently makes positive choices",
            "displays leadership through mature, respectful conduct"],
        10: ["is an exemplary student with perfect behaviour and responsibility",
            "consistently models respect, focus, and maturity in every situation",
            "shows exceptional leadership and encourages others to behave appropriately",
            "is polite, responsible, and a role model for the entire class"]
    }
    return random.choice(comments.get(score, ["is developing behaviour skills"]))

# --- Behaviour issue dropdown ---



# ---------------------------
# Skill function list
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
# Comment builder
# ---------------------------
def build_comment(name, pronoun, clauses, scores):
    avg = sum(scores) / len(scores)
    if avg <= 3:
        opening = f"{name} is finding English challenging and needs extra support."
    elif avg <= 6:
        opening = f"{name} is making steady progress across English skills."
    else:
        opening = f"{name} demonstrates strong English ability and approaches work confidently."
    sentences = [sentence_with_subject(pronoun, c) for c in clauses]
    return f"{opening} {' '.join(sentences)}"


# ---------------------------
# Generate full comment
# ---------------------------
def generate_comment(name, scores, gender_choice="She", grade_level="Grade 4", teacher_name="", behaviour_issue="None"):
    subject_name = name.strip()
    pronoun_cap = "She" if gender_choice.lower().startswith("s") else "He"
    _ = grade_level  # placeholder for future grade-specific logic
    clauses = [func(score) for func, score in zip(SKILL_FUNCS, scores)]


    behaviour_line = ""
    if behaviour_issue and behaviour_issue != "None":
        issue_phrases = {
            "Disruptive in class": "becomes distracted or disruptive during class",
            "Poor listening": "has difficulty listening carefully at times",
            "Speaking in native language": "speaks in their native language instead of English sometimes",
            "Not completing homework": "forgets to complete homework regularly",
            "Not raising hand / calling out": "calls out answers without raising a hand",
            "Not paying attention": "loses focus and needs reminders to stay on task"
        }
        issue_text = issue_phrases.get(behaviour_issue, behaviour_issue.lower())
        behaviour_line = f"\n\nBehaviour Concern: {pronoun_cap} sometimes {issue_text}."

    sentences = build_comment(subject_name, pronoun_cap, clauses, scores)
    avg = sum(scores) / len(scores)

    if avg <= 3:
        closing = f"Let’s keep working together to build {subject_name}’s skills step by step."
    elif avg <= 6:
        closing = f"{subject_name} is improving — keep up the steady effort each week."
    elif avg <= 8:
        closing = f"Great progress, {subject_name}! Keep working hard and stay confident."
    else:
        closing = f"Excellent work, {subject_name}! Keep shining and aiming high."

    conclusion = random.choice([
        "Excellent work!", "Nicely done!", "Fantastic job!",
        "Superb effort!", "Smooth execution!", "Outstanding result!"
    ])
    signature = f"\n– {teacher_name.strip()}" if teacher_name.strip() else ""
    return f"{sentences}\n{conclusion}{signature}\n{closing}{behaviour_line}"


    if avg <= 3:
        closing = f"Let’s keep working together to build {subject_name}’s skills step by step."
    elif avg <= 6:
        closing = f"{subject_name} is improving — keep up the steady effort each week."
    elif avg <= 8:
        closing = f"Great progress, {subject_name}! Keep working hard and stay confident."
    else:
        closing = f"Excellent work, {subject_name}! Keep shining and aiming high."

    conclusion = random.choice([
        "Excellent work!", "Nicely done!", "Fantastic job!",
        "Superb effort!", "Smooth execution!", "Outstanding result!"
    ])
    signature = f"\n– {teacher_name.strip()}" if teacher_name.strip() else ""
    return f"{sentences}\n{conclusion}{signature}\n{closing}"



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
                val = e.get().strip()
                if not val.isdigit():
                    raise ValueError
                num = int(val)
                if not (1 <= num <= 10):
                    raise ValueError
                scores.append(num)
            comment = generate_comment(
    name,
    scores,
    gender_var.get(),
    grade_var.get(),
    teacher_entry.get(),
    behaviour_issue_var.get()
)

            comment_box.delete("1.0", tk.END)
            comment_box.insert(tk.END, comment)
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid scores (1–10) for all fields.")

    def copy_action():
        text = comment_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Nothing to copy", "No comment to copy yet.")
            return
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Comment copied to clipboard.")

    def save_action():
        text = comment_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Nothing to save", "No comment to save yet.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            messagebox.showinfo("Saved", f"Comment saved to {path}")

    def clear_action():
        name_entry.delete(0, tk.END)
        for e in entries:
            e.delete(0, tk.END)

    root = tk.Tk()
    root.title("ESL Comment Generator – Teacher Edition (Unified Builder, Draft 2)")
    root.geometry("980x760")

    tk.Label(root, text="Student Name:").grid(row=0, column=0, padx=6, pady=6, sticky="e")
    name_entry = tk.Entry(root, width=28)
    name_entry.grid(row=0, column=1, sticky="w")

    tk.Label(root, text="Gender:").grid(row=0, column=2, padx=6, sticky="e")
    gender_var = tk.StringVar(value="She")
    tk.OptionMenu(root, gender_var, "She", "He").grid(row=0, column=3, sticky="w")

    tk.Label(root, text="Grade Level:").grid(row=0, column=4, padx=6, sticky="e")
    grade_var = tk.StringVar(value="Grade 4")
    tk.OptionMenu(root, grade_var, "Grade 2", "Grade 4", "Grade 6").grid(row=0, column=5, sticky="w")

    tk.Label(root, text="Teacher Name:").grid(row=0, column=6, padx=6, sticky="e")
    teacher_entry = tk.Entry(root, width=28)
    teacher_entry.grid(row=0, column=7, sticky="w")

    labels = ["Phonics", "Vocabulary", "Spelling", "Reading", "Comprehension",
              "Grammar", "Speaking", "Listening", "Participation", "Writing", "Behaviour"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(root, text=f"{label} (1–10):").grid(row=i+1, column=0, padx=6, sticky="e")
        e = tk.Entry(root, width=8)
        e.grid(row=i+1, column=1, sticky="w", pady=2)
        entries.append(e)
        
    # --- Behaviour issue dropdown ---
        tk.Label(root, text="Specific Behaviour Issue:").grid(row=11, column=2, sticky="e", padx=6)
        behaviour_issue_var = tk.StringVar(value="None")
        tk.OptionMenu(
            root,
            behaviour_issue_var,
            "None",
            "Disruptive in class",
            "Poor listening",
            "Speaking in native language",
            "Not completing homework",
            "Not raising hand / calling out",
            "Not paying attention"
        ).grid(row=11, column=3, sticky="w")


    tk.Button(root, text="Generate Comment", command=generate_action, bg="lightgreen").grid(row=13, column=0, pady=10)
    tk.Button(root, text="Copy Comment", command=copy_action, bg="lightblue").grid(row=13, column=1, pady=10)
    tk.Button(root, text="Save Comment", command=save_action, bg="khaki").grid(row=13, column=2, pady=10)
    tk.Button(root, text="Clear Inputs", command=clear_action, bg="lightpink").grid(row=13, column=3, pady=10)

    comment_box = tk.Text(root, height=20, width=120, wrap="word")
    comment_box.grid(row=14, column=0, columnspan=8, padx=10, pady=10, sticky="w")

    root.mainloop()

if __name__ == "__main__":
    run_gui()
