import streamlit as st
import time

def check_password_strength(password):
    score = 0
    
    # Length check (6 characters minimum)
    if len(password) >= 6:
        score += 1
        
    # Contains number
    if any(char.isdigit() for char in password):
        score += 1
        
    # Contains letter
    if any(char.isalpha() for char in password):
        score += 1
        
    # Determine strength level
    if score == 0:
        strength = "Very Weak"
        color = "red"
    elif score == 1:
        strength = "Weak"
        color = "orange"
    elif score == 2:
        strength = "Medium"
        color = "yellow"
    else:
        strength = "Strong"
        color = "green"
        
    return strength, score, color

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
    
    st.title("🔒 Password Strength Meter")
    st.write("Check how strong your password is!")
    
    # Password input
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        # Add a small delay for better UX
        time.sleep(0.1)
        
        # Check password strength
        strength, score, color = check_password_strength(password)
        
        # Display strength level with color
        st.markdown(f"### Password Strength: <span style='color: {color}'>{strength}</span>", unsafe_allow_html=True)
        
        # Progress bar
        progress = score / 3
        st.progress(progress)
        
        # Requirements checklist
        st.write("### Requirements:")
        st.write(f"- {'✅' if len(password) >= 6 else '❌'} At least 6 characters")
        st.write(f"- {'✅' if any(char.isdigit() for char in password) else '❌'} Contains a number")
        st.write(f"- {'✅' if any(char.isalpha() for char in password) else '❌'} Contains a letter")
        
        # Tips
        if strength in ["Very Weak", "Weak"]:
            st.warning("💡 Tip: Try adding more characters, numbers, or letters to make your password stronger!")

if __name__ == "__main__":
    main() 