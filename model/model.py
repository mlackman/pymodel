from .fields import Field

class Model(type):
  """Metaclass for models"""

  def __new__(meta, name, bases, clsdict):
    cls = super(Model, meta).__new__(meta, name, bases, clsdict)
    field_names = []
    for name, field in clsdict.items():
      if isinstance(field, Field):
        if field.attribute_name is None:
          field.attribute_name = name
        field_names.append(name)

    error_fields = []

    def __init__(self, *args, **kwargs):
      if len(args) != 0:
        raise AttributeError("class '%s' __init__ does not take non keyword arguments" % name)
      attributes = set()
      attributes.update(kwargs.keys())
      attributes.update(field_names)
      self._error_fields = []

      for name in attributes:
        # Add [fieldname]_errors to object attributes, where error messages for specific field is added
        if name in field_names:
          error_field_name = name + "_errors"
          setattr(self, error_field_name, [])
          self._error_fields.append(error_field_name)
        setattr(self, name, kwargs[name] if name in kwargs else None)

    @property
    def has_errors(self):
      return any([getattr(self, error_field_name) != [] for error_field_name in self._error_fields])

    cls.__init__ = __init__
    cls.has_errors = has_errors
    return cls



