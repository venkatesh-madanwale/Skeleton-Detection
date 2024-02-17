from flask import Flask, render_template, request, send_from_directory
from pose_detection import detect_pose

app = Flask(__name__)

# Define the path for uploaded images and the output image
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the uploaded image
        uploaded_file = request.files['image']

        if uploaded_file.filename != '':
            # Save the uploaded image
            image_path = f"static/{uploaded_file.filename}"
            uploaded_file.save(image_path)

            # Perform pose detection and save the result
            output_image_path = "static/output.jpg"
            detect_pose(image_path, output_image_path)

            return render_template('index.html', image_path=output_image_path)

    return render_template('index.html', image_path=None)

if __name__ == '__main__':
    app.run(debug=True)
