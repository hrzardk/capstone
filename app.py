import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path="C:\\Users\\ASUS\\setara-be\\model.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Define a mapping for jobs based on the output indices from the model
job_mapping = {
    0:	"Manager",
    1:	"Delivery truck drivers",
    2:	"Janitor",
    3:	"Retail supervisor",
    4:	"Registered nurse",
    5:	"Administration",
    6:	"Hospitality staff",
    7:	"Graphic designer",
    8:	"Tailor",
    9:	"Digital marketing",
    10:	"Social media specialist",
    11:	"Content writer",
    12:	"Content creator",
    13:	"Web developer",
    14:	"Opearator sewing",
    15:	"Accountant",
    16:	"Operator sampel",
    17:	"Video editor",
    18:	"Virtual broadcaster",
    19:	"Program producer",
    20:	"Waitress",
    21:	"Production operator",
    22:	"Barista",
    23:	"customer service",
    24:	"Telemarketing",
    25:	"Sales",
    26:	"Business & partnership executive",
    27:	"Programmer",
    28:	"Production staff",
    29:	"Cook helper",
    30:	"Host live streamer",
    31:	"Cashier",
    32:	"Online shop admin",
    33:	"Interior designer",
    34:	"Store crew",
    35:	"Bank administration",
    36:	"Industry production",
    37:	"Therapist",
    38:	"Finance",
    39:	"Information, communication, and publication staff",
    40:	"Industrial engineer",
    41:	"Budget analyst",
    42:	"Call center",
    43:	"HR payroll staff",
    44:	"Marketing & creative",
    45:	"Massage service partner",
    46:	"Videographer",
    47:	"SEO staff",
    48:	"Advertiser",
    49:	"Language tutors",
    50:	"Treasurer",
    51:	"Payment officer",
    52:	"Desk support",
    53:	"Partnership executive",
    54:	"Journalist",
    55:	"Carwash service partner",
    56:	"Photo editor",
    57:	"talent acquisition",
    58:	"Pettern & sample maker",
    59:	"Illustrator",
    60:	"Hairdresser",
    61:	"Print staff",
    62:	"Digital campaign optimizer",
    63:	"Computer designer",
    64:	"Bird's nest worker",
    65:	"3D animator",
    66:	"Office organizer",
    67:	"Copywriter",
    68:	"Online store supervisor",
    69:	"Streaming host talent",
    70:	"Logistic staff",
    71:	"helpdesk officer",
    72:	"Creative designer",
    73:	"Ironer",
    74:	"2D motion graphic designer",
    75:	"IT Development",
    76:	"React js developer",
    77:	"Sketch digital artist",
    78:	"Shopkeeper",
    79:	"Quality assurance",
    80:	"Webmaster",
    81:	"Legal officer",
    82:	"Project management officer",
    83:	"Account executive",
    84:	"Admission",
    85:	"Warehouse Supervisor",
    86:	"Packing operator",
    87:	"Data entry staff",
    88:	"Broadcaster",
    89:	"Fabric beader",
    90:	"Psychological counselor",
    91:	"2D designer",
    92:	"3D designer",
    93:	"Instagram admin",
    94:	"Cutting operator",
    95:	"Garment merchandisr staff",
    96:	"CAD designer",
    97:	"Librarian",
    98:	"Fullstack developer",
    99:	"Android & IOS programmer",
    100:"intenet assessor", 
    101:"internet rater",
    102:"executive banking, operations, finance",
    103:"branch operations officer"
}

# Preprocessing function to normalize inputs
def preprocess_input(age, experience, disability, location, gender):
    # Example preprocessing (you may need to adjust based on your model)
    disability_mapping = {"none": 0, "vision": 1, "hearing": 2, "mobility": 3}
    location_mapping = {"urban": 0, "rural": 1}
    gender_mapping = {"male": 0, "female": 1}

    # Normalize age and experience
    age_normalized = age / 100
    experience_normalized = experience / 50

    # Map categorical inputs
    disability_encoded = disability_mapping.get(disability.lower(), -1)
    location_encoded = location_mapping.get(location.lower(), -1)
    gender_encoded = gender_mapping.get(gender.lower(), -1)

    if -1 in [disability_encoded, location_encoded, gender_encoded]:
        raise ValueError("Invalid input values")

    # Return as numpy array
    return np.array([[age_normalized, experience_normalized, disability_encoded, location_encoded, gender_encoded]], dtype=np.float32)

@app.route('/predict', methods=['POST'])
def predict_job():
    try:
        # Parse input JSON
        data = request.json
        age = data.get("age")
        experience = data.get("experience")
        disability = data.get("disability")
        location = data.get("location")
        gender = data.get("gender")

        # Validate inputs
        if None in [age, experience, disability, location, gender]:
            return jsonify({"error": "All input fields are required"}), 400

        # Preprocess inputs
        input_data = preprocess_input(age, experience, disability, location, gender)

        # Perform inference
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])

        # Decode output (get job with the highest probability)
        predicted_job_index = np.argmax(output_data)
        predicted_job = job_mapping.get(predicted_job_index, "Unknown")

        # Return prediction
        return jsonify({
            "predicted_job": predicted_job
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
