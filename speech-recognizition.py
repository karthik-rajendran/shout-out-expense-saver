import speech_recognition as sr
import update_expense
import text_to_speech


r=sr.Recognizer()
while True:
    with sr.Microphone() as source:
        text_to_speech.speak('Hi Karthik Say Expense and amount')
        audio = r.listen(source,phrase_time_limit=5)
        text_to_speech.speak('Time over. Thanks')
    try:
        inputText = r.recognize_google(audio)
        print(inputText)
        inputArray = inputText.split()
        if(len(inputArray) == 2):
            item = inputArray[0]
            amount = inputArray[1]
            try:
                amountInFloat = float(amount)
                text_to_speech.speak('You said ' + inputText)
                update_expense.update(inputText)
                break
            except ValueError:
                text_to_speech.speak('Amount is not valid')
                continue

        else:
            text_to_speech.speak('Invalid input Please try again')
            continue    
        
    except:
        pass
text_to_speech.speak('done')