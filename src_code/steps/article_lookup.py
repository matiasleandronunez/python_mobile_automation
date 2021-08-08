from behave import given, when, then
from behave import matchers
matchers.use_step_matcher("re")


@given(u'I look up (.*)')
def step_impl(context, lookup_term):
    context.landing_page.search_article(lookup_term)


@when(u'I click on the first result displayed')
def step_impl(context):
    context.landing_page.select_first_result()


@then(u'wikipedia article titled (.*) with subtext (.*) is displayed')
def step_impl(context, art_title, epy_text):
    actual_title = context.article_page.get_article_main_title()
    actual_epy = context.article_page.get_article_main_title_epy()

    assert(art_title == actual_title), f"Expected {art_title} but was {actual_title}"
    assert(epy_text == actual_epy), f"Expected {epy_text} but was {actual_epy}"

