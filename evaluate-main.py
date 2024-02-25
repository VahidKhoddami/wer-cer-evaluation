import Levenshtein

def calculate_wer(reference, hypothesis):
    reference_words = reference.split()
    hypothesis_words = hypothesis.split()

    wer = Levenshtein.distance(reference_words, hypothesis_words)

    return wer, len(reference_words)

def calculate_cer(reference, hypothesis):
    
    cer = Levenshtein.distance(reference, hypothesis)

    return cer, len(reference)

def evaluate_transcribe_output(reference_text, transcribe_output):
    wer, total_words = calculate_wer(reference_text, transcribe_output)
    cer, total_chars = calculate_cer(reference_text, transcribe_output)

    word_accuracy = (total_words - wer) / total_words
    char_accuracy = (total_chars - cer) / total_chars

    return {
        'WER': wer,
        'CER': cer,
        'Word_Accuracy': word_accuracy,
        'Char_Accuracy': char_accuracy
    }

#Normal Audio to text evaluation
reference_text = "The stale smell of old beer lingers. It takes heat to bring out the odor. A cold dip restores health and zest. A salt pickle tastes fine with ham. Tacos al pastor are my favorite. A zestful food is the hot-cross bun."
transcribe_output_google = "The stale smell of old beer lingers. It takes heat to bring out the odor a cold dip restores health and zest a salt pickle. Taste fine with ham tacos al Pastore are my favorite a zestful food is the hot cross bun."
transcribe_output_assemblyAi = "The stale smell of old beer lingers. It takes heat to bring out the odor. A cold dip restores health in zest. A salt pickle tastes fine with ham. Tacos al pastor are my favorite. A zestful food is the hot cross bun."
transcribe_output_azure = "The stale smell of old beer lingers. It takes heat to bring out the odor. A cold dip restores health and zest. A salt pickle tastes fine with ham tacos. Al pastora are my favorite. A zestful food is the hot cross bun."
transcribe_output_amazon = "The stale smell of old beer lingers. It takes heat to bring out the odor. A cold dip restores health and zest. A salt pickle tastes fine with ham tacos. El Pastor are my favorite. A zestful food is the hot Cross bun."
transcribe_output_ibm = "the stale smell of old beer lingers it takes heat to bring out the odor a cold dip restores health invest a salt pickled tastes fine with ham tacos al pastor are my favorite a zest for food is the hot cross bun"

evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_google)
print("Evaluation (normal) Result (google):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_assemblyAi)
print("Evaluation (normal) Result (assemblyAI):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_azure)
print("Evaluation (normal) Result (azure):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_amazon)
print("Evaluation (normal) Result (amazon):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_ibm)
print("Evaluation (normal) Result (IBM):", evaluation_result)

# Noisy Audio to text evaluation
reference_text = "The stale smell of old beer lingers"
transcribe_output_google = "the still smell of old gear vendors"
transcribe_output_assemblyAi = "The stale smell of old beer lingers"
transcribe_output_azure = "The stale smell of old beer lingers"
transcribe_output_amazon = "The stale smell of old beer ringers"
transcribe_output_Ibm = "this year "

evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_google)
print("Evaluation (noisy) Result (google):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_assemblyAi)
print("Evaluation (noisy) Result (assemblyAI):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_azure)
print("Evaluation (noisy) Result (azure):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_amazon)
print("Evaluation (noisy) Result (amazon):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_Ibm)
print("Evaluation (noisy) Result (IBM):", evaluation_result)

# Image1 to Text evaluation
reference_text = "A MOVE to stop Mr. Gaitskell from nominating\nany more Labour life Peers is to be made at a\nmeeting of Labour OM Ps tomorrow. Mr. Michael\nFoot has put down a resolution on the subject\nand he is to be backed by Mr. Will Griffiths,\nOM P for Manchester Exchange."
transcribe_output_google = "A MOVE to stop Mr. Gaihhall from nominating\nany\nшоне\nLabour life Peus is to be made at\na\nmeeting of Labour OM Pn tomoiron. Mr. Michael\nFoot ha\ndovu\na\nrevolution on the subject\nand he is to be backed by Mr. Will Griffither,\nOM P\nP for\nManchunki Exchange."
transcribe_output_azure = "A MOVE to stop Mr. Gaihell from nomating\nany more Labour life Peers is to be made at a\nmeeting of Labour OM Pr tomorrow. Mr. Michael\nFoot har put down a resolution on the subject\nand he is to be backed by Mr. Will Griffiths,\nUM P fer Manchester Exchange."
transcribe_output_amazon = "A MOVE to stop Mr. Gaihhell from numerianing\nany more Labour life Peen is to be made at a\nmeeting of labour OM Pn tomorrow. Mr. Michael\nFoot\nhas put down a resolution au the subject\nand he in to be backed by Mr. Will Giffith\nOM P for Manduski Exchange."


evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_google)
print("Evaluation (Image1) Result (google):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_azure)
print("Evaluation (Image1) Result (azure):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_amazon)
print("Evaluation (Image1) Result (amazon):", evaluation_result)

#Image2 to Text evaluation
reference_text = "This is a test!\nThis paper is in bad\ncondition!\nThe system is not working\nWe need help.\nThe pipes are leaking\nand no one is responsible for\nthat, unfortunately."
transcribe_output_google = "This is a text!\nThis paper is in bad\nCandition!\nThe System is not working\nWe need more help.\nThe pipes aut\nleaking\nand\nthat, unfortunately.\nno one is responsible for"
transcribe_output_azure = "This is a test!\nThis paper is in bad\nCondition!\nThe System is not working\nWe need more help\nThe piper are leaking\nand no one is responsible for\nthat, unharswately."
transcribe_output_amazon = "This is a test!\nThis paper is in bad\ncondition!\nThe System is not working\nWe need more help.\nThe Ripes are leaking\nand no one is responsible for\nthat, understanding"
transcribe_output_imagetotextio = "This is a test!\nThis paper is in bad\nCandition!\nThe System is not working\nWe need more help.\nThe pipes art\nleaking\nno one is responsible\nfor\nand no\nthat, unfortunately."

evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_google)
print("Evaluation (Image2) Result (google):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_azure)
print("Evaluation (Image2) Result (azure):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_amazon)
print("Evaluation (Image2) Result (amazon):", evaluation_result)
evaluation_result = evaluate_transcribe_output(reference_text, transcribe_output_imagetotextio)
print("Evaluation (Image2) Result (imagetotextio):", evaluation_result)