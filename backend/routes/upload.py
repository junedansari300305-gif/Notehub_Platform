from flask import Blueprint, request, jsonify # type: ignore
from models.notes import Note
from db_config import db_session

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/api/upload', methods=['POST'])
def upload_note():
    data = request.json
    try:
        new_note = Note(
            title=data.get('title'),
            subject=data.get('subject'),
            semester=data.get('semester'),
            course=data.get('course'),
            college=data.get('college'),
            pdf_link=data.get('pdf_link'),
            youtube_link=data.get('youtube_link')
        )
        db_session.add(new_note)
        db_session.commit()
        return jsonify({'message': 'Note uploaded successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
