from behave import given, when, then
from behave import matchers
matchers.use_step_matcher("re")


@given(u'I post an existing customer to the customer create endpoint')
def step_impl(context):
    try:
        apihelper.post_customer(context.existing_customer)
    except RequestUnexpected as e:
        context.exc = e


@then(u'I verify I get a conflict response from the API')
def step_impl(context):
    assert context.exc is not None
    assert isinstance(context.exc, RequestReturnedConflict)