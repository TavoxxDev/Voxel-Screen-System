from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import base64, io, time, requests
import cv2
import tempfile

app = Flask(__name__)
CORS(app)

GRID = 64
FPS_TIMEOUT = 3

GITHUB_USER = "TavoxxDev"
REPO = "videos"
MEDIA_PATH = "videos"

last_frame = None
last_time = 0
current_audio = None

keys_state = {}


fallback_cap = None
fallback_loaded = False
fallback_last_frame_time = 0
fallback_fps = 24

def load_fallback_video():
    global fallback_cap, fallback_loaded

    if fallback_loaded:
        return

    url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO}/main/{MEDIA_PATH}/espera.mp4"

    r = requests.get(url)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tmp.write(r.content)
    tmp.close()

    fallback_cap = cv2.VideoCapture(tmp.name)
    fallback_loaded = True

def get_fallback_frame():
    global fallback_cap, fallback_last_frame_time

    if not fallback_loaded:
        load_fallback_video()

    if fallback_cap is None or not fallback_cap.isOpened():
        return None

    current_time = time.time()

    if current_time - fallback_last_frame_time < 1 / fallback_fps:
        return None

    fallback_last_frame_time = current_time

    ret, frame = fallback_cap.read()

    if not ret:
        fallback_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = fallback_cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (GRID, GRID))

    return frame.reshape(-1, 3).tolist()


@app.route("/")
def camera_page():
    return render_template("camera.html")

@app.route("/video")
def video_page():
    return render_template("video.html")

@app.route("/doom")
def doom_page():
    return render_template("doom.html")

@app.route("/videosList")
def videos_list():
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO}/contents"
    r = requests.get(url).json()

    videos = []
    for f in r:
        if f["name"].endswith(".mp4"):
            videos.append({
                "name": f["name"],
                "url": f["download_url"]
            })
    return jsonify(videos)

@app.route("/camera", methods=["POST"])
def camera():
    global last_frame, last_time

    raw = base64.b64decode(request.json["image"])
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    img = img.resize((GRID, GRID))

    last_frame = list(img.getdata())
    last_time = time.time()
    return jsonify(ok=True)

@app.route("/foto", methods=["POST"])
def foto():
    global last_frame, last_time

    if "image" not in request.files:
        return jsonify(error="Nenhuma imagem enviada"), 400

    img = Image.open(request.files["image"].stream).convert("RGB")
    img = img.resize((GRID, GRID))

    last_frame = list(img.getdata())
    last_time = time.time()
    return jsonify(ok=True)

@app.route("/cameraGet")
def camera_get():
    global last_frame

    if last_frame is None or time.time() - last_time > FPS_TIMEOUT:
        fallback_frame = get_fallback_frame()
        if fallback_frame:
            last_frame = fallback_frame

    return jsonify(
        ready=True,
        size=GRID,
        data=last_frame
    )

@app.route("/setAudio", methods=["POST"])
def set_audio():
    global current_audio
    current_audio = request.json["audio"]
    return jsonify(ok=True)

@app.route("/audioGet")
def audio_get():
    return jsonify(audio=current_audio)

@app.route("/keyDown", methods=["POST"])
def key_down():
    key = request.json.get("key")
    if not key:
        return jsonify(error="Sem tecla"), 400

    keys_state[key.upper()] = True
    return jsonify(ok=True)

@app.route("/keyUp", methods=["POST"])
def key_up():
    key = request.json.get("key")
    if not key:
        return jsonify(error="Sem tecla"), 400

    keys_state[key.upper()] = False
    return jsonify(ok=True)

@app.route("/keyboardGet")
def keyboard_get():
    return jsonify(keys=keys_state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
