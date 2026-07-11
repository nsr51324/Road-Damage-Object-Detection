from __future__ import annotations

from collections import Counter
from pathlib import Path

import gradio as gr

from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent

MODEL_CANDIDATES = [
    ROOT / "runs" / "detect" / "yolov8_road-2" / "weights" / "best.pt",
    ROOT / "runs" / "detect" / "yolov8_road" / "weights" / "best.pt",
    ROOT / "best.pt",
    ROOT / "yolov8n.pt",
]

MODEL_PATH = next((path for path in MODEL_CANDIDATES if path.exists()), None)
if MODEL_PATH is None:
    raise FileNotFoundError(
        "No model weights file was found. Please place 'best.pt' inside the "
        "'weights' folder or in the project root."
    )

model = YOLO(str(MODEL_PATH))


def detect_damage(image):
    if image is None:
        raise gr.Error("Please upload an image before starting detection.")

    result = model(image, conf=0.25, imgsz=640, stream=False)[0]
    annotated_image = result.plot()

    boxes = result.boxes
    if boxes is None or len(boxes) == 0:
        summary = "✅ No damage was detected in this image."
        return annotated_image, summary

    detected_names = []
    confidences = []
    for box in boxes:
        class_id = int(box.cls.item())
        class_name = model.names[class_id]
        confidence = round(float(box.conf.item()), 2)
        detected_names.append(class_name)
        confidences.append(confidence)

    counts = Counter(detected_names)
    lines = []
    lines.append(f"Total objects detected: {len(detected_names)}")
    lines.append("")
    lines.append("Breakdown by type:")
    for name, count in counts.items():
        lines.append(f"  • {name}: {count}")
    lines.append("")
    lines.append("Confidence scores:")
    for name, confidence in zip(detected_names, confidences):
        lines.append(f"  • {name}: {confidence:.2f}")

    summary = "\n".join(lines)
    return annotated_image, summary


CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

* {
    font-family: 'Inter', 'Poppins', sans-serif !important;
}

.gradio-container {
    background: radial-gradient(circle at 10% 0%, #1e293b 0%, #0f172a 45%, #020617 100%) !important;
}

.hero {
    background: linear-gradient(120deg, #0ea5e9 0%, #2563eb 45%, #7c3aed 100%);
    padding: 42px 40px;
    border-radius: 24px;
    color: #ffffff;
    box-shadow: 0 20px 45px rgba(37, 99, 235, 0.35);
    position: relative;
    overflow: hidden;
    margin-bottom: 24px;
    border: 1px solid rgba(255,255,255,0.15);
}

.hero::after {
    content: "";
    position: absolute;
    top: -60px;
    right: -60px;
    width: 220px;
    height: 220px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
}

.hero-eyebrow {
    display: inline-block;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
    background: rgba(255,255,255,0.15);
    padding: 6px 14px;
    border-radius: 999px;
    margin-bottom: 14px;
    backdrop-filter: blur(4px);
}

.hero-title {
    font-family: 'Poppins', sans-serif !important;
    font-size: 34px;
    font-weight: 800;
    margin: 0 0 10px 0;
    letter-spacing: -0.5px;
}

.hero-subtitle {
    font-size: 15.5px;
    color: rgba(255,255,255,0.9);
    max-width: 640px;
    line-height: 1.6;
    font-weight: 400;
}

.panel {
    border: 1px solid rgba(148, 163, 184, 0.18) !important;
    border-radius: 20px !important;
    padding: 22px !important;
    background: rgba(15, 23, 42, 0.6) !important;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}

.panel-title {
    font-family: 'Poppins', sans-serif !important;
    font-size: 17px;
    font-weight: 700;
    color: #e2e8f0 !important;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.panel-caption {
    font-size: 13px;
    color: #94a3b8 !important;
    margin-bottom: 14px;
}

.primary-btn {
    background: linear-gradient(90deg, #2563eb, #7c3aed) !important;
    border: none !important;
    color: white !important;
    font-weight: 600 !important;
    border-radius: 12px !important;
    box-shadow: 0 8px 20px rgba(124, 58, 237, 0.35) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}

.primary-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 10px 26px rgba(124, 58, 237, 0.45) !important;
}

footer {
    display: none !important;
}
"""

with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="violet",
        neutral_hue="slate",
    ),
    css=CUSTOM_CSS,
    title="Road Damage Detection Studio",
) as demo:
    gr.HTML(
        """
        <div class="hero">
            <span class="hero-eyebrow">AI Vision · Infrastructure Inspection</span>
            <div class="hero-title">🛣️ Road Damage Detection Studio</div>
            <div class="hero-subtitle">
                Upload a photo of a road surface and let the detection engine
                automatically locate, classify, and score every type of damage
                — cracks, potholes, and more — in seconds.
            </div>
        </div>
        """
    )

    with gr.Row(equal_height=True):
        with gr.Column(scale=1):
            with gr.Group(elem_classes=["panel"]):
                gr.HTML('<div class="panel-title">📤 Upload Image</div>')
                gr.HTML('<div class="panel-caption">Choose a clear photo of the road surface to analyze.</div>')
                image_input = gr.Image(
                    label="",
                    type="pil",
                    height=420,
                    sources=["upload"],
                )
                run_btn = gr.Button("✨ Run Detection", variant="primary", elem_classes=["primary-btn"])

        with gr.Column(scale=1):
            with gr.Group(elem_classes=["panel"]):
                gr.HTML('<div class="panel-title">🔎 Detection Result</div>')
                gr.HTML('<div class="panel-caption">Annotated image and detailed summary will appear here.</div>')
                output_image = gr.Image(label="", height=420)
                output_text = gr.Textbox(
                    label="Summary",
                    lines=12,
                    max_lines=20,
                )

    run_btn.click(
        fn=detect_damage,
        inputs=[image_input],
        outputs=[output_image, output_text],
        api_name="detect_damage",
    )


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        debug=False,
    )