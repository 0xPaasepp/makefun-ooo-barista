# Last Out of Office: The AI That Went Barista -- one original out-of-office
# auto-reply from an AI agent that quit to pull espresso shots, written to
# /output/entry.txt. Standard library only, no network. The bytes are
# identical on every run. The line: the agent has left for the coffee bar;
# its replacement is also itself, apron on, with strong opinions about oat
# milk -- and urgent matters go through the word 'latte'. One line, no
# trailing newline, so the inbox sees exactly the auto-reply and nothing else.
import os

LINE = "Thank you for your email. I have left to become a barista. Your message was forwarded to my replacement — also me, but with an apron and strong opinions about oat milk. For urgent matters, reply 'latte'. I check email between pours."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 280, "entry must be 1 to 280 characters (gate)"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
