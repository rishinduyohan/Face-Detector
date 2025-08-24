<div align="center" style="font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, 'Helvetica Neue', Arial; color:#0f172a; line-height:1.6;">

  <h1 style="margin:16px 0 6px; font-size:36px;">🎥 Face Detector (OpenCV + Python)</h1>
  <p style="margin:0 0 12px; font-size:16px; color:#475569;">
    Real-time face detection with FPS counter, timestamp overlay, and dynamic face-count styling.
  </p>

  <!-- Badges -->
  <p>
    <a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-3776AB.svg?logo=python&logoColor=white"></a>
    <a href="#"><img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8.svg?logo=opencv&logoColor=white"></a>
    <a href="#"><img alt="License" src="https://img.shields.io/badge/License-MIT-10B981.svg"></a>
  </p>
</div>

<!-- Summary -->
<section style="max-width:880px; margin:0 auto; padding:0 16px;">
  <h2 style="font-size:22px; margin:16px 0 6px;">✨ Project Overview</h2>
  <p>
    This project is a clean, real-time face detection app built with <strong>OpenCV</strong>. It captures frames from your webcam,
    converts them to grayscale for efficient processing, detects faces using Haar Cascades, and overlays useful UI elements:
    a <strong>live face counter</strong>, <strong>timestamp</strong>, and a <strong>frames-per-second (FPS)</strong> indicator.
    Rectangle colors change dynamically based on the number of faces detected (🟩 green ≤ 2, 🟥 red ≥ 3) for instant visual feedback.
  </p>

  <h3 style="font-size:18px; margin:18px 0 6px;">🌟 Features</h3>
  <ul style="margin:0 0 14px 18px;">
    <li>Real-time webcam capture (VideoCapture)</li>
    <li>Haar Cascade face detection (<code>haarcascade_frontalface_default.xml</code>)</li>
    <li>Dynamic rectangle color based on face count</li>
    <li>On-screen overlays: face count, timestamp, FPS</li>
    <li>Simple keyboard control: press <code>q</code> to quit</li>
  </ul>

  <h3 style="font-size:18px; margin:18px 0 6px;">🧰 Tech Stack</h3>
  <ul style="margin:0 0 14px 18px;">
    <li>Python 3.8+</li>
    <li>OpenCV (<code>opencv-python</code>)</li>
  </ul>

  <h2 style="font-size:22px; margin:20px 0 6px;">🚀 Getting Started</h2>

  <h3 style="font-size:18px; margin:16px 0 6px;">1) Prerequisites</h3>
  <ul style="margin:0 0 14px 18px;">
    <li>Python 3.8 or newer</li>
    <li>Webcam access</li>
  </ul>

  <h3 style="font-size:18px; margin:16px 0 6px;">2) Installation</h3>
  <pre style="background:#0b1220; color:#e5e7eb; padding:14px; border-radius:12px; overflow:auto; margin:0 0 12px;">
pip install opencv-python
  </pre>

  <p style="margin:8px 0 0;">
    The Haar Cascade file is resolved via OpenCV’s built-in path:
    <code>cv2.data.haarcascades + "haarcascade_frontalface_default.xml"</code>
  </p>

  <h3 style="font-size:18px; margin:16px 0 6px;">3) Run</h3>
  <pre style="background:#0b1220; color:#e5e7eb; padding:14px; border-radius:12px; overflow:auto; margin:0 0 12px;">
python main.py
  </pre>

  <h2 style="font-size:22px; margin:20px 0 6px;">🕹️ Controls</h2>
  <ul style="margin:0 0 14px 18px;">
    <li><strong>q</strong> — Quit the app</li>
  </ul>

  <h2 style="font-size:22px; margin:20px 0 6px;">🧪 Troubleshooting</h2>
  <ul style="margin:0 0 14px 18px;">
    <li><strong>Black window / no camera:</strong> ensure your webcam is connected and not used by another app.</li>
    <li><strong>Slow FPS:</strong> close other heavy apps; reduce <code>waitKey</code> delay or resize frames before processing.</li>
    <li><strong>No faces detected:</strong> check lighting, camera angle, and that the Haar Cascade path resolves correctly.</li>
  </ul>

  <h2 style="font-size:22px; margin:20px 0 6px;">🗺️ Roadmap</h2>
  <ul style="margin:0 0 14px 18px;">
    <li>🎯 Add eye/Smile detection</li>
    <li>🕶️ Fun overlays (sunglasses/emoji)</li>
    <li>💾 Snapshot capture (<code>s</code> to save)</li>
    <li>⚙️ CLI flags for camera index and cascade params</li>
  </ul>

  <h2 style="font-size:22px; margin:20px 0 6px;">🤝 Contributing</h2>
  <p>Issues and PRs are welcome! Please open an issue to discuss major changes.</p>
</section>
