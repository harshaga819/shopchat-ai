# ShopSense AI

An AI customer support agent for an online store. It understands natural
language questions, decides which tool(s) to call, chains tool calls when
needed, and returns a clear, customer-friendly answer — without fabricating
information.

Built with **LangChain**, **Gemini 2.5 Flash**, and **Streamlit**.

---

## What it does

Given a question like:

```
Where is my order ORD-1002?
```

the agent decides it needs order information, calls the right tool, and
turns the result into a natural reply:

```
Your order ORD-1002 is currently in transit and is at the Jaipur Hub.
Expected delivery: 29 June 2026.
```

For questions that need more than one piece of information, the agent
chains tool calls on its own — no manual routing logic is written for this.

---

## Tools

| Tool | Purpose |
|---|---|
| `get_order(order_id)` | Fetch order details by order ID |
| `get_product(product_id)` | Fetch product details by product ID |
| `search_products(query)` | Search products by keyword (name or category) |

The LLM decides which of these to call, in what order, based on the
question — it never receives or guesses data outside of what a tool
returns.

---

## Project structure

```
shopsense-ai/
├── app.py            # Streamlit chat interface
├── agent.py          # Agent setup, tool registration, run_agent()
├── tools.py          # The 3 business tools listed above
├── database.py       # In-memory dummy products/orders data
├── llm.py             # Gemini model setup
├── config.py          # Loads GOOGLE_API_KEY from .env
├── requirements.txt
├── .env.example
└── README.md
```

---

## Setup

1. Clone the repo and move into it:

   ```bash
   git clone <repository-url>
   cd shopsense-ai
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your Gemini API key. Copy `.env.example` to `.env` and fill it in:

   ```
   GOOGLE_API_KEY=your_key_here
   ```

   Get a key from [Google AI Studio](https://aistudio.google.com/).

---

## Running it

**Web interface:**

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`.

**Command line:**

```bash
python agent.py
```

Type your question, or `exit` to quit.

---

## Sample inputs and outputs

**Input:** `Where is my order ORD-1002?`
**Output:**
```
Your order ORD-1002 is in transit, currently at the Jaipur Hub.
Expected delivery is 29 June 2026.
```

**Input:** `Tell me about product P101.`
**Output:**
```
The Nike Air Max is a shoe priced at ₹7,999, rated 4.7, with 15 units
in stock.
```

**Input:** `Find shoes under ₹5000.`
**Output:**
```
Here are some shoes under ₹5,000:
1. Puma Runner - ₹4,999
2. Campus Running Shoes - ₹2,999
```

**Input:** `Where is my order ORD-9999?`
**Output:**
```
I couldn't find an order with that ID — could you double-check the
order number?
```

**Input:** `Do you have any laptops?`
**Output:**
```
Sorry, I couldn't find any products matching "laptops" in our
catalog right now.
```

---

## Error handling

- Unknown order IDs and product IDs return a polite "not found" message
  instead of an error or a guess.
- Empty search results are reported honestly — the agent never invents a
  product to fill the gap.
- Tool calls always return structured `{"success": bool, ...}` data, so the
  LLM only ever phrases what actually came back from the tool.

---

## Tech stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| LLM | Gemini 2.5 Flash |
| Agent framework | LangChain (`create_tool_calling_agent`) |
| UI | Streamlit |
| Validation | Pydantic |
| Env management | python-dotenv |

---

## Notes

The product/order data lives in `database.py` as an in-memory dictionary,
standing in for a real database. Swapping it for SQL, MongoDB, or a REST
API wouldn't require any changes to `agent.py` or `tools.py` — only the
data-access layer.
