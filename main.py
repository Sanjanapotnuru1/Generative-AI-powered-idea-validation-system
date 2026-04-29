# main.py

from modules import analyze_idea


def full_analysis(idea):
    return analyze_idea(idea)


# test run
if __name__ == "__main__":
    idea = "AI productivity app for students"
    result = full_analysis(idea)

    import json
    print(json.dumps(result, indent=2))