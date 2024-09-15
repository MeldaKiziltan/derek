from flask import Flask, request
from groq import Groq
import json
app = Flask(__name__)

@app.route('/process_base64', methods=['POST'])
def process_base64():
    base64_string = request.json.get('base64_string')
    if base64_string:
        client = Groq()

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Count the number of red squares in this image, and identify if there is a toy robot or robot drawing in the image. Respond in the following json format: { redSquares: 0, toy_robot: false, robot_drawing: false }."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_string}",
                            },
                        },
                    ],
                }
            ],
            model="llava-v1.5-7b-4096-preview",
        )
        return response.choices[0].message.content, 200
    else:
        return 'No base64 string provided', 400

if __name__ == '__main__':
    app.run(debug=True)
