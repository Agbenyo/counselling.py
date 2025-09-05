import streamlit as st

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'users' not in st.session_state:
    st.session_state.users = {}  # Dictionary to store users

# Function to handle signup
def signup(username, password):
    if username in st.session_state.users:
        st.error("Username already exists! Please choose a different one.")
    else:
        st.session_state.users[username] = password
        st.success("Signup successful! You can now log in.")

# Function to handle login
def login(username, password):
    if username in st.session_state.users and st.session_state.users[username] == password:
        st.session_state.logged_in = True
        st.success("Login successful!")
    else:
        st.error("Invalid username or password!")

# Login and Signup Section
if not st.session_state.logged_in:
    st.header("Login / Signup")
    
    choice = st.selectbox("Select Action", ["Login", "Signup"])

    if choice == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            login(username, password)

    elif choice == "Signup":
        username = st.text_input("Choose a Username")
        password = st.text_input("Choose a Password", type='password')
        if st.button("Signup"):
            signup(username, password)

# If logged in, show the main application
if st.session_state.logged_in:
    # Title of the app
    st.title("Comprehensive Counseling Web Application")

    # Sidebar for navigation
    st.sidebar.header("Navigation")
    options = st.sidebar.selectbox(
        "Choose Option", 
        (
            "Home", 
            "Resource Centre", 
            "Book an Appointment", 
            "One on One Counseling", 
            "Stress Management", 
            "Academic Pressure", 
            "Relationship Challenges", 
            "Mental Health Concerns", 
            "Career Guidance", 
            "Profile Creation", 
            "Anonymous Support", 
            "Workshops and Events", 
            "Group Counseling"
        )
    )

    # Home Section
    if options == "Home":
        st.header("Welcome to the Counseling Service")
        st.write("Explore various resources, book appointments, and seek support.")

    # Resource Centre Section
    elif options == "Resource Centre":
        st.header("Resource Centre")
        search_query = st.text_input("Search for resources")
        st.write("Find helpful resources and links.")
        if search_query:
            st.write(f"Results for '{search_query}':")  # Placeholder for actual search results
        st.write("1. [Mental Health Resources](#)")
        st.write("2. [Crisis Support](#)")
        st.write("3. [Academic Resources](#)")

    # Book an Appointment Section
    elif options == "Book an Appointment":
        st.header("Book an Appointment")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        appointment_type = st.selectbox("Select Appointment Type", ["Individual Counseling", "Group Counseling"])
        counselor = st.selectbox("Choose Counselor", ["Counselor A", "Counselor B"])
        date = st.date_input("Select a Date")
        time = st.time_input("Select a Time")
        
        if st.button("Submit"):
            st.success("Appointment booked successfully!")

    # One on One Counseling Section
    elif options == "One on One Counseling":
        st.header("One on One Counseling")
        st.write("Schedule a private session with a counselor.")
        st.write("Counselor A: Specializes in academic pressure.")
        st.write("Counselor B: Specializes in mental health concerns.")

    # Stress Management Section
    elif options == "Stress Management":
        st.header("Stress Management Resources")
        st.write("Explore techniques and resources for managing stress.")
        if st.button("Get Stress Management Tips"):
            st.write("1. Practice deep breathing.")
            st.write("2. Engage in regular physical activity.")
            st.write("3. Consider mindfulness meditation.")

    # Academic Pressure Section
    elif options == "Academic Pressure":
        st.header("Academic Pressure")
        st.write("Resources to manage academic stress.")
        feedback = st.text_area("Share your experiences with academic pressure:")
        if st.button("Submit Feedback"):
            st.success("Thank you for your feedback!")

    # Relationship Challenges Section
    elif options == "Relationship Challenges":
        st.header("Relationship Challenges")
        st.write("Support and resources for relationship issues.")
        st.write("Join our online sessions for relationship counseling.")

    # Mental Health Concerns Section
    elif options == "Mental Health Concerns":
        st.header("Mental Health Concerns")
        st.write("Resources for various mental health issues.")
        if st.button("Take Self-Assessment"):
            st.write("Self-Assessment results: [Link to assessment tool]")

    # Career Guidance Section
    elif options == "Career Guidance":
        st.header("Career Guidance")
        st.write("Resources to help you with career planning.")
        uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])
        if uploaded_file is not None:
            st.success("Resume uploaded successfully!")

    # Profile Creation Section
    elif options == "Profile Creation":
        st.header("Create Your Profile")
        
        # Upload Profile Image
        profile_image = st.file_uploader("Upload Your Profile Image", type=["jpg", "jpeg", "png"])
        
        if profile_image is not None:
            st.image(profile_image, caption='Uploaded Profile Image', use_column_width=True)
        
        name = st.text_input("Name")
        academic_background = st.text_area("Academic Background")
        counseling_needs = st.text_area("Counseling Needs")
        
        if st.button("Create Profile"):
            if name and academic_background and counseling_needs:
                st.success("Profile created successfully!")
                # Here, you could add functionality to save this data to a database
            else:
                st.error("Please fill in all fields before submitting.")

    # Anonymous Support Section
    elif options == "Anonymous Support":
        st.header("Anonymous Support Options")
        st.write("Reach out for help anonymously. Here are some options:")
        st.write("1. [Anonymous chat lines](#)")
        st.write("2. [Online forums](#)")

    # Workshops and Events Section
    elif options == "Workshops and Events":
        st.header("Workshops and Events")
        st.write("Check out our upcoming workshops and events.")
        st.write("Calendar view of events: [Link to calendar]")

    # Group Counseling Section
    elif options == "Group Counseling":
        st.header("Group Counseling Sessions")
        st.write("Join our group sessions for exam stress and time management.")
        group_choice = st.selectbox("Choose Group", ["Exam Stress Group", "Time Management Group"])
        if st.button("Sign Up"):
            st.success("Successfully signed up for the group!")

    # Footer
    st.sidebar.write("For any inquiries, contact us at: support@counselingapp.com")