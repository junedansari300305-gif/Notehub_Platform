from flask import Blueprint, jsonify # type: ignore

colleges_bp = Blueprint('colleges', __name__)

@colleges_bp.route('/api/colleges', methods=['GET'])
def get_colleges():
    colleges = [
        "Dr. Babasaheb Ambedkar College, Chembur",
        "K.J. Somaiya College of Science and Commerce",
        "SIES College of Arts, Science & Commerce",
        "R.D. National College",
        "Jai Hind College",
        "St. Xavier’s College",
        "Mithibai College",
        "Bhavan’s College",
        "Wilson College",
        "Rizvi College of Arts, Science & Commerce"
    ]
    return jsonify(colleges)
