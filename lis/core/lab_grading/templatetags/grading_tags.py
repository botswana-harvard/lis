from django import template
from ..utils import calculate_grade, get_grading_range

register = template.Library()


@register.filter(name='grading_limit')
def grading_limit(test_code, result_item):
    result_value = result_item.result_item_value
    dob = result_item.result.order.aliquot.receive.patient.dob
    gender = result_item.result.order.aliquot.receive.patient.gender
    datetime_drawn = result_item.result.order.aliquot.receive.datetime_drawn
    limit = get_grading_range(result_value=result_value, range_category='lln', test_code=test_code, dob=dob, gender=gender, datetime_drawn=datetime_drawn)
    if limit:
        return ' (G%s:%s-%s)' % (limit['grade'], limit['lower'], limit['upper'])
    else:
        return ''


@register.filter(name='grade_flag')
def grade_flag(value, result_item):
    result_value = value
    test_code = result_item.test_code
    datetime_drawn = result_item.result.order.aliquot.receive.datetime_drawn
    dob = result_item.result.order.aliquot.receive.patient.dob
    gender = result_item.result.order.aliquot.receive.patient.gender
    grade = calculate_grade(result_value=result_value, dob=dob, gender=gender, datetime_drawn=datetime_drawn, test_code=test_code)
    if grade:
        return '(G%s)' % grade
    else:
        return ''
