import streamlit as st
import re
import random
import string

# --- PASSWORD STRENGTH CHECKER ---
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback


# --- PASSWORD GENERATOR ---
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*"),
    ]
    password += random.choices(characters, k=length - 4)
    random.shuffle(password)
    return "".join(password)


# --- BLACKLIST FOR COMMON PASSWORDS ---
COMMON_PASSWORDS = ["password", "123456", "qwerty", "abc123"]

def is_weak_password(password):
    return password.lower() in COMMON_PASSWORDS


# --- STREAMLIT APP ---
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if password:
    # Check for common weak passwords
    if is_weak_password(password):
        st.error("❌ This is a commonly used weak password. Please choose a stronger one.")
    else:
        # Check password strength
        score, feedback = check_password_strength(password)

        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
            for suggestion in feedback:
                st.write(suggestion)
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below:")
            for suggestion in feedback:
                st.write(suggestion)

            # Suggest a strong password
            st.subheader("💡 Suggested Strong Password")
            suggested_password = generate_strong_password()
            st.code(suggested_password)