from sqlalchemy.orm import Session
from app.models import Calculation
from app.calculation_factory import CalculationFactory

def create_calculation(db: Session, calc):
    result = CalculationFactory.calculate(calc.a, calc.b, calc.type)

    db_calc = Calculation(
        a=calc.a,
        b=calc.b,
        type=calc.type,
        result=result
    )

    db.add(db_calc)
    db.commit()
    db.refresh(db_calc)

    return db_calc