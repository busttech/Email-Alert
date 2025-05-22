from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "ENTER YOUR KEY"

# ── Mail configuration ──────────────────────────────────────────────
app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME="tarun1940c@gmail.com",   # change to your address
    MAIL_PASSWORD=""     # app-specific password
)
mail = Mail(app)
# ────────────────────────────────────────────────────────────────────


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name  = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        # 💡 Basic validation
        if not name or not email:
            flash("Both name and email are required.")
            return redirect("/")

        # Compose and send the message
        msg          = Message(
            subject="Alert – you filled the form",
            sender=app.config["MAIL_USERNAME"],
            recipients=[email],
        )
        msg.body     = (
            f"Hi {name},\n\n"
            "Thank you for submitting the form. "
            "We just wanted to let you know that we’ve received your details.\n\n"
            "— Your Friendly Flask App"
        )
        mail.send(msg)

        flash("Email sent successfully!")
        return redirect("/")

    # GET request → show the form
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
