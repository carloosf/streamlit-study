import streamlit as st

st.write('Use admin123 and 99992222')


def check_min_length(text, min_length):
    return len(text) >= min_length


# Minimum character length for login and password
if 'min_login_length' not in st.session_state:
    st.session_state['min_login_length'] = 6
if 'min_password_length' not in st.session_state:
    st.session_state['min_password_length'] = 6

st.write(st.session_state)
with st.form('Login'):
    login = st.text_input(label='Login')
    password = st.text_input(label='Password', type='password')
    submit = st.form_submit_button('Login')

    # Check login and password length on submit
    if submit:
        if not check_min_length(login, st.session_state['min_login_length']):
            st.error(f"Login must be at least {
                     st.session_state['min_login_length']} characters long.")
        elif not check_min_length(password, st.session_state['min_password_length']):
            st.error(f"Password must be at least {
                     st.session_state['min_password_length']} characters long.")
        else:
            # Authentication logic (replace with your actual logic)
            if login in st.session_state['users']['username']:  # Replace with actual credentials
                st.success("Logged in successfully!")
            else:
                st.error("Invalid login or password.")
