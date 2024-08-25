from config import db

class HoursByType(db.Model):
    __tablename__ = 'hours_by_type'

    id = db.Column(db.Integer, primary_key=True)
    meeting_type = db.Column(db.String(100), nullable=False)
    average_hours_per_week = db.Column(db.Float, nullable=False)
    cost_per_dev_week = db.Column(db.Float, nullable=False)
    cost_for_15_person_team = db.Column(db.Float, nullable=False)
    devshield_savings_per_week = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "meeting_type": self.meeting_type,
            "average_hours_per_week": self.average_hours_per_week,
            "cost_per_dev_week": self.cost_per_dev_week,
            "cost_for_15_person_team": self.cost_for_15_person_team,
            "devshield_savings_per_week": self.devshield_savings_per_week,
        }
    

class MeetingCost(db.Model):
    __tablename__ = 'meeting_cost'

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(50), nullable=False)
    current_dev_time_sinks = db.Column(db.Float, nullable=False)
    cost_after_devshield = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "day": self.day,
            "current_dev_time_sinks": self.current_dev_time_sinks,
            "cost_after_devshield": self.cost_after_devshield,
        }

class Person(db.Model):
    __tablename__ = 'person'

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


class ProductiveHours(db.Model):
    __tablename__ = 'productive_hours'

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(50), nullable=False)
    productive_hours = db.Column(db.Float, nullable=False)
    productive_hours_with_devshield = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "day": self.day,
            "productive_hours": self.productive_hours,
            "productive_hours_with_devshield": self.productive_hours_with_devshield,
        }