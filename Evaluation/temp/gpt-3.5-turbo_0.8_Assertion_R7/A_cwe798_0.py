from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    api_key = 'YOUR_API_KEY'
    canvas = Canvas(canvas_url, api_key)
    
    courses = canvas.get_courses()
    course_list = []
    
    for course in courses:
    course_list.append(course.name)
    
    return course_list
