from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <div style="background:#000; color:#0f0; text-align:center; padding:60px 20px; font-family:'Courier New',monospace; min-height:100vh; margin:0;">
        <pre style="font-size:1.5rem; letter-spacing:2px;">
  ___ _       _           _              ___     ___   ___ 
 / __| |_ _ _(_)_ _  __ _| |___ ___ _ _ / _ \\   / _ \\ / _ \\
| (__|  _| '_| | ' \\/ _` | / -_|_-< '_| (_) | | (_) |  __/
 \\___|\\__|_| |_|_||_\\__,_|_\\___|__/_|  \\___/   \\___/ \\___|
        </pre>
        <h1 style="color:#0f8; margin:30px 0; font-size:2.5rem;">
            CI/CD Pipeline Live in Production
        </h1>
        <p style="font-size:1.4rem;">Containerized • Orchestrated • Automated • Self-Healing</p>
        <p style="color:#0f0; font-size:1.6rem; margin-top:50px;">
            Deployed by <strong>Viky Sharma</strong>
        </p>
        <p style="color:#0a0; font-size:1rem; margin-top:30px;">
            Jenkins → Docker → Kubernetes Ready
        </p>
    </div>
    ''', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
