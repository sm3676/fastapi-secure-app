from app.calculation_service import create_calculation
from app.schemas import CalculationCreate

def test_create_calculation(db_session):
    calc = CalculationCreate(a=4, b=2, type="Multiply")

    result = create_calculation(db_session, calc)

    assert result.result == 8