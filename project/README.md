# 🧠 AFLL Lexical and Syntax Analyzer using PLY

### 📘 Overview
This project is developed as part of the **Automata, Formal Languages, and Logic (AFLL)** course.  
It implements a **Lexical Analyzer** and **Syntax Parser** using **Python Lex-Yacc (PLY)** to verify whether a given input string belongs to a defined **Context-Free Grammar (CFG)**.

---

## ⚙️ Project Objective
To simulate the working of a **compiler front-end** by performing:
1. **Lexical Analysis** – Tokenizing the input using Regular Expressions  
2. **Syntax Analysis** – Validating grammar structure using a CFG parser  

The system accepts or rejects strings based on grammar rules:

S → SS | (S) | ab | ε

---

## 🧩 Automata Constructors Used
| Constructor | Role in Project |
|--------------|-----------------|
| **Regular Expression (RE)** | Defines token patterns in `lexer.py` |
| **Finite Automata (FA/DFA)** | Used internally by PLY lexer to recognize tokens |
| **Pushdown Automata (PDA)** | Simulated by parser for handling nested structures |
| **Context-Free Grammar (CFG)** | Defined explicitly in parser rules |
| **Turing Machine (TM)** | The complete system behaves as a TM recognizer |

---

## ⚙️ Parsing Approach
This project uses the **Bottom-Up Parsing Approach (LALR(1))** implemented through PLY’s YACC module.  
It reads the input **from left to right** and constructs the **rightmost derivation in reverse**.

---

## 🧱 File Structure

AFLL_Lexical_Syntax_Analyzer/
│
├── lexer.py # Defines tokens using Regular Expressions
├── parser.py # Defines grammar rules and parsing logic
├── parsetab.py # Auto-generated parsing table by PLY
├── parser.out # Auto-generated grammar analysis report
└── README.md # Project documentation

---

## 🧠 How It Works
1. The **lexer** converts the input string into tokens (`a`, `b`, `(`, `)`).
2. The **parser** validates the token sequence according to the CFG.
3. If valid → ✅ Accepted  
   If invalid → ❌ Rejected

---

## 🧩 Example Outputs
### ✅ Valid Inputs
ab
(ab)
(ab)(ab)
((ab)(ab))

### ❌ Invalid Inputs
a
abb
(a)
(ab

---

## 🧪 Example Run
Comprehensive Automata Parser (PLY version)
Alphabet: a, b, (, )
Type 'quit' to exit.
Enter string> (ab)(ab)
✅ ACCEPTED: String fits grammar (balanced + matching a/b)
Enter string> (a)
❌ REJECTED: Invalid string (fails CFG or PDA rules)

---

## 📚 Viva Questions (Quick Reference)
| Q | A |
|---|---|
| Approach Used | Bottom-Up Parsing (LALR(1)) |
| Lexer Role | Tokenize input using RE |
| Parser Role | Validate syntax using CFG |
| Automata Constructors | RE, FA, PDA, CFG, TM |
| Grammar Used | S → SS \| (S) \| ab \| ε |
| Output | Accepted / Rejected |

---

## 🧩 Tools & Technology
- **Language:** Python 3  
- **Library:** PLY (Python Lex-Yacc)  
- **Concepts:** Regular Expression, DFA, PDA, CFG, Turing Machine  

Install PLY if not already:
```bash
pip install ply

Input → RE → FA (Lexer) → PDA (Parser) → CFG Validation → TM Decision (Accept/Reject)

👨‍💻 Developer
Akshar Vaghasiya
Diploma to Degree (Computer Engineering)
PES University – AFLL Course Project
Email : vaghasiyaakshar88@gmail.com
LinkedIn Id : https://www.linkedin.com/in/akshar-vaghasiya