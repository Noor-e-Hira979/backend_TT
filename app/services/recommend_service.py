from app.utils.gemini_client import generate_recommendation

def get_role_recommendation(student_profile: dict):

    student_data = f"""
Skills: {student_profile.get('skills')}
Interests: {student_profile.get('interests')}
GPA: {student_profile.get('gpa')}
"""

    result = generate_recommendation(student_data)

    return {"recommendation": result}
