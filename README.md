# aiagent
A Boot.dev course project to build a toy version of Claude Code using Google's free Gemini API.

- [aiagent](#aiagent)
- [Disclaimer](#disclaimer)
- [Prompts](#prompts)

# Disclaimer
This project is intended for educational and learning purposes only. It is not meant for production use or deployment. Use at your own risk.

# Prompts
Manipulating the prompts and messages is important for getting the the tool to work as intended. Anything that involved writing or fixing code involved a message that looked like this:
```shell
uv run main.py "Fix the bug in pkg/calculator.py so that the expression 3 + 7 * 2 returns 17, respecting operator precedence. Use your file editing tools as soon as possible - do not list steps."
```

