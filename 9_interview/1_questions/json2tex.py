import json


def printQuestions(
    jsonPath: str = "online_interview.json",
    schoolName: str = None,
):
    """
    Generate a list of questions from the database.
    """

    if jsonPath is None or jsonPath == "":
        jsonPath = "online_interview.json"

    # Load online_interview.json
    with open(jsonPath, "r") as f:
        data = json.load(f)

        if schoolName is None or schoolName == "":  # reflection
            # Print all 'question' field under 'questions'
            for question in data["questions"]:
                print("\\subsection{" + question["question"] + "}")
                # if "askedBy" in question AND question["askedBy"] is a list with at least one element
                if "askedBy" in question and len(question["askedBy"]) > 0:
                    print("Asked by: ")
                    for school in question["askedBy"]:
                        print(school["name"] + ", " + school["date"] + "; ")
        elif schoolName == "all":  # preparation
            # Print all 'question' field under 'questions'
            for idx, question in enumerate(data["questions"]):
                print(
                    "\\subsection{"
                    + question["question"]
                    + "}\\label{q"
                    + str(idx + 1)
                    + "}"
                )
                for answer in question["prepAnswers"]:
                    print("\\paragraph{Prepared for", end="")
                    for i, employer in enumerate(answer["employers"]):
                        (
                            print(" " + employer, end="")
                            if i == 0
                            else print(", " + employer, end="")
                        )
                    print(":}")
                    print("\\begin{itemize}")
                    for point in answer["answerPoints"]:
                        # if point is string, print it directly
                        if isinstance(point, str):
                            print("\\item " + point)
                        # if point is list, print each element in the list
                        elif isinstance(point, list):
                            print("\\begin{itemize}")
                            for subPoint in point:
                                print("\\item " + subPoint)
                            print("\\end{itemize}")
                    print("\\end{itemize}")
        else:  # school specific
            # Print all 'question' field under 'questions'
            for idx, question in enumerate(data["questions"]):
                print(
                    "\\subsection{"
                    + question["question"]
                    + "}\\label{q"
                    + str(idx + 1)
                    + "}"
                )
                for answer in question["prepAnswers"]:
                    for employer in answer["employers"]:
                        if employer.lower() == schoolName.lower():
                            print("\\begin{itemize}")
                            for point in answer["answerPoints"]:
                                # if point is string, print it directly
                                if isinstance(point, str):
                                    print("\\item " + point)
                                # if point is list, print each element in the list
                                elif isinstance(point, list):
                                    print("\\begin{itemize}")
                                    for subPoint in point:
                                        print("\\item " + subPoint)
                                    print("\\end{itemize}")
                            print("\\end{itemize}")
                            break


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Pass school name")
    parser.add_argument("--json", required=False, help="json file path")
    parser.add_argument("--name", required=False, help="school name")
    args = parser.parse_args()
    printQuestions(args.json, args.name)
