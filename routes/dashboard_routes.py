from flask import Blueprint, render_template
from models.defect_model import Defect
from services.reliability_service import calculate_mtbf
from services.predictive_maintenance import predict_failure

dashboard_bp = Blueprint("dashboard_bp", __name__)

@dashboard_bp.route("/")
def home():

    defects = Defect.query.all()

    total_aircraft = len(set([d.aircraft for d in defects]))
    total_defects = len(defects)
    aog_cases = len([d for d in defects if d.severity == "AOG"])

    mtbf = calculate_mtbf()
    rating = "Good"

    failure_prediction = predict_failure()

    months = ["Jan","Feb","Mar","Apr","May","Jun"]
    trend = [4200,4300,4400,4500,4600,4700]

    return render_template(
        "dashboard.html",
        aircraft=total_aircraft,
        defects=total_defects,
        aog=aog_cases,
        mtbf=mtbf,
        rating=rating,
        status="Operational",
        failure=failure_prediction,
        months=months,
        trend=trend,
        defect_list=defects
    )