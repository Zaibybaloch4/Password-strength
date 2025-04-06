import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter")  
st.title("🔒 Password Strength Meter")

st.markdown("""
**Hello Friends**,  
Welcome to the Password Strength Checker!  

Enter your password below to analyze its strength and receive suggestions for improvement.
""")

password = st.text_input("🔑 Enter your password", type="password")
feedback = []
score = 0

if password:
    # Check password length
    if len(password) >= 12:
        score += 2  
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")

    # Check uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔴 Include both uppercase and lowercase letters.")

    # Check digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔴 Add at least one digit (0-9).")

    # Check symbols
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2  
    else:
        feedback.append("🔴 Use at least one special character (!, @, #, etc.).")

    # Check for common weak passwords
    common_passwords = ["123456", "password", "qwerty", "abc123", "111111"]
    if password.lower() in common_passwords:
        feedback.append("🚨 This password is too common! Choose a unique one.")

    # Strength Bar
    strength_level = ["Weak", "Medium", "Strong", "Very Strong"]
    st.progress(score / 6)

    # Display results
    if score >= 5:
        st.success(f"🟢 {strength_level[3]} Password!")
    elif score >= 3:
        st.warning(f"🟡 {strength_level[2]} Password.")
    else:
        st.error(f"🔴 {strength_level[0]} Password! Consider making improvements.")

    if feedback:
        st.markdown("### 🛠 Suggestions:")
        for suggestion in feedback:
            st.markdown(f"- {suggestion}")

# Password Generator
if st.button("Generate a Strong Password"):
    import random
    import string
    strong_password = "".join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
    st.info(f"🔑 Try this secure password: `{strong_password}`")

