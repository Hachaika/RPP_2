from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange


class RegionForm(FlaskForm):
    name = StringField('Name of region:', validators=[DataRequired()])
    number = IntegerField('Number of region:', validators=[DataRequired()])
    submit = SubmitField('Add')


class RegionListForm(FlaskForm):
    pass


class RegionDeleteForm(FlaskForm):
    id = IntegerField('ID of region to delete:', validators=[DataRequired()])
    submit = SubmitField('Delete')


class RegionUpdateForm(FlaskForm):
    id = IntegerField('ID of region to update:', validators=[DataRequired()])
    new_id = IntegerField('New ID for the region:', validators=[DataRequired()])
    submit = SubmitField('Update')


class CarTaxParamAddForm(FlaskForm):
    id = IntegerField('ID:', validators=[DataRequired()])
    city_id = IntegerField('City ID:', validators=[DataRequired()])
    from_hp_car = IntegerField('Min Horsepower:', validators=[DataRequired()])
    to_hp_car = IntegerField('Max Horsepower:', validators=[DataRequired()])
    start_year = IntegerField('Start Year:', validators=[DataRequired()])
    end_year = IntegerField('End Year:', validators=[DataRequired()])
    rate = StringField('Tax Rate:', validators=[DataRequired()])
    submit = SubmitField('Add')


class CarTaxParamDeleteForm(FlaskForm):
    id = IntegerField('ID:', validators=[DataRequired()])
    submit = SubmitField('Delete')


class CarTaxParamListForm(FlaskForm):
    submit = SubmitField('Refresh')


class CarTaxParamUpdateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    city_id = IntegerField('City ID', validators=[DataRequired()])
    from_hp_car = IntegerField('Min Horsepower', validators=[DataRequired(), NumberRange(min=0)])
    to_hp_car = IntegerField('Max Horsepower', validators=[DataRequired(), NumberRange(min=0)])
    start_year = IntegerField('Start Year', validators=[DataRequired()])
    end_year = IntegerField('End Year', validators=[DataRequired()])
    rate = DecimalField('Tax Rate', validators=[DataRequired()])


class CarTaxCalcForm(FlaskForm):
    city_id = StringField('City ID', validators=[DataRequired()])
    horsepower = IntegerField('Horsepower', validators=[DataRequired()])
    year = IntegerField('Year of Manufacture', validators=[DataRequired()])
    submit = SubmitField('Calculate Tax')