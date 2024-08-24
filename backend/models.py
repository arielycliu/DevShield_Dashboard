from config import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    job_family = db.Column(db.String(80), unique=False, nullable=False)
    job_title = db.Column(db.String(200), unique=False, nullable=False)
    salary = db.Column(db.Integer, unique=False, nullable=False)
    pay_per_hour = db.Column(db.Float, unique=False, nullable=False)
    hours_meetings_per_week = db.Column(db.Integer, unique=False, nullable=False)
    percentage_meetings_per_week = db.Column(db.Float, unique=False, nullable=False)
    hours_2_contiguous = db.Column(db.Integer, unique=False, nullable=False)
    percentage_2_contiguous = db.Column(db.Float, unique=False, nullable=False)
    opportunity_cost_modifier = db.Column(db.Float, unique=False, nullable=False)
    direct_meeting_cost_week = db.Column(db.Float, unique=False, nullable=False)
    implied_opportunity_cost_week = db.Column(db.Float, unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "jobFamily": self.job_family,
            "jobTitle": self.job_title,
            "salary": self.salary,
            "payPerHour": self.job_title,
            "hoursMeetingsPerWeek": self.hours_meetings_per_week,
            "percentageMeetingsPerWeek": self.percentage_meetings_per_week,
            "hours2Contiguous": self.hours_2_contiguous,
            "percentage2Contiguous": self.percentage_2_contiguous,
            "opportunityCostModifier": self.opportunity_cost_modifier,
            "directMeetingCostWeek": self.direct_meeting_cost_week,
            "impliedOpportunityCostWeek": self.implied_opportunity_cost_week
        }