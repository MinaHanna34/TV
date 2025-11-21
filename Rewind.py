from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

COOLDOWN_SECONDS = 20
last_trigger_time = 0  # shared timer


def key(code: str):
    os.system(f"input keyevent {code}")


@app.route("/rew", methods=["GET", "POST"])
def handle_rew():
    global last_trigger_time
    now = time.time()
    diff = now - last_trigger_time
    print(f"/rew → diff {diff:.1f}s")

    if diff > COOLDOWN_SECONDS:
        key("23")      # CENTER
        time.sleep(0.2)
        key("21")      # LEFT
    else:
        key("21")      # LEFT only

    last_trigger_time = now
    return jsonify({"status": "rew ok", "cooldown": diff}), 200


@app.route("/fast", methods=["GET", "POST"])
def handle_fast():
    global last_trigger_time
    now = time.time()
    diff = now - last_trigger_time
    print(f"/fast → diff {diff:.1f}s")

    if diff > COOLDOWN_SECONDS:
        key("85")      # PAUSE
        time.sleep(0.2)
        key("22")      # RIGHT
    else:
        key("22")      # RIGHT only

    last_trigger_time = now
    return jsonify({"status": "fast ok", "cooldown": diff}), 200


if __name__ == "__main__":
    print("TV skip server running on port 5000...")
    app.run(host="0.0.0.0", port=5000)
