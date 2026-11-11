from flask import Blueprint, request, jsonify # type: ignore
from models.notes import Note
from db_config import db_session

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/api/notes', methods=['GET'])
def get_notes():
    subject = request.args.get('subject')
    semester = request.args.get('semester')
    course = request.args.get('course')
    college = request.args.get('college')

    query = db_session.query(Note)
    if subject:
        query = query.filter(Note.subject == subject)
    if semester:
        query = query.filter(Note.semester == semester)
    if course:
        query = query.filter(Note.course == course)
    if college:
        query = query.filter(Note.college == college)

    notes = query.all()
    result = [{
        'id': note.id,
        'title': note.title,
        'subject': note.subject,
        'semester': note.semester,
        'course': note.course,
        'college': note.college,
        'pdf_link': note.pdf_link,
        'youtube_link': note.youtube_link
    } for note in notes]

    return jsonify(result)
