__all__ = ['RequiredValidator']


class Validator(object):
  pass

class RequiredValidator(Validator):
  error_message = "'%s' cannot be empty!"

  def __call__(self, value):
    "Retrurns true if validation ok"
    return value is not None and len(value) != 0

  def error_msg(self, attribute_name, value):
    return self.error_message % (attribute_name.capitalize())
