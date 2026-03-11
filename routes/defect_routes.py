from flask import Blueprint, render_template, request, redirect
from models.defect_model import Defect
from extensions import db

defect_bp = Blueprint("defect_bp", __name__)

@defect_bp.route("/report", methods=["GET","POST"])
def report_defect():

    if request.method == "POST":

        aircraft = request.form["aircraft"]
        component = request.form["component"]
        defect = request.form["defect"]
        severity = request.form["severity"]

        new_defect = Defect(
            aircraft=aircraft,
            component=component,
            defect=defect,
            severity=severity
        )

        db.session.add(new_defect)
        db.session.commit()

        return redirect("/")

    return render_template("report_defect.html")
