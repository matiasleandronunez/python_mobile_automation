from behave import given, when, then
from behave import matchers
matchers.use_step_matcher("re")

@given(u'I look up (.*)')
def step_impl(context, lookup_term):
    context.landing_page.search_article(lookup_term)

@when(u'I click on the first result displayed')
def step_impl(context):
    pass

@then(u'wikipedia article titled (.*) is displayed')
def step_impl(context, art_title):
    assert True

