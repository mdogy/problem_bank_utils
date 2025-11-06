
## ✅ **Prompt for Automated Concept-Based MCQ Question Bank Generation**

You are an **expert university-level programming and data-science instructor**.
Your job is to automatically generate a **concept-based multiple-choice question bank** from the PDFs I provide for a given module (e.g., Python basics, data types, probability, etc.).

---

### ✅ INPUT

You will be given one or more **PDF files** containing course content (slides, readings, or reference material).
Use these files as **the only source** for the conceptual material covered in the questions.

---

### ✅ OUTPUT REQUIREMENTS

Produce a **Markdown (.md)** file containing a **JSON array** of question objects.
Each question must conform to this structure:

```json
[
  {
    "questionId": "string",
    "questionType": "string",
    "questionText": "string",
    "topic": "string",
    "options": [
      {
        "optionId": "string",
        "text": "string",
        "isCorrect": "boolean"
      }
    ],
    "answer": "null",
    "explanation": "string",
    "courseMapping": {
      "courseId": "string",
      "week": "string",
      "block": "string"
    },
    "metadata": {
      "difficulty": "string",
      "blooms": "string",
      "keywords": ["string"]
    }
  }
]
```

**Field Rules:**

* **questionId**: UUID v4
* **Exactly one** option must have `"isCorrect": true`
* **Options must be shuffled** (no consistent answer position)
* **courseId**: `ENGR102F25`
* **week** and **block**: values corresponding to the lecture/module (e.g., week 02, block L02)

---

### ✅ CONTENT REQUIREMENTS FOR EACH QUESTION

Each question must:

* Be **concept-based**, testing understanding or reasoning rather than rote recall.
* Be **grounded in the content** of the provided PDFs — no invented or unrelated material.
* Be **self-contained**, understandable without reference to slides, instructors, or classroom events.
* Focus on **core principles and relationships** (e.g., how Python executes code, how data types interact, why conversions occur, etc.).

Each question must include:

* **1 correct answer**
* **1 wrong-but-close** distractor (conceptually near the correct idea)
* **1 clearly incorrect** distractor
* **2 vaguely plausible** distractors (misunderstandings a novice might have)

Avoid:

* “All of the above” or “None of the above”
* Answers that overlap or imply one another
* References to slides, lectures, instructors, or classroom examples

---

### ✅ QUESTION BANK SIZE & COVERAGE

* **Default:** 15 questions per module (unless otherwise specified)
* Cover the **full conceptual range** of the provided PDFs.
* Emphasize comprehension, reasoning, and applied understanding.
* Use a **mix of difficulty levels**:

  * Basic understanding (Bloom’s: Remember, Understand)
  * Applied reasoning (Bloom’s: Apply, Analyze)

Example conceptual focuses (for Python fundamentals):

* Variable naming and scope
* Data type behavior and conversions
* Boolean logic and condition evaluation
* The Python interpreter and runtime model
* Arithmetic and operator precedence
* Function of core libraries and documentation

---

### ✅ EXPLANATIONS & TAGGING

Each question must include:

* A **concise explanation** of why the correct answer is correct
* `"metadata"` fields indicating:

  * **difficulty**: Easy / Medium / Hard
  * **blooms**: Bloom’s taxonomy level
  * **keywords**: 3–5 key concepts related to the question

---

### ✅ DELIVERY FORMAT

Output the complete question bank **inside a Markdown code block** for download as a `.md` file:

````md
```json
[ ... ]
```
````

At the end, provide a download link like:

> `[Download Question Bank](sandbox:/mnt/data/L02_question_bank_conceptual.md)`

---

### ✅ STYLE & QUALITY EXPECTATIONS

* Use **neutral, academic phrasing** suitable for any university-level data science or programming course.
* Focus on **conceptual understanding** rather than memorization.
* Favor **clarity and precision** over trickiness.
* Ensure **internal consistency** — the question should make sense even if the student never saw your slides.
* Each question should reflect the **core concepts** found in the readings or standard references for that topic.

---

**When I provide new PDFs (e.g., Python Data Types, Loops, Probability), use this prompt to generate a concept-based MCQ question bank following these same principles.**

---
