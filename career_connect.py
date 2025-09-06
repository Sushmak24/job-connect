import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import time

# Page configuration
st.set_page_config(
    page_title="CareerConnect Pro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .login-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        max-width: 400px;
        margin: 2rem auto;
    }
    
    .job-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    
    .job-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 0.5rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    .sidebar .stSelectbox > div > div {
        background-color: #f8f9fa;
        border-radius: 10px;
    }
    
    .success-message {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        margin: 1rem;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
    }
    
    .stats-container {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #e0e0e0;
        padding: 0.5rem 1rem;
    }
    
    .stSelectbox > div > div {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sample data for demonstration
def generate_sample_data():
    companies = ['Google', 'Microsoft', 'Apple', 'Amazon', 'Meta', 'Tesla', 'Netflix', 'Spotify', 'Uber', 'Airbnb']
    job_titles = ['Software Engineer', 'Data Scientist', 'Product Manager', 'UX Designer', 'Marketing Specialist', 'Business Analyst', 'DevOps Engineer', 'Full Stack Developer']
    locations = ['San Francisco', 'New York', 'Seattle', 'Austin', 'Boston', 'Chicago', 'Los Angeles', 'Remote']
    job_types = ['Full-time', 'Internship', 'Part-time', 'Contract']
    
    jobs = []
    for i in range(50):
        job = {
            'id': i+1,
            'title': random.choice(job_titles),
            'company': random.choice(companies),
            'location': random.choice(locations),
            'type': random.choice(job_types),
            'salary': f"${random.randint(60, 200)}k",
            'experience': f"{random.randint(0, 8)}+ years",
            'posted': f"{random.randint(1, 30)} days ago",
            'skills': random.sample(['Python', 'JavaScript', 'React', 'SQL', 'Machine Learning', 'AWS', 'Docker', 'Kubernetes'], 3)
        }
        jobs.append(job)
    
    return pd.DataFrame(jobs)

# Initialize session state
def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'jobs_data' not in st.session_state:
        st.session_state.jobs_data = generate_sample_data()

# Login page
def show_login_page():
    st.markdown("""
    <div class="main-header">
        <h1>🚀 CareerConnect Pro</h1>
        <p>Your Gateway to Dream Jobs and Internships</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown("### Welcome Back! 👋")
        st.markdown("Sign in to discover amazing opportunities")
        
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            
            col_login, col_register = st.columns(2)
            with col_login:
                login_clicked = st.form_submit_button("🔐 Login", use_container_width=True)
            with col_register:
                register_clicked = st.form_submit_button("📝 Register", use_container_width=True)
            
            if login_clicked and username and password:
                if username == "admin" and password == "password":
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("✅ Login successful! Redirecting...")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials. Try admin/password")
            
            elif register_clicked:
                st.info("📧 Registration link sent to your email!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Demo credentials
        st.markdown("---")
        st.info("🎯 **Demo Credentials:**\nUsername: `admin`\nPassword: `password`")

# Main dashboard
def show_dashboard():
    # Header
    st.markdown(f"""
    <div class="main-header">
        <h1>🚀 Welcome back, {st.session_state.username}!</h1>
        <p>Discover your next career opportunity with AI-powered matching</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar filters
    with st.sidebar:
        st.markdown("### 🔍 Search Filters")
        
        search_term = st.text_input("🔎 Search Jobs", placeholder="e.g., Python Developer")
        job_type = st.selectbox("💼 Job Type", ["All", "Full-time", "Internship", "Part-time", "Contract"])
        location = st.selectbox("📍 Location", ["All", "Remote", "San Francisco", "New York", "Seattle", "Austin"])
        experience = st.selectbox("⭐ Experience Level", ["All", "0+ years", "1+ years", "3+ years", "5+ years"])
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Refresh", use_container_width=True):
                st.session_state.jobs_data = generate_sample_data()
                st.rerun()
        with col2:
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state.logged_in = False
                st.rerun()
    
    # Main content area
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 Dashboard", "💼 Job Search", "📊 Analytics", "👤 Profile"])
    
    with tab1:
        show_dashboard_tab()
    
    with tab2:
        show_job_search_tab(search_term, job_type, location, experience)
    
    with tab3:
        show_analytics_tab()
    
    with tab4:
        show_profile_tab()

def show_dashboard_tab():
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>1,247</h2>
            <p>Available Jobs</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>89</h2>
            <p>Internships</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>15</h2>
            <p>Applications</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h2>92%</h2>
            <p>Match Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Recent activities and recommendations
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🎯 Recommended for You")
        
        recommended_jobs = st.session_state.jobs_data.head(3)
        for _, job in recommended_jobs.iterrows():
            st.markdown(f"""
            <div class="job-card">
                <h4>{job['title']} at {job['company']}</h4>
                <p>📍 {job['location']} | 💰 {job['salary']} | ⏰ {job['posted']}</p>
                <p><strong>Skills:</strong> {', '.join(job['skills'])}</p>
                <p><span style="background: #e8f5e8; padding: 0.2rem 0.5rem; border-radius: 15px; font-size: 0.8rem;">🎯 95% Match</span></p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📈 Quick Stats")
        
        # Application status chart
        status_data = pd.DataFrame({
            'Status': ['Applied', 'In Review', 'Interview', 'Rejected'],
            'Count': [8, 4, 2, 1]
        })
        
        fig = px.pie(status_data, values='Count', names='Status', 
                    color_discrete_sequence=['#667eea', '#764ba2', '#f093fb', '#f5576c'])
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(showlegend=False, height=300, margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)
        
        # Recent activity
        st.markdown("### 🔔 Recent Activity")
        activities = [
            "✅ Applied to Google - SWE",
            "👀 Viewed Microsoft job",
            "📄 Updated resume",
            "🎯 Profile viewed 23 times"
        ]
        
        for activity in activities:
            st.markdown(f"<p style='margin: 0.5rem 0; padding: 0.5rem; background: #f8f9fa; border-radius: 8px;'>{activity}</p>", unsafe_allow_html=True)

def show_job_search_tab(search_term, job_type, location, experience):
    st.markdown("### 🔍 Job Search Results")
    
    # Filter data based on selections
    filtered_data = st.session_state.jobs_data.copy()
    
    if search_term:
        filtered_data = filtered_data[
            filtered_data['title'].str.contains(search_term, case=False, na=False) |
            filtered_data['company'].str.contains(search_term, case=False, na=False)
        ]
    
    if job_type != "All":
        filtered_data = filtered_data[filtered_data['type'] == job_type]
    
    if location != "All":
        filtered_data = filtered_data[filtered_data['location'] == location]
    
    if experience != "All":
        filtered_data = filtered_data[filtered_data['experience'] == experience]
    
    st.markdown(f"**Found {len(filtered_data)} opportunities matching your criteria**")
    
    # Job listings
    for _, job in filtered_data.iterrows():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"""
            <div class="job-card">
                <h4>{job['title']}</h4>
                <h5 style="color: #667eea; margin: 0;">{job['company']}</h5>
                <p>📍 {job['location']} | 💼 {job['type']} | 💰 {job['salary']} | ⭐ {job['experience']}</p>
                <p><strong>Required Skills:</strong> {', '.join(job['skills'])}</p>
                <p style="color: #666; font-size: 0.9rem;">Posted {job['posted']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(f"📤 Apply", key=f"apply_{job['id']}", use_container_width=True):
                st.success(f"✅ Applied to {job['title']} at {job['company']}!")
            
            if st.button(f"❤️ Save", key=f"save_{job['id']}", use_container_width=True):
                st.info(f"💾 Saved {job['title']} to your favorites!")

def show_analytics_tab():
    st.markdown("### 📊 Career Analytics Dashboard")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Job market trends
        st.markdown("#### 📈 Job Market Trends")
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
        job_postings = [random.randint(800, 1500) for _ in range(len(dates))]
        
        trend_data = pd.DataFrame({
            'Month': dates,
            'Job Postings': job_postings
        })
        
        fig = px.line(trend_data, x='Month', y='Job Postings', 
                     title='Monthly Job Postings Trend',
                     color_discrete_sequence=['#667eea'])
        fig.update_layout(showlegend=False, height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Salary distribution
        st.markdown("#### 💰 Salary Distribution")
        salary_ranges = ['$50k-70k', '$70k-100k', '$100k-150k', '$150k-200k', '$200k+']
        counts = [15, 35, 25, 20, 5]
        
        fig = px.bar(x=salary_ranges, y=counts, 
                    title='Salary Range Distribution',
                    color_discrete_sequence=['#764ba2'])
        fig.update_layout(showlegend=False, height=350, xaxis_title='Salary Range', yaxis_title='Number of Jobs')
        st.plotly_chart(fig, use_container_width=True)
    
    # Skills in demand
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🛠️ Most In-Demand Skills")
        skills_data = {
            'Skill': ['Python', 'JavaScript', 'React', 'AWS', 'SQL', 'Machine Learning', 'Docker', 'Kubernetes'],
            'Demand': [85, 78, 72, 68, 65, 62, 58, 45]
        }
        skills_df = pd.DataFrame(skills_data)
        
        fig = px.bar(
        skills_df,
        x="Demand",
        y="Skill",
        orientation="h",
        title='Skills Demand (%)',
        color_discrete_sequence=['#667eea'])
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 🏢 Top Hiring Companies")
        companies_data = {
            'Company': ['Google', 'Microsoft', 'Amazon', 'Apple', 'Meta'],
            'Open_Positions': [156, 143, 128, 97, 89]
        }
        companies_df = pd.DataFrame(companies_data)
        
        fig = px.bar(companies_df, x='Company', y='Open_Positions',
                    title='Companies with Most Openings',
                    color_discrete_sequence=['#764ba2'])
        fig.update_layout(showlegend=False, height=400, xaxis_title='Company', yaxis_title='Open Positions')
        st.plotly_chart(fig, use_container_width=True)

def show_profile_tab():
    st.markdown("### 👤 User Profile")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### 📸 Profile Picture")
        st.image("https://via.placeholder.com/200x200/667eea/white?text=User", width=200)
        
        if st.button("📤 Upload New Photo", use_container_width=True):
            st.success("📸 Photo uploaded successfully!")
    
    with col2:
        st.markdown("#### ✏️ Edit Profile")
        
        with st.form("profile_form"):
            name = st.text_input("Full Name", value="John Doe")
            email = st.text_input("Email", value="john.doe@email.com")
            phone = st.text_input("Phone", value="+1 (555) 123-4567")
            location = st.text_input("Location", value="San Francisco, CA")
            
            st.markdown("##### 🎓 Experience Level")
            exp_level = st.selectbox("Experience", ["Entry Level", "Mid Level", "Senior Level", "Executive"])
            
            st.markdown("##### 🛠️ Skills")
            skills = st.multiselect("Select Skills", 
                                  ["Python", "JavaScript", "React", "SQL", "Machine Learning", "AWS", "Docker", "Kubernetes"],
                                  default=["Python", "JavaScript", "React"])
            
            st.markdown("##### 📄 Resume")
            uploaded_file = st.file_uploader("Upload Resume", type=['pdf', 'doc', 'docx'])
            
            if st.form_submit_button("💾 Save Profile", use_container_width=True):
                st.success("✅ Profile updated successfully!")
    
    st.markdown("---")
    
    # Profile completion
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📈 Profile Strength</h3>
            <h2 style="color: #4CAF50;">85%</h2>
            <p>Strong profile! Add 2 more skills to reach 90%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>👁️ Profile Views</h3>
            <h2 style="color: #667eea;">127</h2>
            <p>23 views this week (+18%)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Job Matches</h3>
            <h2 style="color: #764ba2;">23</h2>
            <p>New matches this week</p>
        </div>
        """, unsafe_allow_html=True)

# Main app logic
def main():
    load_css()
    init_session_state()
    
    if not st.session_state.logged_in:
        show_login_page()
    else:
        show_dashboard()

if __name__ == "__main__":
    main()