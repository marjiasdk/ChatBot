import openai

openai.api_key = 'YOUR_API_KEY_HERE'

class Chatbot:
    # staticmethod is used to create a method that can be called without creating an object of the class
    @staticmethod
    def get_response(message):
        response = openai.Completion.create(
            engine='text-davinci-003',
            max_tokens=150,
            temperature=0.7,
            prompt=message + "Chatbot:",
            n=1,
            stop=None,
            timeout=10
        )

        reply = response.choices[0].text.strip()
        return reply

"""
Things to note:

* temperature adjusts the creativity of the bot's response, the higher it is, the more diverse the response will be
* prompt is the text that the bot will use to generate a response, it provides context to prevent nonsensical responses
- with prompt, you should ideally add + "Chatbot:" to the end of the message to make the bot's response more coherent
- otherwise, it will produce the most likely response based on the prompt, which may not be what you want
* engine is the model the bot will use to generate a response, models include gpt-3.5-turbo, davinci, curie, babbage, ada, etc.
* stop is used to stop the bot from generating text after a certain string

"""