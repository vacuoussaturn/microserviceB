from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Store videos in memory for now
videos = []

@app.route('/upload', methods=['POST'])
def upload_video():
    data = request.get_json()

    # Validate input
    if not all(k in data for k in ("title", "description", "url")):
        return jsonify({"error": "Missing fields"}), 400

    video_entry = {
        "title": data["title"],
        "description": data["description"],
        "url": data["url"]
    }
    videos.append(video_entry)

    return jsonify({"message": "Video uploaded successfully", "video": video_entry}), 201

@app.route('/videos', methods=['GET'])
def get_videos():
    return jsonify(videos)

if __name__ == '__main__':
    app.run(port=7006, debug=True)
