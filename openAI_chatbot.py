import openai

openai.api_key = 'YOUR_API_KEY'

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