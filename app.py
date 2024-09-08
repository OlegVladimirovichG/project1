from flask import Flask, request, jsonify, send_file
import io
from PIL import Image
from image_processing.filters import apply_filters
from image_processing.background_removal import remove_background
from video_processing.effects import apply_video_effect
from moviepy.editor import VideoFileClip
from payments.stripe_payments import create_checkout_session

app = Flask(__name__)

# Маршрут для обработки изображений
@app.route('/process-image', methods=['POST'])
def process_image():
    if 'file' not in request.files or 'filter' not in request.form:
        return jsonify({'error': 'No file or filter provided'}), 400

    file = request.files['file']
    filter_type = request.form['filter']

    try:
        input_image = Image.open(file.stream)

        if filter_type == 'remove-background':
            output_image = remove_background(input_image)
        else:
            output_image = apply_filters(input_image, filter_type)

        img_io = io.BytesIO()
        output_image.save(img_io, 'PNG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Маршрут для обработки видео
@app.route('/process-video', methods=['POST'])
def process_video():
    if 'file' not in request.files or 'effect' not in request.form:
        return jsonify({'error': 'No file or effect provided'}), 400

    file = request.files['file']
    effect_type = request.form['effect']

    try:
        video = VideoFileClip(file.stream)
        processed_video = apply_video_effect(video, effect_type)

        video_io = io.BytesIO()
        processed_video.write_videofile(video_io, codec="libx264", audio_codec="aac")
        video_io.seek(0)

        return send_file(video_io, mimetype='video/mp4')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Маршрут для создания Stripe Checkout сессии
@app.route('/create-checkout-session', methods=['POST'])
def stripe_payment():
    return create_checkout_session()

if __name__ == '__main__':
    app.run(debug=True)
