import re
import streamlit as st

def check_password_strength(password):
    score = 0
    tips = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        tips.append("🟠 Password should be at least 8 characters long.")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("🟢 Include at least one uppercase letter.")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("🔵 Include at least one lowercase letter.")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("♥️ Include at least one number (0-9).")
    
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        tips.append("🔷 Include at least one special character (!@#$%^&*).")
    
    return score, tips

def main():
    st.title("🔓 Password Strength Meter")
    password = st.text_input("🔍 Enter your password:", type="password")
    
    if password:
        score, tips = check_password_strength(password)
        
        if score == 5:
            st.success("✅ Strong Password! Secure & Safe.")
        elif score >= 3:
            st.warning("⚠️ Moderate Password! Consider improving it.")
        else:
            st.error("❌ Weak Password! Follow these tips to improve:")
        
        for tip in tips:
            st.write(f"- {tip}")

if __name__ == "__main__":
    main()
