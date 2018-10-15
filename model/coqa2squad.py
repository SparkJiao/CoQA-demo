import json

with open('https://nlp.stanford.edu/data/coqa/coqa-train-v1.0.json', 'r') as coqa_train:
    source = json.load(coqa_train)
    dataset = source['data']

    title = "coqa"
    paragraph = list()
    for data in dataset:
        context = data["story"]
        qas = list()
        questions = data["questions"]
        answer = data["answers"]

        for i in range(questions):
            answers = list()
            question = questions[i]["input_text"]
            answer_item = {"answer_start": answer[i]["span_start"], "text": answer[i]["span_text"]}
            answers.append(answer_item)

            if "additional_answers" in data:
                additional_answers = data["additional_answers"]
                for index in additional_answers:
                    answer_item = {"answer_start":additional_answers[index][i]["span_start"], "text": additional_answers[index][i]["span_text"]}
                    answers.append(answer_item)

            qas_item = {"answers": answers, "question": question, "id": questions[i]["turn_id"]}
            qas.append(qas_item)

        paragraph_item = {"context": context, "qas": qas}
        paragraph.append(paragraph_item)

    data = list()
    data.append({"title": title, "paragraphs": paragraph})

    with open('squad-train.json', 'w') as file:
        json.dump(data, file, indent=4)


with open('https://nlp.stanford.edu/data/coqa/coqa-dev-v1.0.json', 'r') as coqa_train:
    source = json.load(coqa_train)
    dataset = source['data']

    title = "coqa"
    paragraph = list()
    for data in dataset:
        context = data["story"]
        qas = list()
        questions = data["questions"]
        answer = data["answers"]

        for i in range(questions):
            answers = list()
            question = questions[i]["input_text"]
            answer_item = {"answer_start": answer[i]["span_start"], "text": answer[i]["span_text"]}
            answers.append(answer_item)

            if "additional_answers" in data:
                additional_answers = data["additional_answers"]
                for index in additional_answers:
                    answer_item = {"answer_start":additional_answers[index][i]["span_start"], "text": additional_answers[index][i]["span_text"]}
                    answers.append(answer_item)

            qas_item = {"answers": answers, "question": question, "id": questions[i]["turn_id"]}
            qas.append(qas_item)

        paragraph_item = {"context": context, "qas": qas}
        paragraph.append(paragraph_item)

    data = list()
    data.append({"title": title, "paragraphs": paragraph})

    with open('squad-dev.json', 'w') as file:
        json.dump(data, file, indent=4)