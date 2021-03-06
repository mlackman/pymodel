import unittest
import model


class TestCreatingAndAccessingModelProperties(unittest.TestCase):

  class User(metaclass=model.Model):
    username = model.Field()
    password = model.Field()
    non_field = 5

  def test_creating_model(self):
    user = self.User()
    self.assertIsNone(user.username)
    self.assertIsNone(user.password)

  def test_creating_model_with_values(self):
    user = self.User(username="john", password="pword")
    self.assertEqual(user.username, "john")
    self.assertEqual(user.password, "pword")

  def test_attributes_can_be_changed(self):
    user = self.User()
    user.username = "john"
    user.password = "pword"

    self.assertEqual(user.username, "john")
    self.assertEqual(user.password, "pword")

  def test_it_raises_exception_if_trying_to_create_model_with_args(self):
    with self.assertRaises(AttributeError):
      user = self.User(5)

  def test_getting_name_of_the_fields(self):
    self.assertEqual(len(self.User.field_names), 2)
    self.assertIn("username", self.User.field_names)
    self.assertIn("password", self.User.field_names)

class TestModelValidations(unittest.TestCase):

  class User(metaclass=model.Model):
    username = model.Field(validators=[model.RequiredValidator])

  def test_has_errors_is_false_when_created_without_arguments(self):
    user = self.User()
    self.assertFalse(user.has_errors)

  def test_username_errors_contains_error_message_when_username_field_not_present(self):
    user = self.User(username='')
    self.assertTrue(len(user.username_errors) > 0)
    self.assertTrue(len(user.username_errors[0]) > 1)


if __name__ == '__main__':
  unittest.main()
