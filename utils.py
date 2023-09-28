from transformers import BartForConditionalGeneration, BartTokenizer
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

def summerize_it(para):
    inputs = tokenizer(para, return_tensors="pt", max_length=2000, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=500, min_length=100, num_beams=6, length_penalty=2.0, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


if __name__ == "__main__":
    try:
        summary = summerize_it(
         """It can affect cognitive functions and interfere with memory, resulting
            in memory weakness [5]. Habib et al. [6] presented an extensive study regarding the effects of stress
            conditions over different functions of the body
            Diagnosing mental stress at the early stage is crucial to avoid further effects such as body
            dysfunctions. Current clinical practices involve questionnaire-based evaluations, such as perceived
            stress scale [7], stress response inventory [8], and life events and coping inventory [9], which can assess stress conditions. These evaluations are highly subjective and do not reflect the current state of mind
            in most cases. Furthermore, these questionnaires can be easily affected by the participants who are in
            denial [9]. Additionally, lack of awareness and denial regarding stress symptoms complicate stress
            diagnostics [10]. Therefore, to obtain a more reliable evaluation, several computer-aided diagnosis
            (CAD) systems have been employed based on different modalities such as electrocardiography (ECG),
            skin conductance, facial expression, blood pressure, functional near-infrared spectroscopy (fNIR),
            and electroencephalography (EEG)."""
        )
        print(summary)
    except Exception as e:
        print(e)
