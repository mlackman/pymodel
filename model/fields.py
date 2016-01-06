__all__ = ["Field"]


class Field(object):
  """Base class for fields"""
  attribute_name = None
  validators = []

  def __init__(self, validators=None):
    validator_classes = validators or []
    self.validators.extend([validator() for validator in validator_classes])

  def __set__(self, obj, value):
    failing_validations = [validator for validator in self.validators if not validator(value)]
    if failing_validations:
      setattr(obj, self.attribute_name + "_errors", [validator.error_msg(self.attribute_name, value) for validator in failing_validations])
    obj.__dict__["_" + self.attribute_name] = value

  def __get__(self, obj, objType=None):
    return obj.__dict__["_" + self.attribute_name]



